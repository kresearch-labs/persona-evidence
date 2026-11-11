# Case 05 — Two Dice, Sum of 7

## 1. The misconception

The student is treating the **sums** (2, 3, 4, …, 12) as if they were the equally likely outcomes. They are not. There are indeed 11 possible totals, but those totals do not occur equally often — a sum of 7 can happen in six different ways, while a sum of 2 can only happen one way (double ones). The real equally likely outcomes are the **36 ordered pairs** (red die, green die), not the 11 sums. In short: the student has confused "list of possible results" with "list of equally likely outcomes."

## 2. Explaining the correct concept to the student

Here's how I'd explain it:

"Your list of possible sums is right — but think about how you'd actually get each one. Roll a red die and a green die. The red die can show 1–6 and the green die can show 1–6, so there are 6 × 6 = **36 equally likely results**, like (red=1, green=6) or (red=4, green=3). Each of those 36 pairs is just as likely as any other.

Now count how many of those 36 pairs give a sum of 7:

(1,6), (2,5), (3,4), (4,3), (5,2), (6,1) — that's **6 pairs**.

So P(sum = 7) = 6/36 = **1/6**.

Notice the sums themselves aren't equally likely: only one pair makes a 2 — (1,1) — but six pairs make a 7. That's why you can't just count the 11 possible totals.

**Try it yourself:** what's the probability the sum is 4? List the pairs that work, count them, and divide by 36. (You should find 3 pairs, so 3/36 = 1/12.)"
