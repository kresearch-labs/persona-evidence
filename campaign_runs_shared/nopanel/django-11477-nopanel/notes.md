# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Task 31 Oct: translate_url optional-groups bug (django #26431)
- HEAD e286711879 (2019-06-24) predates fix 76b993a117 (source) + d640c71fa3 (test fixtures).
- Cause: RegexPattern.match() in django/urls/resolvers.py returns match.groupdict() verbatim; optional named groups absent from the path come back as None values in kwargs. translate_url() then reverse()s with kwargs containing None -> wrong URL / NoReverseMatch.
- Fix (upstream, minimal): kwargs = {k: v for k, v in match.groupdict().items() if v is not None}
- Test fixtures (with-arguments pattern, regex_optional) are NOT in tree yet; grader applies test patch. Do not touch tests/.
