# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings (task: AnnotationBbox gid)
- Bug: `AnnotationBbox.draw` (lib/matplotlib/offsetbox.py:1449) never calls renderer.open_group/close_group, so SVG backend drops the artist's gid. All sibling containers (legend.py:649, table.py:408, axis.py:298, figure.py:3068, collections.py:1873) do open_group(..., gid=self.get_gid()).
- Fix applied: open_group('annotationbbox', gid=self.get_gid()) after visibility check; close_group('annotationbbox') before stale=False. Only file changed: lib/matplotlib/offsetbox.py (git: M).
- Venv .pth points at matplotlib-22865-panel (different tree, same version string 3.6.0.dev2063+gc6c7ec1978.d20261102); task tree has no built .so; building needs pybind11 (NOT installed; user OK needed for pip install).
- A/B verified on /tmp copy of built 22865 tree: baseline -> 'My_label' NOT in svg; with identical 2-line patch -> <g id="My_label"> present.
- Existing test test_backend_svg.py::test_gid explicitly EXCLUDES OffsetBox instances from gid assertions (line 274) — no test changes needed/allowed.
- Cleanup done: removed borrowed .so/_version.py from task tree; git status shows only M lib/matplotlib/offsetbox.py + untracked meta files.
