# AI Mastery: week plan

Study order for all topics, by week and day. Six study days a week, Sunday is review. Times are topic-package time only; cards, speaking practice and mocks sit on top (see the core brief).

Sunday every week: retests that are due, mixed cards from all weeks, 10 random question-log items answered cold (the weekly gate), and from week 3 one timed mock.

## Before Monday: setup (Sat 14 and Sun 15 Nov 2026)

- Create the Claude project. Paste `00-core-brief.md` into the project instructions, add `01-master-topic-index.md` and `02-week-plan.md` as project files, and save the `topic-lab` skill.
- Install Anki on your laptop and phone, turn on FSRS in the deck options, and import `G01-cards.txt` to confirm the import works.
- Open the tracker. Log every question you remember from the 13 Nov interview in the Question log tab.
- Trial run: work through G01 Token optimization end to end. The page is already built. Time yourself against 70 minutes, then adjust how you pace Monday.
- Record a 3-minute baseline: explain your best project. You will compare against it in week 8.
- Make sure you can reach a GPU. A free notebook tier is enough for week 1.

## Week 1: One token, end to end (16 Nov to 22 Nov 2026)

- **Focus:** Setup and tooling; what an LLM is, tokens, sampling; token optimization; prefill, decode, KV cache and memory math; the design spine and estimation; engineer voice.
- **Gate artifact:** Tiny LM forward pass by hand, the KV-cache calculator, and the token ledger.
- **Mock:** No mock. Record a 3-minute baseline: explain your best project.
- **Load:** 39 topics (T1 26, T2 13, T3 0), 40.1 h, 260 new cards

**Mon 16 Nov** (6.9 h)
- K01 (T2) What inference engineering is
- D01 (T1) What an LLM is
- A01 (T2) Python for AI engineering
- A02 (T1) Async Python
- A03 (T2) Linux and shell fluency
- L01 (T1) Requirements clarification and logical design
- V01 (T1) Engineer voice vs business voice

**Tue 17 Nov** (6.9 h)
- K02 (T2) Inference setup
- K03 (T2) Run your first LLM
- D02 (T1) Tokenization
- A06 (T2) Debugging method
- L02 (T1) Non-functional requirements and tradeoffs
- U01 (T1) How to learn this curriculum
- W01 (T1) Tactical empathy

**Wed 18 Nov** (6.2 h)
- K04 (T1) One token end to end
- D03 (T1) Embeddings and the unembedding
- D10 (T1) Decoding and sampling
- A07 (T2) Profiling Python
- A08 (T1) Vectors, dot product, norms, cosine similarity
- W19 (T2) Active listening and summarizing back

**Thu 19 Nov** (6.6 h)
- K05 (T1) Prefill vs decode
- D11 (T1) Logits, logprobs, perplexity; reading model confidence
- D23 (T2) The open-model landscape
- A09 (T1) Matrices, matmul, tensor shapes, broadcasting, einsum
- L03 (T1) Back-of-the-envelope capacity planning; the latency numbers to know
- X01 (T1) Three-level answers

**Fri 20 Nov** (7.3 h)
- K06 (T1) KV cache
- G01 (T1) Token optimization playbook
- G02 (T1) LLM API mechanics
- A16 (T1) Information theory
- L04 (T2) How a server handles many requests
- U02 (T2) Reading papers
- X02 (T1) The question log

**Sat 21 Nov** (6.2 h)
- K07 (T1) Memory math
- G03 (T1) Prompt engineering fundamentals
- A20 (T2) Complexity for AI systems
- A21 (T1) DSA kata 1
- L08 (T1) API design contracts
- X15 (T2) Company and role research

## Week 2: Attention and retrieval (23 Nov to 29 Nov 2026)

- **Focus:** Backprop, attention, the full transformer; embeddings, ANN, BM25; inference metrics and breaking one GPU; HTTP, SQL, idempotency.
- **Gate artifact:** A nanoGPT-size model trained from scratch, a retrieval benchmark with recall@k, and the benchmark harness.
- **Mock:** No mock. Two timed coding problems with narration.
- **Load:** 42 topics (T1 31, T2 11, T3 0), 44.4 h, 292 new cards

**Mon 23 Nov** (7.3 h)
- K08 (T1) Inference metrics
- D04 (T1) Self-attention
- D05 (T1) Multi-head attention and its variants
- A11 (T1) Derivatives, gradients, chain rule, Jacobians
- L05 (T1) Scaling out
- L07 (T2) Cost-aware architecture and when not to add infrastructure
- R25 (T2) Operating system essentials

**Tue 24 Nov** (7.7 h)
- D06 (T2) Positional information
- D07 (T2) The transformer block
- D08 (T1) Full forward pass of a decoder-only transformer, end to end
- A12 (T1) Backpropagation and autodiff from scratch
- L09 (T2) Service-to-service communication
- L10 (T1) API gateway vs load balancer; L4 vs L7; consistent-hashing load balancing
- W02 (T1) Principled negotiation
- U13 (T2) Working with AI coding agents

