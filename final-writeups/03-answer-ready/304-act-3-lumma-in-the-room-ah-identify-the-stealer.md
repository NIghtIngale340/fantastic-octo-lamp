# ACT 3 — Lumma in the Room-ah!: Identify the Stealer

**Platform:** PCGCTF · **Challenge ID:** 304 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the capture and cited public sources. Exact PCGCTF submission not re-confirmed.

## The challenge

Name the info-stealer talking to `153.92.1.49`.

## Solving it

The title hints "Lumma," but a title isn't attribution — so I leaned on the IDS signature and the request shape. The public exercise flags `ET MALWARE Lumma Stealer Victim Fingerprinting Activity` on this IP, and the capture matches it:

```sh
tshark -nr act.pcap -Y 'ip.dst==153.92.1.49 && http.request' \
  -T fields -e http.host -e http.request.uri
```

```text
whitepepper.su  /api/set_agent?id=3BF67EC0...&agent=Chrome
```

The `/api/set_agent` victim-fingerprinting request to `whitepepper.su` is Lumma Stealer's behaviour.

## Screenshot

![304-saved-evidence.png](../screenshots/304-saved-evidence.png)

## Flag

```text
pcgCTF{Lumma Stealer}
```

## Takeaway

Treat the challenge title as a lead, not proof — confirm with the signature plus the characteristic `set_agent` request.

## References

- [Malware-traffic-analysis: 2026-01-31](https://www.malware-traffic-analysis.net/2026/01/31/index.html)
- [Original challenge description](../../solved/network-forensics/304-act-3-lumma-in-the-room-ah-identify-the-stealer/README.md)
