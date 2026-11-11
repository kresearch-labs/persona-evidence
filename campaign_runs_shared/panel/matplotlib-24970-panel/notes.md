# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- 2026-11-02: Fixed NumPy 1.24 uint8 deprecation/OverflowError in Colormap.__call__ (lib/matplotlib/colors.py ~717-728): `xa = xa.astype(int)` was inside the `dtype.kind == "f"` branch only; for integer input (e.g. uint8) the later `xa[xa > N-1] = self._i_over` (N+1=257) wrote out-of-bound ints into uint8. Fix = upstream 9229e5a2e9: move cast out of float branch, wrap in `np.errstate(invalid="ignore")` (NaN->int RuntimeWarning). Diff blobs match upstream (2d3072da04..ab0d73c4b5).
- Verification: issue repro (plt.get_cmap()(np.empty((0,), dtype=np.uint8)) etc.) passes with warnings-as-errors; test_colors.py 15F/237P, failure set byte-identical to unfixed baseline (pre-existing numpy-2.5-vs-3.6 env failures).

## Decisions
- Workspace had no compiled extensions (gitignored, never built); venv .pth binds matplotlib to sibling matplotlib-22865-panel. Copied sibling's 10 .so (gitignored artifacts) into lib/matplotlib and generated lib/matplotlib/_version.py from git describe (v3.6.0-1362-ga3011dfd1a) so this tree imports via PYTHONPATH. Did NOT touch the shared venv. Full source build would need `pip install pybind11` (user OK required).
