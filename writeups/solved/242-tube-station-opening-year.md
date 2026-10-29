# Tube Station — Opening Year

**Platform:** PCGCTF · **Challenge ID:** 242 · **Category:** OSINT / IMINT · **Points:** 100

**Status:** Solved in the last snapshot; re-checked for this writeup.

## The challenge

When did Piccadilly Circus station (identified in #240/#241) open?

## Solving it

The catch here is that a station has several candidate dates — first opening, a second line, a rebuilt ticket hall. The question asks when it *opened*, so I want the initial date. The London Transport Museum and Historic England both put that in 1906:

```text
Bakerloo line opened:   10 March 1906
Piccadilly line opened: 15 December 1906
→ opening year: 1906
```

Both 1906. The big 1928 modernisation is a later event, not the answer.

## Screenshot

![242-actual-browser-image.png](../screenshots/242-actual-browser-image.png)

## Flag

```text
pcgCTF{1906}
```

## Takeaway

For historical geolocation you have to match the *event* as well as the place — initial opening vs. rebuilds and extensions.

## References

- [London Transport Museum booklet](https://www.ltmuseum.co.uk/sites/default/files/2024-11/London%20Transport%20Museum%20Hidden%20London%20Piccadilly%20Circus%20Tour.pdf)
- [Historic England listing 1226877](https://historicengland.org.uk/listing/the-list/list-entry/1226877)
- [Original challenge and attachments](<../../home/nightingale/CTF/PCGCTF/solved/osint-imint/242-tube-station-opening-year/README.md>)
