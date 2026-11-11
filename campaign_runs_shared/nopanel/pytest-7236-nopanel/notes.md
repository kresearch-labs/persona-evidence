# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- pytest-7236: `--pdb` ran tearDown on skipped unittest tests. Root cause: `TestCaseFunction.runtest()` (src/_pytest/unittest.py:223) unconditionally postpones tearDown when `usepdb`; `TestCaseFunction.teardown()` then calls the saved `_explicit_tearDown()` even though unittest never ran setUp/tearDown for a skipped test.
- Fix (upstream shape): `_is_skipped(obj)` helper + `and not _is_skipped(self.obj)` on the usepdb branch; helper also used in `UnitTestCase.collect` and `_make_xunit_fixture`.
- Verified in C:/Windows/Temp/pytest7236final (project src + testing + tox.ini, `_version.py` stub, test patch from subset_dataset.jsonl) with C:/Windows/Temp/py4661env python3.9 (py 1.11, pluggy 1.6, iniconfig, vendored more_itertools, wcwidth): graded test_pdb_teardown_skipped 2/2 pass (fails on pristine baseline: 1 failed/1 passed), test_unittest.py 52 passed/9 skipped, PASS_TO_PASS 51/51.
- Env caveat: campaign/.venv has no pytest of its own; falls through to system pytest 7.4.4 which cannot import this repo's testing/conftest.py (`Testdir` gone) — `run_checks` fails identically on the pristine tree. Pre-existing, unrelated to the fix.
