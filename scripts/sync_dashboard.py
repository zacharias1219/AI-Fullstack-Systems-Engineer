"""
Synchronizes the AI Mastery frontend dashboard (main.html + index.html) and README.md
from .context/01-master-topic-index.md, .context/02-week-plan.md, .context/AI Mastery tracker - Topics.csv,
and the generated HTML files in the domain folders.

Usage:
  python scripts/sync_dashboard.py
  python scripts/sync_dashboard.py --mark K02:4 K03:5 D02:4 --status Learned --date 2026-11-17
"""
import argparse
import csv
import datetime
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / ".context" / "01-master-topic-index.md"
WEEK_PATH = ROOT / ".context" / "02-week-plan.md"
CSV_PATH = ROOT / ".context" / "AI Mastery tracker - Topics.csv"
README_PATH = ROOT / "README.md"

DOMAIN_FOLDERS = {
    "A": "A - Foundations and Applied Math",
    "B": "B - Classical Machine Learning",
    "C": "C - Deep Learning",
    "D": "D -Transformers and LLM Internals",
    "E": "E - Post-Training",
    "F": "F - Training Infrastructure",
    "G": "G - LLM Application Layer",
    "H": "H - Retrieval and RAG",
    "I": "I - Agents and Orchestration",
    "J": "J - Evals and Quality",
    "K": "K - Inference Engineering and Hardware",
    "L": "L - System Design Concepts",
    "M": "M - Backend Engineering",
    "N": "N - Databases",
    "O": "O - Frontend Engineering",
    "P": "P - Data Engineering",
    "Q": "Q - Cloud",
    "R": "R - DevOps, Platform, MLOps, LLMOps",
    "S": "S - Security, Privacy, Safety, Governance",
    "T": "T - Domain and Applied AI",
    "U": "U - Research and Engineering Craft",
    "V": "V -Business and Product",
    "W": "W - People Skills",
    "X": "X - Interview Craft",
    "Y": "Y - System Design Drills and Case Studies",
}

MONTHS = {"Nov": 11, "Dec": 12, "Jan": 1, "Feb": 2}


def planned_to_iso(planned_str):
    m = re.match(r"^[A-Za-z]+\s+(\d{1,2})\s+([A-Za-z]{3})$", planned_str.strip())
    if not m:
        return ""
    day = int(m.group(1))
    mon_str = m.group(2)
    mon = MONTHS.get(mon_str, 11)
    year = 2026 if mon in (11, 12) else 2027
    return f"{year:04d}-{mon:02d}-{day:02d}"


def add_days(iso_str, days):
    dt = datetime.date.fromisoformat(iso_str) + datetime.timedelta(days=days)
    return dt.isoformat()


