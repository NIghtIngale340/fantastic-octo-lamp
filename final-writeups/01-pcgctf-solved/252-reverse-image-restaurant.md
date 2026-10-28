# Reverse Image — Restaurant

**Platform:** PCGCTF · **Challenge ID:** 252 · **Category:** OSINT / IMINT · **Points:** 100

**Status:** Solved in the last snapshot. Identity is solid; the exact accepted punctuation (the apostrophe) isn't recorded, so I note that below.

## The challenge

Identify the restaurant from an interior photo. (This same image feeds the editor question, #253.)

## Solving it

The counter and interior signage match Katz's Delicatessen in New York. I corroborated it with Bon Appétit's own video, which was filmed there — the same source the #253 editor question hangs on:

```text
Identified: Katz's Delicatessen, New York City
Primary source: Bon Appétit "Working 24 Hours Straight at NY's Most Iconic Deli"
```

The restaurant is this question's answer; the editor (Andrew Knowlton) belongs to #253.

## Screenshot

![252-actual-browser-image.png](../screenshots/252-actual-browser-image.png)

## Flag

```text
pcgCTF{Katz's Delicatessen}
```

The original writes "Katz's" with an apostrophe; I've used an ASCII apostrophe here as the candidate, but that exact character is worth confirming against the accepted string.

## Takeaway

Reverse-image work is strongest when you tie the visual match to a named original source, not just a lookalike. Keep the place and the person who appears there as separate answers.

## References

- [Bon Appétit video](https://www.bonappetit.com/video/watch/working-24-hours-straight-at-new-york-most-iconic-deli)
- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/osint-imint/252-reverse-image-restaurant/README.md>)