**Wed 25 Nov** (7.8 h)
- K09 (T2) Benchmark design
- D13 (T1) Context windows
- G07 (T1) Prompt caching
- G15 (T1) Latency anatomy
- A22 (T1) DSA kata 2
- L12 (T1) Retries, timeouts and idempotency
- L14 (T1) Realtime transports

**Thu 26 Nov** (7.0 h)
- K10 (T1) Percentiles, variance, goodput, SLOs and failure rates; benchmark tools
- H01 (T1) Embeddings for retrieval
- B06 (T1) Ranking and retrieval metrics
- Y01 (T1) Design: URL shortener, from one machine to scale
- R01 (T1) Networking for engineers
- X03 (T1) Thinking aloud, clarifying questions, and handling "I don't know"

**Fri 27 Nov** (7.0 h)
- H02 (T1) Vector search fundamentals
- H03 (T1) HNSW
- C01 (T1) Neural networks from scratch
- M01 (T1) HTTP deeply
- M02 (T1) FastAPI service skeleton
- N01 (T1) SQL fluency 1

**Sat 28 Nov** (7.7 h)
- K11 (T1) Break one GPU
- H04 (T2) IVF, product quantization, IVF-PQ, DiskANN, ScaNN; memory math
- H05 (T1) Sparse retrieval
- C02 (T2) Activations, initialization, vanishing and exploding gradients
- C03 (T2) Normalization
- C05 (T2) PyTorch fluency
- N02 (T1) SQL fluency 2
- X04 (T1) Coding round craft

## Week 3: RAG and the engine (30 Nov to 06 Dec 2026)

- **Focus:** The RAG pipeline, chunking, hybrid search, reranking; eval mindset and golden sets; vLLM, continuous batching, PagedAttention; database design and indexing; AWS core; statistics.
- **Gate artifact:** An 80-line RAG with a 50-item golden set, and the scheduler simulator.
- **Mock:** Mock 1: ML and LLM deep dive.
- **Load:** 44 topics (T1 30, T2 14, T3 0), 45.5 h, 296 new cards

**Mon 30 Nov** (7.8 h)
- K12 (T1) From PyTorch to a real engine
- D09 (T2) Architectures
- D14 (T1) The LLM optimization map
- A13 (T1) Probability essentials
- L13 (T1) Batching, backpressure, tail latency and load shedding
- Q01 (T1) Cloud fundamentals
- V02 (T1) Unit economics for AI products

**Tue 01 Dec** (7.8 h)
- G04 (T2) Advanced prompting
- G06 (T1) Function and tool calling
- G08 (T1) Context engineering
- A15 (T1) Statistics for experiments
- L15 (T1) AuthN and AuthZ
- L16 (T1) Relational database design; a key-value store on SQL
- L17 (T1) Indexing and B-trees

**Wed 02 Dec** (7.7 h)
- K13 (T1) Batching
- G20 (T2) Semantic caching
- G24 (T2) Embeddings in apps
- H06 (T1) Hybrid search and fusion
- A23 (T2) DSA kata 3
- L18 (T2) Query planning
- Q02 (T1) AWS IAM
- W04 (T1) Structured communication

**Thu 03 Dec** (7.3 h)
- K14 (T2) Scheduler knobs and policy
- H07 (T1) Reranking
- H08 (T1) Chunking
- B01 (T1) Bias-variance tradeoff, underfitting and overfitting, learning curves
- Y21 (T1) Case study: Stripe's idempotency keys
- X05 (T1) ML and LLM deep-dive rounds
- M16 (T2) Concurrency correctness

**Fri 04 Dec** (7.3 h)
- H09 (T1) The RAG pipeline end to end
- H16 (T2) Vector databases
- J01 (T1) Eval mindset
- B03 (T1) Validation done right
- M03 (T1) Concurrency models
- M04 (T2) Database access
- Q03 (T1) AWS networking

**Sat 05 Dec** (7.7 h)
- K15 (T1) PagedAttention and KV memory management
- J02 (T1) Golden sets
- B08 (T2) Linear and logistic regression from scratch
- B20 (T2) ML problem framing
- N03 (T1) Query tuning
- N04 (T2) Postgres as an AI database
- U09 (T2) Experiment design for LLM systems
- X06 (T1) Take-home craft

## Week 4: Context, memory, evals (07 Dec to 13 Dec 2026)

- **Focus:** Context management and memory; RAG evals and LLM judges; prefix caching and one-GPU tuning; isolation and scaling a database; Docker; prompt injection.
- **Gate artifact:** An eval harness on the RAG app (recall@5, faithfulness) and a memory store with all four types.
- **Mock:** Mock 2: coding round plus a take-home review.
- **Load:** 47 topics (T1 27, T2 20, T3 0), 46.5 h, 296 new cards

**Mon 07 Dec** (7.7 h)
- K16 (T1) Optimize one GPU
- D25 (T2) Chat templates, system prompts, special tokens, stop sequences, tool-call formats
- G09 (T1) Context management over long sessions
- A24 (T2) DSA kata 4
- L19 (T1) ACID transactions, locking, isolation levels and MVCC
- L20 (T2) WAL and crash recovery
- Q04 (T1) EC2
- V24 (T2) Requirements and specs

