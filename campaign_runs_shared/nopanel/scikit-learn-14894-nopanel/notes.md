# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Build environment (2026-11-02)
- venv for build/test: C:/Windows/Temp/sk12682-venv (numpy 1.26.4 w/ distutils, scipy, Cython 3.0.8, pytest)
- Cython 3.0.8 too new for sklearn 0.22: pre-generate .c with `C:/Windows/System32/cython -2 -I <numpy-include> <pyx>` then `setup.py build_ext --inplace`
- 7 pyx fail even with -2 (cy3 semantics): liblinear.pyx (except* vs noexcept), _splitter.pyx (qsort cmp), quad_tree.pyx (double->SIZE_t, read-only base), _tree.pyx (2**int->int, read-only base), kd/ball_tree via binary_tree.pxi (np.log2->ITYPE_t), fast_dict.pyx (iterator->const_iterator)
- Build-only edits planned: add `noexcept nogil` to blas fns, cast np.log2/2** results, use insert(end, args) w/o dec, arr.base via PyArray_SetBaseObject

## Task complete (2026-11-02 22:20)
- BUG #14894 FIXED in sklearn/svm/base.py _sparse_fit: guard n_SV == 0 with sp.csr_matrix((n_class, n_SV)) (upstream approach)
- Regression test added: sklearn/svm/tests/test_svm.py::test_svr_sparse_no_support_vectors
- Verification: sparse SVR repro fits OK (dual_coef_ (1,0), n_SV 0); 117 passed in sklearn/svm/tests/test_svm.py + test_sparse.py
- Run tests: cd <ws> && PYTHONPATH=C:/Windows/Temp/pyshim:C:/Windows/Temp/jl C:/Python312/python.exe3 -m pytest sklearn/svm/tests/ -q -W ignore::DeprecationWarning -p no:cacheprovider
- Build-only edits (Cython 3 compat, do NOT revert): binary_tree.pxi (2 casts), _tree.pyx (cast + 2x np.PyArray_SetBaseObject), quad_tree.pyx (cast + PyArray_SetBaseObject), fast_dict.pyx (const_iterator)
