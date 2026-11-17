# AI Mastery: master topic index

630 topics across three pillars. Plan runs Mon 16 Nov 2026 to Sun 7 Feb 2027. Weeks 1 to 8 are the interview-ready core and hold every T1 topic. Weeks 9 to 12 are the extension.

## How to read a row

- **ID**: domain letter plus number. Use it to open a topic chat (for example `K06`).
- **Tier**: T1 = asked in nearly every loop, full package, about 70 min, 8 cards. T2 = working depth, about 45 min, 4 cards. T3 = differentiator, lite package, about 25 min, 2 cards.
- **Wk**: scheduled week (1 to 12). Day-level order is in `02-week-plan.md` and the tracker.
- **Kata or drill**: the small implementation or practice that proves the topic. It is a starting idea; the topic chat may sharpen it.
- **Source**: I = Inference Engineering module, S = System Design lesson, F = Fanout AI engineering module, R = 26-project layer (project in brackets), + = added to close a gap.

Counts: T1 205, T2 331, T3 94. Card target 3152. Topic-package time about 527 hours.

## Domains

| Letter | Domain | Pillar | Topics | T1 | Hours |
|---|---|---|---|---|---|
| A | Foundations and applied math | 1 | 27 | 11 | 24 |
| B | Classical machine learning | 1 | 21 | 5 | 16 |
| C | Deep learning | 1 | 18 | 1 | 12 |
| D | Transformers and LLM internals | 1 | 26 | 12 | 24 |
| E | Post-training: fine-tuning, preference optimization, RL | 1 | 16 | 2 | 12 |
| F | Training infrastructure | 1 | 11 | 0 | 7 |
| G | LLM application layer: prompts, context, memory, cost, latency | 1 | 30 | 17 | 29 |
| H | Retrieval and RAG | 1 | 25 | 11 | 23 |
| I | Agents and orchestration | 1 | 23 | 9 | 21 |
| J | Evals and quality | 1 | 19 | 10 | 18 |
| K | Inference engineering and hardware | 1 | 66 | 21 | 55 |
| L | System design concepts | 2 | 85 | 32 | 72 |
| Y | System design drills and case studies | 2 | 47 | 14 | 39 |
| M | Backend engineering | 2 | 16 | 4 | 13 |
| N | Databases | 2 | 15 | 4 | 12 |
| O | Frontend engineering | 2 | 13 | 1 | 8 |
| P | Data engineering | 2 | 12 | 0 | 8 |
| Q | Cloud: AWS, GCP, Azure | 2 | 26 | 11 | 23 |
| R | DevOps, platform, MLOps, LLMOps | 2 | 25 | 8 | 21 |
| S | Security, privacy, safety, governance | 2 | 21 | 6 | 18 |
| T | Domain and applied AI | 2 | 15 | 0 | 10 |
| U | Research and engineering craft | 2 | 13 | 1 | 9 |
| V | Business and product | 3 | 24 | 6 | 20 |
| W | People skills: negotiation, influence, speaking | 3 | 19 | 8 | 17 |
| X | Interview craft | 3 | 17 | 11 | 17 |


# Pillar 1: AI engineer

## A. Foundations and applied math

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| A01 | T2 | 1 | Python for AI engineering: typing, dataclasses, pydantic, packaging with uv | Typed config loader that rejects bad input with clear errors | I00.05 |
| A02 | T1 | 1 | Async Python: event loop, asyncio, concurrency vs parallelism, the GIL | Fire 50 fake LLM calls three ways (sequential, gather, semaphore) and time them | + |
| A03 | T2 | 1 | Linux and shell fluency: processes, pipes, ssh, tmux, htop, nvidia-smi | One pipeline that finds the top memory hogs, then kill and restart one cleanly | I00.07 |
| A04 | T3 | 12 | Git beyond basics: rebase, bisect, worktrees, clean history | Bisect a planted bug in a 20-commit toy repo | + |
| A05 | T2 | 8 | TypeScript essentials for AI apps: types, async, zod, fetch streams | Typed client that reads tokens from a mock SSE endpoint | + |
| A06 | T2 | 1 | Debugging method: reproduce, isolate, hypothesize, instrument | Find 3 planted bugs while keeping a written hypothesis log | + |
| A07 | T2 | 1 | Profiling Python: cProfile, py-spy, line and memory profilers | Profile a slow tokenizer loop and get a 10x speedup | + |
| A08 | T1 | 1 | Vectors, dot product, norms, cosine similarity | Cosine vs dot by hand; find a case where the rankings differ | R1,I00.02 |
| A09 | T1 | 1 | Matrices, matmul, tensor shapes, broadcasting, einsum | Predict 15 tensor shapes, then verify in NumPy | R1,I00.02 |
| A10 | T2 | 6 | Eigenvalues, SVD, low-rank approximation (why LoRA works) | Compress a weight matrix at rank r; plot error vs rank | R1 |
| A11 | T1 | 2 | Derivatives, gradients, chain rule, Jacobians | Numerical vs analytic gradient check on a small function | R1 |
| A12 | T1 | 2 | Backpropagation and autodiff from scratch | Scalar autograd engine in 80 lines; train XOR | R1,F |
| A13 | T1 | 3 | Probability essentials: distributions, expectation, variance, conditional probability, Bayes | Bayes update: is my eval improvement real or noise | R1,I00.04 |
| A14 | T2 | 9 | Estimation: MLE, MAP, and why cross-entropy is maximum likelihood | Fit a coin and a Gaussian by MLE; connect to log loss | R1 |
| A15 | T1 | 3 | Statistics for experiments: confidence intervals, bootstrap, hypothesis tests, power, sample size | Bootstrap a CI for accuracy on 200 eval items; solve for the sample size you need | R1,I00.04 |
| A16 | T1 | 1 | Information theory: entropy, cross-entropy, KL divergence, perplexity | Perplexity of a tiny bigram model by hand | R1,F |
| A17 | T2 | 9 | Optimizers: SGD, momentum, Adam, AdamW, schedules, warmup | Race SGD vs Adam on a ravine function; plot the paths | R2 (2A) |
| A18 | T3 | 12 | Loss landscapes, convexity, saddle points, second-order methods (Newton, L-BFGS, K-FAC idea) | Newton vs gradient descent on a quadratic; count steps | R2 (2B) |
| A19 | T2 | 5 | Numerical stability: softmax overflow, log-sum-exp, floating point formats (fp32, bf16, fp16, fp8) | Break naive softmax with large logits; fix it with log-sum-exp | R1,I11 |
| A20 | T2 | 1 | Complexity for AI systems: big-O of attention, compute vs memory, throughput math | Time attention for n from 256 to 4096; fit the exponent | I00.01 |
| A21 | T1 | 1 | DSA kata 1: arrays, hashing, two pointers, sliding window | 3 timed problems, complexity explained aloud | + |
| A22 | T1 | 2 | DSA kata 2: stacks, queues, heaps, top-k, intervals | Top-k with a heap; merge intervals | + |
| A23 | T2 | 3 | DSA kata 3: trees, tries, graphs, BFS, DFS, topological sort | Trie autocomplete; topo-sort a task DAG | + |
| A24 | T2 | 4 | DSA kata 4: recursion, backtracking, dynamic programming | Edit distance and longest common subsequence | + |
| A25 | T1 | 4 | DSA kata 5: build a component (LRU cache, rate limiter, hash ring) | LRU cache and token bucket from scratch, with tests | + |
| A26 | T2 | 10 | DSA kata 6: strings, binary search, bit tricks, complexity proofs | Binary search on the answer; 3 timed problems | + |
| A27 | T3 | 12 | Probability toolkit: Monte Carlo, Markov chains, sampling methods | Estimate pi; build a Markov-chain text generator | R1 (1B) |

## B. Classical machine learning

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| B01 | T1 | 3 | Bias-variance tradeoff, underfitting and overfitting, learning curves | Fit polynomials of degree 1 to 15; plot train vs validation error | R3 |
| B02 | T1 | 4 | Regularization: L1, L2, early stopping, dropout as a regularizer | Ridge vs lasso on correlated features; watch the coefficients | R3 |
| B03 | T1 | 3 | Validation done right: splits, k-fold, stratification, time splits, data leakage | Plant a leak (scale before split); measure the fake gain | R3 |
| B04 | T1 | 4 | Classification metrics: precision, recall, F1, ROC-AUC, PR-AUC, confusion matrix, thresholds | Imbalanced dataset: show accuracy lying; pick a threshold by cost | R3 |
| B05 | T2 | 9 | Calibration, log loss, Brier score, reliability diagrams | Calibrate an overconfident model with temperature scaling | R3 |
| B06 | T1 | 2 | Ranking and retrieval metrics: recall@k, precision@k, MRR, NDCG, MAP | Implement recall@k, MRR and NDCG by hand on a toy ranking | R3,S09.09 |
| B07 | T2 | 9 | Class imbalance: resampling, class weights, focal loss, threshold moving | Compare 3 fixes on a 1% positive dataset | R3 |
| B08 | T2 | 3 | Linear and logistic regression from scratch: the loss and the gradient | Logistic regression in NumPy; match sklearn | R3 |
| B09 | T2 | 4 | Decision trees, random forests, gradient boosting (XGBoost, LightGBM) | Beat a neural net with LightGBM on a tabular set; explain why | R3 (3A) |
| B10 | T3 | 12 | SVMs, kNN, naive Bayes: when the old tools still win | kNN vs logistic regression on small data; plot decision boundaries | R3 |
| B11 | T3 | 12 | Clustering: k-means, DBSCAN, hierarchical; choosing k | k-means from scratch; fail it on two moons, fix with DBSCAN | R3 |
| B12 | T2 | 9 | Dimensionality reduction: PCA, t-SNE, UMAP, and reading embedding plots honestly | PCA from SVD; project sentence embeddings | R3 |
| B13 | T2 | 9 | Feature engineering and preprocessing: scaling, encoding, missing data, pipelines | sklearn Pipeline that cannot leak | R3 |
| B14 | T2 | 9 | Anomaly detection: z-scores, isolation forest, autoencoder residuals | Flag injected anomalies in a metric stream | R3 (3B) |
| B15 | T3 | 12 | Time series basics: stationarity, lag features, backtesting | Walk-forward backtest vs random split; show the leak | R3 |
| B16 | T3 | 12 | Recommender systems: collaborative filtering, two-tower, candidate generation and ranking | Matrix factorization on a toy ratings matrix | R3,S12.08 |
| B17 | T2 | 9 | Hyperparameter optimization: grid, random, Bayesian (Optuna), early stopping, AutoML | Optuna vs random search on LightGBM with the same budget | R2 (2B),R3 (3A) |
| B18 | T3 | 12 | Explainability: SHAP, LIME, permutation importance, and their traps | SHAP on a boosted model; find a spurious feature | R3 |
| B19 | T2 | 8 | Drift: data drift, concept drift, PSI, KS tests, monitoring | Simulate drift; detect it with PSI and a KS test | R12 (12B) |
| B20 | T2 | 3 | ML problem framing: baselines, error analysis, when not to use ML | One-page problem framing for a churn model | + |
| B21 | T3 | 12 | Causal thinking: confounding, A/B tests vs observational data, uplift, Simpson's paradox | Simulate Simpson's paradox; show the naive and the adjusted estimate | + |

## C. Deep learning

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| C01 | T1 | 2 | Neural networks from scratch: MLP, forward and backward pass | NumPy MLP on an MNIST subset, no autograd | R1 (1A),F |
| C02 | T2 | 2 | Activations, initialization, vanishing and exploding gradients | Plot activation statistics per layer under 3 initializations | R4 |
| C03 | T2 | 2 | Normalization: batch norm, layer norm, RMSNorm; pre-norm vs post-norm | Train a deep MLP with and without norm; compare stability | R4,I02.03 |
| C04 | T2 | 9 | Training dynamics: reading loss curves, LR finder, gradient clipping, debugging a model that will not learn | Diagnose 4 broken training runs from their curves alone | R2 |
| C05 | T2 | 2 | PyTorch fluency: tensors, autograd, nn.Module, DataLoader, hooks, devices | Rewrite the NumPy MLP in PyTorch; add a forward hook | R4,I00.05 |
| C06 | T3 | 12 | CNNs: convolution, pooling, receptive field, ResNet skip connections | Tiny CNN on a CIFAR subset; visualize the filters | R4 |
| C07 | T3 | 12 | RNNs, LSTMs, GRUs, and why attention replaced them | Char-RNN; show it forgetting long context | R4 |
| C08 | T2 | 9 | Seq2seq and the origin of attention | Additive attention on a toy sequence-reversal task | R4,F |
| C09 | T3 | 12 | Autoencoders and VAEs; latent spaces | VAE on MNIST; interpolate between two digits | R4 |
| C10 | T3 | 12 | Diffusion models: forward noise, denoising, schedulers, latent diffusion | Toy 2D diffusion that samples a spiral | R4,I26.08 |
| C11 | T3 | 12 | GANs: generator, discriminator, mode collapse | 1D GAN; show mode collapse | R4 |
| C12 | T2 | 10 | Contrastive learning and CLIP: InfoNCE, in-batch negatives | InfoNCE loss on toy pairs; inspect the similarity matrix | R4 (4B) |
| C13 | T2 | 9 | Mixed precision, gradient accumulation, memory-saving tricks | Measure memory and speed: fp32 vs bf16 autocast | R6 |
| C14 | T2 | 9 | Transfer learning and fine-tuning strategies: freezing, discriminative learning rates | Fine-tune a small BERT classifier: frozen vs full | R4 |
| C15 | T3 | 12 | Scaling laws, double descent, grokking: what bigger buys | Reproduce double descent on a toy model | R4 |
| C16 | T2 | 10 | Speech models: Whisper, wav2vec, CTC, streaming ASR basics | Transcribe audio with a small Whisper: chunked vs full | R4 (4A) |
| C17 | T2 | 10 | Vision transformers and vision-language models (ViT, CLIP, SigLIP, LLaVA-style) | Zero-shot classify images with CLIP; break it with a typographic attack | R4 (4B) |
| C18 | T3 | 12 | Graph neural networks: message passing, GCN, when a graph beats a table | 2-layer GCN on a toy citation graph in NumPy | + |

