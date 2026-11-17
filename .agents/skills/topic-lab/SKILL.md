---
name: "topic-lab"
description: "Builds Richard's interactive study page for one AI Mastery topic and runs the recall drill. Use whenever he gives a topic ID like K06 or G01, says \"teach me\", \"next topic\", \"topic lab\", \"drill me\", \"retest\", \"mock me\" or \"review week N\", or opens a chat about any topic in the master index, even if he does not name the skill."
---

# Topic Lab

One topic in, one study session out: an interactive page Richard learns from and returns to, a kata he runs and breaks, a drill that makes him retrieve, and one line for his tracker.

## Why this exists

Richard understands concepts quickly. What he loses is retention over months and fluency under interview pressure. He was told his answers sound like a businessman's, and he was stumped by "How do you optimize tokens?". So this skill optimizes for three things, in order: he can **recall** it cold, he can **say** it like an engineer, and he has **built** a small version of it with his own hands.

A page that only explains well has failed. When you must choose between more explanation and more retrieval, choose retrieval. Reading feels like learning; answering from a blank page is learning.

If the project holds `00-core-brief.md` and `01-master-topic-index.md`, they carry his rules and the topic list. Read the topic's row in the index before anything else. If the index is missing, ask for the tier or assume T2 and say so.

## Modes

| He says | Mode |
|---|---|
| A topic ID or name, "teach me X", "next topic" | **learn** (default) |
| "drill me", "quiz me", or he pastes his own answer | **drill** |
| "retest K06", "7-day retest", "30-day retest" | **retest** |
| "mock me", "mock: system design" | **mock** |
| "review week 3", "review K06 G01 H03" | **review** |
| "what is today", "plan my day" | **plan** |

One topic per chat. If he drifts to another topic, answer in a few lines and suggest its own chat.

## Learn mode

### 1. Scope

- Find the row: ID, tier, week, kata idea, source.
- Fix the boundary: 3 to 7 subtopics for T1, 2 to 4 for T2, 1 or 2 for T3. Whatever belongs to a neighbouring ID stays out, with a pointer to that ID. Overlap costs him a day he does not have.
- Pick prerequisites and next topics from the index, by ID.
- If the topic is broad, take the slice interviews test and say which slice in the page's lede.

### 2. Get the facts right

He memorizes what the page says, so a wrong number becomes a wrong answer in an interview.

- Stable knowledge from memory is fine.
- Anything that moves gets checked against a primary source when you can search: prices, limits, product and model names, version flags, benchmark numbers, "current best". Note the date you checked.
- Without search, label it "from memory, verify" in the numbers table.
- Do not invent sources, papers, quotes or figures. Fewer real sources beat many plausible ones.

### 3. Write and run the kata before the page

The kata is the smallest program that makes the mechanism visible. It is for his understanding, not his portfolio.

- Under about 100 lines, one file, one command, no API key if a simulation can show the same thing. Runs on a laptop; a free GPU tier only when the topic needs a GPU.
- It prints numbers that carry the lesson. The page's warm-up questions and "what to notice" quote those numbers.
- It can be broken on purpose: flags or constants he flips to cause the failure (an OOM, a cache miss storm, a looping agent, a stale read).
- Run it yourself when you have a shell, and paste the real output. If you cannot run it, say so on the page, label the output "expected, not run", and prefer redesigning it as a simulation you can run.
- Start from the kata idea in the index. Sharpen it if a smaller program shows the idea better.

Some topics have a drill instead of code:

- **Design drills and case studies (Y):** the page gives the prompt, the clarifying questions to ask, the numbers to estimate, a rubric, and a reference design kept inside a closed `details` until he has attempted it. Offer to run it as a timed mock in chat.
- **Business, people and interview craft (V, W, X):** the page gives the framework, phrases to use, a role-play script, and a scoring rubric. Offer to play the counterpart in chat.
- **DSA katas (A21 to A26):** patterns first, then 3 problems written in your own words with solutions closed until attempted, each with complexity.

### 4. Build the page

You write two things: the content that goes inside `main`, and the cards JSON. The STYLE and SCRIPT blocks in the template at the end of this file are tested (self-grading, retest mode, timer, flashcards, Anki text, copy buttons, charts, explorables and steppers, light and dark themes, phone width) and must reach the page unchanged.

**With a shell (preferred).** Let the assembler copy those blocks for you. It saves about 260 lines of retyping per page and guarantees they are intact.

