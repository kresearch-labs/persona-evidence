# TASK
The project (sympy, checked out at an old commit) has this issue:

pprint unicode does not format subscripts on Greek letters
Good:

[ -t₀⋅w₀   -t₁⋅w₀   -t₂⋅w₀]


Bad:

[ -t₀⋅ω0   -t₁⋅ω0   -t₂⋅ω0]





Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
