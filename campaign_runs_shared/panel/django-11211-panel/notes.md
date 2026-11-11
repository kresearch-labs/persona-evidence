# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- TASK.md (GFK prefetch + UUID pk, Django #30343): root cause = GenericForeignKey.get_prefetch_queryset matched `pk.get_prep_value()` (raw str for UUIDField) against `obj.pk` (UUID) -> dict miss -> None. Fix: added `UUIDField.get_prep_value` (to_python cast), identical to upstream commit 1afbc96a75. File: django/db/models/fields/__init__.py (blob 2307dcae25..0d8612532d). Verified: repro_gfk_uuid.py passes; runtests prefetch_related contenttypes_tests generic_relations model_fields.test_uuid = 240 OK; model_fields basic queries = 678 OK. Repro script left at repro_gfk_uuid.py (untracked).
