# Case 27 — Answer

## 1. The misconception

The student believes list positions in Python are counted starting at 1 ("the 1st score through the 5th score"), i.e. they are applying everyday human counting to list indexing. Python lists are **zero-indexed**: the first element is `scores[0]` and the last is `scores[len(scores) - 1]`. So `range(1, len(scores) + 1)` produces the indices 1, 2, 3, 4, 5 — it skips the first element (`scores[0]`, the 88) and then crashes on the last iteration with `IndexError: list index out of range` when it tries `scores[5]`, which does not exist. A secondary misconception is that you must index into a list at all to visit its items; in Python you can loop over the list directly.

## 2. Explaining the correct concept

Here's how I'd put it to the student:

Your instinct to count "1st, 2nd, 3rd..." is perfectly natural — that's how people count. But Python starts counting positions at **0**, not 1. Think of the index as "how many steps from the start of the list": the first element is 0 steps away, so it's `scores[0]`. For your list:

```
scores = [88, 92, 79, 85, 94]
index:     0   1   2   3   4
```

So with 5 elements, the legal indices are 0 through 4 — never 5. That's why `scores[5]` blows up: you're asking for the 6th element of a 5-element list.

Two ways to fix your loop:

**Option A — keep your index-based style, but start at 0:**
```python
for i in range(len(scores)):   # range(5) gives 0, 1, 2, 3, 4
    print(scores[i])
```
Note that `range(n)` already stops *before* `n`, so `range(len(scores))` gives exactly the valid indices — no `+ 1` needed.

**Option B — the more Pythonic way: skip indices entirely.**
```python
for score in scores:
    print(score)
```
When you just want to look at each item in order, you don't need positions at all — the loop hands you each element directly. This version can never go out of range.

**Quick self-check for similar problems:** if a list has `n` items, its indices run from `0` to `n - 1`. If you ever write `scores[len(scores)]`, you've gone one too far. And ask yourself: "Do I actually need the position number?" If not, loop over the list itself.
