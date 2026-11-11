# Arm 1 — Reference answer — 05-tutoring case-05 (probability: two dice sum to 7)

## 1. The misconception

The student is treating the **outcomes as the 11 possible sums** (2 through 12) and assuming each *total* is equally likely. That's the classic "equiprobable outcomes" error: the outcomes of the *experiment* are not the sums — they are the **36 combinations** the two dice can land on, and sums are NOT equally likely (a sum of 7 has six ways; a sum of 2 has only one). Counting *kinds* of outcomes instead of *individual* outcomes makes the probability wrong.

## 2. Explaining it to the student

"Your mistake is really reasonable — you counted the possible answers (2 to 12), and there are 11 of them, so 1/11 sounds fair. But let's check whether every total is equally easy to roll, because 'possible' doesn't mean 'equally likely.'

Roll a red die and a green die. Write down what they could show as pairs (red, green):

- To get a sum of 2: only (1,1). That's **1 way**. 
- To get a sum of 12: only (6,6). That's **1 way**. 
- To get a sum of 7: (1,6), (2,5), (3,4), (4,3), (5,6)... careful — (1,6) and (6,1) are different, because the dice are different colors! The ways are (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). That's **6 ways**.

Now count ALL the pairs: red die has 6 options, green die has 6 options, so 6 × 6 = **36 equally likely pairs**.

So P(sum = 7) = 6 ways out of 36 = **6/36 = 1/6** — about 17%, not 1/11 (about 9%).

Here's the shape of it, if you list how many ways each total happens: 
2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1. 
Add those up: 1+2+3+4+5+6+5+4+3+2+1 = 36. ✓

See the pyramid? 7 is at the top because the most pairs land there. If totals were equally likely, the bar chart would be flat — and it isn't."

## Quick check for the student (same idea, new problem)

*With the same two dice, what's P(sum = 2)?* 
Ways to make 2: just (1,1) → 1 way out of 36 → **1/36**. (Not 1/11!) 
And *P(sum = 2 OR 12)?* 1 + 1 = 2 ways → **2/36 = 1/18**.

**Rule to remember:** in probability, count *outcomes of the experiment* (the 36 pairs), not the *different values* of the answer (the 11 sums). List the pairs — or find the total by multiplying options — and then count the winning ones.
