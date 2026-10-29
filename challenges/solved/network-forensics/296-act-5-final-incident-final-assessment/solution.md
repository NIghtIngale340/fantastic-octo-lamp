# ACT 5 - FINAL INCIDENT: Final Assessment — analysis

Answer: **10.3.14.135**

Candidate flag (not platform validated):

```text
pcgCTF{10.3.14.135}
```

Capture: `2017-02-11-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.src == 10.3.14.135
```

Evidence: Frames 6, 1350, 2055; TCP streams 8.

The third client exhibits ordinary Apple services and Reddit browsing, with neither ransomware-specific pattern attributed to .131 and .134. Clean means no observed evidence of infection in this capture, not a forensic guarantee about the endpoint.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