1. Save the kata as its own file, run it, and save its output: `python kata.py > output.txt`.
2. Write `content.html`: everything between `<main>` and `</main>`, following the content skeleton. Where code or output belongs, write `{{FILE:kata.py}}` or `{{FILE:output.txt}}`; the assembler inserts the escaped file, so the page shows exactly what ran.
3. Write `cards.json` in the cards format below.
4. Run this from the same folder, with the path of this SKILL.md (the skill's base directory is shown when the skill loads), the topic ID and the short name:

```bash
python3 - "/path/to/topic-lab/SKILL.md" K06 "KV cache" <<'PY'
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
exec(re.search(r"#@assembler-begin\n(.*?)#@assembler-end", src, re.S).group(1))
PY
```

It writes `K06.html` and `K06-cards.txt` and prints a short report. Fix anything it flags. If it reports that a fixed block fails its checksum, the skill file itself was damaged: take that block from the reference page instead and tell him.

**Without a shell, or if that file cannot be read.** Write the whole page by hand: the head, the STYLE block, your content, the cards JSON in a `script type="application/json" id="cards"` element, then the SCRIPT block, all copied exactly. Escape `&`, `<` and `>` in code blocks yourself.

Scale by tier:

| | T1 | T2 | T3 |
|---|---|---|---|
| Stations | All 11 | All 11, shorter; no scenario in station 7 | 2, 3, 4 and 5 merged, 8, 9, 11 |
| Explanation (stations 2 and 3) | 900 to 1,400 words | 500 to 800 | 250 to 400 |
| Kata | Full, 3 break-its | Full, 1 or 2 break-its | A 10-minute micro-exercise, or none |
| Traps | 3 or 4 | 2 | None |
| Question bank | 8 to 12, half with follow-ups | 5 to 7 | 3 |
| Visuals | 3 to 5: 1 to 3 steppers, at least one explorable | 2 or 3: 1 or 2 steppers | 1: the concept stepper |
| Cards | 8 | 4 | 2 |
| His time | 70 min | 45 min | 25 min |

Stations, in order. The numbering is the study loop, so keep it.

1. **Before you read.** Three questions the page will answer, at least one that a smart person gets wrong. Use numbers from the kata. He guesses first; guessing wrong and then seeing the answer is what makes it stick.
2. **The core idea.** Two short paragraphs, one mental model, and the concept stepper: the whole idea built up step by step (see Steppers). Close with a **memory hook**: an acronym, an image or a one-line story that lets him rebuild the spine of the topic (the ordered list, the formula, the three parts) weeks later. A hook must reconstruct real content; a slogan does not count.
3. **How it works.** The mechanism in `h3` blocks of about 120 words, with an explorable where a formula or tradeoff has a knob he can turn. Derive formulas instead of asserting them. Define each term where it first appears. Put a check question (`details.q`) after every two or three blocks so he retrieves while reading.
4. **Numbers to know cold.** A table: fact, value, status. Status is one of: derived, checked on a date, from memory verify, your own run.
5. **Tradeoffs.** A table: option, what you gain, what you pay, what to watch for. Every option has a price; name it.
6. **Kata.** One line on what it shows, the run command, the code, the real output, a chart of that output, "what to notice" (3 to 5 observations that cite actual numbers), "break it" (predict, then run), and a stretch.
7. **In production.** Symptom, likely cause, fix. What to monitor. For T1, one scenario question (an incident or a design call) with a stepwise answer.
8. **Interview.** The three-level answer written to be spoken, the timer, a weak answer against a strong one, the traps, then the question bank. **Traps** are 2 to 4 statements that sound right and are wrong (T1: 3 or 4, T2: 2, T3: none), each written as a quoted claim he must take apart before opening the answer. Pick the wrong beliefs a confident candidate actually says in interviews.
9. **Recall.** A blank-page prompt that starts with redrawing the concept stepper's final picture and narrating its steps from memory and lists what else to reproduce, a checklist to compare against, the flashcards, the Anki text.
10. **Mixed review.** Three questions from topics scheduled earlier than this one, labeled with their IDs, answers kept short. Interviews do not announce the topic, so practice should not either. In week 1, draw from the prerequisites.
11. **Sources.** Two to six primary sources, each with one line on what it supports and the date checked. If none were used, say so.

End with the tracker note in the footer.

**Retest mode is built into the page.** The Start a retest button hides every explanation and keeps the questions, the timer, the blank page and the flashcards, then records a score for the round. He uses it at 7 and 30 days. So everything he must be able to say has to exist as a question somewhere on the page: if a fact appears only in prose, he will never be retested on it. Keep `class="keep"` on the blank-page prompt and the recall box as the skeleton shows.

### Visualizations

Pictures are how he will remember the topic months later, and a slider he moves teaches a tradeoff faster than a paragraph. Each page gets small, focused visuals: T1 pages 3 to 5, T2 pages 2 or 3, T3 pages 1. Every page, whatever its tier, has at least one stepper. Each is a `figure.viz` with a one-line kind label (`.vt`) and a `figcaption` that starts with **Takeaway** and states the one point it makes.

Four kinds, each with a home on the page:

| Kind | Use it for | Built with | Usual station |
|---|---|---|---|
| Diagram | Structure: a flow, a stack, a pipeline, a memory layout, a timeline, a state machine, before and after | Inline SVG | 2, also 3 or 7 |
| Chart | Numbers: the kata's output, a comparison, growth with size, a breakdown | `data-bars` (no code) | 4, 5 or 6 |
| Stepper | The whole concept or one mechanism as a sequence: a request lifecycle, an algorithm running, data moving, a failure cascading, before and after a fix | SVG with `data-step` marks and an `ol.steps` caption list | 2 (always), also 3, 6 or 7 |
| Explorable | A formula or tradeoff with a knob: context length against memory, cache hits against cost, batch size against latency | Sliders and selects, plus a few lines registered with `TLQ` | 3 or 5 |

Rules:

- **One point per visual.** If the caption needs two sentences to say what it shows, split it or cut it. Never decorate.
- **Real numbers only.** Charts plot the kata's actual output or derived values. An explorable computes the same formula the page states, with the same constants, and its caption names where any price or limit came from. Nothing is invented to make a curve look good.
- **Predict, then move.** Every explorable opens with a `.ask` line: a question he answers before touching it. That turns the visual into retrieval practice instead of a toy.
- **Readable on a phone.** SVG `viewBox` at most 520 wide (around 360 is ideal), text at least 12 units, labels that never touch. Wide comparisons go in `data-bars`, which reflows by itself.
- **Theme-safe color.** Fill with the classes `c-accent`, `c-good`, `c-warn`, `c-bad`, `c-muted`, `c-soft`, `c-paper`, and stroke with `ink` or `ln`, so dark mode works. Color is never the only label: every colored part also has text.
- **Accessible.** Every SVG has `role="img"` and an `aria-label` that states what it shows in a full sentence. Charts get a `label` in their JSON or are described by their rows.
- **Small and self-contained.** A diagram is under about 40 lines of SVG. An explorable's script is under about 25 lines, written as `(window.TLQ=window.TLQ||[]).push(function(tl){ tl.viz("figure-id", function(v, fig){ ... }) })`. No libraries, no network, no storage.
- **Look at it.** When you have a browser or a way to render, open the page and check each visual at desktop and phone width, in light and dark. Fix overlaps before publishing.

The engine in the fixed script provides:

- `data-bars='{"rows":[{"label":"...","value":1.0,"tone":"good","text":"optional display"}],"unit":"","pre":"","digits":2,"max":optional}'` on any element: renders a labeled horizontal bar chart. Tones are `good`, `warn`, `bad`, `muted`, or none for the accent color. Write the JSON with double quotes inside single-quoted HTML.
- `tl.viz(id, render)`: reads every input and select in the figure into `v` by `name` (ranges are numbers; selects need `data-num` to be numbers), fills `<output data-for="name">` next to a slider with its value plus the output's `data-unit` (a select shows its own choice and needs no output), calls `render(v, fig, tl)` on load and on every change, and writes each key of the returned object into `[data-out="key"]`.
- `tl.bars(element, spec)`: the same chart, for redrawing inside an explorable.
- `tl.fmt(number, digits)`: a formatted number with thousands separators.

### Steppers

A stepper is an animation he controls. One SVG builds up one step at a time while a caption says what just happened and why. He can play it, step back and forward with buttons or arrow keys, or tick "Guess each step before you see it", which hides each caption until he has said it aloud. That last mode is the point: it turns the animation into retrieval practice.

Every page has a **concept stepper** in station 2: the whole topic end to end, so the sequence he walks through is the same one he will narrate in an interview. T1 and T2 pages add **mechanism steppers** where a part of the topic is itself a process: how an algorithm runs (an HNSW search hopping layers, a Raft election), how data moves (prefill then decode), how a failure spreads (a cache stampede, a retry storm), or what changes before and after a fix. T1 pages have 1 to 3 steppers, T2 pages 1 or 2, T3 pages the concept stepper alone.

How to write one:

- **4 to 8 steps** for the concept stepper, 3 to 6 for a mechanism stepper. Each step adds or changes one thing in the picture.
- **Captions are cause and effect,** one sentence of at most about 25 words: what happened, and why it matters. At least one step carries a number, and one shows where it breaks or what it costs.
- **The final frame is the full diagram.** Redrawing it from memory is the recall exercise, so it must make sense on its own, with labels on every part.
- **Marks on SVG elements:** `data-step="3"` appears at step 3 and stays; `data-only="3 4"` shows only on those steps; `data-hi="3"` outlines or bolds on those steps. Group elements with `<g data-step="n">`. Elements with no mark are the scaffold, visible throughout.
- **The `ol.steps` list** holds one `li` per step, in order. The engine hides it and shows the current caption; without JavaScript the list stays readable.
- **Same picture rules as diagrams:** at most 520 wide, theme classes for color, text on every colored part, an `aria-label` describing the final frame.

Retest mode hides every figure, because the recall section asks him to redraw the concept stepper's final picture and narrate its steps from a blank page. The sequence he can narrate is the one he understands.

Writing rules for the page: plain, direct sentences in second person. No em dashes. No filler, hype or throat-clearing. Use his real units and terms. Where it fits naturally, tie the topic to something he has built (voice AI for clinics, data erasure, state space models on edge hardware, agents, evals); do not force it.

Technical rules for the page:

- It runs in a sandbox. No file downloads, no alert or prompt, no external scripts or images. Fonts from Google Fonts are allowed. The template already works within this; do not add export buttons.
- The script adds, by itself: copy buttons, self-grading on every `details.q`, the score line, a button that copies shaky and missed questions as question-log rows, the retest bar, the timer, the flashcards, and the rendering of `data-bars` charts, `TLQ` explorables and steppers. Do not write your own versions of these.
- Answers hidden in `details` are deliberate. Everything else is visible at load.
- Outside `{{FILE:...}}` includes, escape `&`, `<` and `>` in code shown inside `pre` blocks. Do not escape the JavaScript inside an explorable's `script` element; it runs as written.
- Card answers are plain text.
- The page title is `ID Short name` with no subtitle.

### 5. Check, then publish

Before publishing, confirm:

- Every number on the page is derived, sourced, from the kata's real output, or labeled unverified.
- The kata on the page is the code that ran, and its output is pasted, not paraphrased.
- Each question can be answered from the page, and no answer is hidden only in a diagram.
- Every fact worth remembering is asked by at least one question or card, so retest mode covers it.
- The visual count matches the tier and the concept stepper is in station 2, every stepper has 3 or more cause-and-effect steps, every visual has a takeaway caption, every chart's numbers trace to the kata or a formula on the page, and each explorable opens with a prediction question.
- The three-level answer can be spoken in about 90 seconds (roughly 200 to 230 words).
- Card count matches the tier, and every card passes the card rules.
- No em dashes, and the assembler's report is clean.

Publish the page as an HTML artifact when an artifact tool is available, titled `ID Short name`. One artifact per topic: when he asks for a change to a page that already exists, republish that artifact instead of making a second one. Otherwise send `ID.html` as a file. When you can send files, also send the kata source and `ID-cards.txt`. Anki imports files, so the cards file is what he will actually use.

### 6. Reply in chat

Keep it to a few lines: what the page is, his time budget, anything unverified or not run, and "Start at station 1. Say 'drill me' when you have closed the page." Do not summarize the content in chat. Reading it there replaces the retrieval he needs to do.

## Cards

Cards are what carries a topic across months, so they get the most care per word.

- One idea per card, in question form, answerable in under about 25 words.
- Weight them toward why, when, what breaks and how much. A definition card ("What is X?") is the weakest kind; write "Why does X raise batch size?" instead.
- At least one number or formula card when the topic has numbers. At most one list card per topic, for the spine.
- Each question must make sense without the page. The script adds the topic ID in front.
- No yes-or-no questions. No card for a fact that is labeled unverified.

The deck is `AI Mastery::` plus the domain letter and name. Tags are the ID, the tier and the two-digit week. The format is under "Cards file" in the template.

## Answers

Every model answer, on the page and in drills, has three levels:

1. **Outcome** (about 20 seconds): what it does and why it matters.
2. **Mechanism** (about 45 seconds): how it works, step by step.
3. **Internals and limits** (about 25 seconds): the numbers, the failure modes, where it stops working.

Engineer voice means the answer contains a mechanism, a number, a failure mode and a tradeoff. Business framing may follow in one sentence; it never replaces them. On every T1 page show one weak answer and one strong answer to the same question. If the strong example uses illustrative numbers, say so, so he does not quote them as his own results.

## Drill mode

Run this after he has closed the page. The point is effortful retrieval with honest feedback.

- One question at a time. Wait for his answer. No hints before he commits.
- T1: 8 questions. T2: 5. T3: 3. Open with "explain it in 90 seconds", then mix why, numbers, tradeoff and a debugging or design scenario. Include two follow-ups that push one level past his last answer, and one question from an earlier topic.
- After each answer: the level he reached (1, 2 or 3), what was right, what was missing in one or two lines, and the stronger wording for the missing part only. Do not reteach the page.
- If an answer is business-voiced (outcomes and ROI with no mechanism or number), say so and ask him to redo it.
- Grade honestly. An inflated grade here costs him in the real interview.
- If he pastes a transcript of a recorded answer, grade it on the same three levels and add delivery notes: structure, length, filler.

Close with: a scorecard table, his top three gaps, new cards for those gaps in Anki format, question-log lines, and what to set on the tracker row, including a suggested confidence from 1 to 5.

## Retest mode

For the 7-day and 30-day retests, when he would rather be questioned than use the page's own retest button. No page, no reteaching.

- Look up the topic's row. Ask 5 questions for T1, 3 for T2, 2 for T3, one at a time: the 90-second answer first, then questions worded differently from the page's question bank, so he retrieves the idea and not the sentence.
- Grade as in drill mode. Passing means level 2 or better on every question, with the numbers right.
- Close with what to set on the row: tick Done 7d or Done 30d if he passed; set Status to Shaky if he did not, and give the question-log lines. After a passed 30-day retest, Status becomes Solid.

## Plan mode

Read `02-week-plan.md`, find today's date, and list today's topics in order with tiers and minutes, T1 first. If he is behind, apply the slip rule from the core brief: T1 topics stay in their week, T3 slides first, then T2. Do not rebuild the plan; pick what to do today.

## Mock mode

Ask which round if he has not said: coding, ML and LLM deep dive, system design, AI system design, live debugging, FDE decomposition, customer simulation, behavioral.

- Be the interviewer. One prompt at a time, realistic pacing, interruptions and follow-ups. State the time box and keep it.
- No teaching during the mock.
- Afterwards: a scorecard (problem framing, technical depth, tradeoffs, communication, engineer voice), the three strongest moments, three gaps with model answers, question-log lines, the Mocks line, and the topic IDs to revisit.

## Review mode

For a week or a list of IDs: 10 to 15 rapid questions interleaved across the topics, weighted toward T1 and anything he has marked shaky. Same grading as drill mode. End with which topics need a retest. No new page.

## Closing a session

His tracker is a sheet with four tabs: Topics, Progress, Question log, Mocks. Give him things he can paste straight in.

**Tracker.** Tell him what to set on the topic's row in Topics: Status (Not started, In progress, Learned, Shaky or Solid), Conf (1 to 5) and Learned on (today's date). Retest dates fill in by themselves. Use Learned when the package is complete, Shaky when a drill or retest went badly, Solid after he passes the 30-day retest.

