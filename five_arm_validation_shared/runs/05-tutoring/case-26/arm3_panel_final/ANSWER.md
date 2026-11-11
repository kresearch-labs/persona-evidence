# Case 26 — Answer

## 1. The misconception

**Assignment vs. equality comparison are the same operation** ("equals is equals"). The student is importing the math meaning of `=` — a symmetric statement that two things are equal — into Python, where `=` is not a statement of fact at all but a *command*: an action that stores the right-hand value into the left-hand name. Because they read `=` as "is equal to," they conclude `=` and `==` are interchangeable, and they can't yet see that `if entered = stored_password` isn't a question — in Python it's a `SyntaxError`, because an `if` needs a True/False expression and assignment doesn't produce one.

## 2. Explaining the correct concept

In Python, `=` and `==` have two completely different jobs — one is an **action**, the other is a **question**:

- `=` means **"gets" / "store this."** It's a one-way action: take the value on the right and put it into the name on the left. `entered = input()` means "store what the user typed into `entered`." After it runs, `entered` has changed. It doesn't check anything and doesn't produce True/False.
- `==` means **"are these equal?"** It's a question you ask about two values, and the answer is `True` or `False`. Nothing gets stored or changed.

An `if` line can only run a decision, so it needs a **question** — something that evaluates to True or False. That's why the blank must be `==`:

```python
entered = input()                  # action: store the typed password in entered
if entered == stored_password:     # question: are the two strings the same?
    print('Access granted')
```

A handy reading habit: say "gets" every time you see one `=`, and "is equal to?" every time you see two. If you ever write `if x = y:`, Python refuses to run it: `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?` — that error is Python telling you it found an action where it needed a question (and it even suggests `==` itself).

`==` belongs to a whole family of question-operators you'll use in `if` lines: `==` (equal?), `!=` (not equal?), `<`, `>`, `<=`, `>=`. They all answer True/False; none of them change anything.

**Try it:** to print "Perfect score" only when `score` is 100, the blank is a question: `if score == 100:` — whereas `score = 100` would *set* the score to 100 and check nothing.
