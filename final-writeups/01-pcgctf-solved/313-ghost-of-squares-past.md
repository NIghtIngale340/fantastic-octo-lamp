# Ghost of Squares Past

**Platform:** PCGCTF · **Challenge ID:** 313 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot, but two of the five clue images weren't preserved, so points 2 and 4 rest on the teammate's recorded reading rather than something I could re-check. Flagging that honestly.

## The challenge

Identify five Savannah squares in compass order, combine the first four's establishment years, and append the surname of the monument at the centre square.

## Solving it

Each clue points to a Savannah square; the answer is the establishment years in clue order plus the central monument's surname:

```text
Point 1: Johnson Square   → 1733
Point 2: (image missing)  → reported 1742
Point 3: Chippewa Square  → 1815
Point 4: (image missing)  → reported 1733
Centre:  Gordon monument  → gordon
```

Assembled in clue order: `1733-1742-1815-1733-gordon`.

## Screenshot

![313-original-clues.png](../screenshots/313-original-clues.png)

## Flag

```text
deadface{1733-1742-1815-1733-gordon}
```

## Still to do

- Recover the point 2 and point 4 clue images and verify those two squares/years against primary records rather than the teammate's note.

## Takeaway

Assemble multi-part OSINT answers strictly in the order the clue specifies — and keep the two unverified years visibly marked rather than presenting them as confirmed.

## Reference

- [Original challenge and attachments](../../solved/deadface/313-ghost-of-squares-past/README.md)
