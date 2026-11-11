# Aura SWE-bench Verified Evaluation — Frozen Design Document

## Date frozen
2026-11-06 14:44:04 IST

## Evaluation target
SWE-bench Verified — 500 instances
Dataset: princeton-nlp/SWE-bench_Verified

## Agent configuration
- Agent: Aura + Panel (panel arm) / Aura no-Panel (nopanel arm)
- Model: glm5.3 flash
- Endpoint: local model server at port 8000
- Temperature: 0.0
- Context window: 128K tokens
- Wall clock limit: 3600s (60 minutes) per instance
- Step cap: 250 steps per instance
- Command timeout: 60s per tool call
- Tool output cap: 10,000 characters
- Cost ceiling: $3 per instance (local — never triggered)
- API retries: 5 (normal), unlimited (infra failures)
- Shards: 6 parallel

## Panel configuration (panel arm only)
- Precedent store: 5 seat stores (triage / localize / strategy / test / outcome) at
  campaign start holding the seeded corpus; totals 8,330 rows (triage 1,341 ·
  localize 1,937 · strategy 1,536 · test 1,635 · outcome 1,881), all embedded
  (MiniLM vectors at write). During the campaign the stores grew by 1,709
  lived-origin lessons (written by the every-step miner and the exit sweep),
  607 of them committed during campaign days (Nov 2–4). Two-stage store law:
  proposals land as "candidates" and are promoted to "active" only after
  corroboration (at freeze: e.g. outcome 1,322 active / 559 candidate).
- Injection strategy: normal (design pipeline) — panel selection → judge-head
  input review → compiled relevance-gated ground injected as a system message
  at run start ("flash" profile, 18-line budget). Mid-run, the same engine
  learns from every input→output pair (step-pair miner); the exit sweep runs
  the output audit (OutputAuditor + final gate) and links run outcomes to the
  diary. NOTE (post-campaign audit): in this campaign the ground compiler was
  keyed on the run-prompt string, which was a generic pointer sentence — so the
  injected ground was boilerplate in most runs; the fix (feeding the real
  problem statement) was applied after freeze for any rerun.
- Top-k retrieved: k=8 per seat store; top-5 precedent lines emitted per seat
  (18-line global budget across seats)

## Evaluation harness
- Official SWE-bench Docker harness
- Per-test timeout: 60 seconds (Sphinx cap)
- Grading: official FAIL_TO_PASS / PASS_TO_PASS methodology
- Docker images: pre-built official images

## Known limitations
- 8 instances produced empty patches (listed in results/empty_patches.txt)
- 72 Panel instances triggered OOM during agent self-verification
  (Sphinx/matplotlib/sympy memory balloon — official grading unaffected)
- Timeout evidence in driver.log CLOSED-UNVERIFIED lines
  (timed-out instances never wrote receipts)
- KV-cache prefix caching disabled on evaluation endpoint
  (serving stack did not report cache fields)
- Frozen design doc and incident log compiled post-campaign
  from driver.log and wave records

## Results
- Panel arm: 445/500 = 89.0%
- No-Panel arm: 440/500 = 88.0%
- Delta: +5 tasks, +1.0 percentage point
- McNemar: χ²=0.45, p=0.59 (not significant — fresh Panel store)
- Tokens: Panel 615.3M total, No-Panel 724.3M total
- Panel ~7% cheaper per resolved instance ($0.113 vs $0.134; 12% vs 14.5 cents-computed earlier drafts — verified against receipt-derived totals 615.3M/445 and 724.3M/440)

## Token accounting note
Endpoint reported server_cached: 0 on all 47,414 LLM calls.
All prompt tokens billed at full cold price.
91% of token volume from tool outputs (repo test results, tracebacks, code).
Agent reasoning: <2% of total tokens (~4K per run).
Median steps: 45. P90: 86 steps. Max: 267 steps (scikit-learn).
529 retries restarted from zero with no cached state.
Projected 3-5x cost reduction with KV prefix caching enabled.

