# Tube Station — Station

**Platform:** PCGCTF · **Challenge ID:** 241 · **Category:** OSINT / IMINT · **Points:** 100

**Status:** Solved in the last snapshot; re-checked for this writeup.

## The challenge

Name the exact station in the entrance photo (same image as the city question, #240).

## Solving it

The red roundel only tells you it's the London Underground — the station name is on the blue sign above the staircase:

```text
PICCADILLY CIRCUS STATION
```

I confirmed against TfL's own listing for the stop so I wasn't matching a lookalike entrance elsewhere. This question wants the station, so: Piccadilly Circus.

## Screenshot

![241-actual-browser-image.png](../screenshots/241-actual-browser-image.png)

## Flag

```text
pcgCTF{Piccadilly Circus}
```

## Takeaway

One image answers several questions at different levels — keep the city (#240) and station (#241) answers separate, and anchor each to the right sign.

## References

- [TfL station page](https://tfl.gov.uk/tube/stop/940GZZLUPCC/piccadilly-circus-underground-station)
- [Original challenge and attachments](<../../home/nightingale/CTF/PCGCTF/solved/osint-imint/241-tube-station-station/README.md>)