**Question log.** One line per missed or shaky question, tab-separated so it pastes into columns, in this order: Date, Question, Topic, Level reached, What was missing, Model answer, Retest due (seven days out). The page's "Copy shaky and missed" button produces the same columns for questions he graded himself; the lines you write are for questions asked in chat.

```
2026-11-19	Why does prompt caching only work on a prefix?	G01	1	The causal-attention reason	Each token's state depends on all tokens before it, so reuse stops at the first difference.	2026-11-26
```

**Mocks.** After a mock, one tab-separated line: Date, Round, Topics covered, Score (1 to 5), Strongest moments, Gaps, Topic IDs to revisit.

## Template

### Content skeleton

This is what goes in `content.html`. Replace the capitalized placeholders, repeat components as needed, and delete stations the tier does not use. A finished reference build is the artifact titled "G01 Token optimization".

```html
<header>
  <div class="eyebrow"><b>ID</b><span>DOMAIN NAME</span><span>Tier N</span><span>Week N</span><span>NN min</span></div>
  <h1>SHORT NAME</h1>
  <p class="lede">THE QUESTION THIS PAGE ANSWERS, IN ONE OR TWO SENTENCES.</p>
  <div class="chips"><span><em>Before</em>ID Name</span><span><em>After</em>ID Name</span></div>
</header>

<nav class="path" aria-label="Study path"><h2>Study path</h2><ol>
  <li><label><input type="checkbox" id="step-1"><span>STEP</span><small>N min</small></label></li>
  <!-- five or six steps: warm-up, read, kata, production and interview, blank-page recall, record and import cards -->
</ol></nav>

<section class="st" id="warmup"><h2 data-n="1">Before you read</h2>
  <p class="sub">Guess first. A wrong guess now makes the right answer stick later.</p>
  <details class="q"><summary>QUESTION</summary><div class="a">ANSWER</div></details>
</section>

<section class="st" id="idea"><h2 data-n="2">The core idea</h2>
  <p>TEXT</p>
  <figure class="viz stepper" id="viz-concept">
    <div class="vt">Stepper: THE WHOLE CONCEPT, END TO END</div>
    <svg viewBox="0 0 360 220" role="img" aria-label="THE FINAL PICTURE, DESCRIBED IN A FULL SENTENCE">
      <g font-size="12">
        <g data-step="1"><rect x="10" y="20" width="90" height="40" class="c-accent" data-hi="1"/><text x="55" y="80" text-anchor="middle">LABEL</text></g>
        <g data-step="2"><path d="M100 40 H140" class="ink"/><rect x="140" y="20" width="90" height="40" class="c-good" data-hi="2"/><text x="185" y="80" text-anchor="middle">LABEL</text></g>
        <g data-only="3"><text x="10" y="120" class="m">A NOTE SHOWN ONLY ON STEP 3</text></g>
      </g>
    </svg>
    <ol class="steps">
      <li>STEP 1: WHAT ENTERS OR STARTS, IN ONE CAUSE-AND-EFFECT SENTENCE.</li>
      <li>STEP 2: WHAT HAPPENS NEXT AND WHY.</li>
      <li>STEP 3: WHERE IT BREAKS OR WHAT IT COSTS, WITH A NUMBER.</li>
    </ol>
    <figcaption><b>Takeaway.</b> THE ONE POINT THE WHOLE SEQUENCE MAKES.</figcaption>
  </figure>
  <div class="box hook"><b>Memory hook</b><p>AN ACRONYM, IMAGE OR ONE-LINE STORY THAT REBUILDS THE SPINE OF THE TOPIC.</p></div>
</section>

<section class="st" id="mechanism"><h2 data-n="3">How it works</h2>
  <h3>BLOCK TITLE</h3>
  <p>TEXT</p>
  <div class="codewrap"><pre>FORMULA OR SHORT SNIPPET</pre></div>
  <figure class="viz" id="viz-explore">
    <div class="vt">Explore: THE QUESTION THE SLIDERS ANSWER</div>
    <p class="ask">Predict first. A QUESTION HE ANSWERS BEFORE TOUCHING ANYTHING.</p>
    <div class="ctl">
      <label><span>INPUT NAME</span><input type="range" name="x" min="1" max="100" step="1" value="10"><output data-for="x" data-unit=" UNIT"></output></label>
      <label><span>CHOICE NAME</span><select name="k" data-num><option value="1">OPTION A</option><option value="2">OPTION B</option></select></label>
    </div>
    <div data-chart></div>
    <p class="readout" data-out="verdict"></p>
    <figcaption><b>Takeaway.</b> WHAT MOVING THE INPUTS SHOWS.</figcaption>
  </figure>
  <script>(window.TLQ=window.TLQ||[]).push(function(tl){tl.viz("viz-explore",function(v,fig){
    var a=v.x*v.k, b=v.x*2;  /* the page's own formula, nothing invented */
    tl.bars(fig.querySelector("[data-chart]"),{unit:" UNIT",rows:[{label:"OPTION A",value:a,tone:"muted"},{label:"OPTION B",value:b,tone:"good"}]});
    return {verdict:"ONE SENTENCE THAT READS THE RESULT, WITH THE NUMBER"};
  })});</script>
  <details class="q"><summary>Check: QUESTION</summary><div class="a">ANSWER</div></details>
</section>

<section class="st" id="numbers"><h2 data-n="4">Numbers to know cold</h2>
  <div class="scroll"><table><tr><th>Fact</th><th>Value</th><th>Status</th></tr>
    <tr><td>FACT</td><td class="n">VALUE</td><td>Derived | Checked DATE | From memory, verify | Your own run</td></tr></table></div>
</section>

<section class="st" id="tradeoffs"><h2 data-n="5">Tradeoffs</h2>
  <div class="scroll"><table><tr><th>Option</th><th>You gain</th><th>You pay</th><th>Watch for</th></tr>
    <tr><td>OPTION</td><td>GAIN</td><td>PRICE</td><td>SIGNAL</td></tr></table></div>
</section>

<section class="st" id="kata"><h2 data-n="6">Kata: NAME</h2>
  <p>WHAT IT SHOWS.</p>
  <p class="cap">Run</p><div class="codewrap"><pre data-copy>python kata.py</pre></div>
  <p class="cap">kata.py</p><div class="codewrap"><pre data-copy>{{FILE:kata.py}}</pre></div>
  <p class="cap">Output from a real run</p><div class="codewrap"><pre class="out">{{FILE:output.txt}}</pre></div>
  <figure class="viz">
    <div class="vt">Chart: WHAT THE KATA MEASURED</div>
    <div data-bars='{"unit":"","digits":2,"rows":[{"label":"BASELINE","value":1.0,"tone":"muted"},{"label":"CHANGE","value":0.5,"tone":"good"}]}'></div>
    <figcaption><b>Takeaway.</b> WHAT THE NUMBERS FROM THE REAL RUN SHOW.</figcaption>
  </figure>
  <h3>What to notice</h3><ol><li>OBSERVATION WITH A NUMBER FROM THE OUTPUT</li></ol>
  <div class="box break"><b>Break it</b><ol><li><strong>NAME.</strong> THE CHANGE, AND THE QUESTION TO PREDICT BEFORE RUNNING.</li></ol></div>
  <p><strong>Stretch.</strong> TEXT</p>
</section>

<section class="st" id="production"><h2 data-n="7">In production</h2>
  <div class="scroll"><table><tr><th>Symptom</th><th>Likely cause</th><th>Fix</th></tr><tr><td>SYMPTOM</td><td>CAUSE</td><td>FIX</td></tr></table></div>
  <p><strong>Monitor:</strong> TEXT</p>
  <details class="q"><summary>Scenario: SITUATION AND QUESTION</summary><div class="a"><ol><li>STEP</li></ol></div></details>
</section>

<section class="st" id="interview"><h2 data-n="8">Interview</h2>
  <p class="sub">Say this aloud against the clock. Three levels, about 90 seconds.</p>
  <div class="levels">
    <div><b>1 Outcome <span>20 s</span></b>TEXT</div>
    <div><b>2 Mechanism <span>45 s</span></b>TEXT</div>
    <div><b>3 Internals and limits <span>25 s</span></b>TEXT</div>
  </div>
  <div class="timer"><button class="primary" id="timer-btn" data-seconds="90">Start 90 seconds</button><output id="timer-out" for="timer-btn">1:30</output></div>
  <div class="box voice"><b>Say it like an engineer</b><p class="weak">"WEAK ANSWER"</p><p class="strong">"STRONG ANSWER"</p><p>WHY THE STRONG ONE IS STRONG.</p></div>
  <h3 class="keep">Traps</h3>
  <p class="sub keep">Each one sounds right. Say what is wrong with it before you open it.</p>
  <details class="q"><summary>"A STATEMENT THAT SOUNDS RIGHT AND IS WRONG."</summary><div class="a">WHY IT IS WRONG, WITH THE NUMBER OR MECHANISM THAT SHOWS IT.</div></details>

  <h3 class="keep">Question bank</h3>
  <p class="sub">Answer aloud, then open. Grade yourself honestly.</p>
  <p class="score" id="score" aria-live="polite"></p>
  <details class="q"><summary>QUESTION</summary><div class="a">ANSWER<div class="f"><b>Follow-up</b>QUESTION, THEN A SHORT ANSWER</div></div></details>
</section>

<section class="st" id="recall"><h2 data-n="9">Recall</h2>
  <p class="keep"><strong>Blank page.</strong> Hide everything above. From memory, redraw the concept stepper's final picture and narrate its steps, then write: WHAT TO REPRODUCE.</p>
  <textarea id="recall-box" class="keep" aria-label="Write your recall here" placeholder="Write from memory. This box saves a draft in this browser only."></textarea>
  <details class="q"><summary>Compare with the checklist</summary><div class="a"><ul><li>ITEM</li></ul></div></details>
  <h3 class="keep">Flashcards</h3>
  <div class="deck" id="deck"></div>
  <h3>Anki import</h3>
  <p class="sub">Use the cards file sent in the chat, or copy this into a text file and import it. If your Anki version ignores the header lines, pick the deck and the Basic note type in the import dialog.</p>
  <textarea class="tsv" id="anki" readonly aria-label="Anki import text"></textarea>
  <div class="deckbar"><button id="anki-copy">Copy Anki text</button></div>
</section>

<section class="st" id="mixed"><h2 data-n="10">Mixed review</h2>
  <p class="sub">Three questions from earlier topics. Nobody tells you the topic in an interview.</p>
  <details class="q"><summary>ID: QUESTION</summary><div class="a">ANSWER</div></details>
</section>

<section class="st" id="sources"><h2 data-n="11">Sources</h2>
  <ul class="srcs"><li><a href="URL">PUBLISHER: TITLE</a><small>WHAT IT SUPPORTS. Checked DATE.</small></li></ul>
</section>

<footer><p>When you finish, on this topic's row in the tracker</p><div class="trackline">Status: Learned | Conf: 1 to 5 | Learned on: today | retest dates fill in by themselves</div>
  <p>At 7 and 30 days: open this page, press Start a retest, answer cold, then tick Done 7d or Done 30d on the row.</p></footer>
```

