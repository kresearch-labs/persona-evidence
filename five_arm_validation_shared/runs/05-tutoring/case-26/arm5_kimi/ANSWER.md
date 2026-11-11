# Case 26 — Answer

## 1. The misconception

The student confuses the **assignment operator** (`=`) with the **equality comparison operator** (`==`). They believe "=" means "is equal to" everywhere, so `=` and `==` must be interchangeable. In fact they do completely different jobs: `=` *gives* a variable a value (it changes state), while `==` *asks a question* — "are these two values equal?" — and produces a True/False answer without changing anything. An `if` condition needs a True/False question, so it needs `==`. (In Python, `if entered = stored_password` is actually a syntax error, not a silent bug — but the underlying confusion is the same one that in languages like C causes the condition to silently assign and almost always evaluate as true.)

## 2. Explaining the correct concept

Think of it this way: `=` is a **command**, `==` is a **question**.

- `entered = stored_password` *commands*: "take whatever is in `stored_password` and stuff it into `entered`." After this runs, the old value of `entered` is gone — overwritten. Nothing is being checked.
- `entered == stored_password` *asks*: "do these two hold the same value?" It answers `True` or `False` and leaves both variables untouched.

An `if` statement is a decision point — it can only react to a question whose answer is True or False. So the blank must be filled with `==`:

```python
entered = input()
if entered == stored_password:
    print('Access granted')
```

A quick self-check that transfers to any similar problem: **"Am I trying to change a variable, or am I trying to compare two things?"** Changing → one `=`. Comparing → two `==`. Also notice the asymmetry the student missed: if `=` and `==` really did the same thing, the language wouldn't need both. Whenever a language gives you two similar-looking symbols, assume they differ and find out how.

Justification: the student's own reasoning ("'=' means equals… both = and == do the same thing") explicitly states the assignment-vs-comparison confusion, so the diagnosis targets that exact belief rather than the wrong character alone.
