# TASK
The project (sympy, checked out at an old commit) has this issue:

kernS: 'kern' referenced before assignment
from sympy.core.sympify import kernS

text = "(2*x)/(x-1)"
expr = kernS(text)  
//  hit = kern in s
// UnboundLocalError: local variable 'kern' referenced before assignment


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
