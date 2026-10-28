# EASY PACKET 1 #09 — Packet Identity

**Platform:** PCGCTF · **Challenge ID:** 91 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the capture (`EASY_PACKET_1.pcap`). Exact PCGCTF submission not re-confirmed.

## The challenge

Recover the IPv4 identification value.

## Solving it

```sh
tshark -nr EASY_PACKET_1.pcap -T fields -e ip.id
```

```text
0xbed2
```

tshark shows it as hex `0xbed2`; the challenge wants decimal, which is 48850.

## Screenshot

![091-decisive-evidence.png](../screenshots/091-decisive-evidence.png)

## Flag

```text
pcgCTF{48850}
```

## Reference

- [Original challenge description](../../solved/network-forensics/091-easy-packet-1-09-packet-identity/README.md)
