# TASK
The project (sympy, checked out at an old commit) has this issue:

Rational calc value error
python 3.11, sympy 1.11.1
when calc Rational('0.5', '100'), the value is 1/100100; but Rational(0.5, 100) the value is 1/200, this value is the true value, and the version of sympy 1.8 is normal


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
