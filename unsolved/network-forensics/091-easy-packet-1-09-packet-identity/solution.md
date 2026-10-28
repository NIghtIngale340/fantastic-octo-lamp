# EASY PACKET 1 #09  Packet Identity — analysis

Answer: **0xbed2 (48850 decimal)**

Candidate flag (not platform validated):

```text
pcgCTF{48850}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && ip.id == 0xbed2
```

Evidence: Frames 1; TCP streams 0.

The IPv4 Identification field is hexadecimal 0xbed2, decimal 48850. The flag candidate uses Wireshark's hexadecimal notation; the grader's numeric representation is unvalidated.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.

## Day 1 formatting correction

Garcia explicitly reports `pcgCTF{48850}` as accepted. This replaces our untested spelling `pcgCTF{0xbed2}`. The packet-derived raw value is preserved; the acceptance report is attributed to the teammate and was not retested in our account. [Imported source](../../../team-writeups/garcia-day1/source.md).
