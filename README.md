# Persona — evidence

Everything behind the numbers in the paper *Persona: A Growable Personality Layer That Turns Any Agent Into a Companion That Learns You*: raw run records, official grade reports, test sets, scorers, and the paper source.

- Engine: [kresearch-labs/Persona](https://github.com/kresearch-labs/Persona)
- Agent with Persona inside: [kresearch-labs/aura-agent](https://github.com/kresearch-labs/aura-agent)
- Trained pblocks (packed): linked from the Persona repository

Every run here was made on one consumer PC with a low-cost flash model through a public API, under the limits stated in the paper. Infrastructure retries and missing receipts are part of the record and are left as they happened.

## What is here

| Folder | Paper section | What it holds |
|---|---|---|
| `campaign_runs_shared/` | Results, Token Economics | The 1,000-run paired A/B on SWE-bench Verified (500 instances × panel / no-panel): 24 official harness reports, the manifest, per-run receipts, session tapes, patches, the incident log, and the frozen design document. `VERIFY.md` explains how to check every claim. |
| `five_arm_validation_shared/` | Personas for Any Task | The sealed five-field test (medical, legal, creative, finance, tutoring): sealed arm map, per-domain keys, grades, and the finance re-grade note. `SOURCES.md` gives case provenance. |
| `original8_shared/` | Persona in Action | The eight showcase runs (forecaster, mathematician, game build, detective, film, doctor, music, couple simulation), each with the pblocks it used. |
| `keel_guard_evaluation/` | The security persona | Keel Guard's 750-request test set, scorer, both result files, the Llama Guard 3 comparison, and the exact and similarity leak checks. |
| `paper/` | — | LaTeX source of the paper (ACL style). Upload the folder to Overleaf and compile `main_v2.tex` with pdfLaTeX. |

Heavy media from the showcase runs (game assets, film and music files, 336 files) are in `original8-release.zip`, attached to this repository's GitHub Release. Unzip it at the repository root and the files land in their original folders.

## Check the headline numbers

SWE-bench Verified, panel vs no-panel (needs only Python):

```bash
python recompute_swe_totals.py
```

It prints each wave and the totals: 445 vs 440.

Keel Guard needs the Aura agent installed (for the frozen embedder) and the packed Keel Guard pblock. Copy `keel_guard_evaluation/` into the pblock folder as `evaluation/`, then run from the pblock folder:

```bash
python evaluation/score_keel_guard.py evaluation/test_set.csv results.csv
```

It prints 89.4% of harmful requests stopped and 55.2% of benign requests wrongly stopped. Add `--rule agree` to use the stricter rule, which sends a request to DOUBT whenever the judgment head and the nearest cases disagree.

## Reproduce and extend

We ask for independent reproduction on proper evaluation infrastructure: rerun the paired SWE-bench A/B, rerun the five-field test with a significance test, keep training Keel Guard on new misuse cases and benign look-alikes, and grow pblocks in new domains. Results from others, whatever they show, will be linked from the Persona repository.

## License

Evidence records, documents and the paper source: CC BY 4.0. Scripts: MIT. Content from third parties keeps its own license: SWE-bench issues and code from their open-source projects, public benchmark prompts (JailbreakBench, XSTest), openly licensed PubMed Central case reports, public FBI Vault records, and web pages the agent read during its runs. See `LICENSE`.
