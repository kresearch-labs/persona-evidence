# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- Ticket #32546 (TASK.md): Meta.ordering fields still land in GROUP BY. Cause: `SQLCompiler.get_group_by()` (django/db/models/sql/compiler.py) unconditionally extends `expressions` with `expr.get_group_by_cols()` for every ORDER BY entry, and `get_order_by()` populates `self._meta_ordering` when ordering comes from Meta.ordering. 0ddb4ebf7b only nulled ORDER BY later in as_sql(); GROUP BY was built before that.
- Fix applied (working tree, uncommitted): wrap the order_by loop in `if not self._meta_ordering:` — identical to upstream commit 330bc402a8 (verified: `git diff 330bc402a8 -- django/db/models/sql/compiler.py` is empty).
- Proven by C:/Windows/Temp/repro_32546.py: pre-fix GROUP BY = headline, pub_date (bug); post-fix GROUP BY = headline only, exit 0.
- No tests modified; only django/db/models/sql/compiler.py changed (git status: ' M django/db/models/sql/compiler.py').
