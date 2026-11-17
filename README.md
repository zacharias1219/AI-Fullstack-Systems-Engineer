# AI Fullstack Systems Engineer Mastery

A 12-week interactive engineering curriculum (Mon 16 Nov 2026 to Sun 7 Feb 2027) covering **630 topics** across **3 pillars** and **25 domains**, from linear algebra and LLM internals to distributed inference, system design, cloud deployment, and executive communication.

- **Interactive Dashboard:** Open [`main.html`](./main.html) in a browser to browse all 630 topics by domain, week, tier, or search query, track study progress, and launch the interactive Topic Lab HTML pages.
- **Core Brief & Index:** [`.context/00-core-brief.md`](./.context/00-core-brief.md) | [`.context/01-master-topic-index.md`](./.context/01-master-topic-index.md) | [`.context/02-week-plan.md`](./.context/02-week-plan.md) | [`.context/AI Mastery tracker - Topics.csv`](./.context/AI%20Mastery%20tracker%20-%20Topics.csv)
- **Skill:** [`.skills/topic-lab.skill`](./.skills/topic-lab.skill)

---

## Core Method

Every topic is built around four rules, in order of importance:

1. **Retrieval beats rereading.** Answer warm-up, check, and interview questions from memory before opening the answer, then reproduce the concept stepper and key formulas on a blank page.
2. **Spaced retesting.** Import cards into Anki (FSRS enabled) and retest every topic cold at **7 days** and **30 days** using the built-in `Start a retest` mode on each HTML page.
3. **Small implementations (katas).** One self-contained kata per topic (under ~100 lines, runnable with one command) that prints the numbers that matter and is broken on purpose at least once.
4. **Engineer-voice spoken answers.** Record a 90-second, three-level answer for every T1 and T2 topic:
   - **Level 1: Outcome (20 s)** - what it does and why it matters.
   - **Level 2: Mechanism (45 s)** - how it works step by step.
   - **Level 3: Internals and limits (25 s)** - concrete numbers, failure modes, and tradeoffs.

---

## Tiers, Time Budget, and Daily Shape

| Tier | Meaning | Time | Cards | Visuals per Page | Count |
|---|---|---:|---:|---|---:|
| **T1** | Asked in nearly every loop (all in Weeks 1 to 8) | 70 min | 8 | 3 to 5 (1 to 3 steppers, 1+ explorable) | 205 |
| **T2** | Working engineering depth | 45 min | 4 | 2 or 3 (1 or 2 steppers) | 331 |
| **T3** | Differentiator | 25 min | 2 | 1 (concept stepper) | 94 |
| **Total** | **Weeks 1 to 12** | **~527 h** | **3,152** | | **630** |

### Daily Schedule (10 h/day, Mon to Sat)

| Block | Duration | Focus |
|---|---:|---|
| Topic packages | ~7.3 h | Today's scheduled topics in order (hardest T1 topics first) |
| Anki cards | up to 75 min | Due reviews first, then new cards (suspend low-value cards if >75 min) |
| Speaking and people | 60 min | 90-second recorded answers, role-plays, or timed mocks |
| Close | 15 min | Update tracker row (`Status`, `Conf`, `Learned on`) and question log |

- **Sunday Review:** Due 7d/30d retests, interleaved cards across all prior weeks, the weekly gate (10 random question-log items answered cold in 3 levels), and a timed mock (starting Week 3).
- **Slip Rule:** T1 topics never slip out of their scheduled week. If a day runs long, T3 slides first, then T2 (to Sunday or Week 12).

---

## Domains and Folders

### Pillar 1: AI Engineer (Domains A to K)

