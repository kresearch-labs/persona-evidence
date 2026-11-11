# TASK
The project (sympy, checked out at an old commit) has this issue:

mathematica_code gives wrong output with Max
If I run the code

```
x = symbols('x')
mathematica_code(Max(x,2))
```

then I would expect the output `'Max[x,2]'` which is valid Mathematica code but instead I get `'Max(2, x)'` which is not valid Mathematica code.


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
