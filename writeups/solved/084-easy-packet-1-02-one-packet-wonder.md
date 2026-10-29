# EASY PACKET 1 #02 — One Packet Wonder

**Platform:** PCGCTF · **Challenge ID:** 84 · **Category:** Network Forensics · **Points:** 100

**Status:** Solved in the authenticated snapshot; field re-pulled from the capture for this writeup.

**Evidence:** [Capture inventory](../evidence/network/packet-locators/capture-inventory.txt): one packet in [EASY_PACKET_1.pcap](../../challenges/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap). A capture-wide count has no individual stream locator.

## The challenge

Count the packets in the capture. The evidence is `EASY_PACKET_1.pcap`, the shared capture for this whole series.

## Solving it

Count the frames:
```sh
tshark -nr EASY_PACKET_1.pcap | wc -l
```

```text
1
```

There's exactly one packet — which is also why every other question in this series reads from frame 1.

## Screenshot

Fresh local reproduction using the command described above.

![Command and result](../screenshots/084-clear-method.png)

## Flag

```text
pcgCTF{1}
```

## Reference

- [Original challenge description](../../challenges/solved/network-forensics/084-easy-packet-1-02-one-packet-wonder/README.md)
