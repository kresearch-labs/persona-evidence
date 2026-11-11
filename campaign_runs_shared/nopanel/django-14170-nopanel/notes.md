# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Django iso_year fix (TASK.md, 31 Oct)
- Cause: `ExtractIsoYear.register_lookup(YearExact/Gt/Gte/Lt/Lte)` in django/db/models/functions/datetime.py registered the YearLookups under lookup_name 'year', so `start_date__iso_year=2020` resolved to YearExact and compiled a BETWEEN on calendar-year bounds — wrong for ISO years (e.g. 2019-12-30 has iso_year 2020).
- Fix: pass `lookup_name='iso_year'` to those five register_lookup calls (same as upstream PR #14157). 5-line diff, source only, no test changes, not committed.
- Verified: repro shows iso_year filters (explicit annotation + implicit lookup) use EXTRACT; `__year` keeps BETWEEN. runtests db_functions.datetime lookup queries: 550 tests, only 6 failures = the [iso_year] subtests of test_extract_year_{exact,greaterthan,lessthan}_lookup, which encode the old buggy BETWEEN behavior and are the tests upstream PR reverted. TASK.md forbids touching tests.
