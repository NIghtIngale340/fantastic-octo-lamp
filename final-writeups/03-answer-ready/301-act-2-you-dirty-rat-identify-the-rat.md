# ACT 2 — You Dirty RAT!: Identify the RAT

**Platform:** PCGCTF · **Challenge ID:** 301 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the capture and cited public sources. Exact PCGCTF submission not re-confirmed.

**Evidence:** Packet 9119 · TCP stream 83 · [2024-07-30-traffic-analysis-exercise.pcap](../../unsolved/network-forensics/274-act-3-malware-investigation-compromised-endpoint/files/2024-07-30-traffic-analysis-exercise.pcap).

## The challenge

Name the RAT family beaconing to `141.98.10.79`.

## Solving it

Use [the shared capture](../../unsolved/network-forensics/274-act-3-malware-investigation-compromised-endpoint/files/2024-07-30-traffic-analysis-exercise.pcap) as `act.pcap`.

The capture has ~102 outbound packets containing the string `STRRAT`, and the beacon names itself in cleartext:

```sh
tshark -nr act.pcap -Y 'tcp.payload contains "STRRAT"' \
  -T fields -e tcp.payload | head -n 1 | xxd -r -p | strings
```

```text
ping|STRRAT|1BE8292C|DESKTOP-SKBR25F|ccollier|Microsoft Windows 11 Pro|64-bit|Windows Defender||1.6|US:United States|Not Installed|1 Sec
```

`ping|STRRAT|...` — the family is STRRAT, matching the public analysis of this exercise.

## Screenshot

Fresh local reproduction using the command described above.

![Command and result](../screenshots/301-clear-method-v3.png)

## Flag

```text
pcgCTF{STRRAT}
```

## Takeaway

STRRAT's beacon names the family in plaintext; the host/account fields that follow are corroboration, not a reason to invent a different label.

## References

- [Malware-traffic-analysis: 2024-07-30](https://www.malware-traffic-analysis.net/2024/07/30/index.html)
- [Original challenge description](../../unsolved/osint/301-act-2-you-dirty-rat-identify-the-rat/README.md)
