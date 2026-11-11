# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- 2026-11-03 (sphinx-8721-nopanel): campaign venv cannot run this checkout's pytest suite as-is:
  (1) venv sphinxcontrib-* 2.0.0 require Sphinx>=5.0, checkout is 3.5.0+ -> VersionRequirementError on any build;
      workaround: patch `Sphinx.require_sphinx` in the test process only (sitecustomize), never in project files.
  (2) venv has no real pytest; `_pytest_repo_src.pth` injects work/pytest-7205-nopanel/src (pytest 5.4.1.dev), which
      HANGS (R state, GB-scale RSS) when rendering a failure report between sphinx-app tests on Python 3.12.
      Passing runs complete fine (control: test_errors.py 2 passed). Use --assert=plain + fresh --basetemp + timeout.
  (3) test_viewcode's viewcode-block assertion is stale for this venv's pygments (expects 2021-era `<span>    </span>`
      markup); current pygments emits plain indentation -> that one assertion fails independent of any source change.
- 2026-11-03 (sphinx-8721-nopanel): #8720 fix = guard in collect_pages (sphinx/ext/viewcode.py): skip singlehtml,
  skip epub* unless viewcode_enable_epub. A/B verified via C:/Windows/Temp/vc_manual.py (replica of test_viewcode + epub checks):
  pre-fix epub build emits _modules/, post-fix it does not; html output unchanged; enable_epub=True still works.
