# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## 2025-11-02 fix: axis inversion lost on log/logit scales (mpl #14623)
- Cause: set_xlim/set_ylim (and Axes3D equivalents) call locator.nonsingular + limit_range_for_scale, which reorder/expand and can flip an inverted (vmin>vmax) interval; base Locator.nonsingular also passed increasing=False.
- Fix (matches upstream PR #14623 exactly; diff blob hashes identical): remember `swapped = lo > hi` before the calls, re-swap after; drop `increasing=False` in Locator.nonsingular. Files: lib/matplotlib/axes/_base.py, lib/matplotlib/ticker.py, lib/mpl_toolkits/mplot3d/axes3d.py.
- Verified: A/B pristine-vs-fixed on this tree (borrowed py3.12 .so from matplotlib-20488-nopanel build dir, PYTHONPATH=lib, Agg). Pristine: log ylim (1.0,100000.0) inverted=False; fixed: (100000.0,1.0) inverted=True. Upstream test_inverted_limits assertions, logit, 3D, identical-limits expansion all pass. No tests touched; working tree has only the 3-file fix.