| ID | Folder | Topics | T1 | Hours | Built Pages |
|---|---|---:|---:|---:|---|
| **A** | [`A - Foundations and Applied Math`](./A%20-%20Foundations%20and%20Applied%20Math) | 27 | 11 | 24 h | [`A01`](./A%20-%20Foundations%20and%20Applied%20Math/A01%20Python%20for%20AI%20engineering.html), [`A02`](./A%20-%20Foundations%20and%20Applied%20Math/A02%20Async%20Python.html), [`A03`](./A%20-%20Foundations%20and%20Applied%20Math/A03%20Linux%20and%20shell%20fluency.html), [`A06`](./A%20-%20Foundations%20and%20Applied%20Math/A06%20Debugging%20method.html), [`A07`](./A%20-%20Foundations%20and%20Applied%20Math/A07%20Profiling%20Python.html), [`A08`](./A%20-%20Foundations%20and%20Applied%20Math/A08%20Vectors,%20dot%20product,%20norms,%20cosine%20similarity.html) |
| **B** | [`B - Classical Machine Learning`](./B%20-%20Classical%20Machine%20Learning) | 21 | 5 | 16 h | - |
| **C** | [`C - Deep Learning`](./C%20-%20Deep%20Learning) | 18 | 1 | 12 h | - |
| **D** | [`D -Transformers and LLM Internals`](./D%20-Transformers%20and%20LLM%20Internals) | 26 | 12 | 24 h | [`D01`](./D%20-Transformers%20and%20LLM%20Internals/D01%20What%20an%20LLM%20is.html), [`D02`](./D%20-Transformers%20and%20LLM%20Internals/D02%20Tokenization.html), [`D03`](./D%20-Transformers%20and%20LLM%20Internals/D03%20Embeddings%20and%20the%20unembedding.html), [`D10`](./D%20-Transformers%20and%20LLM%20Internals/D10%20Decoding%20and%20sampling.html) |
| **E** | [`E - Post-Training`](./E%20-%20Post-Training) | 16 | 2 | 12 h | - |
| **F** | [`F - Training Infrastructure`](./F%20-%20Training%20Infrastructure) | 11 | 0 | 7 h | - |
| **G** | [`G - LLM Application Layer`](./G%20-%20LLM%20Application%20Layer) | 30 | 17 | 29 h | - |
| **H** | [`H - Retrieval and RAG`](./H%20-%20Retrieval%20and%20RAG) | 25 | 11 | 23 h | - |
| **I** | [`I - Agents and Orchestration`](./I%20-%20Agents%20and%20Orchestration) | 23 | 9 | 21 h | - |
| **J** | [`J - Evals and Quality`](./J%20-%20Evals%20and%20Quality) | 19 | 10 | 18 h | - |
| **K** | [`K - Inference Engineering and Hardware`](./K%20-%20Inference%20Engineering%20and%20Hardware) | 66 | 21 | 55 h | [`K01`](./K%20-%20Inference%20Engineering%20and%20Hardware/K01%20What%20inference%20engineering%20is.html), [`K02`](./K%20-%20Inference%20Engineering%20and%20Hardware/K02%20Inference%20setup.html), [`K03`](./K%20-%20Inference%20Engineering%20and%20Hardware/K03%20Run%20your%20first%20LLM.html), [`K04`](./K%20-%20Inference%20Engineering%20and%20Hardware/K04%20One%20token%20end%20to%20end.html) |

### Pillar 2: Supplementary Systems and Cloud (Domains L, Y, M to U)

| ID | Folder | Topics | T1 | Hours | Built Pages |
|---|---|---:|---:|---:|---|
| **L** | [`L - System Design Concepts`](./L%20-%20System%20Design%20Concepts) | 85 | 32 | 72 h | [`L01`](./L%20-%20System%20Design%20Concepts/L01%20Requirements%20and%20logical%20design.html), [`L02`](./L%20-%20System%20Design%20Concepts/L02%20Non-functional%20requirements.html) |
| **Y** | [`Y - System Design Drills and Case Studies`](./Y%20-%20System%20Design%20Drills%20and%20Case%20Studies) | 47 | 14 | 39 h | - |
| **M** | [`M - Backend Engineering`](./M%20-%20Backend%20Engineering) | 16 | 4 | 13 h | - |
| **N** | [`N - Databases`](./N%20-%20Databases) | 15 | 4 | 12 h | - |
| **O** | [`O - Frontend Engineering`](./O%20-%20Frontend%20Engineering) | 13 | 1 | 8 h | - |
| **P** | [`P - Data Engineering`](./P%20-%20Data%20Engineering) | 12 | 0 | 8 h | - |
| **Q** | [`Q - Cloud`](./Q%20-%20Cloud) | 26 | 11 | 23 h | - |
| **R** | [`R - DevOps, Platform, MLOps, LLMOps`](./R%20-%20DevOps,%20Platform,%20MLOps,%20LLMOps) | 25 | 8 | 21 h | - |
| **S** | [`S - Security, Privacy, Safety, Governance`](./S%20-%20Security,%20Privacy,%20Safety,%20Governance) | 21 | 6 | 18 h | - |
| **T** | [`T - Domain and Applied AI`](./T%20-%20Domain%20and%20Applied%20AI) | 15 | 0 | 10 h | - |
| **U** | [`U - Research and Engineering Craft`](./U%20-%20Research%20and%20Engineering%20Craft) | 13 | 1 | 9 h | [`U01`](./U%20-%20Research%20and%20Engineering%20Craft/U01%20Learning%20system.html) |

