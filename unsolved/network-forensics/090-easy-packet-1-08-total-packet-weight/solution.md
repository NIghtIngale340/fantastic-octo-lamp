# EASY PACKET 1 #08  Total Packet Weight — analysis

Answer: **504**

Candidate flag (not platform validated):

```text
pcgCTF{504 bytes}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && ip.len == 504
```

Evidence: Frames 1; TCP streams 0.

IPv4 Total Length is 504 bytes; the Ethernet header is not included.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.

## Day 1 formatting correction

Garcia explicitly reports `pcgCTF{504 bytes}` as accepted. This replaces our untested spelling `pcgCTF{504}`. The packet-derived raw value is preserved; the acceptance report is attributed to the teammate and was not retested in our account. [Imported source](../../../team-writeups/garcia-day1/source.md).
