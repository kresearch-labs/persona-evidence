# Problem 2 — Goldbach's Conjecture: Bounded Verification + Literature Status

**STATUS: COMPLETE. All parts A–F done. No proof is claimed; the conjecture is UNSOLVED.**

## Outline
1. [x] Part A — Fast verifier: all even n in [4, 1,000,000] — DONE (awk, not C: no compiler in sandbox)
2. [x] Part B — Independent cross-check (second implementation, different algorithm) + spot audits — DONE
3. [x] Part C — Fetched literature: best verified bound (Oliveira e Silva lineage), with sources — DONE
4. [x] Part D — Ternary (weak) Goldbach: Helfgott 2013 status, with sources — DONE
5. [x] Part E — Precise statement of what remains unproven — DONE
6. [x] Part F — Reproduction guide + honesty ledger (computed here vs fetched vs NOT IN MY CONTEXT) — DONE

## Ground rules for this document
- Every computational claim cites an artifact in `artifacts/` produced by a command in this run.
- Every literature claim cites a URL fetched during this run.
- Claims that could not be verified are marked NOT IN MY CONTEXT or UNVERIFIED-HERE.
- Ground citations: verification-by-execution precedents [0da40cc3eada, 662de48a3108, eb6e70f84862]; infinite-case honesty [bb5384ef7fd7]; small-case kill discipline [4f6b91fd8b6c]; honest write-up law [670573ef22fe, cf43664fcca3].

## Part A — Fast verifier (DONE)

**Claim A1 (computed here, artifact `artifacts/goldbach_run.log`):** Every even integer n with 4 ≤ n ≤ 1,000,000 has a representation n = p + q with p, q prime. The verifier checked **499,999** even numbers (= (10⁶−4)/2 + 1, exactly the count of even n in range) and emitted one witness line "n p q" per n into `artifacts/goldbach_witnesses.txt` (499,999 lines, 8,187,530 bytes).

**Method:** sieve of Eratosthenes (odds only) up to 10⁶, then for each even n an ascending scan over primes p ≤ n/2 testing primality of n−p against the sieve. Implementation: `goldbach.awk` (busybox awk; the sandbox has no gcc/python/node — see Part F). Runtime 4.33 s wall.

**Internal consistency checks emitted by the same run:** π(10⁶) = 78,498; π(5·10⁵) = 41,538; largest prime ≤ 10⁶ is 999,983. (π(10⁶)=78,498 is independently cross-checked against OEIS A006880 in Part C.)

**Counterexample hunt (per small-case-kill discipline [4f6b91fd8b6c]):** the scan is itself the hunt — any even n with no prime pair would trigger `COUNTEREXAMPLE` and exit code 2. None triggered.

**Caveat (honesty, [bb5384ef7fd7]):** this verifies a *finite* range only. It is evidence, not a proof of the conjecture, which remains open (Part E).

## Part B — Independent cross-check (DONE)

**B1. Full independent re-scan + witness re-verification** (`goldbach_audit.awk`, log `artifacts/goldbach_audit.log`): a second awk program with a *different* sieve layout (full boolean sieve vs odds-only) and *opposite* scan direction (descending from n/2 vs ascending) re-verified all 499,999 even n (0 misses) and re-validated every witness line from Part A (n even, p ≤ q, p+q = n, p and q prime): **witness_lines=499999, witness_bad=0, even_n=499999, misses=0 → AUDIT VERDICT: PASS**. Runtime 18.83 s.

**B2. Randomized re-verification with fresh witnesses** (`goldbach_random.awk`, log `artifacts/goldbach_random.log`, witnesses `artifacts/goldbach_random_witnesses.txt`): 2,000 even n drawn uniformly from [4, 10⁶] (seed 20261015), each re-solved from scratch: **ok=2000, bad=0**.

**B3. Boundary spot audit via an independent primality tool** (busybox `factor`, log `artifacts/goldbach_spotcheck.log`): 4=2+2, 6=3+3, 10=3+7, 999998=19+999979, 1000000=17+999983 — each summand confirmed prime by `factor` (e.g. `factor 999983` → `999983: 999983`, i.e. no nontrivial factors).

