# ACT 4 - LUMMA IN THE ROOM: Victim Hostname — analysis

Answer: **DESKTOP-ES9F3ML**

Candidate flag (not platform validated):

```text
pcgCTF{DESKTOP-ES9F3ML}
```

Capture: `2026-01-31-traffic-analysis-exercise.pcap`

Filter:

```wireshark
dhcp || (nbns && eth.src == 00:21:5d:c8:0e:f2)
```

Evidence: Frames 1, 2, 3, 4, 5.

DHCP Host Name is DESKTOP-ES9F3ML; DHCP offers/acknowledges 10.1.21.58. NBNS independently advertises the same hostname.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
