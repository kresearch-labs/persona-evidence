# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## 2026-10-30 TASK.md — reverse tz conversion in Trunc/Extract (ticket #32724)
- HEAD d89f976bdd (Apr 2021, post-3.2). Regression: 10d1261984 changed _get_timezone_name() to str(timezone); pytz/zoneinfo Etc/GMT-10 now yields 'Etc/GMT-10' instead of '+10'.
- Postgres _prepare_tzname_delta() flips +/- (correct only for bare offsets like '+10'), so 'Etc/GMT-10' -> query 'Etc/GMT+10' = opposite zone.
- Upstream fix for this exact ticket: cbba49971b (#32992, 3.2.7): _get_timezone_name -> timezone.tzname(None) or str(timezone). Verified empirically here: pytz/zi Etc/GMT-10 tzname(None)='+10'; zi named zones return None (fallback needed); dtz named keeps its name.
- Later #33279 (661316b066, 4.0) reworked backends with split_tzname_delta — NOT needed for this ticket; minimal fix = timezone.py only.
- Tests dir untouched per TASK.md. venv: campaign venv lacks asgiref/pytest; runner python3 has all deps + pytest 7.4.4 (runs checkout via cwd).
