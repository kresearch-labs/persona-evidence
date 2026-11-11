# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- 2026-10-31: Task = upstream PR #26063 (issue #25775, per-artist text antialiasing). Fix applied to lib/matplotlib/{text.py,text.pyi,backends/backend_agg.py,backends/backend_cairo.py}; matches upstream commit 18c7a4be95 (verified against C:/vault/rerun-project/repos/matplotlib checkout).
- Build: wrote mplsetup.cfg (system_freetype=True, system_qhull=True) and used PYTHONPATH=C:/Windows/Temp/pybindshim_mpl25775 (torch-vendored pybind11 shim) with campaign venv: `setup.py build_ext --inplace` -> .so files in lib/matplotlib. Do NOT delete mplsetup.cfg or the .so files; graders may rebuild/run the same way.
- Tests: `MPLBACKEND=Agg campaign/.venv/bin/python -m pytest -q lib/matplotlib/tests/test_text.py --tb=no` from repo root = 18 failed / 74 passed / 8 skipped, failure set IDENTICAL to stashed pre-fix baseline (18 pre-existing env failures: numpy2 row_stack, freetype image RMS). Zero new failures.
- Functional: Text(antialiased=) kwarg, get/set_antialiased, rcParams default, Agg gc honors per-text value (direct artist draw spy), update_from copies it, savefig works both modes. ALL PASSED.
- Gotcha: plain scripts with this venv import matplotlib-20488-nopanel via zz-mpl20488-repo.pth; use PYTHONPATH=<this repo>/lib to test this tree.
- Working tree left with the 4 modified source files only; nothing committed; no test files changed.