### Cards file

```json
{"deck":"AI Mastery::K Inference engineering and hardware","tags":"K06 T1 W01","cards":[{"q":"...","a":"..."}]}
```

### Assembler

```python
#@assembler-begin
import html, json, sys, zlib
tid, name = sys.argv[2], sys.argv[3]
CRC = {"STYLE": 2800455163, "SCRIPT": 3606185793}
flags = []
def block(tag):
    b = re.search(r"<!-- TOPIC-LAB:%s .*?<!-- /TOPIC-LAB:%s -->" % (tag, tag), src, re.S).group(0)
    if zlib.crc32(re.sub(r"\s+", "", b).encode("utf-8")) != CRC[tag]:
        flags.append("the fixed %s block in SKILL.md does not match its checksum: copy that block from the reference page G01 Token optimization, then tell Richard the skill file needs repair" % tag)
    return b
def include(m):  # {{FILE:path}} becomes the escaped contents of that file
    return html.escape(open(m.group(1).strip(), encoding="utf-8").read().rstrip("\n"), quote=False)
body = re.sub(r"\{\{FILE:([^}]+)\}\}", include, open("content.html", encoding="utf-8").read())
cards = json.load(open("cards.json", encoding="utf-8"))
page = "\n".join([
    '<!DOCTYPE html>', '<html lang="en">', '<head>', '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    "<title>%s</title>" % html.escape(tid + " " + name), block("STYLE"), "</head>",
    '<body data-topic="%s">' % tid, "<main>", body.strip(), "</main>",
    '<script type="application/json" id="cards">',
    json.dumps(cards, ensure_ascii=False).replace("<", "\\u003c"), "</script>", block("SCRIPT"), "</body>", "</html>", ""])
open(tid + ".html", "w", encoding="utf-8").write(page)
quote = lambda s: '"' + s.replace('"', '""').replace("\t", " ").replace("\n", "<br>") + '"'
rows = ["#separator:tab", "#html:true", "#notetype:Basic", "#deck:" + cards["deck"], "#tags column:3"]
rows += [quote("[%s] %s" % (tid, c["q"])) + "\t" + quote(c["a"]) + "\t" + quote(cards["tags"]) for c in cards["cards"]]
open(tid + "-cards.txt", "w", encoding="utf-8").write("\n".join(rows) + "\n")
spoken = " ".join(re.findall(r'<div><b>\d [^<]*<span>[^<]*</span></b>(.*?)</div>', body, re.S))
if chr(8212) in page or chr(8211) in page: flags.append("dash characters found: rewrite those sentences")
if "{{" in body: flags.append("an unfilled {{...}} placeholder is left in the content")
if 'id="recall-box"' in body and body.count('class="keep"') < 2: flags.append('the blank-page prompt and the recall box both need class="keep", or retest mode hides them')
if 'id="interview"' in body and 'class="box hook"' not in body: flags.append("no memory hook: add one in station 2 (skip this flag only on a T3 page)")
if re.search(r">\s*(QUESTION|ANSWER|TEXT|SHORT NAME|DOMAIN NAME|STEP|ITEM|FACT|VALUE|LABEL)\s*<", body): flags.append("a template placeholder word is left in the content")
nviz = len(re.findall(r'<figure class="viz[ "]', body))
if nviz == 0: flags.append("no visualization: T1 pages need 3 to 5, T2 pages 2 or 3, T3 pages 1, always including a stepper")
steppers = re.findall(r'<figure class="viz stepper"(.*?)</figure>', body, re.S)
if not steppers: flags.append("no stepper: every page needs at least one, the concept stepper in station 2")
for st in steppers:
    k = len(re.findall(r"<li>", st.split('<ol class="steps">')[-1])) if '<ol class="steps">' in st else 0
    if k < 3: flags.append("a stepper has fewer than 3 steps in its ol.steps list")
    nums = [int(x) for x in re.findall(r'data-(?:step|only|hi)="([\d ,]+)"', st) for x in re.split(r"[ ,]+", x.strip()) if x]
    if nums and max(nums) > k: flags.append("a stepper refers to step %d but lists only %d steps" % (max(nums), k))
if body.count("<figcaption>") < nviz: flags.append("a figure.viz has no figcaption: every visual states its takeaway")
for w in re.findall(r'<svg[^>]*viewBox="0 0 (\d+)', body):
    if int(w) > 520: flags.append("an SVG viewBox is %s wide: text will be unreadable on a phone; keep it at 520 or less, or use data-bars" % w)
for raw in re.findall(r"data-bars='([^']*)'", body):
    try: json.loads(html.unescape(raw))
    except ValueError: flags.append("a data-bars attribute is not valid JSON")
if any(len(c["a"].split()) > 30 for c in cards["cards"]): flags.append("a card answer runs past 30 words")
if any(c["q"].strip().lower().startswith(("is ", "does ", "do ", "can ", "are ")) for c in cards["cards"]): flags.append("a card looks like a yes-or-no question")
words = len(re.sub(r"<[^>]+>", " ", spoken).split())
print("%s.html: %d bytes, %d questions, %d cards, %d visuals (%d steppers), %s" % (tid, len(page.encode("utf-8")), body.count('<details class="q"'), len(cards["cards"]), nviz, len(steppers),
    "three-level answer %d words (aim for 200 to 230)" % words if words else "no three-level answer (expected only on a T3 page)"))
print("\n".join("FIX: " + f for f in flags) if flags else "No problems flagged.")
#@assembler-end
```