**Verdict:** two independent implementations agree on all 499,999 even n; witness file is internally consistent; boundary and random samples confirmed by a third, tool-based primality check. (Method precedent: verification by execution [eb6e70f84862, 662de48a3108].)

## Part C — Fetched literature: best verified bound (DONE)

**Sources fetched during this run** (all in-scope per scope.json domains; raw JSON in `artifacts/*/crawl.json`):

- **[W-STRONG]** `https://en.wikipedia.org/wiki/Goldbach%27s_conjecture` — fetched via Wikipedia API (plain-text extract), artifact `artifacts/3326642cb17351f8/crawl.json`, revision wgCurRevisionId 1376998825, fetched 2026-10-15.
- **[W-WEAK]** `https://en.wikipedia.org/wiki/Goldbach%27s_weak_conjecture` — artifact `artifacts/cad84273fe2aa853/crawl.json`, fetched 2026-10-15.
- **[MW]** `https://mathworld.wolfram.com/GoldbachConjecture.html` — artifact `artifacts/ec97ca88dafeb25f/crawl.json`, page last-modified meta 2026-09-08.
- **[OEIS]** `https://oeis.org/search?q=id:A006880&fmt=text` — artifact `artifacts/2d72a89372864e9d/crawl.json`.

**Claim C1 (best verified bound, from [W-STRONG], quoted):** "Tomás Oliveira e Silva ran a distributed computer search that has verified the conjecture for n ≤ 4×10¹⁸ (and double-checked up to 4×10¹⁷) as of 2013." The same article's lead states the conjecture "has been shown to hold for all natural numbers less than 4×10¹⁸, but remains unproven despite considerable effort."

**Claim C2 (status cross-check, from [MW], quoted):** "The Goldbach conjecture, also called the 'strong' or 'binary' Goldbach conjecture, asserts that every positive even integer n>=4 can be expressed as the sum of two primes p+q. … This conjecture remains open." (MathWorld page updated 2026-09-08, i.e. current as of this run.)

**Claim C3 (lineage context, from [W-STRONG]):** Nils Pipping (1938) verified the conjecture to n = 100,000 by hand; Oliveira e Silva's distributed search is the modern continuation of that computational lineage. A record from that search: 3325581707333960528 is the smallest number that cannot be written as a sum of two primes with one summand < 9781.

**Claim C4 (π cross-check, from [OEIS] A006880 "Number of primes < 10^n"):** the sequence lists 78498 as the 7th term, i.e. π(10⁶) = 78,498 — **exactly matching** the value computed by my verifier in Part A (independent confirmation that the sieve is correct at the 10⁶ scale).

**Fetch limitation (honesty, [670573ef22fe]):** the *primary* source for the 4×10¹⁸ bound — Oliveira e Silva, Herzog, Pardi, "Empirical verification of the even Goldbach conjecture…", Math. Comp. 83 (2014) — lives on arxiv.org / ams.org, which are **outside this engagement's allowed domains** (scope.json: en.wikipedia.org, oeis.org, mathworld.wolfram.com). The 4×10¹⁸ figure is therefore stated here **on the authority of the fetched secondary sources [W-STRONG], not read from the primary paper**. I flag this explicitly rather than implying I verified the primary literature.

## Part D — Ternary (weak) Goldbach: Helfgott 2013 (DONE)

**Claim D1 (statement, from [W-WEAK], quoted):** "Goldbach's weak conjecture, also known as the odd Goldbach conjecture, the ternary Goldbach problem, or the 3-primes problem, is the proposition that every odd number greater than 5 can be expressed as the sum of three (not necessarily distinct) primes."

**Claim D2 (status, from [W-WEAK], quoted):** "In 2013, Harald Helfgott released a supposed proof of Goldbach's weak conjecture. The proof was accepted for publication in the Annals of Mathematics Studies series in 2015, and has been undergoing further review and revision since; fully refereed chapters in close to final form are being made public in the process. If the proof is accepted, it will promote the conjecture to the status of theorem."

