# Case 05 — Answer

## 1. The misconception

The student assumes that all **outcomes are automatically equally likely** — that because the possible sums are 2 through 12 (eleven sums), each sum must have probability 1/11. This is the "equally likely outcomes" fallacy: listing the possible results is not enough; you must check whether each result happens equally often. The sums are **not** equally likely, because different sums can be produced by different numbers of dice combinations (e.g., 2 can only come from 1+1, while 7 comes from many pairs).

## 2. The correct concept, explained to the student

The eleven sums are not the real "equally likely" outcomes — the **pairs of dice faces** are. Since the red die and the green die are separate dice, rolling them gives 6 × 6 = **36 equally likely ordered pairs** (red, green), like (1,1), (1,2), …, (6,6). Each pair has probability 1/36.

Now count how many of those pairs give a sum of 7:

(1,6), (2,5), (3,4), (4,3), (5,2), (6,1) — that's **6 pairs**.

Note that (1,6) and (6,1) are different outcomes: red 1 with green 6 is not the same roll as red 6 with green 1.

So the probability is:

**P(sum = 7) = 6/36 = 1/6**

The key rule to remember: **probability = (number of favorable equally-likely outcomes) ÷ (total number of equally-likely outcomes)** — and the equally-likely outcomes here are the 36 dice pairs, not the 11 sums. You can check this: a sum of 2 comes from only 1 pair (1,1), so its probability is 1/36 — much smaller than 1/6, which shows the sums can't all be equally likely.

**Correct answer: 1/6**, because 6 of the 36 equally likely (red, green) dice pairs sum to 7.