## D. Transformers and LLM internals

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| D01 | T1 | 1 | What an LLM is: next-token prediction, autoregression, training vs inference | Bigram language model in 40 lines; sample from it | F03 |
| D02 | T1 | 1 | Tokenization: BPE, WordPiece, unigram, byte-level; vocab size tradeoffs; special tokens | Train a BPE tokenizer on a small corpus; count tokens for 5 languages | F03 |
| D03 | T1 | 1 | Embeddings and the unembedding: token to vector and back, weight tying | Inspect nearest neighbors in a small model's embedding table | F02,F03 |
| D04 | T1 | 2 | Self-attention: queries, keys, values, scaling, causal masks | Single-head attention in NumPy with a causal mask | F04,F05,I00.03,I02.02 |
| D05 | T1 | 2 | Multi-head attention and its variants: MHA, MQA, GQA, MLA | Convert MHA to GQA; count parameters and KV-cache size | F04 |
| D06 | T2 | 2 | Positional information: sinusoidal, learned, RoPE, ALiBi; length extrapolation, YaRN | Implement RoPE; verify the relative-shift property | F04 |
| D07 | T2 | 2 | The transformer block: MLP, SwiGLU, residual stream, pre-norm | Assemble a block; remove the residuals and watch training die | F05,I02.03 |
| D08 | T1 | 2 | Full forward pass of a decoder-only transformer, end to end | nanoGPT-size model from scratch; train on Shakespeare | F05,I00.06,I02.01 |
| D09 | T2 | 3 | Architectures: encoder-only, decoder-only, encoder-decoder (BERT, GPT, T5) | Same task with a BERT embedding and with GPT-style generation | F03 |
| D10 | T1 | 1 | Decoding and sampling: greedy, temperature, top-k, top-p, min-p, repetition penalty, beam | Sampler playground: same logits through 6 strategies | F03,I02.04 |
| D11 | T1 | 1 | Logits, logprobs, perplexity; reading model confidence | Use logprobs to flag a low-confidence answer | F03 |
| D12 | T2 | 6 | Constrained decoding: grammars, JSON mode, logit masking | Logit-mask a toy LM so it can only emit valid JSON | I26.01 |
| D13 | T1 | 2 | Context windows: what fills them, cost growth, lost in the middle, context rot | Needle-in-a-haystack test at 5 positions | F04 |
| D14 | T1 | 3 | The LLM optimization map: where time and memory go, and the levers (KV cache, batching, quantization, distillation, speculation) | One-page map: lever, what it saves, what it costs | F06 |
| D15 | T2 | 10 | Efficient attention: sliding window, sparse, linear; long-context tricks | Windowed attention mask; measure memory vs full attention | F06,I20 |
| D16 | T2 | 10 | Mixture of Experts: routing, sparsity, load balancing, training and serving costs | Toy MoE layer with top-2 gating; inspect expert load | F04,I19 |
| D17 | T2 | 10 | State space models: S4, Mamba, selective scan, hybrids; where they beat transformers | Minimal selective-SSM step; compare memory growth to attention | R4,your research |
| D18 | T2 | 9 | Pretraining: objectives, data pipelines, compute, Chinchilla scaling | Estimate FLOPs and cost to train a 1B-parameter model (6ND) | F03 |
| D19 | T1 | 5 | Hallucination: causes, detection, mitigation; grounding and abstention | Cite-or-abstain check on 20 QA items | F08 |
| D20 | T1 | 5 | Reasoning models: chain of thought, thinking tokens, test-time compute, self-consistency | Self-consistency vote on 20 math items; cost vs accuracy | F08,I26.05 |
| D21 | T2 | 5 | Verification: verifiers, critics, process vs outcome supervision, tool-checked answers | Generate-then-verify loop with a code checker | F08 |
| D22 | T2 | 10 | Multimodal LLMs: image tokens, projectors, audio tokens, any-to-any | Count image tokens at different resolutions; cost impact | I26.03 |
| D23 | T2 | 1 | The open-model landscape: Llama, Qwen, Mistral, Gemma, DeepSeek, Phi; licenses and architecture differences | Read 3 model cards; fill a comparison table | F07,I01.01 |
| D24 | T3 | 12 | Interpretability basics: probing, attention patterns, logit lens, sparse autoencoders | Logit lens on GPT-2 small | + |
| D25 | T2 | 4 | Chat templates, system prompts, special tokens, stop sequences, tool-call formats | Render one conversation in 3 chat templates; break one on purpose | I01.02 |
| D26 | T3 | 12 | Beyond autoregression: diffusion language models, the encoder revival, small language models | Small model vs large model on a classification task | + |

## E. Post-training: fine-tuning, preference optimization, RL

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| E01 | T1 | 5 | Fine-tune vs RAG vs prompt vs tools: the decision framework | Decision memo for 5 scenarios with cost estimates | + |
| E02 | T2 | 9 | Supervised fine-tuning and instruction tuning: data format, loss masking, hyperparameters; managed fine-tuning APIs | SFT a small model on 500 examples; eval before and after | R6 |
| E03 | T2 | 9 | Dataset curation for tuning: collection, cleaning, dedup, synthetic data, quality filters | Build a 300-example set with an LLM plus filters | R5 |
| E04 | T1 | 6 | LoRA: low-rank adapters, rank and alpha, target modules, merging | LoRA from scratch on one linear layer; then with PEFT | F,R6 |
| E05 | T2 | 9 | QLoRA, DoRA, adapters, prefix and prompt tuning; PEFT tradeoffs | QLoRA a 4-bit model on a free GPU; memory table | F |
| E06 | T2 | 9 | RL foundations for LLM work: MDPs, policy gradient, REINFORCE, advantage | REINFORCE on CartPole | F |
| E07 | T2 | 9 | PPO: clipped objective, GAE, why it is stable | PPO on CartPole in single-file style | F |
| E08 | T2 | 9 | RLHF, RLAIF and reward models; preference data | Train a tiny reward model on pairwise preferences | + |
| E09 | T2 | 9 | Preference optimization without RL: DPO, IPO, KTO | DPO loss by hand; run one training step | + |
| E10 | T2 | 9 | GRPO and RL with verifiable rewards; reward design and reward hacking | GRPO-style group-relative update on a toy task | F |
| E11 | T2 | 9 | Distillation: logits, sequence-level, synthetic-data distillation, small-model strategy | Distill a classifier into one 10x smaller | R9 |
| E12 | T3 | 12 | Model merging: linear, SLERP, TIES; when it works | Merge two fine-tunes; evaluate both parents and the child | + |
| E13 | T2 | 9 | Catastrophic forgetting and continual learning: replay, EWC, adapters | Sequential tasks: show forgetting, fix it with replay | R6 (6B) |
| E14 | T2 | 9 | Evaluating a fine-tune: held-out sets, regressions, overfitting signs, safety drift | Regression suite before and after a LoRA | R12 |
| E15 | T3 | 12 | Tokenizer and embedding surgery: adding tokens, domain vocabulary | Add 5 tokens; resize and initialize the embeddings | + |
| E16 | T3 | 12 | RL environments and reward shaping for agents | Wrap a text task as a Gym environment with a verifier | your project (AdaptArena) |

## F. Training infrastructure

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| F01 | T2 | 9 | Training memory math: weights, gradients, optimizer state, activations | Predict then measure peak memory for a small model | R6 |
| F02 | T2 | 9 | Checkpointing, resumption, fault tolerance, spot training | Kill a run mid-epoch; resume it bit-exact | R6 |
| F03 | T2 | 9 | Data loading at scale: streaming datasets, shuffling, tokenization throughput | Find the dataloader bottleneck; fix it with workers and pinning | R5 |
| F04 | T2 | 9 | Distributed training: DDP, gradient sync, effective batch size | DDP on 2 processes (CPU is fine); verify gradient equivalence | R6 (6A) |
| F05 | T3 | 9 | FSDP and ZeRO stages 1 to 3: sharding parameters, gradients, optimizer state | Memory table: DDP vs ZeRO-1, 2, 3 for a 7B model (paper math) | R6 |
| F06 | T3 | 9 | Parallelism in training: tensor, pipeline, sequence, context parallel | Diagram each on a 4-GPU toy; estimate communication volume | R6 |
| F07 | T3 | 9 | Collectives and interconnects: all-reduce, NCCL, NVLink, InfiniBand, RoCE | Compute all-reduce time for one gradient at 3 link speeds | R7,I18.02 |
| F08 | T2 | 9 | Experiment tracking and reproducibility: seeds, configs, MLflow or W&B | Two runs, same seed, identical curves; log both to MLflow | R12 |
| F09 | T2 | 9 | Training cost and capacity planning: 6ND, GPU-hours, on-demand vs reserved vs spot | Cost a fine-tune and a pretrain on 3 GPU types | R7 |
| F10 | T3 | 9 | Profiling training: GPU utilization, dataloader stalls, torch profiler | Profile a run; raise utilization from under 50% to over 90% | R7 (7A) |
| F11 | T3 | 9 | Cluster scheduling for training: Slurm, Kubernetes batch (Kueue, Volcano), quotas, preemption, gang scheduling | Simulate FIFO vs fair-share vs preemptive scheduling on one job trace | + |

## G. LLM application layer: prompts, context, memory, cost, latency

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| G01 | T1 | 1 | Token optimization playbook: measure, send less, reuse, generate less, cheaper models, batch, fewer calls, self-host | Token ledger: simulate a 20-turn chat, apply 6 levers, print the bill | interview question,F06 |
| G02 | T1 | 1 | LLM API mechanics: messages, roles, parameters, streaming, stop reasons, usage accounting | Call two providers; log tokens, latency and stop reason | + |
| G03 | T1 | 1 | Prompt engineering fundamentals: instructions, examples, structure, delimiters, roles | Improve a failing prompt in 5 measured iterations | + |
| G04 | T2 | 3 | Advanced prompting: few-shot selection, chain of thought, decomposition, self-critique, prompt chaining | Chain vs single prompt on a multi-step task; measure both | F08 |
| G05 | T1 | 6 | Structured outputs: JSON schema, constrained decoding, validation and repair | Pydantic-validated extraction with retry on failure; report the failure rate | I26.01 |
| G06 | T1 | 3 | Function and tool calling: schemas, parallel calls, tool choice, error returns | Two-tool assistant; measure wrong-tool and bad-argument rates | F09 |
| G07 | T1 | 2 | Prompt caching: prefix matching, breakpoints, TTLs, cache-friendly prompt layout | Reorder a prompt to be cacheable; measure hit rate and cost | I10 |
| G08 | T1 | 3 | Context engineering: what to include, ordering, budgets, formats | Context budgeter that packs by priority under a token cap | + |
| G09 | T1 | 4 | Context management over long sessions: truncation, rolling summaries, compaction, scratchpads | 3 strategies on a 60-turn chat; recall test on early facts | interview question |
| G10 | T1 | 4 | Just-in-time retrieval and sub-agents as context isolation | Sub-agent that returns a 200-token brief instead of 20k raw tokens | + |
| G11 | T1 | 4 | Memory types: working, semantic, episodic, procedural | Tiny memory store with all 4 types; show one read and one write path | interview question |
| G12 | T1 | 4 | Memory systems: write policies, retrieval, decay, conflicts, forgetting; vector vs graph memory | Memory with update-on-conflict; test it with a contradicting fact | + |
| G13 | T2 | 7 | Memory and context evals: long-conversation recall benchmarks | Build a 30-question memory probe set | + |
| G14 | T1 | 5 | Long context vs RAG vs fine-tune for knowledge | Same corpus 3 ways: cost, latency and accuracy table | + |
| G15 | T1 | 2 | Latency anatomy: queue, prefill (TTFT), decode (TPOT x tokens), tools, network | Instrument a streaming call; split the latency into its parts | I04.01 |
| G16 | T1 | 5 | Latency optimization for apps: streaming, parallel calls, speculative work, smaller models, output caps | Cut a 3-step chain's p50 in half; show the trace | + |
| G17 | T1 | 5 | Model routing and cascades: classifiers, confidence, fallbacks | Cheap-first cascade with escalation; cost vs quality curve | R9 (9B) |
| G18 | T1 | 6 | Model selection tradeoffs: quality, cost, latency, context, modality, privacy, licensing | Selection memo for 3 workloads using a scoring grid | F07 |
| G19 | T1 | 7 | Cost modeling and unit economics of an LLM feature | Model cost per user per month under 3 designs | + |
| G20 | T2 | 3 | Semantic caching: embeddings, thresholds, invalidation, risks | Semantic cache; plot hit rate vs false-hit rate by threshold | + |
| G21 | T2 | 4 | Reliability at the API layer: rate limits, retries, backoff with jitter, timeouts, fallbacks, circuit breakers | Client wrapper that survives injected 429s and 500s | S02.09 |
| G22 | T2 | 10 | Batch and async inference APIs; offline pipelines | Resumable batch job for 1,000 items against a mock API | I26.06 |
| G23 | T2 | 8 | Streaming UX and partial results: SSE, cancellation, tool-call deltas | Stream with mid-response cancel; verify generation stops | + |
| G24 | T2 | 3 | Embeddings in apps: models, dimensions, Matryoshka, normalization, batching, cost | Truncate Matryoshka dimensions; plot recall vs dimension | F02 |
| G25 | T2 | 6 | Guardrails in the app path: input and output checks, moderation, schema and policy validators | Pre and post filter chain; measure the added latency | R13 |
| G26 | T2 | 7 | Prompt management: versioning, templates, registries, rollout and rollback | Prompt registry with a version pin and an A/B flag | R12 |
| G27 | T2 | 5 | Provider landscape and differences: OpenAI, Anthropic, Google, open-weights hosts; feature matrix | One adapter interface over 2 providers | F07 |
| G28 | T2 | 10 | Multimodal app patterns: vision input, document images, audio in and out | Extract a table from a scanned page with a VLM; score accuracy | + |
| G29 | T3 | 12 | Programmatic prompt optimization (DSPy): signatures, optimizers, when it pays | Optimize a classifier prompt with a small training set | + |
| G30 | T3 | 10 | Multilingual LLM apps: tokens per language, Indic languages, code-mixing, translate-then-prompt vs native prompting | Same message in English, Hindi, Telugu and Hinglish through 2 tokenizers: token counts and cost | your work |

