QUALITY ANALYSIS — ALL ARMS x ALL 5 DOMAINS (graded; pass-4 NOT included — pending completion)
=====================================================================================
Sources: 4-arm analyst grades (deleg_9e776f79, spot-verified), PASS3-ARM3-GRADE.json
(arm3 pass-3 re-grade of legal/creative/finance/tutoring), QUALITY-grades-matrix
(tutoring arm1/arm2/arm4), medical 4-arm + arm5 grades, arm5 Kimi sweep (graded medical 21.5).

MEDICAL (30 cases, diagnosis vs embedded ground truth)
  arm4  25.5/30 (85%)  28c/1p/1w   <- crown; source-anchoring signature
  arm3 pass-3 22.0/30  21c/2p/7i   first pass where panel beat no-panel
  arm5 (Kimi, full panel) 21.5/30   same decoys as model -> capacity not binding
  arm2  20.5/30 (68%)  19c/3p/8i
  arm3 pass-2 18.5/30
  arm1  17.5/30 (58%)  15c/5p/10i  elegant-but-wrong pattern

LEGAL (20, construction-law graded)
  arm4  19/19 answered, ALL correct (case-10 arm4 infra-fail) — controlling-authority anchoring
  arm2  ~17/20
  arm3 pass-3  14/20 (14 correct / 6 direction-wrong / 0 hard-wrong)
  arm3 pass-1 ~17/20
  arm1  14 correct, 2 partial, 4 wrong — pattern: right doctrine, losing side

CREATIVE (20, constraint compliance + craft + variety)
  arm4  20/20 compliant, strongest (~9.0/10) — observable price paid before every ending
  arm1  20/20 compliant (~8.6/10) — best comedy/voice; Prue->Dot continuity slip
  arm3 pass-3  19/20 (case-09 word-count artifact)
  arm2/3 pass-1  18/20 in-band
  arm5  pending grade (runs complete)

FINANCE (25, direction class vs historical outcome)
  arm2  ~19 yes, 0 wrong
  arm1  18 yes, 7 partial, 0 wrong — best capital preservation (all 6 blowups SELLed)
  arm4  16 yes, 5 partial, 0 wrong, 3 missing (infra) — highest-conviction BUYs all landed
  arm3 pass-3  11 right / 9 one-class-off / 5 wrong
  arm3 pass-1 ~13 yes, 2-3 wrong

TUTORING (30, exact GT misconception + expert-key explanation)
  arm2  30/30
  arm3 pass-3  30/30
  arm4  29/30 (case-26: SyntaxError vs TypeError slip)
  arm1  7/8 graded (22 answers never ingested — OWED: --ingest-reference 05-tutoring)
  arm5  pending grade

CROSS-DOMAIN VERDICT (pending pass-4)
  arm4 wins medical/legal/creative; arm2/arm1 competitive in finance/tutoring.
  arm4's only losses anywhere = infrastructure (AttributeError crashes), never reasoning.
  Panel beats no-panel only when dose is right (pass-3) and body is lean (arm4).
