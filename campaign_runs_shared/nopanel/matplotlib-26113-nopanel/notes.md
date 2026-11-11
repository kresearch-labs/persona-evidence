# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- 2026-10-31: TASK.md = SWE instance matplotlib__matplotlib-26113 (hexbin mincnt/C inconsistency, gh:12926). Fix applied: lib/matplotlib/axes/_axes.py:5017 `len(acc) > mincnt` -> `>=`. Byte-identical to upstream fcda8c8121 and to the dataset gold patch (subset_dataset.jsonl). Graded test: test_axes.py::test_hexbin_mincnt_behavior_upon_C_parameter[png] (added by test patch, not present at base).
- Verification done in live-test/scratch_26113_verify/{pre,post}_lib (workspace lib + 25775's built .so + generated _version.py + mpl_toolkits/__init__.py to shadow namespace merge). Pre-fix: C+mincnt=1 gives 1 hex vs 3 (bug); post-fix: 3==3 identical. Workspace diff = the one line only.
- Gotcha: campaign/.venv has zz-mpl20488-repo.pth pinning matplotlib to the 20488 checkout; mpl_toolkits is a namespace package merging foreign stale copies — filter sys.path and add an __init__.py when running from another checkout. Workspace itself is unbuilt (no .so, no _version.py); full in-place build blocked on pybind11 (not on machine, pypi.org out of scope).
