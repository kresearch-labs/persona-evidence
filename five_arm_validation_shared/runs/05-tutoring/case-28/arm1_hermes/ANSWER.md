# Arm 1 — Reference answer — 05-tutoring case-28 (zero-based list indexing)

## 1. The misconception

The student believes **lists are indexed starting at 1** — that the number in brackets is the *position* of the item when you count naturally ("1st, 2nd, 3rd..."). In reality, most programming languages (including Python) use **zero-based indexing**: the first item is at index 0, the second at index 1, and so on.

This misconception shows up twice in the student's reasoning:
- They said `colors[3]` is `'green'` (the 3rd item), when it's actually `'gold'` (the 4th item).
- They claimed the last item of a 5-item list is `colors[5]`, when it's actually `colors[4]`. Writing `colors[5]` would crash with an `IndexError`, because there's no 6th slot.

## 2. Explaining it to the student

Great news: your instinct to count is right — you're just counting from the wrong starting number! In Python, the number in brackets isn't "which item" — it's **how far the item is from the start of the list**. The first item has traveled 0 spots, so it's at index 0.

Picture the list laid out with its indexes underneath:

```
'red'   'blue'   'green'   'gold'   'purple'
  0        1         2        3         4
```

So to find `colors[3]`:
1. Find the 3 under the list.
2. Look up: `'gold'`.

That's why `colors[3]` returns `'gold'`, not `'green'`. `'green'` is the 3rd item, but it sits at index **2**, because two items (`'red'` and `'blue'`) come before it.

A handy rule: **index = position − 1**. The 3rd item is at index 2, the 4th item is at index 3.

This also explains the end of the list. A 5-item list uses indexes 0 through 4, so the last item is `colors[4]` — always **length minus 1**. If you try `colors[5]`, Python looks for a spot that doesn't exist and gives you an `IndexError`.

Concrete way to remember it: think of index numbers like building floors in some countries — the ground floor is "floor 0," and the "1st floor" is already one flight up. `colors[0]` is the ground floor of the list.

## Quick check for the student (same idea, new problem)

**Problem:** Given the list
```python
pets = ['cat', 'dog', 'fish', 'bird']
```
(a) What does `pets[2]` return?
(b) How would you get the last item, `'bird'`?

**Solution:**
First lay out the indexes:

```
'cat'   'dog'   'fish'   'bird'
  0       1        2       3
```

(a) `pets[2]` → look above the 2 → `'fish'`. (It's the 3rd pet, at index 2.)
(b) The list has 4 items, so the last index is 4 − 1 = 3: `pets[3]` → `'bird'`. (Careful: `pets[4]` would give an `IndexError`!)