# All originally unsolved Network Forensics — answer sheet

Scope: 38 challenges from the original unsolved snapshot. **35 saved candidates and 3 substantive answers whose accepted wording remains unknown (#83, #102, #112).**

Day 1 update: exact formatting for eight entries was revised using Garcia’s reported successful submissions. Those acceptance reports are attributed to the teammate; no new submissions were made in our account. Capture-format candidate `pcap` is reported rejected. Original packet evidence remains unchanged.

| ID | Challenge | Recovered answer | Candidate flag |
|---:|---|---|---|
| 83 | [EASY PACKET 1 #01  The Capture Signature](../../challenges/unsolved/network-forensics/083-easy-packet-1-01-the-capture-signature/solution.md) | pcap (classic libpcap/tcpdump format) | **Accepted phrase unresolved** |
| 85 | [EASY PACKET 1 #03  Destination at Layer 2](../../challenges/solved/network-forensics/085-easy-packet-1-03-destination-at-layer-2/solution.md) | 00:d0:bc:eb:e0:80 | `pcgCTF{00-D0-BC-EB-E0-80}` |
| 86 | [EASY PACKET 1 #04  Source at Layer 2](../../challenges/solved/network-forensics/086-easy-packet-1-04-source-at-layer-2/solution.md) | 00:1b:63:94:b1:0e | `pcgCTF{00-1B-63-94-B1-0E}` |
| 89 | [EASY PACKET 1 #07  The 20-Byte Header](../../challenges/solved/network-forensics/089-easy-packet-1-07-the-20-byte-header/solution.md) | 20 bytes (IHL = 5) | `pcgCTF{20 bytes}` |
| 90 | [EASY PACKET 1 #08  Total Packet Weight](../../challenges/solved/network-forensics/090-easy-packet-1-08-total-packet-weight/solution.md) | 504 | `pcgCTF{504 bytes}` |
| 91 | [EASY PACKET 1 #09  Packet Identity](../../challenges/solved/network-forensics/091-easy-packet-1-09-packet-identity/solution.md) | 0xbed2 (48850 decimal) | `pcgCTF{48850}` |
| 100 | [EASY PACKET 1 #18  Push and Acknowledge](../../challenges/solved/network-forensics/100-easy-packet-1-18-push-and-acknowledge/solution.md) | PSH and ACK | `pcgCTF{PSH and ACK}` |
| 102 | [EASY PACKET 1 #20  Push to the Application](../../challenges/unsolved/network-forensics/102-easy-packet-1-20-push-to-the-application/solution.md) | Push buffered data to the receiving application without waiting for more data | **Accepted phrase unresolved** |
| 103 | [EASY PACKET 1 #21  Speak HTTP](../../challenges/solved/network-forensics/103-easy-packet-1-21-speak-http/solution.md) | HTTP | `pcgCTF{HTTP}` |
| 111 | [EASY PACKET 1 #29  The Exposed Credentials](../../challenges/solved/network-forensics/111-easy-packet-1-29-the-exposed-credentials/solution.md) | usertest:password | `pcgCTF{usertest/password}` |
| 112 | [EASY PACKET 1 #30  Cleartext on the Wire](../../challenges/unsolved/network-forensics/112-easy-packet-1-30-cleartext-on-the-wire/solution.md) | HTTP Basic credentials are recoverable over unencrypted HTTP; use HTTPS (HTTP over TLS) | **Accepted phrase unresolved** |
| 265 | [ACT 1 - FIRST SIGNAL: Domain Membership](../../challenges/solved/network-forensics/265-act-1-first-signal-domain-membership/solution.md) | FIRSTTOLAST.TECH | `pcgCTF{FIRSTTOLAST}` |
| 267 | [ACT 1 - FIRST SIGNAL: Calling Home](../../challenges/unsolved/network-forensics/267-act-1-first-signal-calling-home/solution.md) | 146.59.71.167 | `pcgCTF{146.59.71.167}` |
| 272 | [ACT 2 - THE COMPROMISE: Who Is brolf?](../../challenges/solved/network-forensics/272-act-2-the-compromise-who-is-brolf/solution.md) | Becka Rolf | `pcgCTF{Becka Rolf}` |
| 273 | [ACT 2 - THE COMPROMISE: RAT Check-In](../../challenges/solved/network-forensics/273-act-2-the-compromise-rat-check-in/solution.md) | /fakeurl.htm | `pcgCTF{/fakeurl.htm}` |
| 274 | [ACT 3 - MALWARE INVESTIGATION: Compromised Endpoint](../../challenges/solved/network-forensics/274-act-3-malware-investigation-compromised-endpoint/solution.md) | 172.16.1.66 | `pcgCTF{172.16.1.66}` |
| 275 | [ACT 3 - MALWARE INVESTIGATION: Endpoint MAC](../../challenges/solved/network-forensics/275-act-3-malware-investigation-endpoint-mac/solution.md) | 00:1e:64:ec:f3:08 | `pcgCTF{00:1e:64:ec:f3:08}` |
| 276 | [ACT 3 - MALWARE INVESTIGATION: Endpoint Name](../../challenges/solved/network-forensics/276-act-3-malware-investigation-endpoint-name/solution.md) | DESKTOP-SKBR25F | `pcgCTF{DESKTOP-SKBR25F}` |
| 277 | [ACT 3 - MALWARE INVESTIGATION: Compromised Account](../../challenges/solved/network-forensics/277-act-3-malware-investigation-compromised-account/solution.md) | ccollier | `pcgCTF{ccollier}` |
| 278 | [ACT 3 - MALWARE INVESTIGATION: User Identity](../../challenges/solved/network-forensics/278-act-3-malware-investigation-user-identity/solution.md) | Clark Collier | `pcgCTF{Clark Collier}` |
| 279 | [ACT 3 - MALWARE INVESTIGATION: C2 Destination](../../challenges/solved/network-forensics/279-act-3-malware-investigation-c2-destination/solution.md) | 141.98.10.79 | `pcgCTF{141.98.10.79}` |
| 280 | [ACT 3 - MALWARE INVESTIGATION: Malware Family](../../challenges/solved/network-forensics/280-act-3-malware-investigation-malware-family/solution.md) | STRRAT | `pcgCTF{STRRAT}` |
| 281 | [ACT 3 - MALWARE INVESTIGATION: Beacon Evidence](../../challenges/solved/network-forensics/281-act-3-malware-investigation-beacon-evidence/solution.md) | DESKTOP-SKBR25F | `pcgCTF{DESKTOP-SKBR25F}` |
| 282 | [ACT 4 - LUMMA IN THE ROOM: Lumma Victim](../../challenges/solved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/solution.md) | 10.1.21.58 | `pcgCTF{10.1.21.58}` |
| 283 | [ACT 4 - LUMMA IN THE ROOM: Victim MAC](../../challenges/solved/network-forensics/283-act-4-lumma-in-the-room-victim-mac/solution.md) | 00:21:5d:c8:0e:f2 | `pcgCTF{00:21:5d:c8:0e:f2}` |
| 284 | [ACT 4 - LUMMA IN THE ROOM: Victim Hostname](../../challenges/solved/network-forensics/284-act-4-lumma-in-the-room-victim-hostname/solution.md) | DESKTOP-ES9F3ML | `pcgCTF{DESKTOP-ES9F3ML}` |
| 285 | [ACT 4 - LUMMA IN THE ROOM: Compromised User](../../challenges/solved/network-forensics/285-act-4-lumma-in-the-room-compromised-user/solution.md) | gwyatt | `pcgCTF{gwyatt}` |
| 286 | [ACT 4 - LUMMA IN THE ROOM: Full User Name](../../challenges/solved/network-forensics/286-act-4-lumma-in-the-room-full-user-name/solution.md) | Gabriel Wyatt | `pcgCTF{Gabriel Wyatt}` |
| 287 | [ACT 4 - LUMMA IN THE ROOM: Malicious Domain](../../challenges/solved/network-forensics/287-act-4-lumma-in-the-room-malicious-domain/solution.md) | whitepepper.su | `pcgCTF{whitepepper.su}` |
| 288 | [ACT 4 - LUMMA IN THE ROOM: Fingerprint API](../../challenges/solved/network-forensics/288-act-4-lumma-in-the-room-fingerprint-api/solution.md) | /api/set_agent | `pcgCTF{/api/set_agent}` |
| 289 | [ACT 5 - FINAL INCIDENT: Map the Network](../../challenges/solved/network-forensics/289-act-5-final-incident-map-the-network/solution.md) | 10.3.14.131_10.3.14.134_10.3.14.135 | `pcgCTF{10.3.14.131_10.3.14.134_10.3.14.135}` |
| 290 | [ACT 5 - FINAL INCIDENT: Host One MAC](../../challenges/solved/network-forensics/290-act-5-final-incident-host-one-mac/solution.md) | 00:25:64:18:4c:2a | `pcgCTF{00:25:64:18:4c:2a}` |
| 291 | [ACT 5 - FINAL INCIDENT: Host Two MAC](../../challenges/solved/network-forensics/291-act-5-final-incident-host-two-mac/solution.md) | 14:da:e9:5b:42:1c | `pcgCTF{14:da:e9:5b:42:1c}` |
| 292 | [ACT 5 - FINAL INCIDENT: Host Three MAC](../../challenges/solved/network-forensics/292-act-5-final-incident-host-three-mac/solution.md) | 00:26:bb:4c:6b:e1 | `pcgCTF{00:26:bb:4c:6b:e1}` |
| 293 | [ACT 5 - FINAL INCIDENT: Find the Victims](../../challenges/solved/network-forensics/293-act-5-final-incident-find-the-victims/solution.md) | 10.3.14.131_10.3.14.134 | `pcgCTF{10.3.14.131_10.3.14.134}` |
| 294 | [ACT 5 - FINAL INCIDENT: First Ransomware](../../challenges/solved/network-forensics/294-act-5-final-incident-first-ransomware/solution.md) | Spora | `pcgCTF{Spora}` |
| 295 | [ACT 5 - FINAL INCIDENT: Second Ransomware](../../challenges/solved/network-forensics/295-act-5-final-incident-second-ransomware/solution.md) | Cerber | `pcgCTF{Cerber}` |
| 296 | [ACT 5 - FINAL INCIDENT: Final Assessment](../../challenges/solved/network-forensics/296-act-5-final-incident-final-assessment/solution.md) | 10.3.14.135 | `pcgCTF{10.3.14.135}` |
