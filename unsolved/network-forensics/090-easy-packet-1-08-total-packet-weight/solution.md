# EASY PACKET 1 #08  Total Packet Weight — analysis

Answer: **504**

Candidate flag (not platform validated):

```text
pcgCTF{504}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && ip.len == 504
```

Evidence: Frames 1; TCP streams 0.

IPv4 Total Length is 504 bytes; the Ethernet header is not included.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