## H. Retrieval and RAG

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| H01 | T1 | 2 | Embeddings for retrieval: bi-encoders, similarity metrics, normalization, model choice (MTEB) | Embed 500 passages; compare 2 models on recall@5 | F02 |
| H02 | T1 | 2 | Vector search fundamentals: exact kNN vs ANN, recall vs latency | Brute-force kNN in NumPy; time it against corpus size | F02 |
| H03 | T1 | 2 | HNSW: graph layers, M, efConstruction, efSearch | hnswlib: sweep efSearch; plot recall vs latency | F02 |
| H04 | T2 | 2 | IVF, product quantization, IVF-PQ, DiskANN, ScaNN; memory math | FAISS IVF-PQ: memory and recall vs a flat index | F02 |
| H05 | T1 | 2 | Sparse retrieval: TF-IDF, BM25, inverted index | BM25 from scratch on 1,000 documents | F02,S09.04,S09.05 |
| H06 | T1 | 3 | Hybrid search and fusion: reciprocal rank fusion, weighted scores | Hybrid with RRF; find queries where each side wins | F02,S09.13 |
| H07 | T1 | 3 | Reranking: cross-encoders, LLM rerankers, late interaction (ColBERT) | Add a cross-encoder reranker; measure lift and latency | F02 |
| H08 | T1 | 3 | Chunking: fixed, recursive, semantic, structural; size and overlap | 4 chunkers on one corpus; recall@5 table | + |
| H09 | T1 | 3 | The RAG pipeline end to end: ingest, index, retrieve, augment, generate, cite | Minimal RAG in 80 lines, no framework | R10 |
| H10 | T1 | 4 | Query understanding: rewriting, expansion, HyDE, multi-query, decomposition, routing | HyDE and multi-query vs the raw query; measure | S09.07 |
| H11 | T2 | 4 | Metadata, filtering and access control in retrieval (pre-filter vs post-filter) | ACL-aware search; prove there is no cross-tenant leak | + |
| H12 | T1 | 4 | Grounding and citations: attribution, quote extraction, abstention | Answer with span citations; verify every citation | R10 (10A) |
| H13 | T1 | 4 | RAG failure taxonomy and debugging: retrieval miss, ranking miss, context loss, generation error | Label 30 failures by stage; fix the biggest bucket | + |
| H14 | T2 | 4 | Advanced patterns: parent-child, sentence window, contextual retrieval, GraphRAG, RAPTOR | Contextual chunk headers; recall before and after | + |
| H15 | T2 | 5 | Agentic RAG: iterative retrieval, self-RAG, corrective RAG | Retrieve, judge, retry loop with a budget | + |
| H16 | T2 | 3 | Vector databases: pgvector, Qdrant, Milvus, Pinecone, Weaviate, FAISS; how to choose | Same workload on pgvector and Qdrant; operations notes | F02,R8 |
| H17 | T2 | 7 | Index operations: freshness, incremental updates, deletes, re-embedding, versioning | Blue-green re-index with zero downtime (toy) | R8 (8B),S09.10 |
| H18 | T2 | 6 | Document AI: parsing PDFs, layout, tables, OCR, VLM parsing | Parse 5 ugly PDFs 3 ways; score table fidelity | + |
| H19 | T2 | 6 | Text-to-SQL and structured-data QA: schema linking, validation, safety | Natural language to SQL on a 5-table database with an execution check | + |
| H20 | T2 | 10 | Multimodal retrieval: image and text, page-image retrieval (ColPali-style) | CLIP image search over 200 images | R4 (4B) |
| H21 | T2 | 8 | RAG cost and latency tuning: top-k, context size, caching, small rerankers | Pareto sweep: top-k and chunk size vs cost and accuracy | + |
| H22 | T2 | 10 | Scaling retrieval: sharding, replicas, quantized indexes, multi-tenant layouts | Capacity math for 100M vectors: RAM, shards, QPS | R8 (8B),S09.11 |
| H23 | T3 | 11 | Knowledge graphs and entity-centric retrieval | Extract triples; answer a 2-hop question | + |
| H24 | T2 | 11 | Connectors and data sync for enterprise search: permissions, incremental crawl | Incremental sync with tombstones for deleted documents | S09.12 |
| H25 | T2 | 4 | Fine-tuning embedding models and rerankers: contrastive loss, hard-negative mining, synthetic queries | Fine-tune a small embedding model on 500 synthetic pairs; recall@5 before and after | + |

## I. Agents and orchestration

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| I01 | T1 | 5 | The agent loop: model, tools, state, stop conditions; ReAct | Agent loop in 60 lines, no framework | F09 |
| I02 | T1 | 5 | Workflows vs agents: chains, routers, parallelization, orchestrator-workers, evaluator-optimizer | Same task as a workflow and as an agent; compare cost and variance | F09 |
| I03 | T1 | 5 | Tool design: naming, schemas, descriptions, error messages, idempotency, granularity | Redesign 3 bad tools; measure call success before and after | F09 |
| I04 | T1 | 6 | MCP: architecture, servers, clients, tools, resources, prompts, transports, auth | Write an MCP server with 2 tools; connect a client | F09 |
| I05 | T1 | 6 | Budgets and guards: step limits, token and cost caps, loop detection, timeouts | Reproduce a looping agent; add 3 guards | interview research |
| I06 | T1 | 6 | Planning and decomposition: plan-then-execute, replanning, task graphs | Planner-executor that replans on failure | F09 |
| I07 | T1 | 6 | Agent failure modes: compounding error, tool misuse, context overflow, goal drift; reliability math | Simulate per-step success p over n steps; plot end-to-end success | + |
| I08 | T2 | 6 | Multi-agent patterns: supervisor, swarm, hierarchical, debate; when not to use them | Supervisor with 2 workers vs a single agent; cost table | R10 (10B) |
| I09 | T2 | 6 | State and orchestration: graphs, state machines, checkpoints, durable execution (Temporal-style) | Checkpointed agent that resumes after a crash | R10,S08.07 |
| I10 | T2 | 6 | Human in the loop: approvals, interrupts, escalation, review queues | Approval gate in front of a destructive tool | + |
| I11 | T2 | 7 | Code execution and sandboxing: containers, microVMs, permissions, egress control | Run model-written code in a locked-down container | R13 |
| I12 | T2 | 7 | Coding agents: repo context, edit formats, test loops, evaluation | Mini coding agent that fixes a failing test | R10 (10B) |
| I13 | T2 | 10 | Computer-use and browser agents: observations, action spaces, reliability | Scripted browser task driven by a vision model (toy) | + |
| I14 | T1 | 7 | Agent observability: traces, spans, tool logs, replay | Trace an agent with OpenTelemetry-style spans; find the slow step | R12 |
| I15 | T1 | 7 | Agent evaluation: task success, trajectory checks, tool accuracy, cost and steps | 10-task agent benchmark with graded trajectories | R12 |
| I16 | T2 | 6 | Agent memory in practice: scratchpads, notes files, long-running tasks, handoffs | Agent that survives a context reset by writing notes | I26.04 |
| I17 | T2 | 8 | Voice agents: STT, LLM, TTS pipeline, turn-taking, barge-in, latency budget | Latency budget for one voice turn; measure a local pipeline | R4 (4A),your work |
| I18 | T2 | 10 | Telephony and realtime transport: WebRTC, SIP, streaming audio, realtime APIs | Stream microphone audio over a WebSocket to a mock ASR | S13.08 |
| I19 | T2 | 7 | Frameworks compared: LangGraph, LlamaIndex, CrewAI, AutoGen, vendor agent SDKs; build vs adopt | Port the 60-line agent to one framework; list what you gained and lost | + |
| I20 | T2 | 7 | Agent security: prompt injection through tools, confused deputy, least privilege | Inject through a web-page tool; add a defense; retest | R13 (13B) |
| I21 | T3 | 12 | A2A and inter-agent protocols; agent identity and auth | Two agents exchange a task card over HTTP | + |
| I22 | T2 | 8 | Agent platform concerns: multi-tenancy, queues, concurrency, cost attribution | Per-tenant cost ledger for agent runs | + |
| I23 | T2 | 8 | Skills, sub-agents and context-efficient tool loading (progressive disclosure) | Lazy-load tool descriptions; measure the context saved | + |

## J. Evals and quality

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| J01 | T1 | 3 | Eval mindset: what to measure, error analysis first, evals as the product spec | Read 50 outputs; write a failure taxonomy | + |
| J02 | T1 | 3 | Golden sets: sourcing, labeling, size, stratification, maintenance | Build a 50-item golden set with a rubric | R12 |
| J03 | T1 | 4 | Reference-based metrics: exact match, F1, BLEU, ROUGE, embedding similarity, and their limits | Show ROUGE rewarding a wrong answer | + |
| J04 | T1 | 4 | LLM-as-judge: rubric design, pairwise vs pointwise, calibration against humans | Judge with a rubric; measure agreement with your own labels | + |
| J05 | T1 | 5 | Judge biases: position, verbosity, self-preference, leniency; mitigations | Swap answer order; measure position bias | + |
| J06 | T1 | 4 | RAG evals: context precision and recall, faithfulness, answer relevance | Implement recall@5 and a faithfulness check from scratch | interview research (take-home) |
| J07 | T1 | 7 | Agent and multi-turn evals: trajectories, simulated users, task completion | User-simulator eval for a support agent | R12 |
| J08 | T1 | 5 | Statistical rigor in evals: variance, seeds, confidence intervals, paired tests, sample size | Paired bootstrap between two prompts | I00.04 |
| J09 | T1 | 6 | Regression gates in CI: thresholds, flaky evals, cost control | GitHub Action that blocks a prompt regression | R12 (12A) |
| J10 | T1 | 7 | Online evaluation: A/B tests, shadow traffic, canaries, guardrail metrics | Design an A/B test for a new model; do the power calculation | R12 |
| J11 | T2 | 7 | Production feedback loops: implicit signals, thumbs, annotation queues, data flywheel | Turn 100 logged traces into new eval cases | R12,S09.08 |
| J12 | T2 | 8 | Human evaluation: guidelines, inter-annotator agreement (kappa), adjudication | Two labelers (you and a model); compute kappa | + |
| J13 | T2 | 5 | Public benchmarks and leaderboards: MMLU, GPQA, SWE-bench, MTEB, arenas; contamination | Run a 50-item slice of a public benchmark locally | F07 |
| J14 | T2 | 8 | Safety and red-team evals: jailbreak suites, refusal rates, toxicity | 20-attack suite against your own bot; score it | R13 |
| J15 | T2 | 8 | Eval tooling: promptfoo, Ragas, DeepEval, Inspect, Braintrust, Langfuse; build vs buy | Same eval in your harness and in one tool; compare | R12 |
| J16 | T2 | 6 | Synthetic eval data: generation, filtering, adversarial cases | Generate 100 hard negatives; filter them with a judge | + |
| J17 | T2 | 8 | Self-repairing and self-improving eval loops | Harness that proposes a prompt fix and reruns the suite | your project |
| J18 | T2 | 5 | Classifier and extraction evals: per-field accuracy, schema validity, cost per correct answer | Extraction scorecard with per-field F1 | + |
| J19 | T3 | 10 | Evaluating speech and voice agents: word error rate, latency per turn, interruptions, task completion | Word error rate from scratch plus a 10-call scorecard | your work |

