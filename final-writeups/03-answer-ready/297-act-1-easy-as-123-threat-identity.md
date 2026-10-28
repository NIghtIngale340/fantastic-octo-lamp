# ACT 1 — Easy as 123: Threat Identity

**Platform:** PCGCTF · **Challenge ID:** 297 · **Category:** Network Forensics / OSINT · **Points:** 100

**Status:** Answer backed by the capture and cited public sources. Exact PCGCTF submission not re-confirmed.

## The challenge

Identify the malware family behind C2 IP `45.131.214.85`.

## Solving it

An IP can host different things over time, so I tied the family to *this* incident rather than a generic reputation label. The capture settles it — the User-Agent names the family outright:

```sh
tshark -nr act.pcap -d tcp.port==443,http -Y 'ip.dst==45.131.214.85 && http.request' \
  -T fields -e http.request.uri -e http.user_agent
```

```text
http://45.131.214.85/fakeurl.htm  NetSupport Manager/1.3
```

ThreatFox (IOC 1755776) independently attributes the same IP and sample to NetSupport Manager RAT. So the family is NetSupport Manager RAT — legitimate remote-admin software abused as a RAT.

## Screenshot

![297-saved-evidence.png](../screenshots/297-saved-evidence.png)

## Flag

```text
pcgCTF{NetSupport Manager RAT}
```

## Takeaway

Bind attribution to the incident's own evidence (the User-Agent here), then corroborate with a threat-intel source — don't lead with a current reputation label.

## References

- [Malware-traffic-analysis: 2026-02-28](https://www.malware-traffic-analysis.net/2026/02/28/index.html)
- [Original challenge description](../../solved/network-forensics/297-act-1-easy-as-123-threat-identity/README.md)
