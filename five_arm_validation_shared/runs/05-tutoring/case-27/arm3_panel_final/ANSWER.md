# Case 27 — Answer

## 1. The misconception behind the answer

The student is treating list indices as **1-based ordinal positions** ("score number i") when Python indexes lists from **0**. Two connected faults, both visible in their steps:

1. **Off-by-one on indexing.** They reason "5 scores, so count the 1st through the 5th" and conclude those are `scores[1]` … `scores[5]`. In Python the 1st score is `scores[0]` and the 5th is `scores[4]`; `scores[5]` does not exist.
2. **Misattributed purpose of the `+ 1`.** They half-remember the `+ 1` idiom and believe it is what makes the loop "reach the 5th score." Actually `range(1, len(scores) + 1)` produces the *ordinals* 1–5 — the wrong objects to use as indices. The `+ 1` belongs to a different job (counting 1..n, e.g. numbering questions); when indexing a list you start at 0 and write `range(len(scores))`, whose exclusive stop already ends exactly at the last valid index, `len - 1`.

What their code actually does (verified by running it): it prints `92, 79, 85, 94` — skipping the first score, `88`, because it starts at index 1 — then crashes with `IndexError: list index out of range` when it asks for `scores[5]`.

## 2. Explaining the correct concept to the student

Your instinct is right: there are 5 scores and you want all of them, from the 1st through the 5th. The only thing that went wrong is *how Python names those positions*.

**The number in brackets is not "which score" — it's "how many steps from the front", and counting starts at 0.**

```
index:      0   1   2   3   4
scores:    88  92  79  85  94
position:  1st 2nd 3rd 4th 5th
```

So the 1st score is `scores[0]`, and the 5th is `scores[4]`. A 5-item list has no `scores[5]` — that's exactly why your version printed `92` first (it started at the 2nd score) and then crashed with `IndexError` when it tried to reach past the end.

**The `+ 1` you remembered is for a different job.** `range(a, b)` counts `a` up to *but not including* `b` — the stop is a fence you stop before, not a item you include. Two consequences:

- `range(1, 6)` gives `1, 2, 3, 4, 5` — the *counting numbers* you wanted, but they're off by one as *indices*.
- When you index a list you start at 0, and the exclusive stop works *for* you: `range(len(scores))` gives `0, 1, 2, 3, 4` — every valid index, ending exactly at the last one. No `+ 1` needed. (You'd only write `range(1, n + 1)` when you want the numbers 1..n themselves, like printing "Question 1 … Question 5".)

**The fix — loop over the valid indices:**

```python
for i in range(len(scores)):
    print(scores[i])
```

Trace it: `i = 0` → prints 88, `i = 1` → 92, `i = 2` → 79, `i = 3` → 85, `i = 4` → 94, then the range runs out. All five, in order, no crash.

**Even simpler:** when you don't need the index itself, Python can hand you each item directly:

```python
for score in scores:
    print(score)
```

Read it as "for each score in scores" — no positions to get wrong at all. Use the `range(len(...))` version only when you genuinely need `i` (e.g. printing the position next to the score — and remember the first position it prints is 0).

**Check yourself with a similar problem:** with `names = ["Ada", "Ben", "Cy"]`, predict what `range(len(names))` produces, then print each name both ways above. If your first printed name is `Ada` and nothing crashes, you've got it.
