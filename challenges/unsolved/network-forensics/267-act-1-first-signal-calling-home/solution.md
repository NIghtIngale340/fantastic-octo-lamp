# ACT 1 - FIRST SIGNAL: Calling Home — analysis

Answer: **146.59.71.167**

Candidate flag (not platform validated):

```text
pcgCTF{146.59.71.167}
```

Capture: `ACT12026-08-09-traffic-analysis-exercise.pcap`

Filter:

```wireshark
ip.src == 172.16.8.49 && ip.dst == 146.59.71.167 && http.request
```

Evidence: Frames 11227, 11714; TCP streams 242, 249.

The compromised host sends repeated short-path POSTs and a FormBook-pattern GET check-in to this IP. Domain www.grinswakebthu.info, path /irpw/, parameter 2kn1, fixed Firefox/39.0 user agent. Prior ACT 4 OSINT analysis independently preserved official ET signature 2050745 and matching network evidence. This is one confirmed C2 answer, not a claim that every contacted external IP is malicious.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
