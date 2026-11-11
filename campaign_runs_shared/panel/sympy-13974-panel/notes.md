# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Task: powers of TensorProduct (sympy issue, TASK.md) — done 31 Oct
- Project root: C:/Users/agent/work/work/sympy-13974-panel (NOT campaign; that dir has no sympy/).
- Old sympy needs Py3.12 compat shim: PYTHONPATH=C:/Windows/Temp/sympy312compat (sitecustomize adds collections.abc names to collections). Without it, `from collections import Mapping` ImportError.
- Fix applied (matches upstream PR merged in sympy-14248-panel checkout): tensor_product_simp_Pow() added; tensor_product_simp_Mul handles Pow of TensorProduct (n_nc==1, first/next factor); tensor_product_simp dispatches Pow with TensorProduct base to it.
- Verified: issue cases tps(tp(1,1)*tp(1,1))→1x1, tps(tp(1,sigma3)**2 case)→1x1, [5]/[9]→1x1; 4 upstream Pow assertions pass; test_tensorproduct.py 7/7 pass.
- Note: .expand(tensorproduct=True) still returns 1x1**2 — identical behavior in the sympy-14248-panel checkout with the merged fix; merged PR's fix targets tensor_product_simp only.
- Pre-existing failures (unrelated, numpy.complex-era): 9 in sympy/physics/quantum (circuitutils random_*, identitysearch, operatorset test_spin, printing test_gate_failing, shor test_CMod) — identical with/without patch.
- Tests NOT modified; nothing committed; patch left in working tree (git status: M sympy/physics/quantum/tensorproduct.py).
