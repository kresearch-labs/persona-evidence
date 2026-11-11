# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## 20826 investigation (this session)
- HEAD a0d2e39972; regression commit v3.4.1..v3.4.2 touching axis.py = 93aabc1d19 (backport PR #20161 "Fix resetting grid visibility").
- 93aabc1d19 made Axis.clear() call _reset_major_tick_kw()/_reset_minor_tick_kw(), which .clear() the whole _major_tick_kw dict — wiping label1On/label2On etc. that Axes.__init__ set via tick_params() (shared axes hide inner labels that way). reset_ticks() then rebuilds ticks with label1On defaulting True -> extra labels/ticks after ax.clear().
- Upstream fix = PR #20826 (merge abf5f0435b, backport 4b5ea5ad8b): in clear(), instead of _reset_*_tick_kw(), only set _major/_minor_tick_kw['gridOn'] from rcParams, preserving other entries. Working tree had this exact change uncommitted (blob 887cf97ef1..7feca94bd9 matches); saved to C:/Windows/Temp/fix20826.patch and reverted to prove causality.
- Next: repro on HEAD (expect bug), re-apply patch, repro again (expect fixed), run test_axes.py.
- PROVEN: with fix in tree, repro -> 4/4 axes OK (FIXED/GOOD); pytest -k 'shared_axes_clear or reset_grid or shared' -> 20 passed. run_checks (pytest from campaign root) fails at collection because it imports the OTHER checkout (matplotlib-20826-panel) — rootdir/env artifact, not the fix; targeted pytest inside the repo passes.
- Final state: working tree has ONLY lib/matplotlib/axis.py modified (7+/2-), identical to upstream PR #20826 fix. No tests touched, nothing committed.
