# ACT 3 — Lumma in the Room-ah!: Domain Pivot

**Platform:** PCGCTF · **Challenge ID:** 305 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the capture. Exact PCGCTF submission not re-confirmed.

## The challenge

Pivot from the Lumma C2 IP (`153.92.1.49`) to its domain.

## Solving it

I used the HTTP Host on the actual C2 requests (the virtual host the request targets), confirmed by the DNS answer that resolved it there:

```sh
tshark -nr act.pcap -Y '(http.host && ip.dst==153.92.1.49) || dns.a==153.92.1.49' \
  -T fields -e dns.qry.name -e http.host
```

```text
whitepepper.su  —
—               whitepepper.su
```

The domain is `whitepepper.su`.

## Screenshot

![305-saved-evidence.png](../screenshots/305-saved-evidence.png)

## Flag

```text
pcgCTF{whitepepper.su}
```

## Takeaway

The HTTP Host on the C2 request is more useful than every name ever hosted at that IP — and the DNS answer confirms it's the right one.

## Reference

- [Original challenge description](../../solved/network-forensics/305-act-3-lumma-in-the-room-ah-domain-pivot/README.md)