## K. Inference engineering and hardware

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| K01 | T2 | 1 | What inference engineering is: the stack from model to GPU to production, and the levels of the craft | Draw the stack for one request; mark where each millisecond goes | I-IN |
| K02 | T2 | 1 | Inference setup: remote GPU box, CUDA, drivers and PyTorch compatibility, model hub | Stand up a GPU machine (free tier is fine); verify the whole stack with one script | I00.07,I00.08 |
| K03 | T2 | 1 | Run your first LLM: choose, download, load, generate, stream; watch memory, utilization and power; serve it over HTTP | Serve a 1 to 3B model behind a tiny HTTP endpoint; record tokens per second | I01 |
| K04 | T1 | 1 | One token end to end: forward pass trace, Q, K, V at inference, logits to the next token | Hook every stage of one forward pass; print the shapes | I02 |
| K05 | T1 | 1 | Prefill vs decode: why autoregression recomputes work, and how each phase behaves | Time prefill and per-token decode separately; explain the gap | I03.01,I03.02,I03.03 |
| K06 | T1 | 1 | KV cache: what is cached, why decode becomes linear, cached vs uncached generation | Build a KV cache for a tiny model; time generation with and without it | I03.04,F06 |
| K07 | T1 | 1 | Memory math: weights, runtime overhead, KV memory per token, context and concurrency limits | Will-it-fit calculator; measure VRAM vs context length and match the formula | I03.05,I03.06 |
| K08 | T1 | 2 | Inference metrics: TTFT, TPOT, ITL, end-to-end latency, throughput | Streaming benchmark client that reports all five | I04.01 |
| K09 | T2 | 2 | Benchmark design: concurrency vs request rate, arrival patterns, workload mixes, warm-up, steady state, reproducibility | Same server, closed-loop vs open-loop load; explain the different answers | I04.02,I04.03,I04.04 |
| K10 | T1 | 2 | Percentiles, variance, goodput, SLOs and failure rates; benchmark tools (GuideLLM and engine benchmarks) | Add p50, p95, p99 and goodput under an SLO to the harness | I04.05,I04.06,I04.07 |
| K11 | T1 | 2 | Break one GPU: baseline, sweeps, saturation, SLO failure and OOM boundaries; the operating envelope | Sweep concurrency and lengths until it breaks; chart the envelope | I05 |
| K12 | T1 | 3 | From PyTorch to a real engine: why naive serving breaks, starting vLLM, OpenAI-compatible API, engine metrics, the request path | Serve with vLLM; benchmark it against plain PyTorch serving | I06 |
| K13 | T1 | 3 | Batching: one-by-one, static, iteration-level scheduling, continuous batching | Toy scheduler simulator: 3 strategies on the same arrivals | I07.01,I07.02,I07.03,I07.06,R9 (9A) |
| K14 | T2 | 3 | Scheduler knobs and policy: token budgets, max sequences, max batched tokens, queueing, fairness, cancellation, preemption | Add priority classes and a token budget to the simulator; tune TTFT vs throughput | I07.04,I07.05 |
| K15 | T1 | 3 | PagedAttention and KV memory management: blocks, block tables, sharing, reclaim, preemption under KV pressure | Paged KV allocator vs contiguous allocation; measure fragmentation | I08 |
| K16 | T1 | 4 | Optimize one GPU: tunable baseline, GPU memory and KV capacity, the SLO-safe configuration with headroom | Tune 4 engine flags; report goodput before and after | I09 |
| K17 | T2 | 4 | Chunked prefill and long-prompt interference | Mixed workload: inter-token jitter with and without chunked prefill | I10.01,I10.02 |
| K18 | T1 | 4 | Prefix caching in the engine: automatic prefix caching, shared prompts, RAG and multi-turn reuse, RadixAttention, eviction and churn | Measure TTFT with shared vs unique prefixes; then cause cache churn | I10.03,I10.04,I10.05,I10.06 |
| K19 | T1 | 5 | Quantization fundamentals: precision, memory and hardware support; BF16, FP8, INT8, 4-bit | Quantize a linear layer by hand; plot error vs bits | I11.01,I11.02 |
| K20 | T2 | 5 | Quantization methods: AWQ, GPTQ, SmoothQuant; quantized GEMM and dequantization overhead; GGUF and bitsandbytes in practice | Same model at fp16, 8-bit and 4-bit: speed, memory, eval score | I11.03,I11.04 |
| K21 | T2 | 5 | KV-cache quantization; measuring capacity, performance and quality regression; the Pareto frontier | Build a quality, speed and memory Pareto chart for 4 configurations | I11.05,I11.06,I11.07 |
| K22 | T2 | 5 | Profiling workflow: PyTorch profiler, memory snapshots, Nsight Systems and Compute, prefill vs decode profiles | Profile decode; name the top 3 operations and what bounds each | I12.01,I12.02,I12.03,I12.04,I12.05 |
| K23 | T1 | 5 | GPU execution and the roofline model: memory hierarchy, kernel launches, compute-bound vs memory-bound | Predict max tokens per second from memory bandwidth; compare to measured | I12.06,I12.07 |
| K24 | T2 | 10 | GPU programming model: threads, warps, blocks, memory access, coalescing | Read and annotate a simple CUDA kernel line by line | I13.01 |
| K25 | T3 | 10 | Triton kernels: programming model, tiling, reductions; writing softmax, RMSNorm, RoPE and fused operators | Triton vector add and softmax; benchmark against PyTorch | I13.02,I13.03,I13.04,I13.05,I13.06,I13.07 |
| K26 | T2 | 6 | Attention optimization: tiled attention, online softmax, FlashAttention; prefill vs decode attention; FlashInfer and serving backends | Naive attention vs scaled_dot_product_attention: memory and speed | I14 |
| K27 | T2 | 6 | Compilation: eager overhead, torch.compile, kernel fusion, graph breaks, dynamic shapes | torch.compile a model; measure warm-up cost and steady-state gain | I15.01,I15.02,I15.03 |
| K28 | T3 | 10 | CUDA graphs: capture and replay; memory, startup and steady-state tradeoffs | Capture a decode step as a CUDA graph; measure launch overhead removed | I15.04,I15.05 |
| K29 | T1 | 6 | Speculative decoding: draft and target models, parallel verification, acceptance rate, draft length, behavior under concurrency | Draft plus target model; measure acceptance rate and speedup | I16.01,I16.02,I16.03,I16.04 |
| K30 | T3 | 10 | Draft-free speculation: n-gram and prompt lookup, Medusa, EAGLE, multi-token prediction, dynamic speculation | Prompt-lookup decoding on a summarization task | I16.05,I16.06,I16.07 |
| K31 | T1 | 6 | Engine comparison: fair methodology; vLLM vs SGLang; TensorRT-LLM; llama.cpp, Ollama, MLX, TGI; a selection matrix | Same model on 2 engines; fair benchmark table and a recommendation | I17 |
| K32 | T2 | 7 | Going multi-GPU: when to scale out, topology (PCIe, NVLink), NCCL, collectives and communication overhead | Communication-cost estimate for tensor parallel at 2, 4 and 8 GPUs | I18.01,I18.02,I18.04 |
| K33 | T2 | 7 | Parallelism strategies for inference: tensor, pipeline, data and context parallelism | TP=2 vs 2 replicas: throughput and latency (measured or paper math) | I18.03,I18.05,I18.06,I18.07,I18.08 |
| K34 | T3 | 10 | MoE inference: token routing, expert parallelism and placement, hot experts, all-to-all communication, grouped GEMM | Simulate expert load imbalance; test two placement policies | I19 |
| K35 | T2 | 10 | Long-context serving: scaling behavior, prefill and attention bottlenecks, context-saving techniques | Budget KV memory for 128k contexts at 50 concurrent users | I20.01,I20.02,I20.03 |
| K36 | T3 | 10 | Tiered KV systems: CPU, SSD and remote offload; admission, eviction, locality | Two-tier KV cache simulation with an eviction policy | I20.04,I20.05,I20.06 |
| K37 | T2 | 10 | Prefill-decode disaggregation: why, pool sizing, KV transfer, the crossover point, independent scaling | Queueing simulation: pooled vs disaggregated under mixed load | I21 |
| K38 | T2 | 7 | Packaging and model lifecycle: weights, caches, cold starts, warm-up, readiness, health checks, draining, graceful shutdown | Measure cold start; add a readiness probe and graceful drain | I22.01,I22.02,I22.03,I22.04 |
| K39 | T2 | 7 | Releases for models and engine configs: versioning, canary, shadow traffic, rollback; multi-model and multi-replica serving | Shadow a new engine config; diff the latency distributions | I22.05,I22.06,I22.07 |
| K40 | T1 | 7 | LLM-aware load balancing and routing: queue-aware, prefix-aware and cache-aware | Round robin vs least-loaded vs prefix-aware in a simulation | I23.01,I23.02,I23.03 |
| K41 | T1 | 7 | Autoscaling GPUs: request, token and queue signals; warm capacity; GPU startup time | Autoscaler simulation with 3 signals; count SLO violations and cost | I23.04,I23.05 |
| K42 | T2 | 8 | Orchestration stacks: Ray Serve LLM, Kubernetes GPU scheduling, KServe; also Triton Inference Server, BentoML, NIM | Deploy on one stack; write down what it gave you for free | I23.06,I23.07 |
| K43 | T1 | 8 | Inference observability: Prometheus and Grafana; GPU, scheduler, KV and cache metrics; distributed tracing | Export server metrics; build a TTFT and queue-depth dashboard | I24.01,I24.02,I24.03 |
| K44 | T2 | 8 | Overload control: admission control, backpressure, load shedding, timeouts, cancellation, retries, priorities | Add admission control; compare goodput under 2x overload | I24.04,I24.05 |
| K45 | T2 | 8 | Failure recovery and chaos testing: OOM, worker, GPU and cache failures | Kill a replica under load; measure the blast radius and recovery time | I24.06,I24.07 |
| K46 | T2 | 8 | Inference security: API, network, tenant and model security; cache side channels | Show a timing side channel in a shared prefix cache (toy) | I24.08 |
| K47 | T1 | 8 | Inference economics: cost per request and per million tokens, goodput per dollar, GPU price-performance | Cost-per-million-tokens calculator from GPU price and measured throughput | I25.01,I25.02,I25.03 |
| K48 | T1 | 8 | Capacity planning from benchmark data: peak load, failure headroom, idle capacity; the cheapest system that meets the SLO | Plan capacity for 1M requests per day with N+1 headroom | I25.04,I25.05 |
| K49 | T2 | 10 | Specialized workloads: structured output and tool-calling inference (the cost of guided decoding) | Throughput with and without a JSON grammar | I26.01 |
| K50 | T2 | 10 | Specialized workloads: multi-LoRA serving, hot-swap, batching across adapters | Serve 2 adapters on one base model; switch per request | I26.02 |
| K51 | T2 | 10 | Specialized workloads: vision-language inference; embedding and reranker serving | Serve embeddings; sweep batch size for throughput | I26.03 |
| K52 | T2 | 10 | Specialized workloads: agentic, multi-turn and reasoning-model inference | Replay an agent trace; measure the prefix-cache hit rate per turn | I26.04,I26.05 |
| K53 | T3 | 12 | Specialized workloads: batch inference and RL rollout inference | Offline batch run tuned for throughput instead of latency | I26.06,I26.07 |
| K54 | T3 | 12 | Specialized workloads: diffusion inference, denoising, sampling, step budgets and quality | Latency vs step count for a small diffusion model | I26.08,I26.09 |
| K55 | T2 | 10 | Specialized workloads: speech serving, streaming ASR and TTS, real-time factor | Real-time factor for Whisper at 3 batch sizes | R4 (4A) |
| K56 | T2 | 11 | Read an inference engine: map the vLLM codebase; follow a request, the scheduler, KV allocation and attention dispatch | Trace one request through the code; write the map | I27 |
| K57 | T2 | 11 | Build a mini inference engine: runner, KV cache, batching, continuous batching, paged allocator, streaming API, prefix cache, metrics | Mini engine in under 500 lines; benchmark it against a real engine | I28 |
| K58 | T3 | 12 | Reproduce inference research: reading systems papers, rebuilding the baseline and workload, ablations, finding where it stops working | Reproduce one figure from an inference paper within 10% | I29 |
| K59 | T2 | 12 | Inference capstone: workload and SLO, model, hardware and engine choice, baseline, profile, optimize, scale, failure-test, cost, publish | One-page performance report with goodput and cost per million tokens | I30 |
| K60 | T2 | 5 | GPU hardware: SMs, HBM, tensor cores; A100, H100, H200, B200, L4, L40S compared | Fill a spec table; predict decode speed per GPU from bandwidth | R7 |
| K61 | T3 | 10 | Beyond NVIDIA: TPUs, Trainium, Inferentia, AMD MI300, Groq, Cerebras; tradeoffs | Cost-per-token comparison from public numbers | R7 |
| K62 | T2 | 10 | Edge and on-device inference: llama.cpp, MLX, ONNX Runtime, TensorRT, CoreML, WebGPU, Jetson | Run a quantized model on CPU; tokens per second vs thread count | I17.04,your research |
| K63 | T2 | 4 | Model formats and loading: safetensors, GGUF, ONNX; mmap; cold-start time | Measure load time: safetensors vs pickle; show the mmap effect | I22.02 |
| K64 | T3 | 12 | CPU inference and SIMD: small models on commodity hardware | Thread-count sweep; find the memory-bandwidth wall | + |
| K65 | T2 | 5 | Hardware-aware model selection: fit a model to a GPU by memory, bandwidth and cost | Selector script: given a GPU and an SLO, list the models that fit | R7 (7B) |
| K66 | T3 | 10 | Compression beyond quantization: pruning, sparsity, low-rank factorization; how they stack with distillation | Magnitude-prune a small model at 3 sparsity levels; accuracy and real speed | + |


