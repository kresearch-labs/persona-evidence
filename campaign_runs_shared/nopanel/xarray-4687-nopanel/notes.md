# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- 2026-11-02: Fixed xr.where attrs bug (issue #4687) in xarray/core/computation.py — keep_attrs param added, byte-identical to upstream commit 84961e6a. Uncommitted in working tree, as TASK.md requires.

## Decisions
- Test env: C:/Windows/Temp/xr4687env (copy of campaign venv: numpy 2.5.4, pandas 3.1.0) + site-packages/xr_compat.py shim (restores np.NaN/unicode_/string_/float_/cumproduct, pd.Int64Index/iteritems, pandas.core.computation.ops.UndefinedVariableError). Run tests via C:/Windows/Temp/xr4687env/bin/xrpytest. The campaign venv alone cannot import this checkout (np.unicode_ removed in numpy 2).
- Pre-existing failures (NOT from the fix, proven vs pristine worktree of d3b6aa6d): test_computation.py 12 failed/148 passed; test_merge.py 5 failed/48 passed — all pandas-3.x API removals (e.g. Index.is_monotonic in groupby.py).
