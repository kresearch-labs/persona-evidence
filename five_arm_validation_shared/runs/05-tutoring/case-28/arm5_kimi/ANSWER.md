# Case 28 Answer

## 1. The misconception

The student assumes list indexing is **1-based** — that `colors[3]` means "the 3rd item," counting 1, 2, 3 the way we count in everyday life. In Python (and most programming languages), indexing is **0-based**: the first item is at index 0. The student's related claim that "the last item of a 5-item list would be `colors[5]`" confirms the same off-by-one misconception — `colors[5]` would actually raise an `IndexError`.

## 2. The correct concept

In Python, the index tells you **how many steps to take from the start of the list**, not which position number to count to. So counting starts at 0:

```
colors = ['red', 'blue', 'green', 'gold', 'purple']
index:      0       1        2       3         4
```

- `colors[0]` → `'red'` (the 1st item)
- `colors[1]` → `'blue'` (the 2nd item)
- `colors[2]` → `'green'` (the 3rd item)
- `colors[3]` → `'gold'` (the 4th item) ← the correct answer
- `colors[4]` → `'purple'` (the 5th, last item)

Two handy rules:
1. **The index is always one less than the "counting" position** — the Nth item lives at index N−1.
2. **The last valid index is `len(colors) - 1`** — for a 5-item list that's index 4; `colors[5]` doesn't exist and Python will raise an `IndexError: list index out of range`.

Quick self-check the student can use on similar problems: write the indices 0, 1, 2, … above the items first, then read off the answer. For example, "what is `colors[2]`?" → index 2 sits above `'green'`.

**Justification:** The student's reasoning ("index 3 means the 3rd item… the last item would be colors[5]") explicitly reveals a 1-based indexing assumption, so the diagnosis targets that off-by-one misconception and the explanation rebuilds indexing as 0-based with a concrete index-to-item mapping and a checkable rule.
