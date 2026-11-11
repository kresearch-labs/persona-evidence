# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- #32511 (deferred fields wrong after nested prefetch back to parent) FIXED in django/db/models/fields/related_descriptors.py.
- Root cause: ReverseOneToOneDescriptor.get_prefetch_queryset and create_reverse_many_to_one_manager unconditionally overwrote the child->parent cache after evaluating the child queryset; when the child queryset had its own nested Prefetch back to the parent, the nested prefetch had already cached the correct (differently-deferred) instance, and the outer loop clobbered it with the parent instance from the outer queryset. Later lookups then saw is_fetched=True and skipped re-fetching, so e.g. .kind raised/wrongly deferred.
- Fix: guard both loops with `if not <field>.is_cached(rel_obj)`. Matches upstream commit f5233dce30 (which only covered the reverse-FK manager); the O2O guard is the additional half needed for the OneToOne variant.
- Verified: standalone repro (O2O + FK variants): 3 queries on iteration, 0 on .profile.user.kind, kind=ADMIN, inner instance has kind loaded/email deferred. Suites green: prefetch_related (105 OK), many_to_one+one_to_one+queries (497 OK), defer+defer_regress+many_to_many+generic_relations+m2m_through (195 OK).