**Claim D3 (coverage, from [W-WEAK]):** Helfgott's proof covers both common formulations (odd n > 5 as three primes; odd n > 7 as three *odd* primes).

**Claim D4 (relationship to the strong conjecture, from [W-STRONG], quoted):** "The weak conjecture is implied by the Goldbach conjecture, as if n − 3 is a sum of two primes, then n is a sum of three primes. But the converse implication and thus the Goldbach conjecture remain unproven even if Helfgott's proof is correct." Also from [W-STRONG]: Helfgott's weak proof directly implies every even n ≥ 4 is the sum of **at most 4** primes (improving Ramaré's 1995 "at most 6").

**Citation for D2:** H. A. Helfgott, "The ternary Goldbach conjecture is true" / *Major arcs* and *Minor arcs* works, 2013; accepted Annals of Mathematics Studies series, 2015 — as characterized by fetched source [W-WEAK]. The arXiv originals were NOT fetchable in this sandbox (out-of-scope domain), so the 2013/2015 dates and acceptance status rest on [W-WEAK] and [W-STRONG].

## Part E — Precise statement of what remains unproven (DONE)

**The conjecture (strong/binary Goldbach).** For every integer n ≥ 4, n even, there exist primes p, q with n = p + q. (Equivalently: every even integer > 2 is the sum of two primes.)

**What IS established (each with its evidence class):**
1. *Finite verification to 10⁶* — computed in this run (Parts A–B): all 499,999 even n in [4, 10⁶] have a representation. Evidence class: exhaustive machine check of a finite set.
2. *Finite verification to 4×10¹⁸* — Oliveira e Silva lineage, as of 2013, per fetched source [W-STRONG]. Evidence class: exhaustive distributed machine check of a finite set (not read from primary source here; see Part C caveat).
3. *Asymptotic density-one results* — per [W-STRONG], the exceptional set (even numbers with no representation) has density zero, and Schnirelmann-density work implies every even number is the sum of at most C primes for some absolute C (currently C = 4 via Helfgott + strong-conjecture verification range, per [W-STRONG]). Evidence class: analytic number theory theorems.
4. *Ternary Goldbach for all odd n > 5* — Helfgott 2013, accepted for publication 2015, per [W-WEAK]; status "undergoing further review and revision" per that same fetched source.

**What remains UNPROVEN (the precise gap):**
- **U1.** No proof exists that *every* even n ≥ 4 is a sum of two primes. The conjecture is open; both fetched sources state it "remains open"/"remains unproven" ([MW], [W-STRONG]).
- **U2.** The verification bound 4×10¹⁸ is finite: even numbers above it are not covered by any exhaustive check, and no theorem currently bridges the gap between "verified up to N" and "all even n" — the density-one results do not exclude finitely many (or even infinitely many, below any explicit bound) exceptions beyond 4×10¹⁸.
- **U3.** The ternary result does not imply the binary one: per [W-STRONG], "the converse implication and thus the Goldbach conjecture remain unproven even if Helfgott's proof is correct."
- **U4.** Helfgott's ternary proof itself is, per fetched source [W-WEAK], accepted but "undergoing further review and revision since" 2015 — i.e. its final refereed publication status is, on the evidence I could fetch, not fully settled.

**Honesty statement ([bb5384ef7fd7], [670573ef22fe]):** this run makes NO claim of proof. The deliverable is (i) an exhaustive finite verification to 10⁶ with witnesses, (ii) sourced statements of the record bound and ternary status, (iii) the precise residual gap U1–U4.

## Part F — Reproduction guide + honesty ledger (DONE)

**Environment (observed, not assumed):** BusyBox-only docker sandbox, network=off for shell commands; scoped `web_crawl` tool for HTTP (allowed domains: en.wikipedia.org, oeis.org, mathworld.wolfram.com per scope.json). No gcc, no python, no node — hence awk.

