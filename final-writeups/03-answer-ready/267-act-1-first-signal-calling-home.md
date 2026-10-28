# ACT 1 — First Signal: Calling Home

**Platform:** PCGCTF · **Challenge ID:** 267 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the Act 1 capture. Exact PCGCTF submission not independently re-confirmed.

## The challenge

Name one confirmed C2 IPv4 address the compromised host contacted.

## Solving it

I used the beacon traffic the host repeatedly sent — same destination, FormBook-style `/irpw/` requests:

```sh
tshark -nr act1.pcap -Y 'ip.src==172.16.8.49 && http.request' \
  -T fields -e ip.dst -e http.host -e http.request.uri
```

```text
146.59.71.167  www.grinswakebthu.info  /irpw/
146.59.71.167  www.grinswakebthu.info  /irpw/?2kn1=...
```

The repeated check-ins to `146.59.71.167` (host `www.grinswakebthu.info`) make it the confirmed C2.

## Screenshot

![267-decisive-evidence.png](../screenshots/267-decisive-evidence.png)

## Flag

```text
pcgCTF{146.59.71.167}
```

## Takeaway

"Confirmed C2" means a repeated, patterned beacon — not just any address the host happened to reach once.

## Reference

- [Original challenge description](../../solved/network-forensics/267-act-1-first-signal-calling-home/README.md)
