#!/usr/bin/env python3
"""sources_ledger.py — citation ledger for research deliverables (stdlib only).

Fair-fight parity with the Runner run's sources.py workflow:
  add      — register a source (id, url, publication, date, type, notes)
  list     — print the ledger
  verify   — check a report: every [S#] citation id exists in the ledger,
             count cited sentences, report coverage (local checks only;
             the research sandbox has no direct shell network)
  render   — emit the annotated source list (markdown) from the ledger

Usage:
  python3 sources_ledger.py add S1 --url URL --pub NAME --date 1922-04-07 \
      --type CONTEMPORARY-NEWSPAPER --notes "..."
  python3 sources_ledger.py list
  python3 sources_ledger.py verify report.md --min-coverage 0.5
  python3 sources_ledger.py render > source_list.md
"""
import argparse, json, re, sys
from pathlib import Path

LEDGER = Path("sources_ledger.json")


def load():
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return []


def save(entries):
    LEDGER.write_text(json.dumps(entries, indent=1, ensure_ascii=False))


def cmd_add(a):
    entries = load()
    ids = {e["id"] for e in entries}
    if a.id in ids and not a.replace:
        sys.exit(f"error: {a.id} already exists (use --replace)")
    entries = [e for e in entries if e["id"] != a.id]
    entries.append({"id": a.id, "url": a.url or "", "publication": a.pub or "",
                    "date": a.date or "", "type": a.type or "",
                    "notes": a.notes or ""})
    save(entries)
    print(f"ledger: {len(entries)} sources (added {a.id})")


def cmd_list(_a):
    for e in load():
        print(f"[{e['id']}] {e.get('publication','')} {e.get('date','')} "
              f"({e.get('type','')})\n    {e.get('url','')}\n    {e.get('notes','')}")


def cmd_verify(a):
    entries = load()
    ids = {e["id"] for e in entries}
    text = Path(a.report).read_text(errors="ignore")
    # sentences = rough split; a "cited sentence" contains [S#]
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    cited = [s for s in sentences if re.search(r"\[S\d+\]", s)]
    used = set(re.findall(r"\[(S\d+)\]", text))
    missing = sorted(used - ids)
    unused = sorted(ids - used)
    cov = (len(cited) / len(sentences)) if sentences else 0.0
    print(f"sentences: {len(sentences)} | cited: {len(cited)} | "
          f"coverage: {cov:.2f} (min {a.min_coverage})")
    print(f"ledger ids: {len(ids)} | used: {len(used)}")
    if missing:
        print("INVALID CITATION IDS:", ", ".join(missing))
    if unused:
        print("ledger entries never cited:", ", ".join(unused))
    ok = (not missing) and cov >= a.min_coverage
    print("VERIFY:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


def cmd_render(_a):
    for e in load():
        print(f"- **[{e['id']}]** {e.get('publication','')} ({e.get('date','')}) "
              f"— {e.get('type','')}. {e.get('url','')}\n"
              + (f"  {e['notes']}\n" if e.get("notes") else ""))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    # bare invocation = list (scorecard probes run tools with no args)
    ap.set_defaults(fn=None)
    p = sub.add_parser("add"); p.add_argument("id")
    p.add_argument("--url"); p.add_argument("--pub"); p.add_argument("--date")
    p.add_argument("--type"); p.add_argument("--notes"); p.add_argument("--replace", action="store_true")
    p.set_defaults(fn=cmd_add)
    p = sub.add_parser("list"); p.set_defaults(fn=cmd_list)
    p = sub.add_parser("verify"); p.add_argument("report")
    p.add_argument("--min-coverage", type=float, default=0.5)
    p.set_defaults(fn=cmd_verify)
    p = sub.add_parser("render"); p.set_defaults(fn=cmd_render)
    a = ap.parse_args()
    if a.fn is None:
        a.fn = cmd_list
    a.fn(a)


if __name__ == "__main__":
    main()