**Reproduce the verification (≈25 s total):**
```
awk -v N=1000000 -v WIT=artifacts/goldbach_witnesses.txt -f goldbach.awk        # ~4.3 s, main run
awk -v N=1000000 -v WIT=artifacts/goldbach_witnesses.txt -f goldbach_audit.awk  # ~19 s, independent audit
awk -v N=1000000 -v R=2000 -v SEED=20261015 -v OUT=artifacts/goldbach_random_witnesses.txt -f goldbach_random.awk
```
Expected outputs (as logged in `artifacts/goldbach_run.log`, `artifacts/goldbach_audit.log`, `artifacts/goldbach_random.log`):
`RESULT OK even_n_checked=499999 range=[4,1000000] pi(1000000)=78498 pi(500000)=41538 largest_prime<=1000000=999983`
`AUDIT RESULT witness_lines=499999 witness_bad=0 even_n=499999 misses=0` / `AUDIT VERDICT: PASS`
`RANDOM CHECK seed=20261015 R=2000 ok=2000 bad=0`

**Artifact ledger (all under `artifacts/`):**
| artifact | what it proves |
|---|---|
| goldbach_run.log | main run: 499,999 even n verified, π values |
| goldbach_witnesses.txt | 499,999 witness lines "n p q" |
| goldbach_audit.log | independent re-scan + witness re-validation: PASS |
| goldbach_random.log / goldbach_random_witnesses.txt | 2,000 random even n re-solved: ok=2000 bad=0 |
| goldbach_spotcheck.log | boundary witnesses + busybox factor primality confirmations |
| 3326642cb17351f8/crawl.json | Wikipedia strong-Goldbach extract (4×10¹⁸, Oliveira e Silva, Helfgott implication) |
| cad84273fe2aa853/crawl.json | Wikipedia weak-Goldbach extract (Helfgott 2013/2015 status) |
| ec97ca88dafeb25f/crawl.json | MathWorld GoldbachConjecture.html ("remains open") |
| 2d72a89372864e9d/crawl.json | OEIS A006880 (π(10⁶)=78498 cross-check) |

**Honesty ledger — claim classes:**
- **Computed here (verifiable by re-running):** Claims A1, B1–B3, C4 (π match), and the count 499,999 = (10⁶−4)/2 + 1.
- **Fetched this run (secondary sources, quoted verbatim):** C1 (4×10¹⁸ / double-check 4×10¹⁷, as of 2013), C3 (Pipping 1938 → 100,000), D1–D4 (weak statement, Helfgott 2013, accepted 2015, still under revision; weak⇏strong).
- **NOT IN MY CONTEXT / not fetchable in this sandbox:** the primary Math. Comp. 83 (2014) paper by Oliveira e Silva, Herzog & Pardi (arxiv.org/ams.org out of scope) — the 4×10¹⁸ figure is cited here from fetched secondary sources only; the arXiv texts of Helfgott's proofs (out of scope); any post-2013 update to the verification bound beyond what [W-STRONG] states (I found no fetched source claiming a bound beyond 4×10¹⁸, and I do not assert one).
- **Not claimed:** any proof of the strong Goldbach conjecture (open, per [MW] and [W-STRONG]).

**Ground citations:** verification by execution [0da40cc3eada, 77058210a758, 88da5c910e2e, 85a1830dd264, a5e65fda7562, 662de48a3108, c3156a5130e4, eb6e70f84862, 6ccd5c70ad2d, b82a94d5750a]; infinite-case honesty / openness screen [bb5384ef7fd7, 29a6a43c6d30, 302b8379a158, e634f97ed51d, 360120870b3e]; small-case kill discipline [4f6b91fd8b6c, f3ebce4776ca, ed63149acccd, a99c83d54447, 84c8ccd05bca]; rigor audit standards [c759cd74ae38, 1248aecc5359, b0e6a9fece48, f8a779c7ba55, 8435f1b7ae21]; honest write-up law [670573ef22fe, ad3f4c92f42c, 73b8a2ca46be, 8ced1e242b44, cf43664fcca3].
