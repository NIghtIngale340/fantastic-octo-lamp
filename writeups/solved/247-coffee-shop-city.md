# Coffee Shop — City

**Platform:** PCGCTF · **Challenge ID:** 247 · **Category:** OSINT / IMINT · **Points:** 100

**Status:** Answer backed by matched photos + local records. Exact PCGCTF submission not re-confirmed.

## The challenge

Which Scottish town holds the photographed coffee shop?

## Solving it

I matched the shop's distinctive corner layout and façade to a geotagged photo of the branch, then cross-checked the street address against local records:

```text
Matching geotagged photo → Blairgowrie branch
Heritage record: 20 Wellmeadow, Blairgowrie
Tourism listing (The Wee Coffee Shop): 1 Allan Street, Blairgowrie
```

The town is Blairgowrie.

## Screenshot

![247-actual-browser-image.png](../screenshots/247-actual-browser-image.png)

## Flag

```text
pcgCTF{Blairgowrie}
```

## Takeaway

Pin a storefront by matching the exact corner/façade to a geotagged photo, then confirm with an address record — don't rely on a single search caption.

## References

- [Geograph photo of the branch](https://www.geograph.org.uk/photo/1647585)
- [Original challenge description](../../challenges/solved/osint-imint/247-coffee-shop-city/README.md)
