# ACT 1 - FIRST SIGNAL: Domain Membership — analysis

Answer: **FIRSTTOLAST.TECH**

Candidate flag (not platform validated):

```text
pcgCTF{FIRSTTOLAST.TECH}
```

Capture: `ACT12026-08-09-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.addr == 172.16.8.49 && kerberos
```

Evidence: Frames 1939, 1961; TCP streams 86, 88.

The victim's machine-account Kerberos exchanges explicitly name realm FIRSTTOLAST.TECH, also usable as lowercase DNS domain firsttolast.tech.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
