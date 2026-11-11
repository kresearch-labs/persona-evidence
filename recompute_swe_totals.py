"""Recompute the SWE-bench Verified headline (panel 445/500, no-panel 440/500)
from the 24 official harness reports in campaign_runs_shared/grades/.

Rule (campaign_runs_shared/design_doc.md): per arm and wave, use the regrade (v2)
when one exists, add the wave-9 arbitration report, otherwise the base report.

    python recompute_swe_totals.py
"""
import glob
import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
reports = {}
for f in glob.glob(os.path.join(HERE, "campaign_runs_shared", "grades", "*.json")):
    m = re.search(r"wave(\d+)_(panel|nopanel)(?:_(v2|arb))?\.json$", f)
    if m:
        level = m.group(3) or "base"
        ids = set(json.load(open(f, encoding="utf-8")).get("resolved_ids", []))
        reports.setdefault((int(m.group(1)), m.group(2)), {})[level] = ids

total = Counter()
print("wave  panel  no-panel")
for w in range(1, 11):
    row = []
    for arm in ("panel", "nopanel"):
        r = reports[(w, arm)]
        ids = r.get("v2", r["base"]) | r.get("arb", set())
        total[arm] += len(ids)
        row.append(len(ids))
    print(f"{w:>4}  {row[0]:>5}  {row[1]:>8}")
print(f"total {total['panel']:>5}  {total['nopanel']:>8}   (paper: 445 vs 440)")
