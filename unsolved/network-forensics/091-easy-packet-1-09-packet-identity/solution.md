# EASY PACKET 1 #09  Packet Identity — analysis

Answer: **0xbed2 (48850 decimal)**

Candidate flag (not platform validated):

```text
pcgCTF{0xbed2}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && ip.id == 0xbed2
```

Evidence: Frames 1; TCP streams 0.

The IPv4 Identification field is hexadecimal 0xbed2, decimal 48850. The flag candidate uses Wireshark's hexadecimal notation; the grader's numeric representation is unvalidated.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