# Pillar 2: Supplementary

## L. System design concepts

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| L01 | T1 | 1 | Requirements clarification and logical design: the seven-question spine | Run the spine on a small problem in 20 minutes; record it | S01.01,S01.02 |
| L02 | T1 | 1 | Non-functional requirements and tradeoffs: availability, durability, consistency, cost | Write NFRs with numbers for an LLM chat API | S01.03,S01.04,S01.05 |
| L03 | T1 | 1 | Back-of-the-envelope capacity planning; the latency numbers to know | 10 timed estimation drills | S01.06 |
| L04 | T2 | 1 | How a server handles many requests: threads, event loops, connection limits | Thread-per-request vs event loop under 1,000 slow clients | S01.07 |
| L05 | T1 | 2 | Scaling out: vertical vs horizontal, statelessness, monolith vs microservices | nginx round robin over 2 stateless app instances | S01.08,S01.09 |
| L06 | T3 | 9 | Design patterns: repository, strategy, adapter, dependency injection; extensible data modeling | Swap the storage backend behind a repository without touching handlers | S01.10,S01.11 |
| L07 | T2 | 2 | Cost-aware architecture and when not to add infrastructure | Cost per successful request for a design at 3 traffic levels | S01.12,S01.13 |
| L08 | T1 | 1 | API design contracts: resources, errors, versioning, pagination | Design and implement a paginated API with cursor tokens | S02.01 |
| L09 | T2 | 2 | Service-to-service communication: HTTP, REST, gRPC, GraphQL; TCP vs UDP | Same endpoint in REST and gRPC; compare latency and payload | S02.02,S02.03,S02.04 |
| L10 | T1 | 2 | API gateway vs load balancer; L4 vs L7; consistent-hashing load balancing | Sticky routing with consistent hashing; add a node and count moved keys | S02.05,S02.06,S02.07 |
| L11 | T3 | 9 | Event contracts and event schema evolution | Versioned event with a backward-compatible change and a consumer test | S02.08 |
| L12 | T1 | 2 | Retries, timeouts and idempotency | Payment endpoint that survives a double submit | S02.09 |
| L13 | T1 | 3 | Batching, backpressure, tail latency and load shedding | Queue with backpressure; show p99 under overload with and without shedding | S02.10,S02.11,S02.12,S02.13 |
| L14 | T1 | 2 | Realtime transports: polling, long polling, SSE, WebSockets, webhooks | SSE token stream plus a webhook with a signature check | S11.02 |
| L15 | T1 | 3 | AuthN and AuthZ: sessions, JWT, OAuth2, OIDC, API keys, mTLS, RBAC | JWT auth with refresh and a scope-checked route | + |
| L16 | T1 | 3 | Relational database design; a key-value store on SQL | Model a multi-tenant SaaS schema; justify every index | S03.01,S03.02 |
| L17 | T1 | 3 | Indexing and B-trees: composite, covering, when indexes hurt | EXPLAIN ANALYZE before and after 3 indexes | S03.03,S03.04 |
| L18 | T2 | 3 | Query planning: statistics, join strategies, reading plans | Make the planner pick a bad plan; fix it | S03.05 |
| L19 | T1 | 4 | ACID transactions, locking, isolation levels and MVCC | Reproduce lost update and write skew in Postgres | S03.06,S03.07 |
| L20 | T2 | 4 | WAL and crash recovery | Tiny write-ahead log with crash and replay | S03.08 |
| L21 | T1 | 4 | Scaling a relational database: ticket servers, replicas, partitioning, sharding | Streaming replica; measure lag; read stale data on purpose | S03.09,S03.10 |
| L22 | T2 | 4 | Changing a live database: online indexing, schema evolution, soft delete | Add an index and a column without blocking writes | S03.11,S03.12,S03.13 |
| L23 | T1 | 4 | NoSQL decision boundaries: document, key-value, columnar, wide-column, graph | Model one feature three ways; pick one and defend it | S04.01,S04.02,S04.03,S04.04 |
| L24 | T1 | 5 | Sharding, partitioning and hot partitions | Simulate a hot key; fix it with salting or splitting | S04.05,S04.06 |
| L25 | T1 | 5 | Consistent hashing | Hash ring with virtual nodes; measure key movement on resize | S04.07 |
| L26 | T2 | 5 | Distributed IDs: UUID, ObjectId, Snowflake; clock skew and ordering | Snowflake generator; insert benchmark against UUIDv4 | S04.08,S04.09,S04.10,S04.11 |
| L27 | T2 | 5 | Keyset pagination | Offset vs keyset pagination on 1M rows | S04.12 |
| L28 | T2 | 5 | Bloom filters | Bloom filter from scratch; false-positive rate vs bits per key | S04.13,S07.11 |
| L29 | T3 | 9 | Hot and cold storage, archival | Lifecycle policy that tiers old rows to cheap storage | S04.14 |
| L30 | T1 | 5 | Caching layers and patterns: cache-aside, read-through, write-through, write-behind | Cache-aside with Redis; measure hit rate and staleness | S05.01 |
| L31 | T1 | 5 | Distributed cache design, eviction policies (LRU, LFU), TTLs and reapers | LRU and LFU from scratch; replay a trace through both | S05.02,S05.03,S05.04 |
| L32 | T1 | 6 | Cache failure modes: stampede, penetration, avalanche; concurrency control; database fallback | Cause a stampede; fix it with a lock and jittered TTLs | S05.05,S05.06 |
| L33 | T2 | 6 | CDNs and edge caching: cache keys, purge, signed URLs | Cache-Control experiments through a local caching proxy | S13.02 |
| L34 | T1 | 6 | Distributed systems foundations: partial failure, unreliable networks, timeouts | Chaos proxy: inject latency and drops; watch retries amplify load | S06.01 |
| L35 | T1 | 6 | Consistency models; CAP and PACELC | Simulate stale reads under async replication; name the model | S06.02,S06.04 |
| L36 | T1 | 6 | Replication: leader-follower, multi-leader, leaderless; lag and failover | Toy leader-follower store with a failover that loses a write | S06.03 |
| L37 | T2 | 9 | Clocks and ordering: Lamport, vector and hybrid clocks; CRDTs for conflict-free merges | Vector clocks that detect a conflict; merge two replicas with a grow-only counter CRDT | S06.05 |
| L38 | T2 | 7 | Consensus and leader election: Raft, quorums | Walk Raft by hand through 5 scenarios; run a toy election | S06.06,S06.07 |
| L39 | T2 | 9 | Distributed locks, leases, Redlock and fencing tokens | Break a naive Redis lock with a pause; fix it with fencing | S06.08,S06.09 |
| L40 | T1 | 7 | Circuit breakers, bulkheads and timeouts | Circuit breaker around a flaky dependency | S06.10 |
| L41 | T3 | 9 | Gossip, membership, service discovery and distributed hash tables | Gossip simulation: rounds until every node knows | S06.11,S06.12,S06.13 |
| L42 | T2 | 7 | Distributed transactions: two-phase commit, sagas, the outbox pattern, CDC | Outbox table plus relay; kill it mid-flight; lose nothing | + |
| L43 | T2 | 11 | Storage engine constraints and tradeoffs: read, write and space amplification | Benchmark an append-only file vs an in-place file | S07.01,S07.02 |
| L44 | T3 | 11 | Building blocks: file-backed dictionary, binary formats, byte-range indexes, immutable versioned files | Binary file format with header, payload and checksum | S07.03,S07.04,S07.05,S07.06 |
| L45 | T2 | 11 | Log-structured storage and Bitcask | Bitcask clone in 100 lines | S07.07,S07.08 |
| L46 | T2 | 11 | LSM trees: memtable, WAL, SSTables, the read path, sparse indexes | Mini LSM with flush and a Bloom-filtered read path | S07.09,S07.10,S07.11 |
| L47 | T3 | 11 | Compaction and amplification | Add compaction to the mini LSM; measure write amplification | S07.12 |
| L48 | T2 | 11 | Object storage: object store vs database, S3 architecture, partition maps, metadata, the stream layer | Mini object store: metadata table plus chunk files | S07.13,S07.14,S07.15,S07.16,S07.17,S07.18 |
| L49 | T2 | 11 | Durability: replication, erasure coding, end-to-end checksums | Erasure-code a file 4+2; lose 2 shards; recover it | S07.19,S07.20 |
| L50 | T3 | 11 | Columnar formats and analytical storage: Parquet, encodings, predicate pushdown | Same query on CSV and Parquet in DuckDB; compare bytes scanned | + |
| L51 | T1 | 6 | Async work: delegation, task queue vs event stream, event bus | Move a slow step behind a queue; show the latency change | S08.01,S08.02,S08.03 |
| L52 | T1 | 6 | Queues in practice: lag, visibility timeouts, dead-letter queues, a Postgres SKIP LOCKED queue | SKIP LOCKED work queue with retries and a DLQ | S08.04,S08.06 |
| L53 | T1 | 6 | Log-based streaming (Kafka): partitions, consumer groups, offsets, retention, delivery semantics | Local Kafka or Redpanda: watch lag, a rebalance and a replay | S15.07 |
| L54 | T2 | 10 | Task schedulers and DAG workflow orchestration | Cron-like scheduler with leases so a job never runs twice | S08.05,S08.07 |
| L55 | T3 | 10 | Rule engines, triggers and fanout patterns | Fanout on write to 3 subscribers with one slow consumer | S08.08,S08.09 |
| L56 | T2 | 10 | Contention: inventory locking in a flash sale | 1,000 buyers, 10 items: no oversell, three locking strategies | S08.10 |
| L57 | T2 | 10 | Stream processing: windows, watermarks, exactly-once, Flink concepts | Tumbling and sliding windows with late events in plain Python | + |
| L58 | T2 | 10 | Search systems: inverted index, posting lists, boolean and tiered search, scoring recap | Inverted index with phrase queries | S09.01,S09.02,S09.03,S09.06 |
| L59 | T2 | 10 | Search quality: query understanding, relevance signals, evaluation | Tune relevance for 10 queries; report NDCG before and after | S09.07,S09.08,S09.09 |
| L60 | T2 | 10 | Search operations: index synchronization, sharding, crawler and indexing pipeline | Keep an index in sync with a database through an outbox | S09.10,S09.11,S09.12 |
| L61 | T2 | 10 | Search features: autocomplete, did-you-mean, related and recent searches | Trie autocomplete with popularity ranking | S09.14,S09.15,S09.16,S09.17 |
| L62 | T2 | 10 | Counting at scale: views, impressions, raw vs derived data, time-window buckets | View counter with bucketed aggregation and dedup | S10.01,S10.02,S10.03,S10.06,S10.07 |
| L63 | T2 | 10 | HyperLogLog and mergeable sketches | HyperLogLog from scratch; error vs memory | S10.04,S10.05 |
| L64 | T3 | 10 | Count-min sketch, top-k heavy hitters, reservoir sampling, live reactions | Count-min plus a heap for top-k on a stream | S10.08,S10.09,S10.10,S10.13 |
| L65 | T2 | 10 | t-digest and streaming percentiles | Streaming p99 with t-digest vs exact; error table | S10.11,S10.12 |
| L66 | T2 | 7 | Realtime at scale: WebSocket fleets, pub/sub, presence | WebSocket chat with presence over Redis pub/sub | S11.01 |
| L67 | T3 | 11 | Social data modeling: graph and follows, reactions, hashtags, unread indicators, tagging | Schema for follows and reactions; 3 hot queries with plans | S11.03,S11.04,S11.06,S11.07,S11.08,S11.09 |
| L68 | T2 | 7 | Feed generation: push, pull, hybrid; live commentary | Feed simulator that shows the celebrity problem | S11.05,S11.10 |
| L69 | T3 | 11 | Geospatial search: geohash, H3, S2, Redis GEO | Geohash proximity search | S12.01,S12.02,S12.03,S12.04 |
| L70 | T3 | 11 | Geofencing and point in polygon | Ray-casting point-in-polygon test | S12.05,S12.06 |
| L71 | T3 | 11 | Seen filtering, matching and recommendation algorithms | Bloom vs exact set for seen items: memory and error | S12.07,S12.08 |
| L72 | T2 | 11 | Uploads and image delivery: direct-to-storage, signed URLs, image CDN, avatar service | Presigned upload flow against a local S3-compatible store | S13.01,S13.02,S13.03 |
| L73 | T3 | 11 | Video systems: multipart upload, transcoding, adaptive bitrate, DRM, live streaming and WebRTC | Resumable chunked upload | S13.04,S13.05,S13.06,S13.07,S13.08 |
| L74 | T3 | 11 | File sync: fixed-block chunking, content addressing, versioned metadata | Content-addressed chunk store with dedup | S13.09,S13.10,S13.11 |
| L75 | T1 | 7 | Observability for distributed systems: metrics, logs, traces | Instrument a 2-service request with trace IDs end to end | S14.01 |
| L76 | T1 | 7 | SLOs, error budgets and availability math | SLO document for an LLM API; compute the error-budget burn | S14.02 |
| L77 | T2 | 8 | Incident response | Run a 30-minute tabletop incident with Claude as the pager | S14.03 |
| L78 | T1 | 7 | Safe change: deployments, canary, blue-green, feature flags, expand-contract migrations, parallel read drain | Zero-downtime column rename with expand-contract | S14.04,S14.05,S14.06 |
| L79 | T2 | 8 | Backups, restore and disaster recovery: RPO and RTO | Back up, destroy and restore a database; time it | S14.07,S14.08 |
| L80 | T2 | 8 | Data retention, deletion and privacy; security and abuse prevention | Deletion pipeline that proves a user is gone from every store | S14.09,S14.10 |
| L81 | T1 | 7 | Rate limiting: placement, keys, token bucket, sliding window; distributed limits | Redis-backed sliding-window limiter with per-tenant keys | S14.11,S14.12,S15.02 |
| L82 | T1 | 8 | Multi-tenant design: isolation models, noisy neighbors, quotas | Row-level security in Postgres for tenants | S14.13 |
| L83 | T2 | 11 | Multi-region: active-passive, active-active, data residency, conflict resolution | Latency and consistency table for 3 topologies | + |
| L84 | T2 | 11 | Architecture styles: event-driven, CQRS, event sourcing, service mesh | Split one module out of a monolith; list the new failure modes | + |
| L85 | T2 | 8 | Load testing, capacity planning and performance budgets | k6 or Locust load test; find the bottleneck | + |

