# ACT 5 - FINAL INCIDENT: Map the Network — analysis

Answer: **10.3.14.131_10.3.14.134_10.3.14.135**

Candidate flag (not platform validated):

```text
pcgCTF{10.3.14.131_10.3.14.134_10.3.14.135}
```

Capture: `2017-02-11-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.src == 10.3.14.131 || ip.src == 10.3.14.134 || ip.src == 10.3.14.135
```

Evidence: Frames 6, 1684, 1771.

These three client IPv4 addresses are ordered numerically. The gateway is 10.3.14.1. Despite the question describing all three as Windows, .135 exhibits Apple/macOS traffic.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
