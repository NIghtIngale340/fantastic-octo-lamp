# EASY PACKET 1 #03  Destination at Layer 2 — analysis

Answer: **00:d0:bc:eb:e0:80**

Candidate flag (not platform validated):

```text
pcgCTF{00-D0-BC-EB-E0-80}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && eth.dst == 00:d0:bc:eb:e0:80
```

Evidence: Frames 1; TCP streams 0.

Ethernet destination address; independently verified from the first six frame bytes.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.

## Day 1 formatting correction

Garcia explicitly reports `pcgCTF{00-D0-BC-EB-E0-80}` as accepted. This replaces our untested spelling `pcgCTF{00:d0:bc:eb:e0:80}`. The packet-derived raw value is preserved; the acceptance report is attributed to the teammate and was not retested in our account. [Imported source](../../../../team/garcia-day1/source.md).