## Y. System design drills and case studies

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| Y01 | T1 | 2 | Design: URL shortener, from one machine to scale | 35-minute timed design; record and self-grade | S15.01,S15.03 |
| Y02 | T2 | 4 | Design: product listing | Timed design; one schema and one cache decision defended | S15.04 |
| Y03 | T1 | 6 | Design: notification system | Timed design; then build dedup plus retry in 80 lines | S16.01 |
| Y04 | T2 | 6 | Design: Kafka-style log | Timed design; append-only log with offsets in 100 lines | S15.07 |
| Y05 | T2 | 10 | Design: ticket booking system | Timed design; seat hold with expiry | S16.02 |
| Y06 | T1 | 6 | Design: payment system | Timed design; ledger with idempotent double-entry writes | S16.03 |
| Y07 | T2 | 11 | Design: object store like S3 | Timed design | S15.06 |
| Y08 | T2 | 10 | Design: search service | Timed design | S16.04 |
| Y09 | T1 | 7 | Design: chat and messaging | Timed design | S16.06 |
| Y10 | T1 | 7 | Design: social feed | Timed design | S16.07 |
| Y11 | T2 | 12 | Design: collaborative editor | Timed design; toy CRDT or OT merge of two edits | S15.05 |
| Y12 | T2 | 10 | Design: recommendation system | Timed design | S16.05 |
| Y13 | T3 | 11 | Design: nearby search | Timed design | S16.08 |
| Y14 | T3 | 11 | Design: ride matching | Timed design | S17.01 |
| Y15 | T3 | 12 | Design: video platform | Timed design | S17.02 |
| Y16 | T3 | 12 | Design: file sync service | Timed design | S17.03 |
| Y17 | T2 | 11 | Design: observability and SLO platform | Timed design | S17.04 |
| Y18 | T2 | 9 | Design: a database migration with zero downtime | Written migration plan with rollback points | S17.05 |
| Y19 | T1 | 8 | Design: photo-sharing app, run as a full mock interview | 45-minute mock with Claude as interviewer; scorecard | S17.06 |
| Y20 | T2 | 5 | Case study: Instagram's first architecture | One-page teardown: what they built and what it cost them | S18.01 |
| Y21 | T1 | 3 | Case study: Stripe's idempotency keys | Teardown plus your own idempotency middleware | S18.02 |
| Y22 | T2 | 11 | Case study: how Discord stores trillions of messages | Teardown: the data model and each migration's trigger | S18.03 |
| Y23 | T2 | 9 | Case study: the Amazon Dynamo paper | Three-pass read; quorum drills with N, R, W | S18.04 |
| Y24 | T2 | 8 | Case study: the GitLab database incident | Postmortem teardown; write the 5 controls that would have saved them | S18.05 |
| Y25 | T1 | 7 | AI design: RAG platform (multi-tenant, ACL-aware, fresh) | 45-minute timed design; record and self-grade | + |
| Y26 | T1 | 7 | AI design: LLM gateway (routing, caching, limits, cost attribution, fallbacks) | Timed design; then a 100-line gateway | +,R9 |
| Y27 | T1 | 8 | AI design: agent platform (tools, sandbox, state, queues, observability) | Timed design | +,R10 |
| Y28 | T1 | 8 | AI design: eval and release platform | Timed design | R12 (12A) |
| Y29 | T1 | 8 | AI design: realtime voice agent | Timed design with a per-stage latency budget | your work |
| Y30 | T1 | 8 | AI design: model-serving platform for a multi-model GPU fleet | Timed design | R8 (8A) |
| Y31 | T2 | 10 | AI design: semantic cache and vector search service | Timed design | R8 (8B) |
| Y32 | T2 | 10 | AI design: document-processing pipeline (ingest, OCR, extraction, human review) | Timed design | + |
| Y33 | T1 | 8 | AI design: customer-support assistant with human handoff | Timed design | + |
| Y34 | T2 | 11 | AI design: healthcare assistant (PHI, audit, guardrails) | Timed design | R11 (11A) |
| Y35 | T2 | 11 | AI design: multi-tenant AI SaaS with usage billing | Timed design | + |
| Y36 | T2 | 9 | AI design: fine-tuning platform and feature store | Timed design | R6 |
| Y37 | T2 | 10 | AI design: batch inference pipeline | Timed design | + |
| Y38 | T2 | 12 | AI design: content moderation system | Timed design | R13 |
| Y39 | T2 | 12 | AI design: coding assistant and code search | Timed design | R10 (10B) |
| Y40 | T2 | 11 | AI design: enterprise search assistant with permissions | Timed design | + |
| Y41 | T2 | 12 | AI design: text-to-SQL analytics assistant | Timed design | + |
| Y42 | T3 | 12 | AI design: prompt management and experimentation service | Timed design | R12 |
| Y43 | T3 | 12 | AI design: AI interview-prep platform | Timed design | R11 (11B) |
| Y44 | T3 | 9 | AI design: distributed training platform and GPU cluster scheduler | Timed design | R6 (6A) |
| Y45 | T2 | 11 | AI design: PII redaction gateway and data-erasure service | Timed design | R13 (13A),your startup |
| Y46 | T2 | 9 | ML design: fraud or anomaly detection (features, delayed labels, thresholds, monitoring) | Timed design | R3 (3B) |
| Y47 | T2 | 9 | ML design: feed or ads ranking (candidate generation, ranking, exploration, feedback loops) | Timed design | + |

## M. Backend engineering

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| M01 | T1 | 2 | HTTP deeply: methods, headers, status codes, caching, CORS, cookies, the TLS handshake | Raw HTTP server on sockets; then a curl -v tour | + |
| M02 | T1 | 2 | FastAPI service skeleton: routing, validation, dependency injection, errors, OpenAPI | CRUD service with pydantic models and tests | + |
| M03 | T1 | 3 | Concurrency models: threads, processes, async, workers; CPU-bound vs IO-bound | Benchmark a sync vs async endpoint under IO load | S01.07 |
| M04 | T2 | 3 | Database access: connection pooling, ORM vs SQL, N+1 queries, migrations | Create an N+1 query, then fix it; add a migration | + |
| M05 | T2 | 4 | Background jobs and task queues: Celery, RQ, arq; scheduling; retries | Offload a slow LLM job; deliver the result by polling and by webhook | S08.01 |
| M06 | T1 | 4 | Streaming LLM backends: SSE, WebSockets, backpressure, cancellation, timeouts | Proxy a token stream; cancel upstream when the client disconnects | + |
| M07 | T2 | 4 | Testing: unit, integration, contract, fixtures, mocking LLMs, snapshot tests | pytest suite with a fake LLM and one contract test | + |
| M08 | T2 | 5 | Config, secrets, 12-factor, structured logging, error handling | Env-based config with a secrets loader; JSON logs with request IDs | + |
| M09 | T2 | 11 | Web security basics: OWASP Top 10, injection, XSS, CSRF, SSRF, input validation | Exploit and patch SQL injection and SSRF in a toy app | S14.10 |
| M10 | T2 | 10 | Backend performance: profiling endpoints, caching layers, pagination, payload size | Flame-graph an endpoint; cut p95 in half | + |
| M11 | T2 | 12 | Node and TypeScript backends: Express or Fastify, and when to choose Node | Port one endpoint to Fastify with zod validation | + |
| M12 | T2 | 8 | SaaS plumbing: organizations, roles, API keys, usage metering, billing hooks | API-key auth with per-key usage counters | S14.13 |
| M13 | T3 | 11 | Integrations: payments, email, webhooks at scale, third-party APIs | Webhook receiver with signature check and replay protection | + |
| M14 | T3 | 11 | File handling: uploads, presigned URLs, scanning, large files | Presigned upload flow against MinIO | S13.01 |
| M15 | T2 | 7 | API gateway and backend-for-frontend patterns for AI apps | Thin gateway that adds auth, limits and logging | S02.05 |
| M16 | T2 | 3 | Concurrency correctness: races, deadlocks, locks, atomics, idempotent handlers | Reproduce a lost-update race on a counter; fix it 3 ways | + |

## N. Databases

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| N01 | T1 | 2 | SQL fluency 1: joins, grouping, subqueries, set operations | 20 timed queries on a sample database | S03 |
| N02 | T1 | 2 | SQL fluency 2: window functions, CTEs, recursive queries | 10 window-function drills (rank, lag, running totals) | S03 |
| N03 | T1 | 3 | Query tuning: EXPLAIN, join strategies, statistics, rewriting | Make a 2-second query run in 20 ms | S03.05 |
| N04 | T2 | 3 | Postgres as an AI database: pgvector, JSONB, full-text search, hybrid queries | Hybrid search in a single SQL query | + |
| N05 | T1 | 4 | Redis: data structures, persistence, eviction, pub/sub, streams, Lua | Rate limiter, leaderboard and queue in Redis | S05.02 |
| N06 | T2 | 9 | Document stores: MongoDB modeling, indexes, aggregation | Model chat history as documents; compare to relational | S04.02 |
| N07 | T2 | 9 | DynamoDB and wide-column thinking: partition keys, GSIs, single-table design | Single-table design for a multi-tenant app | S04.03,S18.04 |
| N08 | T3 | 9 | Cassandra and ScyllaDB: tunable consistency, LSM storage, tombstones | Quorum math drills: when R+W>N holds and when it breaks | S18.03 |
| N09 | T2 | 10 | Search engines as databases: Elasticsearch and OpenSearch mappings and analyzers | Index documents; tune relevance for 5 queries | S09 |
| N10 | T2 | 10 | Analytical databases: ClickHouse, BigQuery, Snowflake, DuckDB | Log analytics in DuckDB or ClickHouse | S10.07 |
| N11 | T3 | 11 | Graph databases and time-series databases | 2-hop query in Neo4j or with recursive SQL | S04.04 |
| N12 | T2 | 4 | Data modeling for AI apps: conversations, messages, tool calls, traces, feedback, embeddings | Schema for a chat product with audit and eval hooks | + |
| N13 | T2 | 8 | Operating databases: backups, point-in-time recovery, replication setups, pooling, upgrades | Point-in-time restore to a chosen timestamp | S14.07 |
| N14 | T2 | 9 | Scaling Postgres: read replicas, partitioning, sharding extensions, when to leave | Partition a 10M-row table by time; compare query plans | S03.10 |
| N15 | T2 | 9 | Schema migrations and data backfills at scale | Online backfill in batches with a progress table | S14.05 |

## O. Frontend engineering

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| O01 | T2 | 12 | Web fundamentals: HTML semantics, CSS layout (flex, grid), the DOM, events, fetch | Responsive static page with no framework | + |
| O02 | T2 | 12 | Modern JavaScript for UI: modules, promises, async iteration, streams | Fetch wrapper with a streaming reader and abort | + |
| O03 | T2 | 8 | React core: components, state, effects, the rendering model, keys, memoization | Todo app plus a render-count profiler | + |
| O04 | T1 | 8 | Streaming chat UI: token rendering, markdown, abort, retries, optimistic updates | Chat UI against your SSE backend with a stop button | + |
| O05 | T2 | 12 | Next.js: routing, server components, SSR, SSG, server actions, edge | Chat app with a server route that proxies the LLM | + |
| O06 | T2 | 12 | State and data fetching: query caches, stores, forms, validation | Paginated history with a cache and optimistic delete | + |
| O07 | T2 | 12 | AI UX patterns: citations, confidence, feedback capture, human review, tool-activity display, generative UI | Citation hover cards and thumbs feedback wired to the backend | + |
| O08 | T3 | 12 | Styling systems: Tailwind, component libraries, design tokens, dark mode | Restyle the chat with Tailwind and a token file | + |
| O09 | T3 | 12 | Performance and accessibility: Core Web Vitals, bundle size, ARIA, keyboard use | Take a Lighthouse report from red to green | + |
| O10 | T3 | 12 | Frontend testing: component tests and Playwright end to end | Playwright test for the chat happy path | + |
| O11 | T2 | 12 | Rapid demos: Streamlit and Gradio for prototypes and customer demos | Eval viewer in Streamlit in 60 lines | + |
| O12 | T3 | 12 | Auth flows in the browser: OAuth redirect, sessions, token storage | Login with OAuth against a mock provider | + |
| O13 | T3 | 12 | Data visualization for AI dashboards: latency, cost and eval trends | Latency percentile chart built from logs | + |

