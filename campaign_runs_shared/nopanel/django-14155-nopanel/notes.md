# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- **#32572 fixed in `django/urls/resolvers.py`** (working tree, uncommitted). Root cause: `__repr__` used `self._func_path`, which for a `functools.partial` view renders as `functools.partial` (partials lack `__name__`). Fix = upstream commit 41850eec99 ("Fixed #32572 -- Improved ResolverMatch.__repr__()", Nick Pope): in `__repr__`, show `repr(self.func)` for partials and switch to `%r` formatting. NOTE: the ticket's `__init__`-unwrap idea was NOT implemented — upstream deliberately keeps `self.func` as the partial; unwrapping would break expected repr/kwargs. Nested partials need no handling (Python 3.5+ collapses them at construction; base commit 2f13c476ab is the direct parent of the fix commit).
- **Verification**: upstream post-fix tests (`test_repr` updated + `test_repr_functools_partial` new) run verbatim from C:/Windows/Temp/test_upstream_32572.py → OK. In-repo suite `urlpatterns_reverse` (102 tests): only `test_repr` fails — it still asserts the pre-fix format and is updated by the upstream test patch (not touched per task rules). Base (stashed) suite: OK.