**Tue 08 Dec** (7.8 h)
- G10 (T1) Just-in-time retrieval and sub-agents as context isolation
- G11 (T1) Memory types
- G12 (T1) Memory systems
- G21 (T2) Reliability at the API layer
- A25 (T1) DSA kata 5
- L21 (T1) Scaling a relational database
- Q05 (T1) S3

**Wed 09 Dec** (8.0 h)
- K17 (T2) Chunked prefill and long-prompt interference
- H10 (T1) Query understanding
- H11 (T2) Metadata, filtering and access control in retrieval (pre-filter vs post-filter)
- L22 (T2) Changing a live database
- L23 (T1) NoSQL decision boundaries
- Q06 (T2) AWS data services
- R02 (T2) Linux internals
- W05 (T1) Influence
- H25 (T2) Fine-tuning embedding models and rerankers

**Thu 10 Dec** (8.1 h)
- K18 (T1) Prefix caching in the engine
- H12 (T1) Grounding and citations
- H13 (T1) RAG failure taxonomy and debugging
- B02 (T1) Regularization
- Y02 (T2) Design: product listing
- M05 (T2) Background jobs and task queues
- R03 (T1) Docker
- X17 (T2) Low-level design and machine-coding rounds

**Fri 11 Dec** (7.3 h)
- H14 (T2) Advanced patterns
- J03 (T1) Reference-based metrics
- B04 (T1) Classification metrics
- M06 (T1) Streaming LLM backends
- M07 (T2) Testing
- S01 (T1) Prompt injection
- X10 (T1) Behavioral rounds

**Sat 12 Dec** (7.7 h)
- K63 (T2) Model formats and loading
- J04 (T1) LLM-as-judge
- J06 (T1) RAG evals
- B09 (T2) Decision trees, random forests, gradient boosting (XGBoost, LightGBM)
- N05 (T1) Redis
- N12 (T2) Data modeling for AI apps
- S02 (T1) Defenses in depth
- U04 (T2) Code quality

## Week 5: Agents begin; quantization (14 Dec to 20 Dec 2026)

- **Focus:** The agent loop, workflows vs agents, tool design; quantization and the roofline; hallucination and reasoning; routing and latency; caching and sharding; CI/CD.
- **Gate artifact:** A quantized model on a quality, speed and memory Pareto chart, and a cheap-first cascade.
- **Mock:** Mock 3: system design.
- **Load:** 45 topics (T1 24, T2 21, T3 0), 43.8 h, 276 new cards

**Mon 14 Dec** (7.3 h)
- K19 (T1) Quantization fundamentals
- K20 (T2) Quantization methods
- D19 (T1) Hallucination
- D20 (T1) Reasoning models
- L24 (T1) Sharding, partitioning and hot partitions
- Q07 (T2) AWS compute choices
- V04 (T1) Build vs buy vs fine-tune vs partner; vendor evaluation

**Tue 15 Dec** (7.2 h)
- K21 (T2) KV-cache quantization
- D21 (T2) Verification
- E01 (T1) Fine-tune vs RAG vs prompt vs tools
- G14 (T1) Long context vs RAG vs fine-tune for knowledge
- L25 (T1) Consistent hashing
- L26 (T2) Distributed IDs
- Q09 (T2) AWS edge and delivery
- R04 (T2) GPU containers

**Wed 16 Dec** (7.7 h)
- K22 (T2) Profiling workflow
- G16 (T1) Latency optimization for apps
- G17 (T1) Model routing and cascades
- G27 (T2) Provider landscape and differences
- H15 (T2) Agentic RAG
- L27 (T2) Keyset pagination
- R05 (T1) CI/CD
- V05 (T1) ROI and business cases for AI projects; baselines and measurement

**Thu 17 Dec** (6.9 h)
- K23 (T1) GPU execution and the roofline model
- I01 (T1) The agent loop
- A19 (T2) Numerical stability
- L28 (T2) Bloom filters
- R06 (T2) Secrets and config management
- S03 (T1) OWASP Top 10 for LLM applications, each with an example
- W06 (T1) Customer discovery

**Fri 18 Dec** (7.8 h)
- K60 (T2) GPU hardware
- I02 (T1) Workflows vs agents
- I03 (T1) Tool design
- J05 (T1) Judge biases
- L30 (T1) Caching layers and patterns
- L31 (T1) Distributed cache design, eviction policies (LRU, LFU), TTLs and reapers
- S05 (T1) PII and sensitive data

**Sat 19 Dec** (6.8 h)
- K65 (T2) Hardware-aware model selection
- J08 (T1) Statistical rigor in evals
- J13 (T2) Public benchmarks and leaderboards
- J18 (T2) Classifier and extraction evals
- Y20 (T2) Case study: Instagram's first architecture
- M08 (T2) Config, secrets, 12-factor, structured logging, error handling
- U05 (T2) Benchmarking methodology
- X08 (T1) System design round craft