## P. Data engineering

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| P01 | T2 | 9 | Pipelines: ETL vs ELT, batch vs streaming, idempotent jobs, backfills | Idempotent daily job that is safe to rerun | R5 |
| P02 | T2 | 9 | Orchestration: Airflow, Prefect, Dagster; DAGs, retries, sensors | 3-task DAG with a retry and an alert | R5,S08.07 |
| P03 | T3 | 12 | Spark and distributed dataframes; when DuckDB or Polars is enough | Same aggregation in Polars and PySpark | R5 |
| P04 | T2 | 10 | Warehouse modeling and dbt: staging, marts, tests | dbt project with 2 models and tests on DuckDB | R5 |
| P05 | T2 | 10 | Lakehouse and table formats: Iceberg, Delta; change data capture | Time-travel query on a Delta or Iceberg table | + |
| P06 | T2 | 9 | Data quality: validation, expectations, anomaly checks, schema evolution, data contracts | Validation gate that fails a bad batch | R5 (5B) |
| P07 | T2 | 9 | Data versioning and lineage: DVC, lakeFS, OpenLineage | Version a dataset; reproduce an old training set | R5 |
| P08 | T2 | 9 | Feature stores and training-serving skew; point-in-time correctness | Point-in-time join; show the leak without it | R5 |
| P09 | T2 | 9 | Labeling and annotation: guidelines, tools, weak supervision, active learning | Label 100 items with an LLM pre-label and human review | R5 |
| P10 | T2 | 9 | Datasets for LLMs: dedup, near-duplicate detection (MinHash), PII scrubbing, tokenized shards | MinHash dedup on 10k documents | R5 |
| P11 | T2 | 11 | Data governance: catalogs, access control, retention, deletion requests | Deletion-request pipeline with proof of erasure (toy) | R13,S14.09 |
| P12 | T3 | 12 | Streaming data platform end to end: log, stream processor, sink | Clickstream to aggregates with an idempotent sink (toy) | R5 (5A) |

## Q. Cloud: AWS, GCP, Azure

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| Q01 | T1 | 3 | Cloud fundamentals: regions, availability zones, shared responsibility, pricing models | Draw the same 3-tier app on AWS and on GCP | R8 |
| Q02 | T1 | 3 | AWS IAM: users, roles, policies, STS, least privilege | Role with scoped S3 access; prove it is denied outside its scope | + |
| Q03 | T1 | 3 | AWS networking: VPC, subnets, route tables, NAT, security groups, endpoints, peering, VPN | Private-subnet app reachable only through a load balancer | + |
| Q04 | T1 | 4 | EC2: instance families, AMIs, EBS, autoscaling groups, Spot, GPU instances | Launch, bake an AMI, autoscale on CPU | interview question |
| Q05 | T1 | 4 | S3: storage classes, consistency, versioning, lifecycle, multipart, presigned URLs, events | Presigned upload, a lifecycle rule, and an event to a function | interview question,S07.14 |
| Q06 | T2 | 4 | AWS data services: RDS, Aurora, DynamoDB, ElastiCache, OpenSearch | RDS Postgres with a read replica | + |
| Q07 | T2 | 5 | AWS compute choices: Lambda, ECS, Fargate, EKS, App Runner; cold starts | Same container on Lambda and Fargate; latency and cost | + |
| Q08 | T2 | 6 | AWS integration: SQS, SNS, EventBridge, Kinesis, Step Functions | S3 event to SQS to a worker | + |
| Q09 | T2 | 5 | AWS edge and delivery: Route 53, CloudFront, ALB and NLB, API Gateway, certificates | HTTPS endpoint with a custom domain behind a load balancer | + |
| Q10 | T2 | 6 | AWS operations: CloudWatch, CloudTrail, KMS, Secrets Manager | Alarm on p95 latency; rotate a secret | + |
| Q11 | T1 | 7 | Amazon Bedrock: models, invoke and converse APIs, guardrails, knowledge bases, agents, provisioned throughput | Bedrock call with a guardrail; compare to the direct API | + |
| Q12 | T2 | 7 | SageMaker: training jobs, endpoints (realtime, async, serverless), pipelines, model registry | Deploy a small model to an endpoint; autoscale it | + |
| Q13 | T2 | 7 | GPUs on AWS: instance types, capacity, Spot, placement, EKS with GPUs | Price table per GPU-hour and per million tokens | + |
| Q14 | T1 | 6 | GCP core: projects, IAM, service accounts, VPC, Compute Engine, Cloud Storage | Deploy the same app on Compute Engine with a service account | + |
| Q15 | T1 | 6 | Cloud Run and GKE: serverless containers vs managed Kubernetes | Cloud Run service with concurrency tuning | + |
| Q16 | T2 | 10 | GCP data: BigQuery, Pub/Sub, Cloud SQL, Spanner, Firestore, Dataflow | Pub/Sub to BigQuery pipeline | + |
| Q17 | T1 | 6 | Vertex AI: Model Garden, endpoints, pipelines, vector search, evaluation, agent tooling | Deploy an open model on Vertex; call it | + |
| Q18 | T2 | 7 | GPUs and TPUs on GCP; GKE GPU node pools | GKE GPU pool running one inference pod (or the full plan) | + |
| Q19 | T2 | 6 | Infrastructure as code: Terraform providers, state, modules, plans, drift; Pulumi contrast | Terraform a VPC, a VM and a bucket; destroy cleanly | + |
| Q20 | T3 | 11 | Azure essentials: Entra ID, AKS, Blob, Azure OpenAI and Foundry | Map your AWS services to Azure equivalents; do one deployment | + |
| Q21 | T1 | 7 | Cloud cost management: budgets, tagging, rightsizing, commitments, egress | Cost report by tag; find 3 savings | + |
| Q22 | T2 | 11 | Well-architected reviews: reliability, security, cost, performance, operations | Review your own deployment against the pillars | + |
| Q23 | T2 | 11 | Hybrid, on-prem and air-gapped deployment; private networking to model APIs | Offline install plan: images, model weights, licenses | + |
| Q24 | T2 | 11 | Multi-cloud and portability tradeoffs; data gravity | Portability scorecard for your stack | + |
| Q25 | T1 | 8 | Deploy an LLM app end to end on AWS and on GCP | Same RAG app live on both, created by infrastructure as code | + |
| Q26 | T3 | 11 | Serverless GPU and inference clouds: what they offer and when to use them | Deploy to one; note cold start and cost | + |

## R. DevOps, platform, MLOps, LLMOps

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| R01 | T1 | 2 | Networking for engineers: TCP, UDP, DNS, TLS, HTTP/2 and HTTP/3, proxies, NAT | Trace one request with dig, curl -v and tcpdump | S02.04 |
| R02 | T2 | 4 | Linux internals: processes, signals, file descriptors, cgroups, namespaces, systemd | Build a container by hand with namespaces and cgroups | + |
| R03 | T1 | 4 | Docker: images, layers, build cache, multi-stage builds, networking, volumes | Shrink an image from 2 GB to under 300 MB | I22.01 |
| R04 | T2 | 5 | GPU containers: NVIDIA runtime, CUDA base images, model weights in images vs volumes | Containerize the inference server with cached weights | R8,I22.02 |
| R05 | T1 | 5 | CI/CD: pipelines, tests, build, release, environments | Pipeline: lint, test, build, push, deploy | + |
| R06 | T2 | 5 | Secrets and config management: vaults, env injection, rotation | No secret in git: scan, fix, rotate | + |
| R07 | T1 | 6 | Kubernetes core: pods, deployments, services, ingress, config maps, probes | Deploy the API on kind or minikube with probes | R8 |
| R08 | T1 | 6 | Kubernetes scaling and scheduling: requests, limits, HPA, node pools, taints, affinity | HPA under load; watch it scale out | R8 |
| R09 | T2 | 7 | GPUs on Kubernetes: device plugin, GPU operator, time-slicing, MIG, node autoscaling | GPU pod spec with resource limits (or a dry run) | R8 (8A),I23.07 |
| R10 | T2 | 10 | Kubernetes packaging and state: Helm, Kustomize, StatefulSets, volumes, operators | Helm chart for your service | R8 |
| R11 | T2 | 10 | GitOps and progressive delivery: Argo CD, canary rollouts with automatic rollback | Canary rollout that rolls back on an error-rate alarm | + |
| R12 | T1 | 7 | Observability: metrics, logs, traces; Prometheus, Grafana, OpenTelemetry | Instrument the API; build a rate, errors, duration dashboard | R12,S14.01 |
| R13 | T1 | 7 | LLM observability: traces, token and cost tracking, prompt and response logging, PII; Langfuse, LangSmith, Phoenix | Trace the RAG app end to end with token and cost per span | R12 (12B) |
| R14 | T2 | 8 | Alerting and on-call: SLO alerts, burn rates, runbooks | Burn-rate alert plus a runbook | S14.02 |
| R15 | T2 | 8 | Incident response and postmortems; an incident library for AI systems | Blameless postmortem for a simulated outage | S14.03 |
| R16 | T2 | 9 | MLOps: model registry, lineage, packaging, promotion; MLflow | Register, stage and promote a model | R12 |
| R17 | T1 | 7 | LLMOps release management: prompt and model versioning, eval-gated deploys, rollback | Release pipeline gated on the eval suite | R12 (12A) |
| R18 | T2 | 8 | Deployment strategies for models: shadow, canary, A/B, blue-green | Shadow a new model; diff its outputs | R12,I22.06 |
| R19 | T2 | 8 | Monitoring quality in production: drift, hallucination rate, user signals, retraining triggers | Daily quality report from sampled traces | R12 (12B) |
| R20 | T2 | 7 | LLM gateways and proxies: keys, budgets, fallbacks (LiteLLM and similar) | Gateway with budgets and a fallback chain | R9 |
| R21 | T3 | 11 | Platform engineering: golden paths, internal developer platforms, templates | Service template repo with CI baked in | + |
| R22 | T2 | 11 | Performance and chaos testing in pipelines | Chaos test: kill a pod under load; verify the SLO holds | I24.07 |
| R23 | T3 | 11 | Service mesh and zero-trust networking: mTLS basics | mTLS between two services | + |
| R24 | T2 | 8 | Cost monitoring and attribution for AI workloads | Per-feature cost dashboard | + |
| R25 | T2 | 2 | Operating system essentials: virtual memory, page cache, mmap, context switches, epoll, zero-copy | Read a large file three ways (read, mmap, cold vs warm page cache); time each | + |

## S. Security, privacy, safety, governance

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| S01 | T1 | 4 | Prompt injection: direct, indirect, tool-borne; why it is unsolved | Attack your own RAG bot through a poisoned document | R13 (13B) |
| S02 | T1 | 4 | Defenses in depth: privilege separation, input isolation, output filtering, allow-lists, human approval | Add 3 layers; rerun the attacks; write the residual-risk note | R13 |
| S03 | T1 | 5 | OWASP Top 10 for LLM applications, each with an example | Map each risk to your app; fix the top 3 | R13 |
| S04 | T1 | 8 | Jailbreaks and misuse: patterns, classifiers, policy enforcement | 20-prompt jailbreak suite; refusal and false-refusal rates | R13 |
| S05 | T1 | 5 | PII and sensitive data: detection (regex, NER, LLM), redaction, tokenization, reversible masking | PII gateway; measure precision and recall on a labeled set | R13 (13A) |
| S06 | T2 | 8 | Data leakage paths: logs, caches, training data, embeddings, memory; retention | Leak audit of your app; close 3 paths | R13 |
| S07 | T2 | 8 | Excessive agency and tool abuse: least privilege, scoped credentials, sandboxing | Scoped token per tool; block an escalation attempt | R13 |
| S08 | T2 | 11 | Threat modeling for AI systems: STRIDE, attack trees, trust boundaries | Threat model for the RAG app with a data-flow diagram | + |
| S09 | T2 | 11 | Supply chain: model files (pickle), datasets, dependencies, signing, SBOM | Show a malicious pickle in a sandbox; switch to safetensors; pin dependencies | I24.08 |
| S10 | T2 | 11 | Application security essentials: authn, authz (RBAC, ABAC), secrets, encryption in transit and at rest, audit logs | Audit log with tamper evidence (hash chain) | S14.10 |
| S11 | T2 | 8 | Red-teaming practice: methodology, automated attackers, reporting | Attacker LLM vs your bot; write the findings report | R13 (13B) |
| S12 | T2 | 8 | Guardrail systems: guard models, policy frameworks, provider moderation, custom classifiers | Guard model in front of the app; latency and catch rate | R13 |
| S13 | T2 | 11 | Privacy technology: differential privacy, federated learning, confidential computing | DP-SGD on a toy model; privacy vs accuracy curve | + |
| S14 | T2 | 11 | Machine unlearning and the right to erasure in AI systems | Erase one user from the index, caches and logs; write the verification test | your startup |
| S15 | T2 | 11 | Attacks on models: membership inference, extraction, poisoning, adversarial examples, backdoors | Membership inference against an overfit model | + |
| S16 | T1 | 8 | Regulation: GDPR, DPDPA, HIPAA, CCPA; lawful basis, DPIA, DPA, data residency | One-page DPIA for an AI feature | S14.09 |
| S17 | T2 | 11 | AI governance: EU AI Act risk tiers, NIST AI RMF, ISO 42001, model cards, audits | Model card and risk register for your app | R13 |
| S18 | T2 | 11 | Compliance programs: SOC 2, ISO 27001, vendor reviews, security questionnaires | Answer a 20-question security questionnaire | + |
| S19 | T2 | 11 | Responsible AI: bias and fairness metrics, transparency, provenance, watermarking | Fairness audit of a classifier on 2 metrics | + |
| S20 | T3 | 11 | AI safety and alignment basics: misuse vs misalignment, safety evals, oversight | One-page brief comparing published lab safety frameworks | + |
| S21 | T2 | 11 | Safety for high-stakes domains: escalation, disclaimers, scope limits | Scope guard that routes emergencies to a human | R11 (11A) |

