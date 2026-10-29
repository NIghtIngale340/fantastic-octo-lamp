# ACT 4 - LUMMA IN THE ROOM: Fingerprint API — analysis

Answer: **/api/set_agent**

Candidate flag (not platform validated):

```text
pcgCTF{/api/set_agent}
```

Capture: `2026-01-31-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.dst == 153.92.1.49 && http.request.uri contains "/api/set_agent"
```

Evidence: Frames 24500, 24601, 25270, 25286; TCP streams 99, 111.

The API endpoint is /api/set_agent. Query strings supply victim ID, token, agent=Chrome/Edge, and optionally act=log; they are not part of the requested path.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
