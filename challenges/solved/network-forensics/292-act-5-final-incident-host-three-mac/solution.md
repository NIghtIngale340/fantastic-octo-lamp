# ACT 5 - FINAL INCIDENT: Host Three MAC — analysis

Answer: **00:26:bb:4c:6b:e1**

Candidate flag (not platform validated):

```text
pcgCTF{00:26:bb:4c:6b:e1}
```

Capture: `2017-02-11-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.src == 10.3.14.135
```

Evidence: Frames 6.

Ethernet source on a DNS query sent by 10.3.14.135.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