## Week 6: Agents in depth; queues; GCP (21 Dec to 27 Dec 2026)

- **Focus:** MCP, budgets, planning, failure modes; speculative decoding and engine comparison; structured outputs; queues, Kafka, consistency; Kubernetes; GCP and Vertex; LoRA.
- **Gate artifact:** An agent with budgets and traces plus the looping-agent fix, and an engine comparison table.
- **Mock:** Mock 4: live debugging plus an FDE decomposition.
- **Load:** 46 topics (T1 27, T2 19, T3 0), 45.8 h, 292 new cards

**Mon 21 Dec** (7.2 h)
- K26 (T2) Attention optimization
- D12 (T2) Constrained decoding
- E04 (T1) LoRA
- G05 (T1) Structured outputs
- L32 (T1) Cache failure modes
- Q08 (T2) AWS integration
- Q10 (T2) AWS operations
- V06 (T2) Product sense

**Tue 22 Dec** (6.9 h)
- K27 (T2) Compilation
- G18 (T1) Model selection tradeoffs
- G25 (T2) Guardrails in the app path
- L33 (T2) CDNs and edge caching
- L34 (T1) Distributed systems foundations
- Q14 (T1) GCP core
- V09 (T1) FDE craft 1

**Wed 23 Dec** (7.3 h)
- H18 (T2) Document AI
- H19 (T2) Text-to-SQL and structured-data QA
- I04 (T1) MCP
- I05 (T1) Budgets and guards
- L35 (T1) Consistency models; CAP and PACELC
- L36 (T1) Replication
- Q15 (T1) Cloud Run and GKE

**Thu 24 Dec** (7.8 h)
- K29 (T1) Speculative decoding
- I06 (T1) Planning and decomposition
- A10 (T2) Eigenvalues, SVD, low-rank approximation (why LoRA works)
- L51 (T1) Async work
- L52 (T1) Queues in practice
- Q17 (T1) Vertex AI
- W09 (T1) Explaining technical ideas

**Fri 25 Dec** (8.4 h)
- I07 (T1) Agent failure modes
- I08 (T2) Multi-agent patterns
- I09 (T2) State and orchestration
- I10 (T2) Human in the loop
- I16 (T2) Agent memory in practice
- L53 (T1) Log-based streaming (Kafka)
- Y03 (T1) Design: notification system
- Q19 (T2) Infrastructure as code
- R07 (T1) Kubernetes core

**Sat 26 Dec** (8.1 h)
- K31 (T1) Engine comparison
- J09 (T1) Regression gates in CI
- J16 (T2) Synthetic eval data
- Y04 (T2) Design: Kafka-style log
- Y06 (T1) Design: payment system
- R08 (T1) Kubernetes scaling and scheduling
- U03 (T2) Technical writing
- X07 (T1) Live debugging rounds

## Week 7: Production (28 Dec to 03 Jan 2027)

- **Focus:** Agent evals and observability; routing, autoscaling, multi-GPU; SLOs, rate limiting, safe change; LLMOps; Bedrock and SageMaker; the first AI system designs.
- **Gate artifact:** An LLM gateway with routing, caching and cost caps, and an eval-gated release pipeline.
- **Mock:** Mocks 5 and 6: AI system design; behavioral.
- **Load:** 48 topics (T1 23, T2 25, T3 0), 45.6 h, 284 new cards

**Mon 28 Dec** (8.0 h)
- K32 (T2) Going multi-GPU
- K33 (T2) Parallelism strategies for inference
- G13 (T2) Memory and context evals
- G19 (T1) Cost modeling and unit economics of an LLM feature
- L38 (T2) Consensus and leader election
- L40 (T1) Circuit breakers, bulkheads and timeouts
- Q11 (T1) Amazon Bedrock
- Q12 (T2) SageMaker
- V08 (T2) AI product failure modes

**Tue 29 Dec** (7.5 h)
- K38 (T2) Packaging and model lifecycle
- G26 (T2) Prompt management
- H17 (T2) Index operations
- I11 (T2) Code execution and sandboxing
- L42 (T2) Distributed transactions
- L66 (T2) Realtime at scale
- L68 (T2) Feed generation
- Q13 (T2) GPUs on AWS
- Q18 (T2) GPUs and TPUs on GCP; GKE GPU node pools
- V13 (T2) Structured problem solving

**Wed 30 Dec** (7.3 h)
- K39 (T2) Releases for models and engine configs
- I12 (T2) Coding agents
- L75 (T1) Observability for distributed systems
- L76 (T1) SLOs, error budgets and availability math
- L78 (T1) Safe change
- Q21 (T1) Cloud cost management
- W07 (T1) Public speaking 1

**Thu 31 Dec** (7.3 h)
- I14 (T1) Agent observability
- I15 (T1) Agent evaluation
- I19 (T2) Frameworks compared
- L81 (T1) Rate limiting
- Y09 (T1) Design: chat and messaging
- R09 (T2) GPUs on Kubernetes
- R12 (T1) Observability

