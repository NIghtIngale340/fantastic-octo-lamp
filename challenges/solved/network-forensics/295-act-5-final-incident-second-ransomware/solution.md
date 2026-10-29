# ACT 5 - FINAL INCIDENT: Second Ransomware — analysis

Answer: **Cerber**

Candidate flag (not platform validated):

```text
pcgCTF{Cerber}
```

Capture: `2017-02-11-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.src == 10.3.14.134 && (http.host contains "p27dokhpz2n7nvgr" || udp.dstport == 6892)
```

Evidence: Frames 8820, 11043, 16354; TCP streams 179, 296.

UDP destination port 6892 and p27dokhpz2n7nvgr.1nmrtq.top match independently published Cerber post-infection behavior. The portal paths include a victim identifier, language selection, captcha, and bitcoin resources.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