def update_csv_marks(marks, status, learned_date):
    if not marks:
        return
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    updates = {}
    for item in marks:
        if ":" in item:
            tid, conf = item.split(":", 1)
            updates[tid.strip().upper()] = conf.strip()
        else:
            updates[item.strip().upper()] = ""

    changed = 0
    for row in rows:
        tid = row["ID"].strip().upper()
        if tid in updates:
            row["Status"] = status
            if updates[tid]:
                row["Conf"] = updates[tid]
            if status in ("Learned", "Solid"):
                row["Learned on"] = learned_date
                row["Retest 7d"] = add_days(learned_date, 7)
                row["Retest 30d"] = add_days(learned_date, 30)
            changed += 1

    with open(CSV_PATH, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Updated {changed} topic row(s) in {CSV_PATH.name} to Status='{status}' (date={learned_date}).")


def update_readme_built_column(existing_html):
    if not README_PATH.is_file():
        return
    txt = README_PATH.read_text(encoding="utf-8")
    by_domain = {}
    for tid, rel in sorted(existing_html.items(), key=lambda x: (x[0][0], int(x[0][1:]))):
        d = tid[0]
        url = "./" + rel.replace(" ", "%20")
        by_domain.setdefault(d, []).append(f"[`{tid}`]({url})")

    def repl(m):
        letter = m.group(2)
        built_str = ", ".join(by_domain.get(letter, [])) if letter in by_domain else "-"
        return f"{m.group(1)}{built_str} |"

    new_txt = re.sub(
        r"^(\|\s*\*\*([A-Z])\*\*\s*\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|\s*)([^|]+?)\s*\|$",
        repl,
        txt,
        flags=re.M,
    )
    if new_txt != txt:
        README_PATH.write_text(new_txt, encoding="utf-8")
        print("Updated Built Pages links in README.md")


def main():
    parser = argparse.ArgumentParser(description="Sync AI Mastery Dashboard & Tracker")
    parser.add_argument("--mark", nargs="*", help="Topic IDs (optionally ID:CONF, e.g. K02:4 D02:5) to update in CSV")
    parser.add_argument("--status", default="Learned", help="Status to set for --mark (default: Learned)")
    parser.add_argument("--date", default=datetime.date.today().isoformat(), help="Learned date YYYY-MM-DD")
    args = parser.parse_args()

    if args.mark:
        update_csv_marks(args.mark, args.status, args.date)

    index_txt = INDEX_PATH.read_text(encoding="utf-8")
    week_txt = WEEK_PATH.read_text(encoding="utf-8")

    existing_html = {}
    for p in sorted(ROOT.rglob("*.html")):
        if p.name.lower() in ("main.html", "index.html"):
            continue
        m = re.match(r"^([A-Z]\d{2})\b", p.name)
        if m:
            existing_html[m.group(1)] = p.relative_to(ROOT).as_posix()

    update_readme_built_column(existing_html)

    domains = []
    for line in index_txt.splitlines():
        m = re.match(r"^\|\s*([A-Z])\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|$", line.strip())
        if m:
            letter, dname, pillar, count, t1, hours = m.groups()
            domains.append({
                "id": letter,
                "name": dname.strip(),
                "folder": DOMAIN_FOLDERS[letter],
                "pillar": int(pillar),
                "topics": int(count),
                "t1": int(t1),
                "hours": int(hours),
            })

    index_topics = {}
    for line in index_txt.splitlines():
        m = re.match(r"^\|\s*([A-Z]\d{2})\s*\|\s*(T[123])\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", line.strip())
        if m:
            tid, tier, wk, full_topic, kata, source = m.groups()
            full_topic = full_topic.strip()
            if ":" in full_topic:
                head, tail = full_topic.split(":", 1)
                short_from_full = head.strip()
                subtopics = [s.strip() for s in re.split(r"[,;]", tail) if s.strip()]
            elif ";" in full_topic:
                head, tail = full_topic.split(";", 1)
                short_from_full = head.strip()
                subtopics = [s.strip() for s in re.split(r"[,;]", tail) if s.strip()]
            else:
                short_from_full = full_topic
                subtopics = [s.strip() for s in full_topic.split(",") if s.strip()] if "," in full_topic else []
            index_topics[tid] = {
                "id": tid,
                "tier": tier,
                "week": int(wk),
                "fullTopic": full_topic,
                "shortFromFull": short_from_full,
                "subtopics": subtopics,
                "kata": kata.strip(),
                "source": source.strip(),
            }

    csv_topics = {}
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, 1):
            tid = row["ID"].strip()
            planned = row["Planned"].strip()
            csv_topics[tid] = {
                "order": idx,
                "shortTopic": row["Topic"].strip(),
                "status": row["Status"].strip() or "Not started",
                "conf": row["Conf"].strip(),
                "learnedOn": row["Learned on"].strip(),
                "retest7d": row["Retest 7d"].strip(),
                "done7d": row["Done 7d"].strip(),
                "retest30d": row["Retest 30d"].strip(),
                "done30d": row["Done 30d"].strip(),
                "planned": planned,
                "isoDate": planned_to_iso(planned),
                "min": int(row["Min"] or 45),
                "cards": int(row["Cards"] or 4),
            }

    weeks_meta = []
    week_blocks = re.split(r"^## Week (\d+):\s*([^\n]+)", week_txt, flags=re.M)
    for i in range(1, len(week_blocks), 3):
        wnum = int(week_blocks[i])
        wtitle = week_blocks[i + 1].strip()
        wbody = week_blocks[i + 2]
        focus_m = re.search(r"-\s*\*\*Focus:\*\*\s*(.+)", wbody)
        gate_m = re.search(r"-\s*\*\*Gate artifact:\*\*\s*(.+)", wbody)
        mock_m = re.search(r"-\s*\*\*Mock:\*\*\s*(.+)", wbody)
        load_m = re.search(r"-\s*\*\*Load:\*\*\s*(.+)", wbody)
        weeks_meta.append({
            "week": wnum,
            "title": wtitle,
            "focus": focus_m.group(1).strip() if focus_m else "",
            "gate": gate_m.group(1).strip() if gate_m else "",
            "mock": mock_m.group(1).strip() if mock_m else "",
            "load": load_m.group(1).strip() if load_m else "",
        })

    topics = []
    for tid, it in sorted(index_topics.items(), key=lambda x: (x[0][0], int(x[0][1:]))):
        ct = csv_topics.get(tid, {})
        dletter = tid[0]
        folder = DOMAIN_FOLDERS[dletter]
        short_title = ct.get("shortTopic") or it["shortFromFull"]
        has_page = tid in existing_html
        href = existing_html[tid] if has_page else f"{folder}/{tid} {short_title}.html"
        topics.append({
            "id": tid,
            "domain": dletter,
            "tier": it["tier"],
            "week": it["week"],
            "order": ct.get("order", 999),
            "planned": ct.get("planned", f"Week {it['week']}"),
            "isoDate": ct.get("isoDate", ""),
            "min": ct.get("min", 70 if it["tier"] == "T1" else 45 if it["tier"] == "T2" else 25),
            "cards": ct.get("cards", 8 if it["tier"] == "T1" else 4 if it["tier"] == "T2" else 2),
            "status": ct.get("status", "Not started"),
            "conf": ct.get("conf", ""),
            "learnedOn": ct.get("learnedOn", ""),
            "retest7d": ct.get("retest7d", ""),
            "retest30d": ct.get("retest30d", ""),
            "shortTitle": short_title,
            "fullTitle": it["fullTopic"],
            "subtopics": it["subtopics"],
            "kata": it["kata"],
            "source": it["source"],
            "hasPage": has_page,
            "href": href,
        })

    data_payload = {
        "domains": domains,
        "weeks": weeks_meta,
        "topics": topics,
    }

    # Read template from main.html and swap the JSON payload
    main_path = ROOT / "main.html"
    html_src = main_path.read_text(encoding="utf-8")
    new_json = json.dumps(data_payload, ensure_ascii=False)
    html_updated = re.sub(
        r'(<script id="dashboard-data" type="application/json">\s*).*?(\s*</script>)',
        lambda m: m.group(1) + new_json + m.group(2),
        html_src,
        flags=re.S,
    )
    # Also update hardcoded counts of ready labs in static markup if present
    ready_count = len(existing_html)
    html_updated = re.sub(r"All Generated \(\d+\)", f"All Generated ({ready_count})", html_updated)
    html_updated = re.sub(r"HTML Page Ready \(\d+\)", f"HTML Page Ready ({ready_count})", html_updated)

    main_path.write_text(html_updated, encoding="utf-8")
    (ROOT / "index.html").write_text(html_updated, encoding="utf-8")
    print(f"Synced main.html and index.html ({ready_count} built HTML pages, {len(topics)} total topics).")


if __name__ == "__main__":
    main()
