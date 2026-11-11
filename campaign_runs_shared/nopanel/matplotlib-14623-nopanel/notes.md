# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings (2026-11-02, log-axis invert task)
- Task repo = work/matplotlib-14623-nopanel, v3.1.x @ d65c9ca20d (just before PR #14623).
- campaign/.venv has zz-mpl20488-repo.pth -> imports the 20488 repo, NOT this one. To run THIS tree: build ext in place (py3.12 needs configparser.SafeConfigParser + np.Inf monkeypatches; ft2font_wrapper.cpp still fails on removed PyUnicode APIs).
- Bug: set_xlim/set_ylim (+3D) lose requested inverted order: base Locator.nonsingular (mtransforms.nonsingular increasing=False) and LogScale.limit_range_for_scale return ascending limits.
- Upstream fix = PR #14623: af1ab00bf6 (swapped) reworked by 7f7b04879c (reverse + sorted(..., reverse=reverse)); also changed base Locator.nonsingular to drop increasing=False. axes3d set_xlim3d/set_ylim3d got same treatment; set_zlim3d untouched upstream.
