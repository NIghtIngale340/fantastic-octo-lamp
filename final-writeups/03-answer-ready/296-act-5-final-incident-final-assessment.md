# ACT 5 — Final Incident: Final Assessment

**Platform:** PCGCTF · **Challenge ID:** 296 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the Act 5 capture. Exact PCGCTF submission not independently re-confirmed.

## The challenge

Which client shows neither ransomware pattern?

## Solving it

10.3.14.135's traffic is all benign — Apple push/Spotlight and Reddit — with no Spora or Cerber IOC:

```sh
tshark -nr act5.pcap -Y 'ip.src==10.3.14.135 && (http.request || dns.qry.name)' \
  -T fields -e dns.qry.name -e http.host -e http.user_agent
```

```text
1-courier.sandbox.push.apple.com   —                   —
—                                  wu-calculator.apple.com  SpotlightNetHelper/... Darwin/14.5.0
www.reddit.com                     —                   —
```

A macOS host browsing normally — the clean machine is 10.3.14.135.

## Screenshot

![296-decisive-evidence.png](../screenshots/296-decisive-evidence.png)

## Flag

```text
pcgCTF{10.3.14.135}
```

## Takeaway

"Not compromised" still needs positive evidence — here, normal Apple/Reddit traffic and the absence of either ransomware IOC.

## Reference

- [Original challenge description](../../solved/network-forensics/296-act-5-final-incident-final-assessment/README.md)
