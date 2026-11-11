# Case 27 — Answer

## 1. The misconception

The student is mixing up **counting positions** (1st, 2nd, 3rd, …) with **Python's indices** (0, 1, 2, …). Python lists are **0-indexed**: the first score lives at `scores[0]`, and the last of 5 scores lives at `scores[4]`. Because the student starts `i` at 1 and runs it up to 5, the loop skips `scores[0]` (the 88) and ends by asking for `scores[5]`, which doesn't exist — so the program crashes with an `IndexError` after printing only four scores. This is the classic **off-by-one error** caused by treating the index as "which score number" instead of "how far from the start."

## 2. Explaining the correct concept to the student

Your instinct to count the scores 1 through 5 is good — but Python doesn't count that way. In Python, a list's positions start at **0**, not 1. Think of the index as "how many steps from the front door," not "which number item":

```
index:      0   1   2   3   4
scores = [ 88, 92, 79, 85, 94 ]
```

So `scores[0]` is 88 (the 1st score), and `scores[4]` is 94 (the 5th score). There is no `scores[5]` — that's one step past the end, which is why your version crashes.

`range(1, len(scores) + 1)` produces 1, 2, 3, 4, 5 — human counting numbers. But to use them as indices you need 0, 1, 2, 3, 4. The fix is to drop the 1 and the `+ 1`:

```python
for i in range(len(scores)):
    print(scores[i])
```

`range(len(scores))` gives exactly 0 through 4 — every valid index, nothing skipped, nothing past the end.

**A shortcut worth learning:** when you want *the items themselves* and don't care about the positions, Python lets you loop straight over the list:

```python
for score in scores:
    print(score)
```

This reads as "for each score in scores, print it" — no indices to miscount at all.

**Check yourself with a similar problem:** print every letter of `word = "cat"` using a range loop. (Hint: `len("cat")` is 3, so the indices are 0, 1, 2 — your loop should start at 0 and need no `+ 1`.)
