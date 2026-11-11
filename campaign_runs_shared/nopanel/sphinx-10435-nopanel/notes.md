# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings
- sphinx-10435 (LaTeX inline code role): visit_literal in sphinx/writers/latex.py (~L1702-1718) splices pygments Verbatim output: replaces '\begin{Verbatim}[commandchars=\\\{\}]' with '\sphinxcode{\sphinxupquote{' and strips '\end{Verbatim}'. The newlines around the PYG content then hit LaTeX text mode => visible spaces at start/end in PDF (issue #10435, from #10251).
- Fix (matches test_latex_code_role expectation byte-for-byte): call highlight_block(..., nowrap=True) and emit r'\sphinxcode{\sphinxupquote{' + CR + hlcode.rstrip() + CR + '}}'. PygmentsBridge.highlight_block forwards **kwargs to the formatter, so nowrap works. Newlines are safe inside \sphinxupquote because it sets \endlinechar\m@ne and uses \scantokens (sphinxlatexliterals.sty L770-797) — they are gobbled, no space in PDF.
- Env fixes needed to run tests: venv lacked imagesize, sphinxcontrib*, alabaster (copied from C:/Windows/Temp/sphinx-tv2 venv); pygments 2.21 emitted '\PYG{+w}{ }' for spaces but test expects ' ' => swapped in system pygments 2.17.2 (old 2.21 kept at pygments-2.21.0.bak in site-packages).
- Project root is C:/Users/agent/work/work/sphinx-10435-nopanel (NOT campaign; campaign only hosts the venv).
