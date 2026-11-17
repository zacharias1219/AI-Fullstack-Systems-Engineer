"""
Validates all Topic Lab HTML study pages against the Topic Lab v4 assembler rules in
.agents/skills/topic-lab/SKILL.md.
"""
import html
import json
import pathlib
import re
import zlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_PATH = ROOT / ".agents" / "skills" / "topic-lab" / "SKILL.md"
skill_src = SKILL_PATH.read_text(encoding="utf-8")
CRC = {"STYLE": 2800455163, "SCRIPT": 3606185793}

all_ok = True
for p in sorted(ROOT.rglob("*.html")):
    if p.name.lower() in ("main.html", "index.html"):
        continue
    page = p.read_text(encoding="utf-8")
    flags = []
    for tag in ("STYLE", "SCRIPT"):
        m = re.search(r"<!-- TOPIC-LAB:%s .*?<!-- /TOPIC-LAB:%s -->" % (tag, tag), page, re.S)
        if not m:
            flags.append(f"missing {tag} block")
        elif zlib.crc32(re.sub(r"\s+", "", m.group(0)).encode("utf-8")) != CRC[tag]:
            flags.append(f"{tag} block does not match v4 checksum")

    m_main = re.search(r"<main>(.*)</main>", page, re.S)
    body = m_main.group(1) if m_main else page
    tier_m = re.search(r"Tier\s*(\d)", body)
    tier = int(tier_m.group(1)) if tier_m else 2

    if chr(8212) in page or chr(8211) in page:
        flags.append("dash characters found (em/en dash)")
    if "{{" in body:
        flags.append("unfilled {{...}} placeholder")
    if 'id="recall-box"' in body and body.count('class="keep"') < 2:
        flags.append('blank-page prompt and recall box both need class="keep"')

    nviz = len(re.findall(r'<figure class="viz[ "]', body))
    steppers = re.findall(r'<figure class="viz stepper"(.*?)</figure>', body, re.S)
    nstep = len(steppers)
    explorables = len(re.findall(r"tl\.viz\(", body))

    if tier == 1:
        if not (3 <= nviz <= 5):
            flags.append(f"T1 needs 3 to 5 visuals, got {nviz}")
        if not (1 <= nstep <= 3):
            flags.append(f"T1 needs 1 to 3 steppers, got {nstep}")
        if explorables < 1:
            flags.append("T1 needs at least one explorable (tl.viz)")
    elif tier == 2:
        if not (2 <= nviz <= 3):
            flags.append(f"T2 needs 2 or 3 visuals, got {nviz}")
        if not (1 <= nstep <= 2):
            flags.append(f"T2 needs 1 or 2 steppers, got {nstep}")
    elif tier == 3:
        if nviz < 1 or nstep < 1:
            flags.append(f"T3 needs at least 1 concept stepper, got viz={nviz} step={nstep}")

    if not steppers:
        flags.append("no stepper found")
    for st in steppers:
        k = len(re.findall(r"<li>", st.split('<ol class="steps">')[-1])) if '<ol class="steps">' in st else 0
        if k < 3:
            flags.append(f"stepper has {k} < 3 steps")
        nums = [int(x) for x in re.findall(r'data-(?:step|only|hi)="([\d ,]+)"', st) for x in re.split(r"[ ,]+", x.strip()) if x]
        if nums and max(nums) > k:
            flags.append(f"stepper refers to step {max(nums)} but lists only {k} steps")

    idea_m = re.search(r'<section class="st" id="idea">(.*?)</section>', body, re.S)
    if not idea_m or 'id="viz-concept"' not in idea_m.group(1) or 'class="viz stepper"' not in idea_m.group(1):
        flags.append("concept stepper (viz-concept) missing from station 2 (#idea)")

    if body.count("<figcaption>") < nviz:
        flags.append(f"figure.viz count ({nviz}) > figcaption count ({body.count('<figcaption>')})")

    for w in re.findall(r'<svg[^>]*viewBox="0 0 (\d+)', body):
        if int(w) > 520:
            flags.append(f"SVG viewBox width {w} > 520")

    for svg_tag in re.findall(r"<svg[^>]*>", body):
        if 'role="img"' not in svg_tag or "aria-label=" not in svg_tag:
            flags.append("SVG missing role='img' or aria-label")

    for raw in re.findall(r"data-bars='([^']*)'", body):
        try:
            json.loads(html.unescape(raw))
        except ValueError:
            flags.append("invalid JSON in data-bars")

    if explorables > 0:
        for fig_m in re.finditer(r'<figure class="viz"[^>]*id="([^"]+)"[^>]*>(.*?)</figure>', body, re.S):
            fid, fbody = fig_m.group(1), fig_m.group(2)
            if f'tl.viz("{fid}"' in body or f"tl.viz('{fid}'" in body:
                if 'class="ask"' not in fbody:
                    flags.append(f"explorable {fid} missing .ask prediction question")

    status = "OK" if not flags else "FAIL: " + "; ".join(flags)
    if flags:
        all_ok = False
    print(f"{p.name:42} | T{tier} | viz={nviz} step={nstep} exp={explorables} | {status}")

if not all_ok:
    raise SystemExit(1)