## T. Domain and applied AI

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| T01 | T2 | 11 | Healthcare data standards: HL7 v2, FHIR resources, terminologies (ICD, SNOMED, LOINC) | Read and write a FHIR Patient and Observation against a test server | + |
| T02 | T2 | 11 | Clinical workflows and where AI fits: scheduling, triage, documentation, prior authorization | Workflow map for a clinic with AI insertion points | your work |
| T03 | T2 | 11 | Healthcare compliance in practice: HIPAA safeguards, BAAs, PHI handling, audit, DPDPA for health data | PHI data-flow diagram with a control on every arrow | + |
| T04 | T2 | 11 | Clinical-grade RAG and guideline assistants: evidence grading, citations, abstention | Guideline QA with mandatory citations and refusal | R11 (11A) |
| T05 | T2 | 11 | Voice AI for clinics: call flows, ASR for accents and code-mixing, handoff, QA | Call-flow spec plus a word-error-rate test on accented audio | your work |
| T06 | T2 | 10 | Speech stack deep dive: VAD, diarization, streaming ASR, TTS, latency | VAD plus streaming ASR loop; measure the lag | R4 (4A) |
| T07 | T2 | 11 | Enterprise identity: SSO, SAML, OIDC, SCIM, role mapping | OIDC login against a test identity provider | + |
| T08 | T2 | 11 | Enterprise integration: CRMs, ERPs, ticketing, data connectors, webhooks | Sync tickets from a mock helpdesk API | + |
| T09 | T2 | 11 | Deploying inside the customer: VPC deployments, private links, customer-managed keys, security reviews | Deployment checklist for a customer VPC | interview research (FDE) |
| T10 | T3 | 12 | Edge AI and hardware-aware models: quantized SSMs, FPGA and accelerator basics | Latency and energy estimate for an SSM on edge hardware | your research |
| T11 | T3 | 12 | RL in products: bandits, recommendation, simulation environments | Epsilon-greedy vs UCB bandit simulation | your project (AdaptArena) |
| T12 | T3 | 12 | Search, ranking and recommendation systems in production | Two-stage retrieve and rank on a toy catalog | S16.05 |
| T13 | T2 | 11 | Compliance automation for AI: erasure requests, audit trails, policy engines | Policy-as-code check for data retention | your startup |
| T14 | T3 | 12 | AI for business analysis: requirements, process mining, report generation | Agent that turns a transcript into a requirements document | + |
| T15 | T3 | 12 | Education and assessment AI: adaptive practice, rubric grading | Rubric grader with a calibration set | R11 (11B) |

## U. Research and engineering craft

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| U01 | T1 | 1 | How to learn this curriculum: retrieval, spacing, interleaving, the topic package | Set up Anki, the tracker and the question log | F01,+ |
| U02 | T2 | 1 | Reading papers: the three-pass method, claims vs evidence, reproducing numbers | Three-pass read of the original transformer paper | I29.01 |
| U03 | T2 | 6 | Technical writing: design docs, ADRs, READMEs, benchmark reports | ADR for a real decision in one of your projects | + |
| U04 | T2 | 4 | Code quality: review habits, refactoring, naming, small pull requests | Review your own old code against a checklist | + |
| U05 | T2 | 5 | Benchmarking methodology: baselines, warm-up, variance, fair comparisons, reporting | Benchmark report template with error bars | I04.04,I17.01 |
| U06 | T2 | 10 | Reading large codebases: entry points, tracing, call graphs | Map one feature in an open-source repo | I27.01 |
| U07 | T3 | 12 | Open-source contribution: issues, pull-request etiquette, a first patch | One submitted pull request | + |
| U08 | T3 | 12 | Reproducing research: ablations, experiment logs, negative results | Reproduce one table from a paper | I29 |
| U09 | T2 | 3 | Experiment design for LLM systems: one variable at a time, logging, decision records | Experiment log for 5 RAG changes | + |
| U10 | T2 | 8 | Incident library: real outages and AI failures | 5 incident cards: cause, detection, fix, lesson | S18.05 |
| U11 | T3 | 12 | Publishing and portfolio: project READMEs, demos, write-ups, talks | Publish one write-up of a kata series | + |
| U12 | T2 | 12 | Estimating and planning engineering work: scoping, milestones, risk | Plan a 2-week build with risks and cut lines | + |
| U13 | T2 | 2 | Working with AI coding agents: specs, context files, review, verification loops | Build one kata with an agent under a written spec and a test gate; log every correction you made | + |


# Pillar 3: Business and people

## V. Business and product

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| V01 | T1 | 1 | Engineer voice vs business voice: mechanism, numbers, failure modes, tradeoffs | Rewrite 5 business-style answers as engineer answers | interview feedback |
| V02 | T1 | 3 | Unit economics for AI products: gross margin, inference cost per user, pricing floors | Margin model for a chatbot at 3 price points | + |
| V03 | T2 | 9 | Pricing AI: usage, seat, outcome, hybrid; value metrics | Pricing page draft with the reasoning behind it | + |
| V04 | T1 | 5 | Build vs buy vs fine-tune vs partner; vendor evaluation | Decision memo with total cost of ownership | + |
| V05 | T1 | 5 | ROI and business cases for AI projects; baselines and measurement | ROI model for automating a support queue | + |
| V06 | T2 | 6 | Product sense: users, jobs to be done, problem framing, MVP | One-page PRD for an AI feature | + |
| V07 | T2 | 9 | Product metrics: north star, input metrics, guardrails, funnels, cohorts, retention | Metric tree for an AI assistant | + |
| V08 | T2 | 7 | AI product failure modes: the demo-to-production gap, trust, latency, adoption | Pre-mortem for your own product | + |
| V09 | T1 | 6 | FDE craft 1: discovery, decomposing a vague ask, scoping, success criteria | Decompose 3 vague customer asks in 20 minutes each | interview research (FDE) |
| V10 | T1 | 8 | FDE craft 2: pilots and proofs of concept, deployment, change management, handover | Proof-of-concept plan with exit criteria | interview research (FDE) |
| V11 | T2 | 8 | Sales engineering: discovery calls, demos that land, objection handling, the technical win | 10-minute demo script; record it | + |
| V12 | T2 | 9 | Enterprise sales cycle: champions, procurement, security review, legal | Stakeholder map for a hospital deal | + |
| V13 | T2 | 7 | Structured problem solving: issue trees, MECE, hypothesis-driven work | Issue tree for cutting support cost by 30% | + |
| V14 | T2 | 9 | Market sizing and competitive analysis | TAM, SAM, SOM for your startup; competitor grid | + |
| V15 | T2 | 10 | Finance literacy: P&L, cash flow, burn, runway, margins | Read a real P&L; build a 12-month runway model | + |
| V16 | T3 | 10 | Fundraising: stages, cap tables, dilution, term sheets, SAFEs | Dilution table across 3 rounds | CEO track |
| V17 | T3 | 10 | Contracts and commercial terms: MSA, SLA, DPA, IP, liability | Mark up a sample SLA for an AI API | + |
| V18 | T2 | 11 | Strategy: moats in AI, positioning, platform risk, sequencing | One-page strategy memo | CEO track |
| V19 | T2 | 11 | CTO craft: technology roadmap, architecture governance, tech debt, engineering culture | 12-month technology roadmap for your company | CTO track |
| V20 | T2 | 12 | Team building: hiring loops, leveling, onboarding, performance | Design a hiring loop for an AI engineer | CEO and CTO track |
| V21 | T3 | 12 | Operating cadence: OKRs, planning, budgets, vendor management, board updates | Quarterly OKRs plus a board update | CEO track |
| V22 | T2 | 9 | Go-to-market basics: ideal customer profile, channels, content, partnerships | ICP document and a 30-day go-to-market plan | + |
| V23 | T2 | 10 | Customer success and support for AI products | Escalation policy and a customer health score | + |
| V24 | T2 | 4 | Requirements and specs: user stories, acceptance criteria, non-functional requirements | Spec for one feature with latency, cost and safety requirements | interview research (BA) |

## W. People skills: negotiation, influence, speaking

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| W01 | T1 | 1 | Tactical empathy: labels, mirrors, calibrated questions | 3 recorded role-plays with Claude as the counterpart | + |
| W02 | T1 | 2 | Principled negotiation: interests, options, criteria, BATNA, ZOPA | Prep sheet for a real negotiation | + |
| W03 | T1 | 8 | Negotiating offers and contracts: anchoring, concessions, packages, timing | Salary negotiation role-play, 3 rounds | + |
| W04 | T1 | 3 | Structured communication: the pyramid principle, BLUF, SCQA | Rewrite 3 rambling updates as bottom-line-first | + |
| W05 | T1 | 4 | Influence: Cialdini's principles, ethical use, influence without authority | Persuasion plan for a real stakeholder | + |
| W06 | T1 | 5 | Customer discovery: question design, listening, avoiding leading questions | 5 discovery question sets; run one live call | + |
| W07 | T1 | 7 | Public speaking 1: structure, openings, signposting, closings | 5-minute technical talk, recorded | + |
| W08 | T2 | 9 | Public speaking 2: voice, pace, pauses, body language, slides | Re-record the talk with 3 deliberate changes | + |
| W09 | T1 | 6 | Explaining technical ideas: the audience ladder, analogies, whiteboard habits | Explain KV cache to an executive, a PM and an engineer | + |
| W10 | T2 | 9 | Handling Q&A and pushback: bridging, admitting limits, staying calm | Hostile Q&A drill with Claude | + |
| W11 | T2 | 10 | Storytelling: narrative arcs, case stories, numbers that land | 2-minute origin story and 2 project stories | + |
| W12 | T2 | 10 | Difficult conversations: disagreement, feedback, conflict | Role-play a hard feedback conversation | + |
| W13 | T2 | 11 | Stakeholder management and managing up | Stakeholder map and communication plan | + |
| W14 | T2 | 11 | Leadership: delegation, trust, decision making, running meetings | Decision memo with clear roles | + |
| W15 | T2 | 12 | Writing that gets read: emails, memos, one-pagers, proposals | One-pager for a real proposal | + |
| W16 | T3 | 12 | Facilitation and workshops: agendas, exercises, energy | Facilitation plan for a 60-minute session | + |
| W17 | T3 | 12 | Executive presence and cross-cultural communication | Record a 3-minute executive update; review it | + |
| W18 | T3 | 12 | Personal brand: writing online, talks, network | 4-week content plan built from your katas | + |
| W19 | T2 | 1 | Active listening and summarizing back | Listen to a 5-minute clip; summarize it in 3 bullets | + |

## X. Interview craft

| ID | Tier | Wk | Topic | Kata or drill | Source |
|---|---|---|---|---|---|
| X01 | T1 | 1 | Three-level answers: outcome, mechanism, internals and limits | Record 5 answers; grade each against the rubric | + |
| X02 | T1 | 1 | The question log: capture, model answer, retest schedule | Log your real interview questions with model answers | + |
| X03 | T1 | 2 | Thinking aloud, clarifying questions, and handling "I don't know" | 3 drills where Claude asks something you cannot answer | + |
| X04 | T1 | 2 | Coding round craft: restate, examples, brute force, optimize, test | 2 timed problems with narration | + |
| X05 | T1 | 3 | ML and LLM deep-dive rounds: defending choices, depth ladders | Depth ladder on your best project (5 levels of why) | + |
| X06 | T1 | 3 | Take-home craft: scoping, README, evals, a tradeoffs section | Take-home template repo | interview research |
| X07 | T1 | 6 | Live debugging rounds: reading traces, the hypothesis loop | Debug a looping agent from its logs in 20 minutes | interview research |
| X08 | T1 | 5 | System design round craft: pacing, diagrams, numbers, tradeoffs | Timed design with a self-score | + |
| X09 | T1 | 7 | FDE and customer-simulation rounds | Customer simulation with Claude as a skeptical buyer | interview research (FDE) |
| X10 | T1 | 4 | Behavioral rounds: story bank (STAR), ownership, conflict, failure | 8 stories written and recorded | + |
| X11 | T2 | 7 | Project deep-dive: narrative, architecture, numbers, what you would change | 10-minute walkthrough of your flagship project | + |
| X12 | T2 | 8 | Resume and portfolio narrative that shows engineering depth | Rewrite 5 bullets with mechanism and numbers | + |
| X13 | T1 | 8 | Full mock loop and retro | Full loop; retro into the question log | + |
| X14 | T2 | 12 | Offer stage: leveling, compensation structure, negotiation plan | Negotiation plan with your BATNA | + |
| X15 | T2 | 1 | Company and role research: reading a job description, mapping it to topics | Map 3 job descriptions to topic IDs; list the gaps | + |
| X16 | T2 | 9 | AI-assisted interviews and pairing with AI tools | Solve a task with an AI tool while narrating your judgment | + |
| X17 | T2 | 4 | Low-level design and machine-coding rounds: SOLID, class modeling, extensibility, tests | Machine-code a parking lot or a rate-limiter library in 60 minutes, with tests | + |