**Fri 01 Jan** (7.8 h)
- K40 (T1) LLM-aware load balancing and routing
- I20 (T2) Agent security
- J07 (T1) Agent and multi-turn evals
- Y10 (T1) Design: social feed
- Y25 (T1) AI design: RAG platform (multi-tenant, ACL-aware, fresh)
- R13 (T1) LLM observability
- X09 (T1) FDE and customer-simulation rounds

**Sat 02 Jan** (7.7 h)
- K41 (T1) Autoscaling GPUs
- J10 (T1) Online evaluation
- J11 (T2) Production feedback loops
- Y26 (T1) AI design: LLM gateway (routing, caching, limits, cost attribution, fallbacks)
- M15 (T2) API gateway and backend-for-frontend patterns for AI apps
- R17 (T1) LLMOps release management
- R20 (T2) LLM gateways and proxies
- X11 (T2) Project deep-dive

## Week 8: Ship and defend (04 Jan to 10 Jan 2027)

- **Focus:** Inference economics, capacity planning, observability; safety and red-teaming; voice agents; deploy on AWS and GCP; AI system designs; the streaming chat UI.
- **Gate artifact:** The same RAG app live on AWS and on GCP from infrastructure as code.
- **Mock:** Full mock loop: coding, deep dive, system design, FDE, behavioral. Core complete on Sun 10 Jan.
- **Load:** 52 topics (T1 17, T2 35, T3 0), 46.1 h, 276 new cards

**Mon 04 Jan** (7.6 h)
- K42 (T2) Orchestration stacks
- G23 (T2) Streaming UX and partial results
- H21 (T2) RAG cost and latency tuning
- L77 (T2) Incident response
- L79 (T2) Backups, restore and disaster recovery
- L80 (T2) Data retention, deletion and privacy; security and abuse prevention
- O03 (T2) React core
- O04 (T1) Streaming chat UI
- V10 (T1) FDE craft 2

**Tue 05 Jan** (7.2 h)
- K43 (T1) Inference observability
- I17 (T2) Voice agents
- A05 (T2) TypeScript essentials for AI apps
- L82 (T1) Multi-tenant design
- Q25 (T1) Deploy an LLM app end to end on AWS and on GCP
- R14 (T2) Alerting and on-call
- R15 (T2) Incident response and postmortems; an incident library for AI systems
- V11 (T2) Sales engineering

**Wed 06 Jan** (7.6 h)
- K44 (T2) Overload control
- K45 (T2) Failure recovery and chaos testing
- I22 (T2) Agent platform concerns
- L85 (T2) Load testing, capacity planning and performance budgets
- Y19 (T1) Design: photo-sharing app, run as a full mock interview
- Y24 (T2) Case study: the GitLab database incident
- Y27 (T1) AI design: agent platform (tools, sandbox, state, queues, observability)
- R18 (T2) Deployment strategies for models
- R19 (T2) Monitoring quality in production

**Thu 07 Jan** (7.2 h)
- K46 (T2) Inference security
- I23 (T2) Skills, sub-agents and context-efficient tool loading (progressive disclosure)
- J12 (T2) Human evaluation
- Y28 (T1) AI design: eval and release platform
- R24 (T2) Cost monitoring and attribution for AI workloads
- S04 (T1) Jailbreaks and misuse
- S06 (T2) Data leakage paths
- W03 (T1) Negotiating offers and contracts

**Fri 08 Jan** (8.0 h)
- K47 (T1) Inference economics
- J14 (T2) Safety and red-team evals
- B19 (T2) Drift
- Y29 (T1) AI design: realtime voice agent
- Y30 (T1) AI design: model-serving platform for a multi-model GPU fleet
- S07 (T2) Excessive agency and tool abuse
- S11 (T2) Red-teaming practice
- S12 (T2) Guardrail systems
- X12 (T2) Resume and portfolio narrative that shows engineering depth

**Sat 09 Jan** (8.4 h)
- K48 (T1) Capacity planning from benchmark data
- J15 (T2) Eval tooling
- J17 (T2) Self-repairing and self-improving eval loops
- Y33 (T1) AI design: customer-support assistant with human handoff
- M12 (T2) SaaS plumbing
- N13 (T2) Operating databases
- S16 (T1) Regulation
- U10 (T2) Incident library
- X13 (T1) Full mock loop and retro

## Week 9: Training (11 Jan to 17 Jan 2027)

- **Focus:** Fine-tuning, LoRA variants, RL (PPO, GRPO), preference optimization; training infrastructure; classical ML depth; data engineering.
- **Gate artifact:** A LoRA fine-tune with a before-and-after regression suite.
- **Mock:** Two mocks, mixed rounds.
- **Load:** 68 topics (T1 0, T2 57, T3 11), 47.3 h, 250 new cards

**Mon 11 Jan** (8.0 h)
- D18 (T2) Pretraining
- E02 (T2) Supervised fine-tuning and instruction tuning
- E03 (T2) Dataset curation for tuning
- E05 (T2) QLoRA, DoRA, adapters, prefix and prompt tuning; PEFT tradeoffs
- A14 (T2) Estimation
- A17 (T2) Optimizers
- L06 (T3) Design patterns
- L11 (T3) Event contracts and event schema evolution
- L29 (T3) Hot and cold storage, archival
- P01 (T2) Pipelines
- V03 (T2) Pricing AI
- Y46 (T2) ML design: fraud or anomaly detection

