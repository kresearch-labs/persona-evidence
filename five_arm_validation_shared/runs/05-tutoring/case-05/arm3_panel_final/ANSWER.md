# Case 05 — Answer

## 1. The misconception

The student is treating the eleven possible **sums** (2 through 12) as if they were eleven **equally likely outcomes**. That's the "outcomes must be equally likely" trap: they've counted the *results you could write down* instead of the *ways the dice can actually land*. In reality a sum of 7 can happen in 6 different ways while a sum of 2 can happen in only 1 way, so the totals are not equally likely at all. The real sample space is the 36 ordered pairs (red, green), not the 11 sums.

## 2. Explaining the correct concept

Here's how I'd explain it to the student:

"Your list of totals — 2, 3, 4, ..., 12 — is a good start, but those totals are **not all equally likely**, and that's the missing piece. To get probabilities right, count the outcomes the dice actually produce, not the totals you can name.

The dice are different colors, so (red=2, green=5) and (red=5, green=2) are **different** rolls. List every roll as a pair (red, green). Red has 6 possibilities and green has 6, so there are 6 × 6 = **36 equally likely rolls**.

Now count how many of those 36 rolls give each total — a 6-by-6 grid works perfectly (rows = red die, columns = green die):

| red\green | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| **1** | 2 | 3 | 4 | 5 | 6 | **7** |
| **2** | 3 | 4 | 5 | 6 | **7** | 8 |
| **3** | 4 | 5 | 6 | **7** | 8 | 9 |
| **4** | 5 | 6 | **7** | 8 | 9 | 10 |
| **5** | 6 | **7** | 8 | 9 | 10 | 11 |
| **6** | **7** | 8 | 9 | 10 | 11 | 12 |

Look down the diagonal: the sum 7 appears in **6 cells** — (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). Meanwhile the sum 2 appears in only **1 cell** — (1,1). That's why the totals aren't equally likely: 7 has six ways of happening, 2 has only one.

So:

P(sum is 7) = 6/36 = **1/6**

Notice 1/6 is bigger than your 1/11 — that's exactly because 7 is the *most common* total, sitting on the longest diagonal.

**Your turn (similar problem):** roll the same two dice. What's the probability the sum is 4? Count the cells that contain a 4 in the grid, put that over 36, and simplify. (Check: you should find 3 ways — (1,3), (2,2), (3,1) — so 3/36 = 1/12.)"

**One-line justification:** the probability is 6/36 = 1/6 because the 36 ordered (red, green) pairs are the equally likely outcomes, and exactly 6 of them — (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) — sum to 7.