### Pillar 3: Business, People, and Interview Craft (Domains V, W, X)

| ID | Folder | Topics | T1 | Hours | Built Pages |
|---|---|---:|---:|---:|---|
| **V** | [`V -Business and Product`](./V%20-Business%20and%20Product) | 24 | 6 | 20 h | [`V01`](./V%20-Business%20and%20Product/V01%20Engineer%20voice%20vs%20business%20voice.html) |
| **W** | [`W - People Skills`](./W%20-%20People%20Skills) | 19 | 8 | 17 h | [`W01`](./W%20-%20People%20Skills/W01%20Tactical%20empathy.html), [`W19`](./W%20-%20People%20Skills/W19%20Active%20listening%20and%20summarizing%20back.html) |
| **X** | [`X - Interview Craft`](./X%20-%20Interview%20Craft) | 17 | 11 | 17 h | - |

---

## 12-Week Roadmap

Weeks 1 to 8 form the **interview-ready core** (containing all 205 T1 topics). Weeks 9 to 12 cover advanced depth, training/serving scale, and full interview loops.

| Week | Dates | Theme | Topics (T1/T2/T3) | Hours | Gate Artifact & Mock |
|---|---|---|---:|---:|---|
| **W01** | 16 Nov - 22 Nov | One token, end to end | 39 (26/13/0) | 40.1 h | Tiny LM forward pass, KV-cache calculator, token ledger |
| **W02** | 23 Nov - 29 Nov | Attention and retrieval | 42 (31/11/0) | 44.4 h | nanoGPT from scratch, retrieval benchmark (recall@k) |
| **W03** | 30 Nov - 06 Dec | RAG and the engine | 44 (30/14/0) | 45.5 h | 80-line RAG + 50-item golden set, scheduler sim; Mock 1 (ML/LLM) |
| **W04** | 07 Dec - 13 Dec | Context, memory, evals | 47 (27/20/0) | 46.5 h | RAG eval harness + 4-type memory store; Mock 2 (Coding + Take-home) |
| **W05** | 14 Dec - 20 Dec | Agents, quantization, caches | 47 (28/19/0) | 46.9 h | 60-line agent, INT8 quantizer, router; Mock 3 (AI System Design) |
| **W06** | 21 Dec - 27 Dec | MCP, LoRA, speculation, streams | 48 (24/24/0) | 46.0 h | MCP server, LoRA from scratch, speculative decoding; Mock 4 (System Design) |
| **W07** | 28 Dec - 03 Jan | Guardrails, observability, prod | 49 (23/26/0) | 46.4 h | Guarded traced agent, Kubernetes + Terraform; Mocks 5 & 6 |
| **W08** | 04 Jan - 10 Jan | Core consolidation & full loop | 44 (16/28/0) | 39.7 h | Core T1 gate complete; Full interview loop (5 rounds) |
| **W09** | 11 Jan - 17 Jan | Post-training & training infra | 63 (0/56/7) | 44.9 h | SFT + DPO/GRPO + DDP katas; 2 timed mocks |
| **W10** | 18 Jan - 24 Jan | Long context, MoE, SSMs, scale | 65 (0/62/3) | 47.8 h | Mamba/SSM step, MoE router, multi-GPU serving; 2 timed mocks |
| **W11** | 25 Jan - 31 Jan | Distributed systems & drills | 66 (0/58/8) | 46.8 h | System design case studies + cloud architecture; 2 timed mocks |
| **W12** | 01 Feb - 07 Feb | Differentiators & final loops | 76 (0/0/76) | 31.7 h | T3 sweep + 3 full interview loops |

---

## Topic Lab Commands

When working with the `topic-lab` skill in chat:

- `<ID>` or `teach me <ID>` (e.g. `K04`): Build the interactive study page, kata, and Anki cards for that topic.
- `drill me`: Run an interactive recall drill after closing the page (graded on Levels 1, 2, and 3).
- `retest <ID>`: Run a cold 7-day or 30-day retest without reteaching.
- `mock me`: Run a timed interview round (coding, ML/LLM deep dive, system design, AI system design, live debugging, FDE decomposition, customer simulation, or behavioral).
- `review week <N>`: Rapid interleaved drill across a week's topics.
- `what is today`: Show today's scheduled topics from `02-week-plan.md` applying the slip rule.
