# Airport Context — Building

**Platform:** PCGCTF · **Challenge ID:** 244 · **Category:** OSINT / IMINT · **Points:** 100

**Status:** Answer backed by signage + the airport's own site. Exact PCGCTF submission not re-confirmed.

## The challenge

Identify the airport building from its signage.

## Solving it

Zooming into the overhead sign, the branding reads `YVR CONNECTS` / `YVR.CA` — the IATA code for Vancouver. The airport's own site confirms `YVR` is Vancouver International Airport:

```text
Signage: YVR CONNECTS / YVR.CA
yvr.ca/about → Vancouver International Airport
```

(An airport code can be reused by unrelated businesses, so I treated `YVR` as a lead and confirmed it against the official source.)

## Screenshot

![244-actual-browser-image.png](../screenshots/244-actual-browser-image.png)

## Flag

```text
pcgCTF{Vancouver International Airport}
```

## Takeaway

Read the specific branding (the YVR code), then confirm the institution against its own site rather than a generic search caption.

## References

- [Official YVR page](https://www.yvr.ca/en/about-yvr)
- [Original challenge description](../../unsolved/osint-imint/244-airport-context-building/README.md)