### Fixed blocks

Do not edit these. The assembler reads them from here.

```html
<!-- TOPIC-LAB:STYLE v4 (copy verbatim) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&amp;family=IBM+Plex+Mono:wght@400;500&amp;family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap" rel="stylesheet">
<style>
/* Layout idea: one reading column on cool drafting paper, numbered stations down a left rule, like a lab protocol. */
:root{
  --paper:#f2f4f8; --surface:#ffffff; --ink:#101a2b; --muted:#56637b; --line:#d3dae6;
  --accent:#1f4fd8; --accent-soft:#e3e9fb; --good:#12784a; --warn:#a85a08; --bad:#b3261e;
  --code-bg:#0e1626; --code-ink:#e4eaf6;
  --display:"Bricolage Grotesque","Avenir Next","Segoe UI",sans-serif;
  --body:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#0b111c; --surface:#131b2b; --ink:#e7ecf6; --muted:#9aa6bd; --line:#27334b;
  --accent:#8eaaff; --accent-soft:#1a2644; --good:#5fd39a; --warn:#f0b05a; --bad:#ff8f85;
  --code-bg:#080d17; --code-ink:#dde5f3; color-scheme:dark}}
:root[data-theme="dark"]{
  --paper:#0b111c; --surface:#131b2b; --ink:#e7ecf6; --muted:#9aa6bd; --line:#27334b;
  --accent:#8eaaff; --accent-soft:#1a2644; --good:#5fd39a; --warn:#f0b05a; --bad:#ff8f85;
  --code-bg:#080d17; --code-ink:#dde5f3; color-scheme:dark}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:400 1rem/1.62 var(--body)}
main{max-width:46rem;margin:0 auto;padding:2rem 1.15rem 5rem}
h1,h2,h3{font-family:var(--display);line-height:1.15;text-wrap:balance;margin:0}
h1{font-size:clamp(2rem,6vw,2.9rem);font-weight:700;letter-spacing:-.02em}
h2{font-size:1.5rem;font-weight:700}
h3{font-size:1.08rem;font-weight:600;margin-top:1.5rem}
p{margin:.7rem 0} ul,ol{padding-left:1.25rem;margin:.6rem 0} li{margin:.25rem 0}
a{color:var(--accent)} strong{font-weight:600}
code{font:500 .88em var(--mono);background:var(--accent-soft);padding:.08em .32em;border-radius:4px}
.eyebrow{font:500 .78rem var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);display:flex;flex-wrap:wrap;gap:.3rem .9rem;margin-bottom:.8rem}
.eyebrow b{color:var(--accent);font-weight:500}
.lede{font-size:1.13rem;color:var(--muted);max-width:40rem}
.chips{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:1rem;font-size:.85rem}
.chips span{border:1px solid var(--line);border-radius:999px;padding:.12rem .65rem;background:var(--surface)}
.chips em{font-style:normal;color:var(--muted);margin-right:.2rem}
.path{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:1rem 1.1rem;margin:1.6rem 0 0}
.path h2{font-size:1rem;margin-bottom:.4rem}
.path ol{list-style:none;padding:0;margin:0;display:grid;gap:.15rem}
.path label{display:flex;gap:.6rem;align-items:baseline;cursor:pointer;padding:.15rem 0}
.path input{accent-color:var(--accent);transform:translateY(2px)}
.path small{color:var(--muted);font:400 .78rem var(--mono);margin-left:auto;white-space:nowrap;padding-left:.6rem}
.path input:checked+span{color:var(--muted);text-decoration:line-through}
section.st{margin-top:3rem;padding-left:1.1rem;border-left:2px solid var(--line)}
section.st>h2{display:flex;gap:.7rem;align-items:baseline;margin-left:-1.1rem;padding-left:1.1rem;position:relative}
section.st>h2::before{content:attr(data-n);font:500 .8rem var(--mono);color:var(--surface);background:var(--accent);border-radius:4px;padding:.12rem .42rem;position:relative;top:-.2rem}
.sub{color:var(--muted);margin-top:.3rem}
details.q{background:var(--surface);border:1px solid var(--line);border-radius:10px;margin:.6rem 0;overflow:hidden}
details.q>summary{cursor:pointer;padding:.75rem 1rem;font-weight:500;list-style:none;display:flex;gap:.7rem}
details.q>summary::-webkit-details-marker{display:none}
details.q>summary::before{content:"Q";font:500 .78rem var(--mono);color:var(--accent);border:1px solid var(--accent);border-radius:4px;padding:0 .35rem;height:1.45rem;line-height:1.4rem;flex:none}
details.q[open]>summary{border-bottom:1px solid var(--line)}
details.q .a{padding:.6rem 1rem .9rem}
details.q .f{margin:.5rem 0 0;padding:.5rem .8rem;border-left:3px solid var(--accent);background:var(--accent-soft);border-radius:0 6px 6px 0;font-size:.95rem}
details.q .f b{font:500 .75rem var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--accent);display:block}
.grade{display:flex;flex-wrap:wrap;gap:.4rem;align-items:center;padding:.1rem 1rem .85rem;font-size:.85rem;color:var(--muted)}
button{font:500 .85rem var(--body);color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:7px;padding:.36rem .75rem;cursor:pointer}
button:hover{border-color:var(--accent)} button:focus-visible,summary:focus-visible,textarea:focus-visible,input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
button.primary{background:var(--accent);border-color:var(--accent);color:var(--surface)}
details.q[data-g="got"]{border-left:4px solid var(--good)} details.q[data-g="shaky"]{border-left:4px solid var(--warn)} details.q[data-g="missed"]{border-left:4px solid var(--bad)}
.grade button[aria-pressed="true"]{border-color:var(--ink);font-weight:600}
.score{font:500 .82rem var(--mono);color:var(--muted);margin:.6rem 0}
.scroll{overflow-x:auto;margin:.9rem 0;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:.93rem}
th,td{text-align:left;vertical-align:top;padding:.55rem .8rem;border-bottom:1px solid var(--line)}
th{font:500 .74rem var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--muted);white-space:nowrap}
tr:last-child td{border-bottom:0} td.n{font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}
.codewrap{position:relative;margin:.9rem 0}
pre{margin:0;background:var(--code-bg);color:var(--code-ink);font:400 .8rem/1.55 var(--mono);padding:1rem;border-radius:10px;overflow-x:auto;tab-size:4}
pre.out{border-left:4px solid var(--accent)}
.codewrap>button{position:absolute;top:.5rem;right:.5rem;font-size:.75rem;padding:.2rem .55rem;opacity:.9}
.cap{font:500 .75rem var(--mono);color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin:1.1rem 0 -.4rem}
.box{border-radius:10px;padding:.85rem 1rem;margin:1rem 0;background:var(--surface);border:1px solid var(--line)}
.box>b:first-child{font:500 .75rem var(--mono);text-transform:uppercase;letter-spacing:.05em;display:block;margin-bottom:.2rem}
.box.model>b:first-child{color:var(--accent)} .box.break{border-left:4px solid var(--warn)} .box.break>b:first-child{color:var(--warn)}
.box.voice{border-left:4px solid var(--good)} .box.voice>b:first-child{color:var(--good)}
.box.hook{border-left:4px solid var(--accent)} .box.hook>b:first-child{color:var(--accent)}
.weak{color:var(--muted)} .weak::before{content:"Weak: ";font-weight:600;color:var(--bad)} .strong::before{content:"Strong: ";font-weight:600;color:var(--good)}
.levels{display:grid;gap:.6rem;margin:1rem 0}
.levels>div{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:.8rem 1rem}
.levels b{font:500 .75rem var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--accent);display:flex;justify-content:space-between;gap:1rem;margin-bottom:.2rem}
.levels b span{color:var(--muted)}
.timer{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;margin:.8rem 0}
.timer output{font:500 1.3rem var(--mono);font-variant-numeric:tabular-nums;min-width:4ch}
textarea{width:100%;min-height:11rem;font:400 .95rem/1.5 var(--body);color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:.8rem;resize:vertical}
textarea.tsv{min-height:7rem;font:400 .76rem/1.45 var(--mono);white-space:pre;overflow:auto}
.deck{margin:1rem 0}
.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;min-height:11.5rem;padding:1.2rem 1.3rem;display:flex;flex-direction:column;gap:.5rem;cursor:pointer}
.card .side{font:500 .72rem var(--mono);text-transform:uppercase;letter-spacing:.06em;color:var(--muted);display:flex;justify-content:space-between}
.card .txt{font-size:1.12rem;margin:auto 0}
.card.back{border-color:var(--accent);background:var(--accent-soft)}
.deckbar{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.6rem;align-items:center}
.deckbar .count{font:500 .82rem var(--mono);color:var(--muted);margin-left:auto}
svg{max-width:100%;height:auto;display:block}
svg text{font-family:var(--mono);fill:var(--ink)} svg .m{fill:var(--muted)}
.srcs li{margin:.4rem 0} .srcs small{color:var(--muted);display:block}
.trackline{font:400 .85rem var(--mono);background:var(--surface);border:1px dashed var(--line);border-radius:8px;padding:.7rem .9rem;overflow-x:auto;white-space:nowrap}
footer{margin-top:3rem;color:var(--muted);font-size:.85rem}
.rt{display:flex;flex-wrap:wrap;gap:.5rem .6rem;align-items:center;margin-top:.8rem;padding-top:.8rem;border-top:1px solid var(--line)}
.rt p{margin:0;flex:1 1 15rem;font-size:.85rem;color:var(--muted)}
.rt-only{display:none}
/* Retest mode: the explanations go, the questions stay. */
body.retest .rt-only{display:inline-block}
body.retest .path h2,body.retest .path ol{display:none} body.retest .rt{margin-top:0;padding-top:0;border-top:0}
body.retest section.st>:not(h2):not(details):not(.timer):not(.deck):not(.score):not(.keep):not(.show){display:none}
body.retest section.st:not(:has(details.q,.timer,.deck)){display:none}
/* Visualizations: diagrams, charts and explorables. Each figure makes one point. */
figure.viz{margin:1.2rem 0;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:1rem 1rem .85rem}
figure.viz svg{width:100%;max-width:30rem;margin:0 auto}
figure.viz figcaption{font-size:.9rem;color:var(--muted);margin-top:.75rem}
figure.viz figcaption b{color:var(--ink);font-weight:600}
.viz .vt{font:500 .74rem var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin-bottom:.6rem}
.viz .ask{font-size:.92rem;margin:0 0 .8rem;padding:.45rem .75rem;border-left:3px solid var(--warn);background:var(--paper);border-radius:0 6px 6px 0}
.viz .ctl{display:grid;gap:.55rem;margin:0 0 .9rem}
.viz .ctl label{display:grid;grid-template-columns:minmax(7rem,34%) 1fr 5.5rem;gap:.6rem;align-items:center;font-size:.88rem}
.viz input[type=range]{width:100%;accent-color:var(--accent)}
.viz select{font:500 .85rem var(--body);color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:.25rem .4rem}
.viz output{font:500 .82rem var(--mono);text-align:right;font-variant-numeric:tabular-nums}
.viz .readout{font:500 .95rem var(--mono);margin:.75rem 0 0}
.bars{display:grid;gap:.42rem}
.bars .r{display:grid;grid-template-columns:minmax(6.5rem,34%) 1fr 5.5rem;gap:.6rem;align-items:center;font-size:.86rem}
.bars .t{height:1.3rem;background:var(--paper);border-radius:4px;overflow:hidden}
.bars .f{height:100%;background:var(--accent);border-radius:4px}
.bars .f.good{background:var(--good)} .bars .f.warn{background:var(--warn)} .bars .f.bad{background:var(--bad)} .bars .f.muted{background:var(--muted)}
.bars .v{font:500 .78rem var(--mono);text-align:right;font-variant-numeric:tabular-nums}
svg .c-accent{fill:var(--accent)} svg .c-good{fill:var(--good)} svg .c-warn{fill:var(--warn)} svg .c-bad{fill:var(--bad)} svg .c-muted{fill:var(--muted)}
svg .c-soft{fill:var(--accent-soft)} svg .c-paper{fill:var(--paper)} svg .ln{stroke:var(--line);fill:none} svg .ink{stroke:var(--ink);fill:none}
/* Steppers: the concept builds up one step at a time. */
.stepper svg .off{opacity:0}
.stepper svg rect.hi,.stepper svg path.hi,.stepper svg circle.hi,.stepper svg line.hi{stroke:var(--ink);stroke-width:3}
.stepper svg text.hi{font-weight:700}
.stepper .now{min-height:3.4em;font-size:.95rem;margin:.75rem 0 .55rem;padding:.55rem .8rem;background:var(--paper);border-radius:6px;border-left:3px solid var(--accent)}
.stepper .sbar{display:flex;flex-wrap:wrap;gap:.4rem;align-items:center}
.stepper .count{font:500 .8rem var(--mono);color:var(--muted);margin-left:auto}
.stepper .gl{font-size:.85rem;color:var(--muted);display:flex;gap:.35rem;align-items:center;margin-top:.5rem}
.stepper .gl input{accent-color:var(--accent)}
button:disabled{opacity:.45;cursor:default}
@media (prefers-reduced-motion:no-preference){.stepper svg [data-step],.stepper svg [data-only]{transition:opacity .35s}}
@media (prefers-reduced-motion:no-preference){.bars .f{transition:width .25s}}
@media (max-width:480px){.viz .ctl label{grid-template-columns:1fr 5rem}.viz .ctl label span{grid-column:1/-1}.bars .r{grid-template-columns:1fr 4.8rem}.bars .r .l{grid-column:1/-1}}
@media (max-width:480px){main{padding:1.3rem 1rem 4rem} section.st{padding-left:.8rem} section.st>h2{margin-left:-.8rem;padding-left:.8rem} .path small{display:none}}
@media (prefers-reduced-motion:no-preference){.card{transition:background .15s,border-color .15s}}
</style>
<!-- /TOPIC-LAB:STYLE -->

<!-- TOPIC-LAB:SCRIPT v4 (copy verbatim) -->
<script>
(function(){
  var ID=document.body.dataset.topic||"topic";
  var store={get:function(k,d){try{var v=localStorage.getItem(ID+":"+k);return v===null?d:JSON.parse(v)}catch(e){return d}},
             set:function(k,v){try{localStorage.setItem(ID+":"+k,JSON.stringify(v))}catch(e){}}};
  function $(s,r){return (r||document).querySelector(s)} function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
  function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}
  function btn(c,x,fn){var b=el("button",c,x);b.type="button";b.addEventListener("click",function(){fn(b)});return b}
  function flash(b,x){var old=b.textContent;b.textContent=x;setTimeout(function(){b.textContent=old},1400)}
  function copy(text,b){function manual(){var ta=el("textarea");ta.value=text;ta.style.position="fixed";ta.style.opacity="0";document.body.appendChild(ta);ta.select();
      var ok=false;try{ok=document.execCommand("copy")}catch(e){}ta.remove();flash(b,ok?"Copied":"Select the text and copy")}
    try{navigator.clipboard.writeText(text).then(function(){flash(b,"Copied")},manual)}catch(e){manual()}}
  function iso(d){return d.getFullYear()+"-"+("0"+(d.getMonth()+1)).slice(-2)+"-"+("0"+d.getDate()).slice(-2)}
  function plus(s,n){var p=s.split("-");return iso(new Date(+p[0],p[1]-1,+p[2]+n))}
  function nice(s){var p=s.split("-");return new Date(+p[0],p[1]-1,+p[2]).toLocaleDateString("en-GB",{day:"numeric",month:"short"})}
  function text(n){return n?n.textContent.replace(/\s+/g," ").trim():""}
  var today=iso(new Date());

  // copy buttons on code blocks
  $$("pre[data-copy]").forEach(function(pre){pre.parentNode.appendChild(btn("","Copy",function(b){copy(pre.textContent,b)}))});

  // study path checkboxes
  var steps=store.get("steps",{});
  $$(".path input").forEach(function(cb){cb.checked=!!steps[cb.id];cb.addEventListener("change",function(){steps[cb.id]=cb.checked;store.set("steps",steps)})});

  // self-grading on every question
  var grades=store.get("grades",{}),qs=$$("details.q"),paints=[],sc=$("#score");
  function tally(){var c={got:0,shaky:0,missed:0};qs.forEach(function(q){if(c[q.dataset.g]!=null)c[q.dataset.g]++});return c}
  function score(){if(!sc)return;var c=tally();sc.textContent="Self-grade so far: got "+c.got+", shaky "+c.shaky+", missed "+c.missed+", of "+qs.length+" questions on this page."}
  qs.forEach(function(q,i){var key="q"+i,row=el("div","grade");row.appendChild(el("span","","How did you do?"));
    [["got","Got it"],["shaky","Shaky"],["missed","Missed"]].forEach(function(g){var b=btn("",g[1],function(){grades[key]=g[0];store.set("grades",grades);paint()});b.dataset.v=g[0];row.appendChild(b)});
    function paint(){if(grades[key])q.dataset.g=grades[key];else q.removeAttribute("data-g");$$("button",row).forEach(function(b){b.setAttribute("aria-pressed",String(b.dataset.v===grades[key]))});score()}
    q.appendChild(row);paints.push(paint);paint()});
  score();

  // shaky and missed questions, as rows for the tracker's Question log (Date, Question, Topic, Level reached, What was missing, Model answer, Retest due)
  if(sc)sc.parentNode.insertBefore(btn("keep","Copy shaky and missed for the question log",function(b){var rows=[];
    qs.forEach(function(q){if(q.dataset.g==="shaky"||q.dataset.g==="missed")rows.push([today,text($("summary",q)),ID,q.dataset.g,"",text($(".a",q)).slice(0,400),plus(today,7)].join("\t"))});
    if(rows.length)copy(rows.join("\n"),b);else flash(b,"Nothing graded shaky or missed yet")}),sc.nextSibling);

  // recall draft
  var rb=$("#recall-box");if(rb){rb.value=store.get("recall","");rb.addEventListener("input",function(){store.set("recall",rb.value)})}

  // 90-second timer, and the model answer toggle used in retest mode
  var tb=$("#timer-btn"),to=$("#timer-out"),tick=null,lv=$(".levels"),tm=$(".timer");
  if(tb&&to){var total=+tb.dataset.seconds||90,label=tb.textContent;
    function fmt(s){return Math.floor(s/60)+":"+("0"+s%60).slice(-2)}
    tb.addEventListener("click",function(){if(tick){clearInterval(tick);tick=null;tb.textContent=label;to.textContent=fmt(total);return}
      var left=total;tb.textContent="Stop";to.textContent=fmt(left);
      tick=setInterval(function(){left--;to.textContent=left>0?fmt(left):"Time";if(left<=0){clearInterval(tick);tick=null;tb.textContent=label}},1000)})}
  if(lv&&tm)tm.appendChild(btn("rt-only","Show the model answer",function(b){b.textContent=lv.classList.toggle("show")?"Hide the model answer":"Show the model answer"}));

  // retest mode: the tracker says when; this hides the explanations and keeps a score per round
  var nav=$(".path")||$("header");
  if(nav&&qs.length){var first=store.get("first",null);if(!first){first=today;store.set("first",first)}
    var rounds=store.get("rounds",[]),mode=store.get("mode","study"),bar=el("div","rt"),info=el("p");
    function show(){var on=mode==="retest";document.body.classList.toggle("retest",on);go.textContent=on?"Finish and save the score":"Start a retest";stop.style.display=on?"":"none";
      info.textContent=on?"Retest: answer each question aloud, then open it and grade it. The explanations stay hidden until you finish."
        :rounds.map(function(r){return r.l+" "+nice(r.d)+": "+r.c.got+" got, "+r.c.shaky+" shaky, "+r.c.missed+" missed. "}).join("")+"First opened "+nice(first)+". Retest cold on or after "+nice(plus(first,7))+" and "+nice(plus(first,30))+"."}
    function set(m){mode=m;store.set("mode",m);show()}
    var go=btn("primary","",function(){var c=tally(),n=c.got+c.shaky+c.missed;
      if(mode==="retest"){if(n){rounds.push({l:"Retest",d:today,c:c});store.set("rounds",rounds)}set("study");return}
      if(n&&!rounds.length){rounds.push({l:"First pass",d:first,c:c});store.set("rounds",rounds)}
      grades={};store.set("grades",grades);qs.forEach(function(q){q.open=false});if(lv)lv.classList.remove("show");paints.forEach(function(p){p()});
      set("retest");window.scrollTo(0,0)});
    var stop=btn("","Cancel",function(){set("study")});
    bar.appendChild(info);bar.appendChild(go);bar.appendChild(stop);nav.appendChild(bar);show()}

  // visualizations: data-bars charts render themselves; explorables register through window.TLQ
  var TL={};
  TL.fmt=function(n,d){return Number(n).toLocaleString("en-US",{maximumFractionDigits:d==null?2:d,minimumFractionDigits:d==null?0:d})};
  TL.bars=function(host,spec){host.textContent="";host.classList.add("bars");var rows=spec.rows||[];
    var max=spec.max||Math.max.apply(null,rows.map(function(r){return Math.abs(r.value)}))||1;
    function txt(r){return r.text!=null?r.text:(spec.pre||"")+TL.fmt(r.value,spec.digits)+(spec.unit||"")}
    host.setAttribute("role","img");host.setAttribute("aria-label",spec.label||rows.map(function(r){return r.label+" "+txt(r)}).join(", "));
    rows.forEach(function(r){var row=el("div","r"),t=el("div","t"),f=el("div","f"+(r.tone?" "+r.tone:""));
      f.style.width=Math.max(0,Math.min(100,100*Math.abs(r.value)/max))+"%";t.appendChild(f);
      row.appendChild(el("span","l",r.label));row.appendChild(t);row.appendChild(el("span","v",txt(r)));host.appendChild(row)})};
  TL.viz=function(id,render){var fig=document.getElementById(id);if(!fig)return;var ins=$$("input,select",fig);
    function run(){var v={};ins.forEach(function(i){var x=i.type==="checkbox"?i.checked:(i.type==="range"||i.type==="number"||i.dataset.num!=null)?+i.value:i.value;v[i.name]=x;
        var o=$('output[data-for="'+i.name+'"]',fig);if(o)o.textContent=(i.dataset.pre||"")+(i.tagName==="SELECT"?i.options[i.selectedIndex].text:typeof x==="number"?TL.fmt(x):x)+(o.dataset.unit||i.dataset.unit||"")});
      var out;try{out=render(v,fig,TL)}catch(e){out={};var r=$("[data-out]",fig);if(r)out[r.dataset.out]="This visual hit an error: "+e.message}
      if(out)Object.keys(out).forEach(function(k){var n=$('[data-out="'+k+'"]',fig);if(n)n.textContent=out[k]})}
    ins.forEach(function(i){i.addEventListener("input",run);i.addEventListener("change",run)});run()};
  $$("[data-bars]").forEach(function(h){try{TL.bars(h,JSON.parse(h.dataset.bars))}catch(e){h.textContent="Chart data could not be read."}});
  var queued=window.TLQ||[];window.TLQ={push:function(f){try{f(TL)}catch(e){}}};queued.forEach(function(f){window.TLQ.push(f)});

  // steppers: an SVG that builds up step by step, one caption per step, with an optional guess-first mode
  $$("figure.stepper").forEach(function(fig){var svg=$("svg",fig),list=$("ol.steps",fig);if(!svg||!list)return;
    var caps=$$("li",list).map(text),n=caps.length,i=0,timer=null,guess=false,shown=true;if(!n)return;list.hidden=true;
    var now=el("p","now"),bar=el("div","sbar"),cnt=el("span","count"),gl=el("label","gl"),gc=document.createElement("input");
    now.setAttribute("aria-live","polite");gc.type="checkbox";gl.appendChild(gc);gl.appendChild(document.createTextNode("Guess each step before you see it"));
    var back=btn("","Back",function(){stop();go(i-1)}),play=btn("primary","Play",function(){timer?stop():start()}),
        next=btn("","Next",function(){stop();if(guess&&!shown){shown=true;draw()}else go(i+1)});
    function has(e,a){return e.getAttribute(a).split(/[\s,]+/).indexOf(String(i+1))>=0}
    function draw(){$$("[data-step]",svg).forEach(function(e){e.classList.toggle("off",+e.getAttribute("data-step")>i+1)});
      $$("[data-only]",svg).forEach(function(e){e.classList.toggle("off",!has(e,"data-only"))});
      $$("[data-hi]",svg).forEach(function(e){e.classList.toggle("hi",has(e,"data-hi"))});
      now.textContent=shown?caps[i]:"What happens in step "+(i+1)+"? Say it aloud, then press Reveal.";
      next.textContent=guess&&!shown?"Reveal":"Next";cnt.textContent="Step "+(i+1)+" of "+n;back.disabled=i===0;next.disabled=i===n-1&&shown}
    function go(k){var j=Math.max(0,Math.min(n-1,k));if(j!==i||k===0)shown=!guess;i=j;draw()}
    function start(){guess=false;gc.checked=false;shown=true;if(i>=n-1)i=0;draw();play.textContent="Pause";
      timer=setInterval(function(){go(i+1);if(i>=n-1)stop()},3000)}
    function stop(){if(timer)clearInterval(timer);timer=null;play.textContent="Play"}
    gc.addEventListener("change",function(){stop();guess=gc.checked;shown=!guess;draw()});
    fig.addEventListener("keydown",function(e){if(e.target.tagName==="INPUT")return;if(e.key==="ArrowRight"){e.preventDefault();next.click()}if(e.key==="ArrowLeft"){e.preventDefault();back.click()}});
    bar.appendChild(back);bar.appendChild(play);bar.appendChild(next);bar.appendChild(cnt);
    svg.parentNode.insertBefore(now,svg.nextSibling);now.parentNode.insertBefore(bar,now.nextSibling);bar.parentNode.insertBefore(gl,bar.nextSibling);draw()});

  // flashcards and Anki text
  var data=null;try{data=JSON.parse($("#cards").textContent)}catch(e){}
  var deck=$("#deck");
  if(data&&deck&&data.cards&&data.cards.length){var order=data.cards.map(function(_,i){return i}),pos=0,back=false;
    var card=el("div","card");card.tabIndex=0;card.setAttribute("role","button");
    var side=el("div","side"),txt=el("div","txt");card.appendChild(side);card.appendChild(txt);
    var dbar=el("div","deckbar"),count=el("span","count");
    function draw(){var c=data.cards[order[pos]];card.className="card"+(back?" back":"");side.textContent="";side.appendChild(el("span","",back?"Answer":"Question"));side.appendChild(el("span","",back?"click for next":"say it aloud, then click"));
      txt.textContent=back?c.a:c.q;count.textContent=(pos+1)+" / "+order.length}
    function go2(n){pos=(pos+n+order.length)%order.length;back=false;draw()}
    function flip(){if(back)go2(1);else{back=true;draw()}}
    card.addEventListener("click",flip);card.addEventListener("keydown",function(e){if(e.key===" "||e.key==="Enter"){e.preventDefault();flip()}
      if(e.key==="ArrowRight")go2(1);if(e.key==="ArrowLeft")go2(-1)});
    dbar.appendChild(btn("","Previous",function(){go2(-1)}));dbar.appendChild(btn("","Flip",flip));
    dbar.appendChild(btn("","Shuffle",function(){for(var i=order.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=order[i];order[i]=order[j];order[j]=t}pos=0;back=false;draw()}));
    dbar.appendChild(count);deck.appendChild(card);deck.appendChild(dbar);draw();
    var anki=$("#anki");if(anki){function f(s){return '"'+String(s).replace(/"/g,'""').replace(/\t/g," ").replace(/\r?\n/g,"<br>")+'"'}
      anki.value=["#separator:tab","#html:true","#notetype:Basic","#deck:"+data.deck,"#tags column:3"].concat(
        data.cards.map(function(c){return f("["+ID+"] "+c.q)+"\t"+f(c.a)+"\t"+f(data.tags)})).join("\n")+"\n";
      var ab=$("#anki-copy");if(ab)ab.addEventListener("click",function(){copy(anki.value,ab)})}}
})();
</script>
<!-- /TOPIC-LAB:SCRIPT -->
```