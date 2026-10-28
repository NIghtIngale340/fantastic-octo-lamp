# ACT 4 - LUMMA IN THE ROOM: Malicious Domain — analysis

Answer: **whitepepper.su**

Candidate flag (not platform validated):

```text
pcgCTF{whitepepper.su}
```

Capture: `2026-01-31-traffic-analysis-exercise.pcap`

Filter:

```wireshark
dns.a == 153.92.1.49 || (ip.dst == 153.92.1.49 && http.request)
```

Evidence: Frames 23723, 24500; TCP streams 99.

DNS maps whitepepper.su to 153.92.1.49; HTTP Host confirms the same domain.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
