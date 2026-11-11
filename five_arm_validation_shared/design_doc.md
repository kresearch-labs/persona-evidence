# Five-Arm Validation — Frozen Results Summary (sanitized)

## Test
pblocks panel validation across 5 professional domains:
medical (30), legal (20), creative (20), finance (25), tutoring (30) — 125 cases per arm.

## Arms (final working versions only)
- arm5: Kimi full panel
- arm3: aura + panel (pass-4, right-sized dose)
- arm2: aura, no panel (control)
- arm1: reference agent (single-shot)
(experiments-engine arm and pass-1/3 intermediates excluded from finals)

## Scoring
Frozen rubrics + domain keys (results/domain-keys/); finance on outcome-based
key; creative verified numerically (word counts); tutoring 3-part rule
(diagnosis + expert-key + no factual error). Final method: RAW POINTS —
sum of 5 domain cells / 125.

## Results (raw points / 125)
- arm5: 107.1 = 85.7%
- arm3: 106.7 = 85.4%  (panel beats no-panel by +2.4)
- arm2: 103.8 = 83.0%
- arm1: 100.8 = 80.6%

## Integrity
- sealed arm-map preserved (results/arm-map.sealed.json)
- referee watchdog audit excerpt (72,966 judgment rows)
- arm1 tutoring debt (22 cases) closed 2026-11-06: single-shot runs,
  same endpoint/format, graded by frozen 3-part rule (grade-arm1-tutoring.json,
  signed sha256)
- finance re-graded outcome-based (consensus bias removed), all arms
- per-run records: runs/<domain>/<case>/<arm>/ (record.json + ANSWER.md +
  console) — universal-metrics/v1 schema, sealed codes, output hashes

## Verified laws (from the campaign)
1. DOSE: right-sized panel +11-14 points over stuffed (pass-1 71.8 -> 83-86)
2. FORMAT: simple vs complex-tight — a wash on fixed body
3. MODEL: capacity not binding (Kimi = model within 0.3)
4. FINANCE: conviction domain — decisive arms win
