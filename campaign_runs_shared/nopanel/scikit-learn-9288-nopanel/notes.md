# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- Fixed KMeans n_jobs=1 vs n_jobs>1 inertia mismatch (issue #10865) in sklearn/cluster/k_means_.py: seeds for the n_init runs are now drawn once up front and used in BOTH the serial loop (random_state=seeds[it]) and the Parallel path, so both paths consume the RandomState identically. Diff: 6 insertions, 2 deletions, single file. No tests touched, nothing committed.

## Decisions
- Build/run environment for this old tree (py3.12, numpy 1.26.4): C:/Windows/Temp/sk12682-venv; np.float/np.int aliases restored via PYTHONPATH=C:/Windows/Temp/shim (sitecustomize kept OUTSIDE the repo so the diff stays minimal).
- Extensions built in place: liblinear.c regenerated with Cython 0.29.37 (3.0.8 rejects its BLAS noexcept pattern), _k_means.c with system Cython 3.0.8 (0.29.37 output hits py3.12 _PyCFrame.use_tracing). A failed first build had left a poisoned liblinear.c stub ("#error Do not use this file") that broke later rebuilds.
- Cluster suite: 123/123 test_k_means pass; 3 remaining failures (2 k_means_ doctests numpy-repr spacing, 1 feature_agglomeration setuptools DeprecationWarning) fail identically on the pristine tree -> environmental.
