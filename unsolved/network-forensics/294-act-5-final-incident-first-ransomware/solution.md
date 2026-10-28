# ACT 5 - FINAL INCIDENT: First Ransomware — analysis

Answer: **Spora**

Candidate flag (not platform validated):

```text
pcgCTF{Spora}
```

Capture: `2017-02-11-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.src == 10.3.14.131 && http.host == "spora.biz"
```

Evidence: Frames 16762, 16772, 16979; TCP streams 299.

The first host accesses spora.biz, the ransomware-specific domain. The HTTP stream includes redirects and DDoS-Guard interstitials; those pages alone are not proof of executable delivery. Family attribution combines this ransomware-specific domain, the challenge's infection context, and primary Spora research.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