**Tue 12 Jan** (7.6 h)
- E06 (T2) RL foundations for LLM work
- B05 (T2) Calibration, log loss, Brier score, reliability diagrams
- B07 (T2) Class imbalance
- L37 (T2) Clocks and ordering
- L39 (T2) Distributed locks, leases, Redlock and fencing tokens
- L41 (T3) Gossip, membership, service discovery and distributed hash tables
- P02 (T2) Orchestration
- P06 (T2) Data quality
- V07 (T2) Product metrics
- V12 (T2) Enterprise sales cycle
- F11 (T3) Cluster scheduling for training

**Wed 13 Jan** (8.2 h)
- E07 (T2) PPO
- E08 (T2) RLHF, RLAIF and reward models; preference data
- E09 (T2) Preference optimization without RL
- E10 (T2) GRPO and RL with verifiable rewards; reward design and reward hacking
- B12 (T2) Dimensionality reduction
- B13 (T2) Feature engineering and preprocessing
- Y18 (T2) Design: a database migration with zero downtime
- Y23 (T2) Case study: the Amazon Dynamo paper
- P07 (T2) Data versioning and lineage
- V14 (T2) Market sizing and competitive analysis
- Y47 (T2) ML design: feed or ads ranking

**Thu 14 Jan** (7.9 h)
- E11 (T2) Distillation
- E13 (T2) Catastrophic forgetting and continual learning
- E14 (T2) Evaluating a fine-tune
- F01 (T2) Training memory math
- F02 (T2) Checkpointing, resumption, fault tolerance, spot training
- B14 (T2) Anomaly detection
- B17 (T2) Hyperparameter optimization
- Y36 (T2) AI design: fine-tuning platform and feature store
- Y44 (T3) AI design: distributed training platform and GPU cluster scheduler
- P08 (T2) Feature stores and training-serving skew; point-in-time correctness
- V22 (T2) Go-to-market basics

**Fri 15 Jan** (8.0 h)
- F03 (T2) Data loading at scale
- F04 (T2) Distributed training
- F05 (T3) FSDP and ZeRO stages 1 to 3
- F06 (T3) Parallelism in training
- C04 (T2) Training dynamics
- N06 (T2) Document stores
- N07 (T2) DynamoDB and wide-column thinking
- N08 (T3) Cassandra and ScyllaDB
- P09 (T2) Labeling and annotation
- P10 (T2) Datasets for LLMs
- W08 (T2) Public speaking 2
- W10 (T2) Handling Q&A and pushback

**Sat 16 Jan** (7.6 h)
- F07 (T3) Collectives and interconnects
- F08 (T2) Experiment tracking and reproducibility
- F09 (T2) Training cost and capacity planning
- F10 (T3) Profiling training
- C08 (T2) Seq2seq and the origin of attention
- C13 (T2) Mixed precision, gradient accumulation, memory-saving tricks
- C14 (T2) Transfer learning and fine-tuning strategies
- N14 (T2) Scaling Postgres
- N15 (T2) Schema migrations and data backfills at scale
- R16 (T2) MLOps
- X16 (T2) AI-assisted interviews and pairing with AI tools

## Week 10: Inference depth and modalities (18 Jan to 24 Jan 2027)

- **Focus:** Kernels, MoE, tiered KV, disaggregation, specialized serving; speech, vision, state space models; search internals and sketches; data platforms.
- **Gate artifact:** One specialized serving benchmark (multi-LoRA or speech), plus HyperLogLog and t-digest from scratch.
- **Mock:** Two mocks, mixed rounds.
- **Load:** 66 topics (T1 0, T2 53, T3 13), 45.2 h, 238 new cards

**Mon 18 Jan** (7.7 h)
- K24 (T2) GPU programming model
- K25 (T3) Triton kernels
- K28 (T3) CUDA graphs
- D15 (T2) Efficient attention
- A26 (T2) DSA kata 6
- L54 (T2) Task schedulers and DAG workflow orchestration
- L55 (T3) Rule engines, triggers and fanout patterns
- L56 (T2) Contention
- L57 (T2) Stream processing
- P04 (T2) Warehouse modeling and dbt
- V15 (T2) Finance literacy
- J19 (T3) Evaluating speech and voice agents

**Tue 19 Jan** (7.7 h)
- K30 (T3) Draft-free speculation
- K34 (T3) MoE inference
- K35 (T2) Long-context serving
- D16 (T2) Mixture of Experts
- D17 (T2) State space models
- D22 (T2) Multimodal LLMs
- L58 (T2) Search systems
- L59 (T2) Search quality
- L60 (T2) Search operations
- P05 (T2) Lakehouse and table formats
- V16 (T3) Fundraising
- K66 (T3) Compression beyond quantization

