# Verification Guide — How to Independently Verify the SWE-bench Claims

This document describes how a third party can verify every claim in this
evidence package (`campaign_runs_shared/`) using only its contents plus
public resources.

## Claim 1 — Resolution scores (PANEL 445/500, NOPANEL 440/500)

**Files needed:** `grades/*.json` (24 official swebench harness reports)

**Method:** for each arm and wave, take the report with the highest
revision level (v2 > arb > base — reflecting the regrade/arbitration
protocol documented in design_doc.md), read `resolved_ids`, sum to 500.

**Reference tally (recomputable):**

| wave | panel | nopanel | notes |
|---|---|---|---|
| 1 | 44 | 45 | base |
| 2 | 45 | 39 | base |
| 3 | 46 | 47 | base |
| 4 | 43 | 42 | base |
| 5 | 48 | 47 | base |
| 6 | 43 | 42 | base |
| 7 | 43 | 43 | base |
| 8 | 43 | 43 | panel v2 (regraded after panel retry) |
| 9 | 44 | 45 | base + arbitration delta (panel +2, nopanel +1) |
| 10 | 46 | 47 | panel v2 (after the 5-failure retry: +sympy-19783) |
| **TOTAL** | **445** | **440** | delta +5 (1.0 pp) |

## Claim 2 — Manifest integrity

**Files needed:** `manifest.jsonl` + `grades/*.json`

Every one of the 1000 manifest rows' `resolved` flag is consistent with
the corresponding grade report's membership. Spot-check any wave:
compare `resolved` against `instance_id ∈ resolved_ids` — 50/50 must
agree per wave (validated: w2 50/50; full-sweep validated at freeze).

## Claim 3 — Per-run evidence

For each of the 1000 instance folders:
- `prediction.json` — the exact patch row fed to the grading harness
- `patch.diff` — the working-tree diff the agent produced
- `receipt.json` — model, tokens (prompt/completion), steps, tool_calls,
  status, timestamps (948 runs; 52 lightweight folders from lost wave-1
  workdirs are marked in the manifest `note` field)
- `events.jsonl` / `sessions_*.jsonl` — full interaction tape, including
  the panel ground block injected at run start (panel arm)
- `audit.jsonl` — tool-call audit trail

Verify: patches begin with `diff --git` (all non-empty patches do);
empty-patch instances are listed in `results/empty_patches.txt`.

## Claim 4 — Token economy

Receipts sum to Panel 615.3M / No-Panel 724.3M tokens. Per-call
`llm_usage` events sum higher (gross re-send billing; see design doc
"Token accounting note" and "Token Economy Analysis"). Both accountings
are internally consistent; the discrepancy is the receipts' final-state
vs events' per-call gross.

## Claim 5 — Statistical honesty

McNemar test on 500 paired outcomes: b=30 (panel-only wins), c=25
(nopanel-only), χ²=0.45, exact p=0.59 — NOT significant at p<0.05.
The +5 delta is directional evidence, not proof of superiority.
The design doc's panel-configuration section documents the ground-key
defect that explains the weak signal, plus the post-freeze fix.

## Full re-verification (requires public resources)

To re-execute rather than re-check grading:
1. Public dataset: princeton-nlp/SWE-bench_Verified (Hugging Face)
2. Public harness: github.com/SWE-bench/SWE-bench (docker images on
   Docker Hub under swebench/sweb.eval.*)
3. Feed any folder's `prediction.json` into the harness
   (`python -m swebench.harness.run_evaluation`) — resolved/unresolved
   must match the grade report here
4. Model reproduction requires a GLM-5.3-Flash-class endpoint; the
   session tapes document the exact prompts and tool flows.
