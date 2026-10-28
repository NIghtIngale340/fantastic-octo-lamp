# ACT 5 - FINAL INCIDENT: Host One MAC — analysis

Answer: **00:25:64:18:4c:2a**

Candidate flag (not platform validated):

```text
pcgCTF{00:25:64:18:4c:2a}
```

Capture: `2017-02-11-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.src == 10.3.14.131
```

Evidence: Frames 1771.

Ethernet source on an IPv4 packet sent by 10.3.14.131.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
