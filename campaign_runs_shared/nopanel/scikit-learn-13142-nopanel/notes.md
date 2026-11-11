# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- 13142 (GaussianMixture): fit_predict != predict when n_init>1. Cause: in BaseMixture.fit_predict the final e-step ran BEFORE _set_parameters(best_params), so labels came from the last init, not the best. Fix: moved the final e-step after _set_parameters (matches upstream PR #13142). Tree can't be compiled here (needs numpy<2; PyPI out of scope) — verified by loading repo's base.py+gaussian_mixture.py over installed sklearn's support modules: original fails (labels differ), fixed passes (n_init 1/5, all cov types, warm_start).
