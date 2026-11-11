# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- 2026-10-31: Task = upstream PR #26063 (text antialiasing param). Fix applied to lib/matplotlib/{text.py,text.pyi,backends/backend_agg.py,backends/backend_cairo.py}; matches upstream commit 18c7a4be95 exactly.
- The campaign venv imports matplotlib from the 20488 checkout via .pth (zz-mpl20488-repo.pth). To test THIS checkout: run pytest from the repo root (pytest inserts lib/ first), or PYTHONPATH=$PWD/lib for python -c.
- This checkout had no compiled extensions; built in-place with: PYTHONPATH=C:/Windows/Temp/pybindshim_mpl25775 .venv/bin/python setup.py build_ext --inplace (pybind11 shim copied from 25332-panel/_pybindshim; mplsetup.cfg with system_freetype/system_qhull = True).
- Pre-existing failures (NOT from the fix): 18 in test_text.py (image baselines vs freetype 2.13, test_parse_math*), 1 in test_agg.py (numpy.row_stack removed in numpy 2.x). Verified identical before/after via git stash.
