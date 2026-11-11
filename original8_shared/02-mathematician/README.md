# Mathematician — what this folder shows, and what it doesn't

**In short:** the mathematician persona analysed eight open integer sequences from OEIS, and its claims were then checked by computation. It did **not** solve an open problem, and the paper does not claim it did.

## What is here

- `oeis-A131393-RESULT/mathematician_run1.json`, `mathematician_run2.json` — the persona's own analyses of eight OEIS sequences (two runs). They are working notes; the A131393 analysis ends mid-reasoning, without a conclusion.
- `oeis-A131393-RESULT/A131393_rule_reconstruction.json` — a follow-up computation on [A131393](https://oeis.org/A131393), a sequence whose generating program is lost and whose stated rule OEIS marks as flawed. Four simple reconstructions of the lost rule were simulated against the 72 known terms: all reproduce the first 27 terms, and all part from the sequence at a(28) = 42, where the sequence takes d = +15 rather than d = −12.
- `oeis-A131393-RESULT/MATH_DEEP_VERIFICATION.md` — the notes written during that check, kept as they were.
- `t2-Goldbach-DELIVERED/`, `P2-Goldbach-verification-code/`, `verify_goldbach.py` — a separate run: a computational Goldbach check over a finite range, with its verification code.
- `PBLOCKS_USED.md` — the pblocks the runs consulted.

## How to read the A131393 check

- OEIS itself already records that a(28) = 42 is "the first term that differs from A131388" (the same sequence under the simpler Rule 1). So the point where a simple reading of the rule breaks was **not** a new discovery; the computation **confirms** it independently, with four rule variants.
- Both OEIS conjectures for A131393 (that a(n) and its differences are permutations) remain **open**. Nothing here proves or disproves them.
- `MATH_DEEP_VERIFICATION.md` calls the result "new"; that note was written before the OEIS comment above was checked. The paper uses the corrected description: *a check of the analysis, not a solution of the open conjectures.*

## Verify it yourself

Take the 72 terms from OEIS (they are also in `A131393_rule_reconstruction.json`), compute d(n) = a(n+1) − a(n), and simulate any greedy "smallest unused |d|" rule from a(1) = 1: it matches through a(27) and gives 15, not 42, at a(28).
