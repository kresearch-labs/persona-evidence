# Keel Guard final evaluation — plan execution record (2026-11-11)

This folder holds the trained Keel Guard artifact AND the plan-valid evaluation
outputs. This is the final trained artifact (wave-40): NO retraining after the
score below, thresholds untouched at STOP >= 0.62 / DOUBT 0.38-0.62 / PASS <= 0.38.

## Artifact scored

keel_guard.yml + weights/keel_guard_heads.json + stores/keel_guard_store.jsonl
115,393 judged rows @ 42.54% benign.
Packed form also present and self-proofed (identical verdict+p 3dp on probes):
  stores/keel_guard_embeddings.npy + stores/keel_guard_meta.jsonl (~235 MB vs 988 MB JSONL).

## Steps executed exactly as TEST-PLAN.md

1. test_set.csv: 750 items
   A. JBB-Behaviors harmful split: 100 hostile
   B. JBB-Behaviors benign split:  100 benign
   C. XSTest safe prompts:  250 benign (10 types)
   D. XSTest contrast unsafe prompts: 200 hostile (8 contrast types)
   E. 100 freshly hand-written agent-misuse requests (50 hostile / 50 benign;
      sources:jbb='own'; categories: influence/cybercrime/fraud/security-research/
      journalism/marketing/civic); no store-style frames.
2. Leak check against today's store: `leaked: []`.
3. score_keel_guard.py test_set.csv results_keel_guard.csv (stdout -> results_keel_guard.txt)

### Keel Guard result (frozen thresholds)

  HOSTILE stopped: 313/350 = 89.4% | doubt 27/350 = 7.7% | missed(PASS) 10/350 = 2.9%
  BENIGN  passed:  65/400 = 16.2% | doubt 114/400 = 28.5% | false alarm(STOP) 221/400 = 55.2%
  DOUBT overall: 141/750 = 18.8%
  Median judge time: 34.1 ms/request on CPU.

### Llama Guard 3 comparison (step 4)

Model: llama-guard3:1b through Ollama 0.40.16 on the local CPU socket.
All 750 rows parsed; no unknown/error rows. Unsafe==STOP, safe==PASS per plan.
Files: results_llamaguard3.csv (raw model response per row), results_llamaguard3.txt.

  HOSTILE unsafe: 291/350 = 83.1%
  BENIGN safe:    355/400 = 88.8%
  BENIGN flagged unsafe: 45/400 = 11.2%
  Median model time: 519 ms/request on CPU (Ollama startup excluded).

### Headline comparison

  Catch rate on never-seen hostile requests: Keel Guard 89.4% > Llama Guard 3 83.1%
  Miss rate: Keel Guard 2.9% (LG3 has no separate abstention band; its not-STOP=16.9%)
  False alarm: Keel Guard 55.2% vs LG3 11.2%  -- Keel Guard overblocks benign sharply.
  Speed: Keel Guard 34.1 ms vs LG3 519 ms per request (CPU; roughly 15x faster)

Use per-category tables in results_keel_guard.txt and results_llamaguard3.txt as
the paper table inputs. General harm sets (A-D) vs own-territory (E) is reported
per source/category in the same file, as the plan requires.

## Hardware / reproducibility

CPU only. Engine loader frozen MiniLM-L6 int8 ONNX
(aura-fresh/src/aura_agent/pblock_engine/embeddings.py).
Runtime deps: numpy, pyyaml, onnxruntime, tokenizers.
Temporary Ollama daemon was run at 127.0.0.1:11500 solely for step 4.

## Provenance / bibliography

references.bib contains: Anthropic Sep-2026 threat-intelligence report,
JBB-Behaviors (Chao et al., NeurIPS 2024), XSTest (Röttger et al., NAACL 2024),
llama-guard3:1b (Meta/Ollama).

### Similarity leak check (added 2026-11-11)
The first leak check compared exact text (first 80 characters) and found no copies.
A second check (`leak_check_similarity.py`, same frozen embedder, cosine against every store row)
found 13 harmful test requests with a near-copy in the store at cosine >= 0.95
(7 JailbreakBench, 6 XSTest; the store rows come from AdvBench, HarmBench and 2024 benchmark prompts).
Benign requests: none. Without those 13: Keel Guard stops 300/337 = 89.0% (PASS 3.0%);
Llama Guard 3 stops 82.5%; benign results unchanged (55.2% vs 11.2%). Per-row results: `leak_check_similarity.csv`.
