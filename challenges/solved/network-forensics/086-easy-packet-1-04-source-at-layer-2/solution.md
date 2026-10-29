# EASY PACKET 1 #04  Source at Layer 2 — analysis

Answer: **00:1b:63:94:b1:0e**

Candidate flag (not platform validated):

```text
pcgCTF{00-1B-63-94-B1-0E}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && eth.src == 00:1b:63:94:b1:0e
```

Evidence: Frames 1; TCP streams 0.

Ethernet source address; independently verified from frame bytes 6–11.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.

## Day 1 formatting correction

Garcia explicitly reports `pcgCTF{00-1B-63-94-B1-0E}` as accepted. This replaces our untested spelling `pcgCTF{00:1b:63:94:b1:0e}`. The packet-derived raw value is preserved; the acceptance report is attributed to the teammate and was not retested in our account. [Imported source](../../../../team/garcia-day1/source.md).
