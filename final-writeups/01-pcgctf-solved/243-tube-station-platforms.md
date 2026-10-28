# Tube Station — Platforms

**Platform:** PCGCTF · **Challenge ID:** 243 · **Category:** OSINT / IMINT · **Points:** 100

**Status:** Solved in the last snapshot; re-checked for this writeup.

## The challenge

How many platforms does Piccadilly Circus have?

## Solving it

The trap is answering "two" because it serves two lines. Each line has two numbered platforms. From TfL's station layout:

```text
Bakerloo:   platforms 1 and 2
Piccadilly: platforms 3 and 4
→ 4 unique platforms
```

So four. Live arrival boards change; the numbered platform layout doesn't, so that's what I counted.

## Screenshot

![243-actual-browser-image.png](../screenshots/243-actual-browser-image.png)

## Flag

```text
pcgCTF{4}
```

## Takeaway

Operator pages mix stable infrastructure facts with transient service data — count the numbered platforms, not the trains currently showing.

## References

- [TfL Bakerloo view](https://tfl.gov.uk/tube/stop/940GZZLUPCC/piccadilly-circus-underground-station?lineId=bakerloo)
- [TfL Piccadilly view](https://tfl.gov.uk/tube/stop/940GZZLUPCC/piccadilly-circus-underground-station?lineId=Piccadilly)
- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/osint-imint/243-tube-station-platforms/README.md>)
