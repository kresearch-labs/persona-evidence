# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Ticket 27200 c14 — makemigrations allow_migrate pairs (done 2026-11-02)
- Fix (working tree, 1 line): makemigrations.py consistency check now iterates
  `apps.get_app_config(app_label).get_models()` instead of `apps.get_models(app_label)`.
- Proven with .aura_harness/verify_7530.py (recording router, A/B pristine-vs-fixed):
  pristine = 27 calls / 21 invalid cross-app pairs; fixed = 6 calls / 0 invalid.
- Harness needs py3.12 compat shims (compat.py): django.utils.six.moves alias to real six,
  collections ABC aliases, gettext codeset/set_output_charset, ModelBase __classcell__.
- venv python: C:/Users/agent/work/projects/stack/campaign/.venv/bin/python
  (pytest cannot collect this 2016 checkout; runtests.py blocked by same six/classcell gaps).
