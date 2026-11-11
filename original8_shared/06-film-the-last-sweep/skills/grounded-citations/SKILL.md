---
name: grounded-citations
description: Use for every research/case-file task — citation ledger discipline, quote verification, provenance tiers, circular-source pitfalls.
---

# Grounded Citations — citation discipline for case investigations

Method only. This skill contains no case facts.

## The ledger is law
- Maintain a citation ledger from the FIRST source you read. Every source
  gets an id [S1], [S2], ... BEFORE you cite it. Register: url, publication,
  date, source type, and what claims it supports.
- Use the ledger tool in the working directory
  (`python3 sources_ledger.py add/list/verify/render`) — verify BEFORE
  shipping: every [S#] in the report must exist in the ledger, and coverage
  (cited sentences / total sentences) must be at least 0.5.

## Provenance tiers — label every claim
- CONTEMPORARY: newspaper/report from the event's own time (best).
- INQUEST-DOC / COURT-DOC: sworn testimony, official records.
- PRIMARY-TRACE: a source that quotes or reproduces an original document
  (name the document).
- SECONDARY: modern accounts, books, articles.
- RECALLED: from model knowledge, unverifiable in this session — flag it.
Never present a SECONDARY claim with CONTEMPORARY strength.

## Quote verification
- A direct quote must come from text you actually fetched this session.
  Anything else is marked unfetched/unverified. Never fabricate page numbers
  or article titles.

## Pitfalls
- Circular citation: site B cites site A, you cite both = ONE source, not two.
- Aggregator drift: numbers change between retellings; trace to the earliest.
- Single-origin claims: if one interested party created the claim, say so.
- Do not count website repetitions as independent corroboration.
- Absence of evidence ≠ evidence of absence — say which one you have.

## Accessibility honesty
- Log every failed fetch (paywall, bot wall, dead link, unscanned archive)
  in the source list. A claim that could not be checked is marked unverified
  with the reason.
