# ACT 4 — Lumma in the Room: Malicious Domain

**Platform:** PCGCTF · **Challenge ID:** 287 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the Act 4 capture. Exact PCGCTF submission not independently re-confirmed.

**Evidence:** Packets 23723, 24500 · TCP stream 99 · UDP stream 99 · [2026-01-31-traffic-analysis-exercise.pcap](../../unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/files/2026-01-31-traffic-analysis-exercise.pcap).

## The challenge

Identify the C2 domain behind 153.92.1.49.

## Solving it

Use [the shared capture](../../unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/files/2026-01-31-traffic-analysis-exercise.pcap) as `act4.pcap` for the commands below.

The DNS answer ties the name to the IP, and the HTTP Host confirms it:

```sh
tshark -nr act4.pcap -Y 'dns.a==153.92.1.49 || (http.host && ip.dst==153.92.1.49)' \
  -T fields -e dns.qry.name -e dns.a -e http.host | sort -u | head -n 8
```

```text
whitepepper.su
whitepepper.su	153.92.1.49
```

The C2 domain is `whitepepper.su`.

## Screenshot

Fresh local reproduction using the command described above.

![Command and result](../screenshots/287-clear-method.png)

## Flag

```text
pcgCTF{whitepepper.su}
```

## Takeaway

Tie the domain to the IP via the DNS answer rather than assuming — then the HTTP Host is corroboration, not the sole source.

## Reference

- [Original challenge description](../../unsolved/network-forensics/287-act-4-lumma-in-the-room-malicious-domain/README.md)
