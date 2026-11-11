# TASK
The project (sympy, checked out at an old commit) has this issue:

Complement doesn't work when input is a mixture of Symbols and numbers
```
>>> a=FiniteSet(x,y,2)
>>> b=Interval(-10,10)
>>> Complement(a,b)
{x, y}
```
`{x, y} \ [-10,10]` is expected as output.


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
