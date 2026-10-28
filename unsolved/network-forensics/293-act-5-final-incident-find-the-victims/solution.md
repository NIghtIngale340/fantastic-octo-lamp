# ACT 5 - FINAL INCIDENT: Find the Victims — analysis

Answer: **10.3.14.131_10.3.14.134**

Candidate flag (not platform validated):

```text
pcgCTF{10.3.14.131_10.3.14.134}
```

Capture: `2017-02-11-traffic-analysis-exercise.pcap`

Filter:

```wireshark
(ip.src == 10.3.14.131 && http.host == "spora.biz") || (ip.src == 10.3.14.134 && (http.host contains "p27dokhpz2n7nvgr" || udp.dstport == 6892))
```

Evidence: Frames 8820, 11043, 16762; TCP streams 179, 299.

The .131 host accesses the Spora payment domain; .134 emits Cerber-pattern UDP/6892 traffic and visits the Cerber payment portal. These are the two infected endpoints in ascending order.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
