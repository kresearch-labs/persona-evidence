# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## 2026-08-31 — ticket #33199 change_aliases fix session
- Shell cwd = C:/Users/agent/work/work/django-15128-panel (Django 4.1.dev checkout, ticket #33199 repro target).
- File tools root = same dir. /tmp writes refused; scratch files go in repo root (repro_33199_tmp.py, delete after).
- Test venv: C:/Users/agent/work/projects/stack/campaign/.venv/bin/python (imports THIS checkout, py3.12).
- Repro approach: use tests/runtests.py with settings module tests (INSTALLED_APPS includes 'queries' app models) — no manual app registry needed.
- Scratch repro file: repro_33199_tmp.py (settings.configure + apps.all_models registration attempt FAILED: reverse rels not resolved; runtests.py path is the way).
- Fix target: django/db/models/sql/query.py — table_alias() alias numbering collides with rhs aliases during combine(); change_aliases asserts keys∩values==∅.
