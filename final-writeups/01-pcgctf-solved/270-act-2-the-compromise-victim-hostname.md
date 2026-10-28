# ACT 2 — The Compromise: Victim Hostname

**Platform:** PCGCTF · **Challenge ID:** 270 · **Category:** Network Forensics · **Points:** 100

**Status:** Solved in the authenticated snapshot; reproduced from the Act 2 capture.

## The challenge

Recover the infected client's hostname.

## Solving it

The host announces its name in both DHCP (before it has an IP) and NBNS:

```sh
tshark -nr act2.pcap -Y 'eth.src==00:19:d1:b2:4d:ad && (dhcp.option.hostname || nbns.name)' \
  -T fields -e dhcp.option.hostname -e nbns.name
```

```text
DESKTOP-TEYQ2NR   —
—                 DESKTOP-TEYQ2NR<20> (Server service)
```

Both agree: `DESKTOP-TEYQ2NR`.

## Screenshot

![270-decisive-evidence.png](../screenshots/270-decisive-evidence.png)

## Flag

```text
pcgCTF{DESKTOP-TEYQ2NR}
```

## Takeaway

When DHCP and NBNS name the same host, that's solid corroboration — no need to guess from anything else.

## Reference

- [Original challenge description](../../solved/network-forensics/270-act-2-the-compromise-victim-hostname/README.md)
