# ACT 4 - LUMMA IN THE ROOM: Victim MAC — analysis

Answer: **00:21:5d:c8:0e:f2**

Candidate flag (not platform validated):

```text
pcgCTF{00:21:5d:c8:0e:f2}
```

Capture: `2026-01-31-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.src == 10.1.21.58 && ip.dst == 153.92.1.49
```

Evidence: Frames 24500; TCP streams 99.

Ethernet source address on the infected host's C2 request.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
