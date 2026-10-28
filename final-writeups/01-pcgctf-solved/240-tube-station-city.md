# Tube Station — City

**Platform:** PCGCTF · **Challenge ID:** 240 · **Category:** OSINT / IMINT · **Points:** 100

**Status:** Solved in the last snapshot; I re-checked the image and the operator page for this writeup.

## The challenge

Identify the city from a photo of an underground station entrance. (The city and station questions share the same image.)

## Solving it

The network branding and station name answer different questions. The "Underground" roundel just tells you it's the London Underground network — the sign above the staircase names the specific station. Reading the entrance sign in the photo:

```text
PICCADILLY CIRCUS STATION
```

That's the anchor. To be sure, I checked TfL's own page for the station, which lists its address city as London:

```text
https://tfl.gov.uk/tube/stop/940GZZLUPCC/piccadilly-circus-underground-station
→ Piccadilly Circus Underground Station, London
```

This question only asks for the city, so the answer is London.

## Screenshot

![240-actual-browser-image.png](../screenshots/240-actual-browser-image.png)

## Flag

```text
pcgCTF{London}
```

## Takeaway

One image can answer several questions at different levels — city vs. exact station. Keep those answers separate and anchor each to the sign, not the branding.

## References

- [Transport for London station page](https://tfl.gov.uk/tube/stop/940GZZLUPCC/piccadilly-circus-underground-station)
- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/osint-imint/240-tube-station-city/README.md>)