**Wed 20 Jan** (7.2 h)
- K36 (T3) Tiered KV systems
- K37 (T2) Prefill-decode disaggregation
- K49 (T2) Specialized workloads: structured output and tool-calling inference
- G22 (T2) Batch and async inference APIs; offline pipelines
- C12 (T2) Contrastive learning and CLIP
- L61 (T2) Search features
- L62 (T2) Counting at scale
- L63 (T2) HyperLogLog and mergeable sketches
- L64 (T3) Count-min sketch, top-k heavy hitters, reservoir sampling, live reactions
- Q16 (T2) GCP data
- V17 (T3) Contracts and commercial terms

**Thu 21 Jan** (7.5 h)
- K50 (T2) Specialized workloads: multi-LoRA serving, hot-swap, batching across adapters
- G28 (T2) Multimodal app patterns
- H20 (T2) Multimodal retrieval
- C16 (T2) Speech models
- L65 (T2) t-digest and streaming percentiles
- Y05 (T2) Design: ticket booking system
- Y08 (T2) Design: search service
- R10 (T2) Kubernetes packaging and state
- R11 (T2) GitOps and progressive delivery
- V23 (T2) Customer success and support for AI products

**Fri 22 Jan** (7.5 h)
- K51 (T2) Specialized workloads: vision-language inference; embedding and reranker serving
- K52 (T2) Specialized workloads: agentic, multi-turn and reasoning-model inference
- K55 (T2) Specialized workloads: speech serving, streaming ASR and TTS, real-time factor
- H22 (T2) Scaling retrieval
- Y12 (T2) Design: recommendation system
- Y31 (T2) AI design: semantic cache and vector search service
- Y32 (T2) AI design: document-processing pipeline (ingest, OCR, extraction, human review)
- Y37 (T2) AI design: batch inference pipeline
- T06 (T2) Speech stack deep dive
- W11 (T2) Storytelling

**Sat 23 Jan** (7.6 h)
- K61 (T3) Beyond NVIDIA
- K62 (T2) Edge and on-device inference
- I13 (T2) Computer-use and browser agents
- I18 (T2) Telephony and realtime transport
- C17 (T2) Vision transformers and vision-language models (ViT, CLIP, SigLIP, LLaVA-style)
- M10 (T2) Backend performance
- N09 (T2) Search engines as databases
- N10 (T2) Analytical databases
- U06 (T2) Reading large codebases
- W12 (T2) Difficult conversations
- G30 (T3) Multilingual LLM apps

## Week 11: Enterprise and domain (25 Jan to 31 Jan 2027)

- **Focus:** Healthcare, identity, on-prem, multi-region; privacy, unlearning, governance; storage engines; reading an engine and building a mini one.
- **Gate artifact:** A mini inference engine benchmarked against a real one, and an erasure verification test.
- **Mock:** Two mocks, one of them a customer simulation.
- **Load:** 67 topics (T1 0, T2 47, T3 20), 43.6 h, 228 new cards

**Mon 25 Jan** (7.2 h)
- L43 (T2) Storage engine constraints and tradeoffs
- L44 (T3) Building blocks
- L45 (T2) Log-structured storage and Bitcask
- L46 (T2) LSM trees
- L47 (T3) Compaction and amplification
- P11 (T2) Data governance
- Q20 (T3) Azure essentials
- Q22 (T2) Well-architected reviews
- Q23 (T2) Hybrid, on-prem and air-gapped deployment; private networking to model APIs
- Q24 (T2) Multi-cloud and portability tradeoffs; data gravity
- V18 (T2) Strategy

**Tue 26 Jan** (7.4 h)
- K56 (T2) Read an inference engine
- H23 (T3) Knowledge graphs and entity-centric retrieval
- L48 (T2) Object storage
- L49 (T2) Durability
- L50 (T3) Columnar formats and analytical storage
- L67 (T3) Social data modeling
- L69 (T3) Geospatial search
- Q26 (T3) Serverless GPU and inference clouds
- R21 (T3) Platform engineering
- R22 (T2) Performance and chaos testing in pipelines
- R23 (T3) Service mesh and zero-trust networking
- S08 (T2) Threat modeling for AI systems
- S09 (T2) Supply chain

**Wed 27 Jan** (7.7 h)
- L70 (T3) Geofencing and point in polygon
- L71 (T3) Seen filtering, matching and recommendation algorithms
- L72 (T2) Uploads and image delivery
- L73 (T3) Video systems
- L74 (T3) File sync
- L83 (T2) Multi-region
- L84 (T2) Architecture styles
- S10 (T2) Application security essentials
- S13 (T2) Privacy technology
- S14 (T2) Machine unlearning and the right to erasure in AI systems
- S15 (T2) Attacks on models
- V19 (T2) CTO craft

**Thu 28 Jan** (7.2 h)
- Y07 (T2) Design: object store like S3
- Y13 (T3) Design: nearby search
- Y14 (T3) Design: ride matching
- Y17 (T2) Design: observability and SLO platform
- Y22 (T2) Case study: how Discord stores trillions of messages
- S17 (T2) AI governance
- S18 (T2) Compliance programs
- S19 (T2) Responsible AI
- S20 (T3) AI safety and alignment basics
- S21 (T2) Safety for high-stakes domains
- W13 (T2) Stakeholder management and managing up

