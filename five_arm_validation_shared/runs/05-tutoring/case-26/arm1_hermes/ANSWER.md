# Arm 1 — Reference answer — 05-tutoring case-26 (assignment `=` vs. comparison `==` in conditions)

## 1. The misconception

The student believes that `=` and `==` are interchangeable — that both mean "equals" in the mathematical sense. This is the classic **conflation of assignment with comparison**.

In most programming languages, including Python, these are two *different operators* that do two *different jobs*:

- `=` **assigns**: it stores a value into a variable (`x = 5` puts 5 in the box named `x`).
- `==` **compares**: it asks a yes/no question about two values (`x == 5` asks "is x equal to 5?" and answers True or False).

Because the student thinks `=` already means "equals," they write `if entered = stored_password:` — which doesn't ask a question at all; it tries to *change* the variable `entered` inside the condition. In Python this is actually a **syntax error**, so the program won't even run. The deeper issue is not just the typo — it's not yet seeing that a condition must be a **question that evaluates to True/False**, while assignment is an **action that changes something**.

## 2. Explaining it to the student

Think of it this way:

- `=` is like **filling in a box**. When you write `score = 10`, you are putting the value 10 into the variable `score`. After this line runs, `score` holds 10. It's an instruction: *"make this so."*
- `==` is like **checking a box against something**. When you write `score == 10`, you are asking: *"Is what's in score equal to 10?"* Python answers with `True` or `False`. Nothing gets changed.

A concrete example:

```python
x = 5        # ACTION: put 5 into x
print(x)     # prints 5

print(x == 5)   # QUESTION: is x equal to 5? → prints True
print(x == 9)   # QUESTION: is x equal to 9? → prints False
```

An `if` statement needs a **question**, because it has to decide whether to run the indented code:

```python
entered = input()          # '=' here: store the typed text in entered
if entered == stored_password:   # '==' here: ASK "are these the same?"
    print('Access granted')
```

Read the `if` line out loud: *"If entered is equal to stored_password..."* — that's a question, so it needs `==`. A quick trick: wherever you'd say "**is** it equal?" in English, use `==`; wherever you'd say "**set** it to," use `=`.

So the fixed blank in the original problem is:

```python
if entered == stored_password:
```

## Quick check for the student (same idea, new problem)

Fill in the blank so the program prints `'You guessed it!'` when the player's guess matches the secret number:

```python
secret = 7
guess = int(input())
if guess ____ secret:
    print('You guessed it!')
```

**Solution:** the blank is `==`.

```python
if guess == secret:
    print('You guessed it!')
```

Why: the `if` line must *ask* "is guess equal to secret?" so it can decide True or False — that requires the comparison operator `==`. Notice the first line, `secret = 7`, correctly uses `=` because there we are *storing* a value, not comparing. One line stores, the other line asks — two different jobs, two different operators.