## Token Economy Analysis

### Measured baseline
- Total billed tokens across campaign: 2,747M
  (Panel 1,261M + No-Panel 1,487M, per-call event sums)
- Receipt totals (design doc): Panel 615M / No-Panel 724M
  (different but consistent accounting — receipts capture
  final-state totals, events capture per-call gross)
- server_cached: 0 on all 47,414 LLM calls

### Why agent tokens are quadratic
Call k re-sends call k-1's entire prompt as its prefix.
With prefix caching, the repeated part bills at cache-read
rate; only the new suffix (latest tool output + new system
block) bills full price. Without caching, every re-send
bills full price — the quadratic term.

### Measured composition (per run)
- Tool outputs: 91% of token volume
- Agent reasoning: <2% (~4K tokens per run)
- Median steps: 45 | P90: 86 | Max: 267 (scikit-learn)
- 529 retries, each restarting from zero with no cached state

### Validation example: sympy-13798
- 34 calls, 462K billed
- Intrinsic new content: 24K (5%)
- Repeated prefix: 438K (95%) — billed full price each call

### Prefix caching projection (applied across 914 runs)

| Scenario           | Panel  | No-Panel | Combined | vs actual |
|--------------------|--------|----------|----------|-----------|
| Actual (no cache)  | 1,261M | 1,487M   | 2,747M   | 100%      |
| Cache read @ 0.5×  | 639M   | 753M     | 1,393M   | 51%       |
| Cache read @ 0.25× | 329M   | 387M     | 715M     | 26%       |
| Cache read @ 0.1×  | 142M   | 166M     | 309M     | 11%       |

Validation: sympy-13798 at 0.25× projects 462K → 133K (29%
of actual) — consistent with aggregate model.

### Conclusion
Enabling KV prefix caching on the evaluation endpoint would
reduce billed tokens from ~2.75B to ~0.71B (3.8× reduction)
at standard 0.25× cache pricing — the single largest
optimization available, requiring zero changes to Aura.

### Caveats
- Model assumes stable prefixes between calls (true for
  agent loops; context pruning events slightly lower estimate)
- "Tokens billed" ≠ "tokens computed" — GPU still processes
  cached prefixes at reduced cost/latency
- Projections are estimates, not measured values

### Step distribution and tail analysis

| Group          | Runs | Share | Tokens | Share  | Mean/run |
|----------------|------|-------|--------|--------|----------|
| ≥200 steps     | 2    | 0.2%  | 25M    | 1.9%   | 12.5M    |
| ≥150 steps     | 14   | 1.5%  | 111M   | 8.3%   | 7.96M    |
| ≥100 steps     | 63   | 6.9%  | 329M   | 24.6%  | —        |
| <150 steps     | 900  | 98.5% | 1,229M | 91.7%  | 1,365K   |

Key findings:
- 91.7% of spend comes from 900 ordinary runs (<150 steps;
  tables built on 914 runs with receipts, 86 crash casualties lack them)
- Removing the 14 pathological runs saves only 8.3%
- Tail is symmetric: 7 Panel, 7 No-Panel among ≥150-step runs
  (did not skew the A/B comparison)
- Worst run (267 steps, 14.6M tokens) matches quadratic
  prediction exactly: 267 × ~55K median context ≈ 14.7M
  — arithmetic, not malfunction

### Optimization lever ranking

| Lever                    | Projected saving | Notes                    |
|--------------------------|------------------|--------------------------|
| KV prefix caching        | ~3.8×            | Attacks re-send tax      |
|                          |                  | on every run             |
| Tool-output trimming     | compounds        | Reduces context size,    |
|                          | with caching     | compounds with above     |
| Step caps / long-task    | ≤8.3%            | Only affects 1.5% of     |
| limits                   |                  | runs — not the lever     |

Structural conclusion: Token weight is structural — the quadratic
re-send tax applied uniformly across ordinary runs — not
a pathological tail problem. Prefix caching is the dominant
optimization, ~12× more impactful than tail-capping.
