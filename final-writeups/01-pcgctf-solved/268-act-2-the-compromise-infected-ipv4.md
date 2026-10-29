# ACT 2 — The Compromise: Infected IPv4

**Platform:** PCGCTF · **Challenge ID:** 268 · **Category:** Network Forensics · **Points:** 100

**Status:** Solved in the authenticated snapshot; reproduced from the Act 2 capture.

**Evidence:** Packet 2638 · TCP stream 40 · [2026-02-28-traffic-analysis-exercise.pcap](../../solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap).

## The challenge

Identify the Windows client generating NetSupport RAT traffic.

## Solving it

Use [the shared capture](../../solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap) as `act2.pcap` for the commands below.

NetSupport RAT announces itself in the User-Agent, so I filtered on it:

```sh
tshark -nr act2.pcap -d tcp.port==443,http -Y 'http.user_agent contains "NetSupport"' \
  -T fields -e ip.src -e ip.dst -e http.user_agent -e http.request.uri | sort -u
```

```text
10.2.28.88	45.131.214.85	NetSupport Manager/1.3	http://45.131.214.85/fakeurl.htm
```

The client is 10.2.28.88, calling out to 45.131.214.85.

## Screenshot

Fresh local reproduction using the command described above.

![Command and result](../screenshots/268-clear-method.png)

## Flag

```text
pcgCTF{10.2.28.88}
```

## Takeaway

Commodity RATs often leave their own name in the User-Agent — `NetSupport Manager/1.3` is a gift.

## Reference

- [Original challenge description](../../solved/network-forensics/268-act-2-the-compromise-infected-ipv4/README.md)
