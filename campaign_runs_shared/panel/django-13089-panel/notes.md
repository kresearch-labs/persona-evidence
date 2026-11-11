# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## 2026-11-01 — TASK.md: django #31728 _cull TypeError (done)
- Cause: `DatabaseCache._cull` did `cursor.fetchone()[0]` after `cache_key_culling_sql()`; when the culling query returns no row (e.g. CULL_FREQUENCY=1 → OFFSET == row count), fetchone() is None → TypeError 'NoneType' object is not subscriptable.
- Fix applied in django/core/cache/backends/db.py only (matches upstream f386454d13 exactly; blob acbe702255): guard `last_cache_key = cursor.fetchone(); if last_cache_key:` before DELETE.
- Verified: pre-fix repro crashed with the exact ticket error at db.py:272; post-fix repro passes; `tests/runtests.py cache --parallel=1` → 476 tests OK (115 skipped, memcached/redis absent). No tests touched, nothing committed.
