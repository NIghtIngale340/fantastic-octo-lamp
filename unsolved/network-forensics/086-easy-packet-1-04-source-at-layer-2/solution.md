# EASY PACKET 1 #04  Source at Layer 2 — analysis

Answer: **00:1b:63:94:b1:0e**

Candidate flag (not platform validated):

```text
pcgCTF{00:1b:63:94:b1:0e}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && eth.src == 00:1b:63:94:b1:0e
```

Evidence: Frames 1; TCP streams 0.

Ethernet source address; independently verified from frame bytes 6–11.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
