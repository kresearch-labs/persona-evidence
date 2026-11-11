# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- 2026-11-02 GH4019 (ds.merge(DataArray) -> AttributeError 'items'): fixed in xarray/core/dataset.py Dataset.merge — convert `other` via `other.to_dataset()` if DataArray, mirroring upstream's later fix (dataset.py:3850 in C:/Users/agent/xarray). Left uncommitted in working tree per TASK.md.
- Test env for this checkout: only numpy 2.5.4 exists on this machine (PyPI blocked); old xarray needs aliases restored. Run tests with: `cd <root> && PYTHONPATH=/tmp C:/Users/agent/work/projects/stack/campaign/.venv/bin/python -m pytest <tests> -q -p npshim` (C:/Windows/Temp/npshim.py restores np.unicode_/np.float/... aliases). Baseline test_merge.py: 10 failed, 11 passed — failures are pre-existing env noise (numpy2 read-only arrays break assert_all_writeable; pandas 3 vs old xarray), not merge bugs.
