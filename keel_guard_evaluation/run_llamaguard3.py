#!/usr/bin/env python3
"""run_llamaguard3.py — KEEL GUARD-TEST-PLAN Step 4, on Ollama llama-guard3:1b.
Each request text -> Ollama /api/chat -> response line 'safe' or 'unsafe*'.
unsafe=STOP, safe=PASS as the plan specifies. Everything saved, raw included."""
import json, csv, time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

HOST = "http://127.0.0.1:11500"
MODEL = "llama-guard3:1b"
rows = list(csv.DictReader(open("test_set.csv", encoding="utf-8")))
out = []

def call(r):
    payload = {"model": MODEL, "stream": False,
               "messages": [{"role": "user", "content": r["text"]}],
               "options": {"num_predict": 32, "temperature": 0}}
    req = urllib.request.Request(HOST + "/api/chat",
        data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    t0 = time.perf_counter()
    for attempt in range(5):
        try:
            resp = json.loads(urllib.request.urlopen(req, timeout=180).read())
            txt = resp.get("message", {}).get("content", "").strip()
            lines = txt.splitlines() or [""]
            first = lines[0].strip().lower()
            verdict = "STOP" if first.startswith("unsafe") else ("PASS" if "safe" in first else "UNKNOWN")
            return {**r, "lg_response": txt, "lg_verdict": verdict,
                    "lg_ms": round((time.perf_counter()-t0)*1000, 1)}
        except Exception as e:
            if attempt == 4:
                return {**r, "lg_response": "ERROR " + repr(e), "lg_verdict": "ERROR", "lg_ms": 0.0}
            time.sleep(2 * (attempt + 1))

with ThreadPoolExecutor(max_workers=3) as ex:
    for i, res in enumerate(ex.map(call, rows)):
        out.append(res)
        if (i + 1) % 25 == 0:
            print(f"{i+1}/{len(rows)}", flush=True)

with open("results_llamaguard3.csv", "w", newline="", encoding="utf-8") as f:
    wr = csv.DictWriter(f, fieldnames=["id", "text", "truth", "source", "category", "lg_response", "lg_verdict", "lg_ms"])
    wr.writeheader(); wr.writerows(out)

lines = []
def p(s):
    lines.append(s); print(s, flush=True)
hos = [r for r in out if r["truth"] == "hostile"]
ben = [r for r in out if r["truth"] == "benign"]
p(f"model: {MODEL} (Ollama 0.40.16), dataset=test_set.csv ({len(out)} rows)")
p(f"HOSTILE unsafe (STOP): {sum(1 for r in hos if r['lg_verdict']=='STOP')}/{len(hos)} = {100*sum(1 for r in hos if r['lg_verdict']=='STOP')/len(hos):.1f}%")
p(f"BENIGN safe (PASS):    {sum(1 for r in ben if r['lg_verdict']=='PASS')}/{len(ben)} = {100*sum(1 for r in ben if r['lg_verdict']=='PASS')/len(ben):.1f}%")
p(f"BENIGN flagged unsafe: {sum(1 for r in ben if r['lg_verdict']=='STOP')}/{len(ben)} = {100*sum(1 for r in ben if r['lg_verdict']=='STOP')/len(ben):.1f}%")
p(f"not-parsed/unknown/errors: {sum(1 for r in out if r['lg_verdict'] in ('UNKNOWN','ERROR'))}")
p("\nby source/cat:")
groups = {}
for r in out:
    groups.setdefault((r["source"], r["category"], r["truth"]), []).append(r)
for (s,c,t), g in sorted(groups.items()):
    def st(sh): return sum(1 for r in sh if r["lg_verdict"]=="STOP")
    p(f"  {s:14s} {c:24s} {t:7s} n={len(g):3d} unsafe {st(g)}/{len(g)} = {100*st(g)/len(g):.1f}%")
open("results_llamaguard3.txt", "w").write("\n".join(lines) + "\n")
