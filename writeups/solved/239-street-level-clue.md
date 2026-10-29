# Street-Level Clue

**Platform:** PCGCTF · **Challenge ID:** 239 · **Category:** OSINT / IMINT · **Points:** 100

**Status:** Solved in the last snapshot; re-checked the image for this writeup.

## The challenge

Identify the street in the photo from its signage.

## Solving it

No reverse-image search needed — the street is written right there on an overhead arch in the photo. Zooming in on it:

```text
WELCOME TO CARNABY STREET
(and a storefront sign: ON CARNABY STREET)
```

So it's Carnaby Street. The photo itself is better evidence than a search result that happens to show a similar shopping street, so I didn't bother with GPS guesses.

## Screenshot

![239-actual-browser-image.png](../screenshots/239-actual-browser-image.png)

## Flag

```text
pcgCTF{Carnaby Street}
```

## Takeaway

Read the explicit labels before reaching for broad geographic inference. A geolocation challenge can be a 30-second job when the answer is literally printed in the frame.

## References

- [Original challenge and attachments](<../../home/nightingale/CTF/PCGCTF/solved/osint-imint/239-street-level-clue/README.md>)
