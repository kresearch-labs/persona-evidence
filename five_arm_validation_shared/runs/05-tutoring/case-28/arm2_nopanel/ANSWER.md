# Case 28 — Answer

## 1. The misconception

The student believes Python lists are **1-indexed** — that the number in brackets is the item's *position when counting from 1* ("index 3 = 3rd item"). In reality, Python list indices are **offsets from the start**: counting begins at **0**, so `colors[3]` means "the item 3 steps after the first one," which is the **4th** item, `'gold'` — not `'green'`.

The same misconception shows in the student's last claim: they say the last item of a 5-item list is `colors[5]`. It's actually `colors[4]`; `colors[5]` doesn't exist and raises `IndexError: list index out of range`. (The last index is always *length − 1*, because one slot is "used up" by starting at 0.)

## 2. Explaining the correct concept

Think of the index not as "which item" but as **how far you've moved from the front door of the list**:

- `colors[0]` = you've moved 0 steps, so you're still standing on the first item → `'red'`
- `colors[1]` = 1 step in → `'blue'`
- `colors[2]` = 2 steps in → `'green'`
- `colors[3]` = 3 steps in → `'gold'`
- `colors[4]` = 4 steps in → `'purple'`

So `colors[3]` returns **`'gold'`**.

A quick way to remember it: **the first item is index 0, so the index is always one less than the counting position.** 3rd item → index 2; 4th item → index 3; last (5th) item → index 4.

Two checks that catch this error every time:

1. **Count from 0, not 1.** Say "zero: red, one: blue, two: green, three: gold" as you point at the items.
2. **Sanity-check the ends.** First item is always `[0]`; last item of a list of length *n* is always `[n − 1]`. For our 5-item list, the last item is `colors[4]` — and asking for `colors[5]` gives an `IndexError`, because there is no item 5 steps past the start.

**Try it yourself:** with `pets = ['cat', 'dog', 'fish']`, what is `pets[2]`? Count from 0: zero → `'cat'`, one → `'dog'`, two → `'fish'`. So `pets[2]` is `'fish'` — the *3rd* item, at index 2. If you can do that, you've got it.
