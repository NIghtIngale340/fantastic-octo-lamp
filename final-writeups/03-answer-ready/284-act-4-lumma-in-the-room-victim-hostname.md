# ACT 4 — Lumma in the Room: Victim Hostname

**Platform:** PCGCTF · **Challenge ID:** 284 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the Act 4 capture. Exact PCGCTF submission not independently re-confirmed.

## The challenge

Recover the Lumma victim's hostname.

## Solving it

The host's DHCP request (sent from 0.0.0.0 before it had an address) names it:

```sh
tshark -nr act4.pcap -Y 'eth.src==00:21:5d:c8:0e:f2 && dhcp.option.hostname' \
  -T fields -e dhcp.option.hostname
```

```text
DESKTOP-ES9F3ML
```

## Screenshot

![284-decisive-evidence.png](../screenshots/284-decisive-evidence.png)

## Flag

```text
pcgCTF{DESKTOP-ES9F3ML}
```

## Takeaway

DHCP option 12 names the host even before it has an IP — match on the MAC to be sure it's the right one.

## Reference

- [Original challenge description](../../solved/network-forensics/284-act-4-lumma-in-the-room-victim-hostname/README.md)
