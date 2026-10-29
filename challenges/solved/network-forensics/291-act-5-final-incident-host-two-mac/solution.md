# ACT 5 - FINAL INCIDENT: Host Two MAC — analysis

Answer: **14:da:e9:5b:42:1c**

Candidate flag (not platform validated):

```text
pcgCTF{14:da:e9:5b:42:1c}
```

Capture: `2017-02-11-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.src == 10.3.14.134
```

Evidence: Frames 1684, 1712.

Ethernet source on packets from 10.3.14.134; DHCP also identifies this host as Knutson-PC.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
