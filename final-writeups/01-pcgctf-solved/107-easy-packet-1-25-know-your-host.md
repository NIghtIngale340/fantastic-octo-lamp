# EASY PACKET 1 #25 — Know Your Host

**Platform:** PCGCTF · **Challenge ID:** 107 · **Category:** Network Forensics · **Points:** 100

**Status:** Solved in the authenticated snapshot; field re-pulled from the capture for this writeup.

## The challenge

Read the HTTP Host header. The evidence is `EASY_PACKET_1.pcap`, the shared capture for this whole series.

## Solving it

```sh
tshark -nr EASY_PACKET_1.pcap -Y http -T fields -e http.host
```

```text
twitter.com
```



## Screenshot

![107-decisive-evidence.png](../screenshots/107-decisive-evidence.png)

## Flag

```text
pcgCTF{twitter.com}
```

## Reference

- [Original challenge description](../../solved/network-forensics/107-easy-packet-1-25-know-your-host/README.md)
