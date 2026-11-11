## 1. The misconception

The student is using **1-based indexing**: they believe the number inside the brackets means "the 3rd item when you count from 1," the way we count objects in everyday life. This is an off-by-one error. It also leads them to the related wrong belief that the last item of a 5-item list is `colors[5]` — which would actually crash with an `IndexError`.

## 2. Explaining the correct concept

In Python, the number in brackets is not "which item" — it's **how many steps you jump from the start of the list**. The list starts at position **0**, not 1, because before you've taken any steps you're already standing on the first item.

So for:

```python
colors = ['red', 'blue', 'green', 'gold', 'purple']
```

think of the indexes as positions measured from the start:

```
index:    0       1        2       3        4
item:  'red'  'blue'  'green'  'gold'  'purple'
```

- `colors[0]` → `'red'` (zero steps from the start = the first item)
- `colors[3]` → `'gold'` (three steps in: red → blue → green → gold)

So `colors[3]` is `'gold'`, not `'green'`. A quick rule: **the item at index `n` is the (n+1)th item** when you count normally.

For the end of the list: since counting starts at 0, the last index of a 5-item list is **5 − 1 = 4**, so the last item is `colors[4]` → `'purple'`. (`colors[5]` is past the end and raises an `IndexError`.) Python also gives you a shortcut: `colors[-1]` always means "the last item."

**Check yourself:** with `colors = ['red', 'blue', 'green', 'gold', 'purple']`, what is `colors[2]`? (Answer: start at 0 for 'red', 1 for 'blue', 2 for 'green' → `'green'`.)
