# ACT 4 - LUMMA IN THE ROOM: Lumma Victim — analysis

Answer: **10.1.21.58**

Candidate flag (not platform validated):

```text
pcgCTF{10.1.21.58}
```

Capture: `2026-01-31-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.dst == 153.92.1.49 && http.request
```

Evidence: Frames 24500, 25270; TCP streams 99, 111.

The source of both Chrome and Edge victim-fingerprinting requests is 10.1.21.58.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
