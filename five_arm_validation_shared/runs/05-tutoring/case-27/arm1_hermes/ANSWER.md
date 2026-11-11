# Arm 1 — Reference answer — 05-tutoring case-27 (zero-based list indexing / off-by-one loop error)

## 1. The misconception

**The student believes Python list indices start at 1.** They are treating the index as the item's *ordinal position* ("1st score, 2nd score, … 5th score") instead of a *zero-based offset*. In their mental model, `scores[1]` is the first score and `scores[5]` is the fifth, so `range(1, len(scores) + 1)` reads naturally as "count from 1 through 5."

This produces two bugs at once:

- **The first element is skipped:** `scores[0]` (88) is never printed.
- **The loop runs off the end:** when `i = 5`, `scores[5]` doesn't exist, so the program crashes with `IndexError: list index out of range`. The actual output is `92, 79, 85, 94`, then a crash.

Worth crediting: the `+ 1` shows the student correctly understands that `range`'s stop value is *excluded*. The flaw isn't how they used `range` — it's that they fed 1-based human counting into a 0-based indexing system.

## 2. Explaining it to the student

In Python, an index doesn't mean "which-number item this is" — it means **how many items come before it**. The first item has zero items before it, so its index is 0. The second has one item before it, so its index is 1, and so on:

| Human position | 1st | 2nd | 3rd | 4th | 5th |
|---|---|---|---|---|---|
| Python index   | 0   | 1   | 2   | 3   | 4   |
| Value          | 88  | 92  | 79  | 85  | 94  |

**Key rule:** a list of length *n* has valid indices `0` through `n − 1`. The last valid index is always `len(list) - 1` — there is no `scores[5]` in a 5-item list.

That gives you the standard pattern for visiting every element:

```python
for i in range(len(scores)):   # i takes 0, 1, 2, 3, 4
    print(scores[i])
```

Notice this needs **no `+ 1`**: `range(len(scores))` already stops one past the last index, which is exactly where you want to stop.

If you prefer your "1 through 5" counting, you must convert to an index by subtracting 1:

```python
for i in range(1, len(scores) + 1):
    print(scores[i - 1])       # position 1 → index 0, position 5 → index 4
```

And when you don't actually need the index, Python lets you loop over the values directly — no counting at all:

```python
for s in scores:
    print(s)
```

Think of it like building floors in many countries: the ground floor is floor 0, so the "5th level up" is labeled 4. Python lists work the same way — the first slot is slot 0.

## Quick check for the student (same idea, new problem)

**Problem:**
```python
pets = ["cat", "dog", "fish", "bird"]
```
(a) Write a loop that prints every pet, in order.
(b) Predict what your original pattern — `for i in range(1, len(pets) + 1): print(pets[i])` — would actually do.

**Solution:**

(a)
```python
for i in range(len(pets)):   # i = 0, 1, 2, 3
    print(pets[i])
```
Output: `cat`, `dog`, `fish`, `bird`. (Even simpler: `for p in pets: print(p)`.)

(b) `range(1, 5)` gives `i = 1, 2, 3, 4`, so it prints `dog`, `fish`, `bird`, then crashes with `IndexError` on `pets[4]` — and `"cat"` never gets printed. To fix that version, you'd need `print(pets[i - 1])`.