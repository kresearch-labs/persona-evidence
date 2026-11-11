# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Leads
- Bug #33975: `__in` RHS with annotate()+alias() keeps 10-col subselect. Trigger: `alias()` (add_annotation select=False) calls `set_annotation_mask(...)` which materializes `annotation_select_mask` from None -> {'book_annotate'}, so `has_select_fields` property (query.py:266) became True and `In.get_prep_lookup` (lookups.py:423) skipped the pk rewrite.
- Upstream fix = commit 32797e7fbf "Fixed #33975" (found via `git log -S has_select_fields`): make `has_select_fields` a class attr default False, set True only in `set_values()`; in `RelatedIn.get_prep_lookup` drop `clear_select_clause()` and use `set_values([target_field])` instead of `add_fields(..., True)`.
- HEAD 0c3981eb50 does NOT contain 32797e7fbf (merge-base check). Working-tree diff now byte-identical to upstream's django/ changes (same blob hashes).

## Decisions
- Fix = cherry-pick the django/ part of 32797e7fbf only (no test changes, per TASK.md). Applied to django/db/models/sql/query.py + django/db/models/fields/related_lookups.py.
- repro_bug.py at repo root is scratch (standalone sqlite repro); tests/ untouched.