**Fri 29 Jan** (6.8 h)
- K57 (T2) Build a mini inference engine
- H24 (T2) Connectors and data sync for enterprise search
- Y34 (T2) AI design: healthcare assistant (PHI, audit, guardrails)
- Y35 (T2) AI design: multi-tenant AI SaaS with usage billing
- T01 (T2) Healthcare data standards
- T02 (T2) Clinical workflows and where AI fits
- T03 (T2) Healthcare compliance in practice
- T04 (T2) Clinical-grade RAG and guideline assistants
- T05 (T2) Voice AI for clinics

**Sat 30 Jan** (7.2 h)
- Y40 (T2) AI design: enterprise search assistant with permissions
- Y45 (T2) AI design: PII redaction gateway and data-erasure service
- M09 (T2) Web security basics
- M13 (T3) Integrations
- M14 (T3) File handling
- N11 (T3) Graph databases and time-series databases
- T07 (T2) Enterprise identity
- T08 (T2) Enterprise integration
- T09 (T2) Deploying inside the customer
- T13 (T2) Compliance automation for AI
- W14 (T2) Leadership

## Week 12: Differentiators and final loops (01 Feb to 07 Feb 2027)

- **Focus:** Frontend for AI apps; paper reproduction; the inference capstone; the T3 sweep; final know-cold review.
- **Gate artifact:** The capstone performance report and a working chat front end.
- **Mock:** Three full mock loops.
- **Load:** 66 topics (T1 0, T2 16, T3 50), 32.8 h, 164 new cards

**Mon 01 Feb** (5.4 h)
- K53 (T3) Specialized workloads: batch inference and RL rollout inference
- D24 (T3) Interpretability basics
- A04 (T3) Git beyond basics
- A18 (T3) Loss landscapes, convexity, saddle points, second-order methods
- Y11 (T2) Design: collaborative editor
- O01 (T2) Web fundamentals
- O02 (T2) Modern JavaScript for UI
- O05 (T2) Next.js
- V20 (T2) Team building

**Tue 02 Feb** (5.2 h)
- K54 (T3) Specialized workloads: diffusion inference, denoising, sampling
- D26 (T3) Beyond autoregression
- A27 (T3) Probability toolkit
- B10 (T3) SVMs, kNN, naive Bayes
- B11 (T3) Clustering
- Y15 (T3) Design: video platform
- Y16 (T3) Design: file sync service
- O06 (T2) State and data fetching
- O07 (T2) AI UX patterns
- V21 (T3) Operating cadence
- B21 (T3) Causal thinking

**Wed 03 Feb** (5.6 h)
- K58 (T3) Reproduce inference research
- E12 (T3) Model merging
- E15 (T3) Tokenizer and embedding surgery
- B15 (T3) Time series basics
- B16 (T3) Recommender systems
- Y38 (T2) AI design: content moderation system
- O08 (T3) Styling systems
- O09 (T3) Performance and accessibility
- O10 (T3) Frontend testing
- O11 (T2) Rapid demos
- W15 (T2) Writing that gets read

**Thu 04 Feb** (5.7 h)
- E16 (T3) RL environments and reward shaping for agents
- B18 (T3) Explainability
- C06 (T3) CNNs
- Y39 (T2) AI design: coding assistant and code search
- Y41 (T2) AI design: text-to-SQL analytics assistant
- O12 (T3) Auth flows in the browser
- O13 (T3) Data visualization for AI dashboards
- P03 (T3) Spark and distributed dataframes; when DuckDB or Polars is enough
- P12 (T3) Streaming data platform end to end
- T10 (T3) Edge AI and hardware-aware models
- W16 (T3) Facilitation and workshops
- W17 (T3) Executive presence and cross-cultural communication

**Fri 05 Feb** (5.3 h)
- K59 (T2) Inference capstone
- G29 (T3) Programmatic prompt optimization (DSPy)
- C07 (T3) RNNs, LSTMs, GRUs, and why attention replaced them
- C09 (T3) Autoencoders and VAEs; latent spaces
- C10 (T3) Diffusion models
- Y42 (T3) AI design: prompt management and experimentation service
- Y43 (T3) AI design: AI interview-prep platform
- T11 (T3) RL in products
- T12 (T3) Search, ranking and recommendation systems in production
- T14 (T3) AI for business analysis
- T15 (T3) Education and assessment AI
- W18 (T3) Personal brand

**Sat 06 Feb** (5.6 h)
- K64 (T3) CPU inference and SIMD
- I21 (T3) A2A and inter-agent protocols; agent identity and auth
- C11 (T3) GANs
- C15 (T3) Scaling laws, double descent, grokking
- M11 (T2) Node and TypeScript backends
- U07 (T3) Open-source contribution
- U08 (T3) Reproducing research
- U11 (T3) Publishing and portfolio
- U12 (T2) Estimating and planning engineering work
- X14 (T2) Offer stage
- C18 (T3) Graph neural networks

