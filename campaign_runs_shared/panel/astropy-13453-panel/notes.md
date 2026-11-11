# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- 2026-10-31 HTML `formats` bug (this task): fixed in astropy/io/ascii/html.py — HTML.write() now sets `self.data.cols = cols` and calls `self.data._set_col_formats()` (mirrors BaseData.str_vals(); same as upstream fix). 2 added lines, no test changes.
- ENV: campaign .venv has NO erfa/pytest — cannot run this repo. Use `C:/Python312/python.exe3` (system dist-packages: numpy 1.26.4 + pyerfa 2.0.1.1 + pytest 7.4.4). Extension modules were NOT built in this checkout; built them once with `C:/Python312/python.exe3 setup.py build_ext --inplace -j4` (gitignored, ~2 min).
- Pre-existing failures in astropy/io/ascii/tests (fail with AND without the fix, numpy-2-binary related): test_c_reader.py::test_int_out_of_order[True/False], test_read.py::test_convert_overflow[False].
