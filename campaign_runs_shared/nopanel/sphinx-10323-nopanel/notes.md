# Agent Journal (structured notes)
<!-- sections: ## Findings | ## Leads | ## Questions | ## Decisions -->
<!-- injected into every prompt — write here what future-you must know -->

## Findings (task: sphinx #10323 prepend whitespace)
- Bug: `:prepend:       </plugin>` — leading spaces of the option value are lost in output.
- Probe (probe_final): sphinx's option converter receives '</plugin>' — spaces already gone BEFORE sphinx's filters run. So the fix is NOT in prepend_filter/append_filter alone.
- PR #10323 in git history = actually the #10318 fix (prepend+dedent ordering); already merged in this checkout (e571479d5 is ancestor of HEAD).
- Upstream master (2025) still has identical prepend_filter/append_filter + unchanged_required → no upstream code fix to copy; must design minimal fix.
- docutils 0.20.1: ExtensionOptions.parse_field_body builds paragraph from indented lines; utils.extract_options takes body[0].astext() as the converter input.
- TODO: pinpoint exact strip point (get_first_known_indented trim_left vs paragraph parse) and find recoverable raw value (field_body.rawsource / block_text).
