**1. The misconception**

The student thinks `=` and `==` are interchangeable — that a single `=` "means equals" and can be used to *compare* two values. In reality, `=` is the **assignment** operator (it stores a value into a variable), while `==` is the **comparison** operator (it asks whether two values are equal and produces True/False). The student has mapped the math symbol "=" (which states a relationship) onto code, where the same-looking symbol does a completely different job: it *changes* a variable instead of *checking* it.

**2. Explaining the correct concept**

In Python, one `=` and two `==` do two different jobs:

- `entered = stored_password` **assigns**: it overwrites `entered` so it now holds the same value as `stored_password`. Nothing is checked, and it doesn't produce True/False — so an `if` written this way is a syntax error in Python.
- `entered == stored_password` **compares**: it looks at the two values and asks "are these equal?" The answer is `True` or `False`, which is exactly what `if` needs.

A good way to remember it: read `=` out loud as "gets" or "is set to" (`entered` *gets* the stored password), and read `==` as "is equal to" (`entered` *is equal to* `stored_password`?).

So the fixed code is:

```python
entered = input()
if entered == stored_password:
    print('Access granted')
```

To solve a similar problem, ask yourself: am I *putting a value into* a variable (one `=`), or *asking a question about* two values (two `==`)? An `if` condition must always be a question, so it needs `==` (or another comparison like `!=`, `<`, `>=`).
