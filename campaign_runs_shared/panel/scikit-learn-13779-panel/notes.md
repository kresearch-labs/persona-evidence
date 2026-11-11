# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Decisions
- 13779 fix = one line in sklearn/ensemble/voting.py (skip None estimators in the sample_weight check). Blessed repo keeps ONLY this change.
- Local verification env: C:/Windows/Temp/sk13779 build copy; PYTHONPATH=C:/Windows/Temp/npsdist/numpy-1.26.4:C:/Windows/Temp/jl; C:/Python312/python.exe3 setup.py build_ext -i. Cython-3 compat patches (binary_tree.pxi, quad_tree.pyx, _tree.pyx, fast_dict.pyx, _build_utils, np-alias shim) live ONLY in the /tmp copy.
- Official spec (subset_dataset.jsonl): F2P = test_none_estimator_with_weights[X0-y0-voter0] and [X1-y1-voter1]; P2P = 1147 tests elsewhere.

## Findings
- Built sklearn 0.22.dev0 in C:/Windows/Temp/sk13779 (50 .so). test_voting.py: 20/20 pass incl. both F2P tests (official test patch applied). Repro (set one estimator to None, refit with sample_weight) works.
- No numpy.distutils anywhere (system numpy 1.26.4 Debian build + venv numpy 2.5.4 both lack it); pip blocked by proxy 403 on pypi.org. numpy 1.26.4 sdist found at C:/Windows/Temp/npsdist and built in place.
