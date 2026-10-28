# All unsolved Network Forensics — answer sheet

**Scope:** all 38 challenges marked unsolved in the archived Network Forensics category. Includes the 15 previously analyzed ACT 4/5 network questions; excludes their two OSINT questions.

**Status:** evidence analysis complete for all 38. No platform acceptance is claimed. The last validation attempt returned `PCGCTF is paused`; no submissions were made for this batch. Original account-status folders remain unchanged.

**Flag formatting:** 36 candidate flags follow the displayed wrapper, but capitalization, separators, numeric units, and full-name spaces have not been validated. Two conceptual questions (#102 and #112) have substantive answers, but the exact phrase required by the grader cannot be inferred reliably from the question. They are explicitly marked instead of inventing accepted flags.

| ID | Challenge | Recovered answer | Candidate flag |
| ---: | --- | --- | --- |
| 83 | [EASY PACKET 1 #01  The Capture Signature](../unsolved/network-forensics/083-easy-packet-1-01-the-capture-signature/solution.md) | pcap (classic libpcap/tcpdump format) | `pcgCTF{pcap}` |
| 85 | [EASY PACKET 1 #03  Destination at Layer 2](../unsolved/network-forensics/085-easy-packet-1-03-destination-at-layer-2/solution.md) | 00:d0:bc:eb:e0:80 | `pcgCTF{00:d0:bc:eb:e0:80}` |
| 86 | [EASY PACKET 1 #04  Source at Layer 2](../unsolved/network-forensics/086-easy-packet-1-04-source-at-layer-2/solution.md) | 00:1b:63:94:b1:0e | `pcgCTF{00:1b:63:94:b1:0e}` |
| 89 | [EASY PACKET 1 #07  The 20-Byte Header](../unsolved/network-forensics/089-easy-packet-1-07-the-20-byte-header/solution.md) | 20 bytes (IHL = 5) | `pcgCTF{20}` |
| 90 | [EASY PACKET 1 #08  Total Packet Weight](../unsolved/network-forensics/090-easy-packet-1-08-total-packet-weight/solution.md) | 504 | `pcgCTF{504}` |
| 91 | [EASY PACKET 1 #09  Packet Identity](../unsolved/network-forensics/091-easy-packet-1-09-packet-identity/solution.md) | 0xbed2 (48850 decimal) | `pcgCTF{0xbed2}` |
| 100 | [EASY PACKET 1 #18  Push and Acknowledge](../unsolved/network-forensics/100-easy-packet-1-18-push-and-acknowledge/solution.md) | PSH and ACK | `pcgCTF{PSH_ACK}` |
| 102 | [EASY PACKET 1 #20  Push to the Application](../unsolved/network-forensics/102-easy-packet-1-20-push-to-the-application/solution.md) | Push buffered data to the receiving application without waiting for more data | **Exact flag phrase unknown; see explanation** |
| 103 | [EASY PACKET 1 #21  Speak HTTP](../unsolved/network-forensics/103-easy-packet-1-21-speak-http/solution.md) | HTTP | `pcgCTF{HTTP}` |
| 111 | [EASY PACKET 1 #29  The Exposed Credentials](../unsolved/network-forensics/111-easy-packet-1-29-the-exposed-credentials/solution.md) | usertest:password | `pcgCTF{usertest:password}` |
| 112 | [EASY PACKET 1 #30  Cleartext on the Wire](../unsolved/network-forensics/112-easy-packet-1-30-cleartext-on-the-wire/solution.md) | HTTP Basic credentials are recoverable over unencrypted HTTP; use HTTPS (HTTP over TLS) | **Exact flag phrase unknown; see explanation** |
| 265 | [ACT 1 - FIRST SIGNAL: Domain Membership](../unsolved/network-forensics/265-act-1-first-signal-domain-membership/solution.md) | FIRSTTOLAST.TECH | `pcgCTF{FIRSTTOLAST.TECH}` |
| 267 | [ACT 1 - FIRST SIGNAL: Calling Home](../unsolved/network-forensics/267-act-1-first-signal-calling-home/solution.md) | 146.59.71.167 | `pcgCTF{146.59.71.167}` |
| 272 | [ACT 2 - THE COMPROMISE: Who Is brolf?](../unsolved/network-forensics/272-act-2-the-compromise-who-is-brolf/solution.md) | Becka Rolf | `pcgCTF{Becka Rolf}` |
| 273 | [ACT 2 - THE COMPROMISE: RAT Check-In](../unsolved/network-forensics/273-act-2-the-compromise-rat-check-in/solution.md) | /fakeurl.htm | `pcgCTF{/fakeurl.htm}` |
| 274 | [ACT 3 - MALWARE INVESTIGATION: Compromised Endpoint](../unsolved/network-forensics/274-act-3-malware-investigation-compromised-endpoint/solution.md) | 172.16.1.66 | `pcgCTF{172.16.1.66}` |
| 275 | [ACT 3 - MALWARE INVESTIGATION: Endpoint MAC](../unsolved/network-forensics/275-act-3-malware-investigation-endpoint-mac/solution.md) | 00:1e:64:ec:f3:08 | `pcgCTF{00:1e:64:ec:f3:08}` |
| 276 | [ACT 3 - MALWARE INVESTIGATION: Endpoint Name](../unsolved/network-forensics/276-act-3-malware-investigation-endpoint-name/solution.md) | DESKTOP-SKBR25F | `pcgCTF{DESKTOP-SKBR25F}` |
| 277 | [ACT 3 - MALWARE INVESTIGATION: Compromised Account](../unsolved/network-forensics/277-act-3-malware-investigation-compromised-account/solution.md) | ccollier | `pcgCTF{ccollier}` |
| 278 | [ACT 3 - MALWARE INVESTIGATION: User Identity](../unsolved/network-forensics/278-act-3-malware-investigation-user-identity/solution.md) | Clark Collier | `pcgCTF{Clark Collier}` |
| 279 | [ACT 3 - MALWARE INVESTIGATION: C2 Destination](../unsolved/network-forensics/279-act-3-malware-investigation-c2-destination/solution.md) | 141.98.10.79 | `pcgCTF{141.98.10.79}` |
| 280 | [ACT 3 - MALWARE INVESTIGATION: Malware Family](../unsolved/network-forensics/280-act-3-malware-investigation-malware-family/solution.md) | STRRAT | `pcgCTF{STRRAT}` |
| 281 | [ACT 3 - MALWARE INVESTIGATION: Beacon Evidence](../unsolved/network-forensics/281-act-3-malware-investigation-beacon-evidence/solution.md) | DESKTOP-SKBR25F | `pcgCTF{DESKTOP-SKBR25F}` |
| 282 | [ACT 4 - LUMMA IN THE ROOM: Lumma Victim](../unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/solution.md) | 10.1.21.58 | `pcgCTF{10.1.21.58}` |
| 283 | [ACT 4 - LUMMA IN THE ROOM: Victim MAC](../unsolved/network-forensics/283-act-4-lumma-in-the-room-victim-mac/solution.md) | 00:21:5d:c8:0e:f2 | `pcgCTF{00:21:5d:c8:0e:f2}` |
| 284 | [ACT 4 - LUMMA IN THE ROOM: Victim Hostname](../unsolved/network-forensics/284-act-4-lumma-in-the-room-victim-hostname/solution.md) | DESKTOP-ES9F3ML | `pcgCTF{DESKTOP-ES9F3ML}` |
| 285 | [ACT 4 - LUMMA IN THE ROOM: Compromised User](../unsolved/network-forensics/285-act-4-lumma-in-the-room-compromised-user/solution.md) | gwyatt | `pcgCTF{gwyatt}` |
| 286 | [ACT 4 - LUMMA IN THE ROOM: Full User Name](../unsolved/network-forensics/286-act-4-lumma-in-the-room-full-user-name/solution.md) | Gabriel Wyatt | `pcgCTF{Gabriel Wyatt}` |
| 287 | [ACT 4 - LUMMA IN THE ROOM: Malicious Domain](../unsolved/network-forensics/287-act-4-lumma-in-the-room-malicious-domain/solution.md) | whitepepper.su | `pcgCTF{whitepepper.su}` |
| 288 | [ACT 4 - LUMMA IN THE ROOM: Fingerprint API](../unsolved/network-forensics/288-act-4-lumma-in-the-room-fingerprint-api/solution.md) | /api/set_agent | `pcgCTF{/api/set_agent}` |
| 289 | [ACT 5 - FINAL INCIDENT: Map the Network](../unsolved/network-forensics/289-act-5-final-incident-map-the-network/solution.md) | 10.3.14.131_10.3.14.134_10.3.14.135 | `pcgCTF{10.3.14.131_10.3.14.134_10.3.14.135}` |
| 290 | [ACT 5 - FINAL INCIDENT: Host One MAC](../unsolved/network-forensics/290-act-5-final-incident-host-one-mac/solution.md) | 00:25:64:18:4c:2a | `pcgCTF{00:25:64:18:4c:2a}` |
| 291 | [ACT 5 - FINAL INCIDENT: Host Two MAC](../unsolved/network-forensics/291-act-5-final-incident-host-two-mac/solution.md) | 14:da:e9:5b:42:1c | `pcgCTF{14:da:e9:5b:42:1c}` |
| 292 | [ACT 5 - FINAL INCIDENT: Host Three MAC](../unsolved/network-forensics/292-act-5-final-incident-host-three-mac/solution.md) | 00:26:bb:4c:6b:e1 | `pcgCTF{00:26:bb:4c:6b:e1}` |
| 293 | [ACT 5 - FINAL INCIDENT: Find the Victims](../unsolved/network-forensics/293-act-5-final-incident-find-the-victims/solution.md) | 10.3.14.131_10.3.14.134 | `pcgCTF{10.3.14.131_10.3.14.134}` |
| 294 | [ACT 5 - FINAL INCIDENT: First Ransomware](../unsolved/network-forensics/294-act-5-final-incident-first-ransomware/solution.md) | Spora | `pcgCTF{Spora}` |
| 295 | [ACT 5 - FINAL INCIDENT: Second Ransomware](../unsolved/network-forensics/295-act-5-final-incident-second-ransomware/solution.md) | Cerber | `pcgCTF{Cerber}` |
| 296 | [ACT 5 - FINAL INCIDENT: Final Assessment](../unsolved/network-forensics/296-act-5-final-incident-final-assessment/solution.md) | 10.3.14.135 | `pcgCTF{10.3.14.135}` |

## 83 — EASY PACKET 1 #01  The Capture Signature

Answer: **pcap (classic libpcap/tcpdump format)**

Capture: `EASY_PACKET_1.pcap`; Frames 1.

Filter: `frame.number == 1`

File magic d4 c3 b2 a1 indicates classic little-endian, microsecond-resolution PCAP; capinfos independently reports pcap. This is file-level evidence, not a packet protocol field. The platform may call this libpcap.

## 85 — EASY PACKET 1 #03  Destination at Layer 2

Answer: **00:d0:bc:eb:e0:80**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && eth.dst == 00:d0:bc:eb:e0:80`

Ethernet destination address; independently verified from the first six frame bytes.

## 86 — EASY PACKET 1 #04  Source at Layer 2

Answer: **00:1b:63:94:b1:0e**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && eth.src == 00:1b:63:94:b1:0e`

Ethernet source address; independently verified from frame bytes 6–11.

## 89 — EASY PACKET 1 #07  The 20-Byte Header

Answer: **20 bytes (IHL = 5)**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && ip.hdr_len == 20`

The IHL nibble is 5, meaning five 32-bit words: 5 × 4 = 20 bytes. The numeric flag candidate uses bytes, without a units suffix.

## 90 — EASY PACKET 1 #08  Total Packet Weight

Answer: **504**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && ip.len == 504`

IPv4 Total Length is 504 bytes; the Ethernet header is not included.

## 91 — EASY PACKET 1 #09  Packet Identity

Answer: **0xbed2 (48850 decimal)**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && ip.id == 0xbed2`

The IPv4 Identification field is hexadecimal 0xbed2, decimal 48850. The flag candidate uses Wireshark's hexadecimal notation; the grader's numeric representation is unvalidated.

## 100 — EASY PACKET 1 #18  Push and Acknowledge

Answer: **PSH and ACK**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && tcp.flags.push == 1 && tcp.flags.ack == 1`

TCP flags value is 0x018. PSH and ACK are set; SYN, FIN, RST, and URG are clear. The underscore separator is a submission-format candidate, not an observed grader requirement.

## 102 — EASY PACKET 1 #20  Push to the Application

Answer: **Push buffered data to the receiving application without waiting for more data**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && tcp.flags.push == 1`

PSH requests the push function: make buffered data available to the receiving user/application rather than waiting for additional data to fill a buffer. It is not a record boundary or a guarantee of immediate application scheduling. This conceptual answer is established, but the challenge does not disclose the exact phrase its flag matcher expects. Do not invent an accepted flag spelling. Reference: https://www.rfc-editor.org/rfc/rfc9293.html#section-3.9.1.2

## 103 — EASY PACKET 1 #21  Speak HTTP

Answer: **HTTP**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && http.request`

The TCP payload starts GET /statuses/replies.xml HTTP/1.1 and is decoded as HTTP.

## 111 — EASY PACKET 1 #29  The Exposed Credentials

Answer: **usertest:password**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && http.authorization`

Authorization is Basic dXNlcnRlc3Q6cGFzc3dvcmQ=. Base64 decoding yields username usertest and password password, separated by a colon. These are challenge-supplied packet contents.

## 112 — EASY PACKET 1 #30  Cleartext on the Wire

Answer: **HTTP Basic credentials are recoverable over unencrypted HTTP; use HTTPS (HTTP over TLS)**

Capture: `EASY_PACKET_1.pcap`; Frames 1; TCP streams 0.

Filter: `frame.number == 1 && http.authorization`

Base64 is encoding, not encryption: an observer can recover the username/password. Protect credential transport with HTTPS/TLS. This is the semantic answer; the exact compound phrase expected inside the flag is not specified. Reference: https://www.rfc-editor.org/rfc/rfc7617.html#section-1

## 265 — ACT 1 - FIRST SIGNAL: Domain Membership

Answer: **FIRSTTOLAST.TECH**

Capture: `ACT12026-08-09-traffic-analysis-exercise.pcap`; Frames 1939, 1961; TCP streams 86, 88.

Filter: `ip.addr == 172.16.8.49 && kerberos`

The victim's machine-account Kerberos exchanges explicitly name realm FIRSTTOLAST.TECH, also usable as lowercase DNS domain firsttolast.tech.

## 267 — ACT 1 - FIRST SIGNAL: Calling Home

Answer: **146.59.71.167**

Capture: `ACT12026-08-09-traffic-analysis-exercise.pcap`; Frames 11227, 11714; TCP streams 242, 249.

Filter: `ip.src == 172.16.8.49 && ip.dst == 146.59.71.167 && http.request`

The compromised host sends repeated short-path POSTs and a FormBook-pattern GET check-in to this IP. Domain www.grinswakebthu.info, path /irpw/, parameter 2kn1, fixed Firefox/39.0 user agent. Prior ACT 4 OSINT analysis independently preserved official ET signature 2050745 and matching network evidence. This is one confirmed C2 answer, not a claim that every contacted external IP is malicious.

## 272 — ACT 2 - THE COMPROMISE: Who Is brolf?

Answer: **Becka Rolf**

Capture: `2026-02-28-traffic-analysis-exercise.pcap`; Frames 339; TCP streams 9.

Filter: `samr.samr_UserInfo21.account_name == "brolf"`

SAMR UserInfo21 pairs brolf with full_name Becka Rolf in one response.

## 273 — ACT 2 - THE COMPROMISE: RAT Check-In

Answer: **/fakeurl.htm**

Capture: `2026-02-28-traffic-analysis-exercise.pcap`; Frames 2638; TCP streams 40.

Filter: `http.user_agent contains "NetSupport"`

264 HTTP requests use the NetSupport Manager/1.3 user agent. The request target can be absolute-form http://45.131.214.85/fakeurl.htm; the requested path is /fakeurl.htm. HTTP is carried on TCP port 443 in this capture, which does not make it TLS.

## 274 — ACT 3 - MALWARE INVESTIGATION: Compromised Endpoint

Answer: **172.16.1.66**

Capture: `2024-07-30-traffic-analysis-exercise.pcap`; Frames 9119; TCP streams 83.

Filter: `tcp contains "STRRAT"`

This source sends a plaintext STRRAT victim-profile beacon to 141.98.10.79:12132.

## 275 — ACT 3 - MALWARE INVESTIGATION: Endpoint MAC

Answer: **00:1e:64:ec:f3:08**

Capture: `2024-07-30-traffic-analysis-exercise.pcap`; Frames 9119; TCP streams 83.

Filter: `frame.number == 9119`

Ethernet source on the confirmed victim's STRRAT beacon.

## 276 — ACT 3 - MALWARE INVESTIGATION: Endpoint Name

Answer: **DESKTOP-SKBR25F**

Capture: `2024-07-30-traffic-analysis-exercise.pcap`; Frames 9119; TCP streams 83.

Filter: `tcp contains "STRRAT"`

The host field in the decoded STRRAT beacon is DESKTOP-SKBR25F. Kerberos machine-account desktop-skbr25f$ independently corroborates it in frame 58.

## 277 — ACT 3 - MALWARE INVESTIGATION: Compromised Account

Answer: **ccollier**

Capture: `2024-07-30-traffic-analysis-exercise.pcap`; Frames 913, 1070; TCP streams 46, 21.

Filter: `kerberos.CNameString == "ccollier" || samr.samr_UserInfo21.account_name == "ccollier"`

Kerberos and SAMR identify account ccollier; the STRRAT beacon also carries ccollier.

## 278 — ACT 3 - MALWARE INVESTIGATION: User Identity

Answer: **Clark Collier**

Capture: `2024-07-30-traffic-analysis-exercise.pcap`; Frames 9759, 10317, 1070; TCP streams 109, 126, 21.

Filter: `frame.number == 10317 || frame.number == 9759 || frame.number == 1070`

LDAP frame 9759 has sn=Collier and givenName=Clark; LDAP frame 10317 has displayName=Clark Collier and the matching user DN. SAMR frame 1070 pairs ccollier with Clark Collier, bridging the account to the directory name.

## 279 — ACT 3 - MALWARE INVESTIGATION: C2 Destination

Answer: **141.98.10.79**

Capture: `2024-07-30-traffic-analysis-exercise.pcap`; Frames 9119; TCP streams 83.

Filter: `tcp contains "STRRAT"`

Destination of the recurring STRRAT beacons; destination TCP port 12132. Do not confuse this with the benign ip-api.com geolocation lookup.

## 280 — ACT 3 - MALWARE INVESTIGATION: Malware Family

Answer: **STRRAT**

Capture: `2024-07-30-traffic-analysis-exercise.pcap`; Frames 9119; TCP streams 83.

Filter: `tcp contains "STRRAT"`

The application payload literally begins ping|STRRAT| and includes the victim profile and version 1.6. No public solution page is needed for attribution.

## 281 — ACT 3 - MALWARE INVESTIGATION: Beacon Evidence

Answer: **DESKTOP-SKBR25F**

Capture: `2024-07-30-traffic-analysis-exercise.pcap`; Frames 9119; TCP streams 83.

Filter: `tcp contains "STRRAT"`

The fourth pipe-separated beacon field is DESKTOP-SKBR25F. The complete first beacon is saved in act3-first-beacon.txt.

## 282 — ACT 4 - LUMMA IN THE ROOM: Lumma Victim

Answer: **10.1.21.58**

Capture: `2026-01-31-traffic-analysis-exercise.pcap`; Frames 24500, 25270; TCP streams 99, 111.

Filter: `ip.dst == 153.92.1.49 && http.request`

The source of both Chrome and Edge victim-fingerprinting requests is 10.1.21.58.

## 283 — ACT 4 - LUMMA IN THE ROOM: Victim MAC

Answer: **00:21:5d:c8:0e:f2**

Capture: `2026-01-31-traffic-analysis-exercise.pcap`; Frames 24500; TCP streams 99.

Filter: `ip.src == 10.1.21.58 && ip.dst == 153.92.1.49`

Ethernet source address on the infected host's C2 request.

## 284 — ACT 4 - LUMMA IN THE ROOM: Victim Hostname

Answer: **DESKTOP-ES9F3ML**

Capture: `2026-01-31-traffic-analysis-exercise.pcap`; Frames 1, 2, 3, 4, 5.

Filter: `dhcp || (nbns && eth.src == 00:21:5d:c8:0e:f2)`

DHCP Host Name is DESKTOP-ES9F3ML; DHCP offers/acknowledges 10.1.21.58. NBNS independently advertises the same hostname.

## 285 — ACT 4 - LUMMA IN THE ROOM: Compromised User

Answer: **gwyatt**

Capture: `2026-01-31-traffic-analysis-exercise.pcap`; Frames 214, 358; TCP streams 4, 8.

Filter: `kerberos.CNameString == "gwyatt" || samr.samr_UserInfo21.account_name == "gwyatt"`

Kerberos names gwyatt; the SAMR user-information response confirms the account.

## 286 — ACT 4 - LUMMA IN THE ROOM: Full User Name

Answer: **Gabriel Wyatt**

Capture: `2026-01-31-traffic-analysis-exercise.pcap`; Frames 358; TCP streams 8.

Filter: `samr.samr_UserInfo21.full_name`

The same SAMR UserInfo21 response pairs account gwyatt with full name Gabriel Wyatt. Preserve the space in the raw answer; the challenge does not specify underscore normalization.

## 287 — ACT 4 - LUMMA IN THE ROOM: Malicious Domain

Answer: **whitepepper.su**

Capture: `2026-01-31-traffic-analysis-exercise.pcap`; Frames 23723, 24500; TCP streams 99.

Filter: `dns.a == 153.92.1.49 || (ip.dst == 153.92.1.49 && http.request)`

DNS maps whitepepper.su to 153.92.1.49; HTTP Host confirms the same domain.

## 288 — ACT 4 - LUMMA IN THE ROOM: Fingerprint API

Answer: **/api/set_agent**

Capture: `2026-01-31-traffic-analysis-exercise.pcap`; Frames 24500, 24601, 25270, 25286; TCP streams 99, 111.

Filter: `ip.dst == 153.92.1.49 && http.request.uri contains "/api/set_agent"`

The API endpoint is /api/set_agent. Query strings supply victim ID, token, agent=Chrome/Edge, and optionally act=log; they are not part of the requested path.

## 289 — ACT 5 - FINAL INCIDENT: Map the Network

Answer: **10.3.14.131_10.3.14.134_10.3.14.135**

Capture: `2017-02-11-traffic-analysis-exercise.pcap`; Frames 6, 1684, 1771.

Filter: `ip.src == 10.3.14.131 || ip.src == 10.3.14.134 || ip.src == 10.3.14.135`

These three client IPv4 addresses are ordered numerically. The gateway is 10.3.14.1. Despite the question describing all three as Windows, .135 exhibits Apple/macOS traffic.

## 290 — ACT 5 - FINAL INCIDENT: Host One MAC

Answer: **00:25:64:18:4c:2a**

Capture: `2017-02-11-traffic-analysis-exercise.pcap`; Frames 1771.

Filter: `ip.src == 10.3.14.131`

Ethernet source on an IPv4 packet sent by 10.3.14.131.

## 291 — ACT 5 - FINAL INCIDENT: Host Two MAC

Answer: **14:da:e9:5b:42:1c**

Capture: `2017-02-11-traffic-analysis-exercise.pcap`; Frames 1684, 1712.

Filter: `ip.src == 10.3.14.134`

Ethernet source on packets from 10.3.14.134; DHCP also identifies this host as Knutson-PC.

## 292 — ACT 5 - FINAL INCIDENT: Host Three MAC

Answer: **00:26:bb:4c:6b:e1**

Capture: `2017-02-11-traffic-analysis-exercise.pcap`; Frames 6.

Filter: `ip.src == 10.3.14.135`

Ethernet source on a DNS query sent by 10.3.14.135.

## 293 — ACT 5 - FINAL INCIDENT: Find the Victims

Answer: **10.3.14.131_10.3.14.134**

Capture: `2017-02-11-traffic-analysis-exercise.pcap`; Frames 8820, 11043, 16762; TCP streams 179, 299.

Filter: `(ip.src == 10.3.14.131 && http.host == "spora.biz") || (ip.src == 10.3.14.134 && (http.host contains "p27dokhpz2n7nvgr" || udp.dstport == 6892))`

The .131 host accesses the Spora payment domain; .134 emits Cerber-pattern UDP/6892 traffic and visits the Cerber payment portal. These are the two infected endpoints in ascending order.

## 294 — ACT 5 - FINAL INCIDENT: First Ransomware

Answer: **Spora**

Capture: `2017-02-11-traffic-analysis-exercise.pcap`; Frames 16762, 16772, 16979; TCP streams 299.

Filter: `ip.src == 10.3.14.131 && http.host == "spora.biz"`

The first host accesses spora.biz, the ransomware-specific domain. The HTTP stream includes redirects and DDoS-Guard interstitials; those pages alone are not proof of executable delivery. Family attribution combines this ransomware-specific domain, the challenge's infection context, and primary Spora research.

## 295 — ACT 5 - FINAL INCIDENT: Second Ransomware

Answer: **Cerber**

Capture: `2017-02-11-traffic-analysis-exercise.pcap`; Frames 8820, 11043, 16354; TCP streams 179, 296.

Filter: `ip.src == 10.3.14.134 && (http.host contains "p27dokhpz2n7nvgr" || udp.dstport == 6892)`

UDP destination port 6892 and p27dokhpz2n7nvgr.1nmrtq.top match independently published Cerber post-infection behavior. The portal paths include a victim identifier, language selection, captcha, and bitcoin resources.

## 296 — ACT 5 - FINAL INCIDENT: Final Assessment

Answer: **10.3.14.135**

Capture: `2017-02-11-traffic-analysis-exercise.pcap`; Frames 6, 1350, 2055; TCP streams 8.

Filter: `ip.src == 10.3.14.135`

The third client exhibits ordinary Apple services and Reddit browsing, with neither ransomware-specific pattern attributed to .131 and .134. Clean means no observed evidence of infection in this capture, not a forensic guarantee about the endpoint.

## Standards and supporting research

- [TCP push semantics — RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html#section-3.9.1.2)
- [HTTP Basic authentication and TLS — RFC 7617](https://www.rfc-editor.org/rfc/rfc7617.html#section-1)
- [Prior ACT 4/5 report with primary ransomware and FormBook sources](../analysis-act4-act5/answers.md)

No reconstructed executables or scripts were run. All packet filters were executed successfully and every cited frame was checked against its filter. The EASY PACKET fields were also checked directly against the capture bytes.

## Evidence file hashes

- `EASY_PACKET_1.pcap` — SHA-256 `e4735559a704fcd56ac790602e875a713f94a665af16ecd3ad49ea40ff394faa`
- `ACT12026-08-09-traffic-analysis-exercise.pcap` — SHA-256 `0ea6b597732a9ce6af9a7e3adff4512c9a91b4bce27184c8fdeb746f05cce170`
- `2026-02-28-traffic-analysis-exercise.pcap` — SHA-256 `3dc470f5490ec15b4024c513e87c67e0b17caeae2a2ce3d83541be24ef407e61`
- `2024-07-30-traffic-analysis-exercise.pcap` — SHA-256 `c48854c24223cf7b4e9880ea72a21a877e4138e4ce36df7b7656e5c6c4043f68`
- `2026-01-31-traffic-analysis-exercise.pcap` — SHA-256 `f755444d0b6eac847e07b73dea0774084b232d8577f536547a12f39b959d7833`
- `2017-02-11-traffic-analysis-exercise.pcap` — SHA-256 `6971ca45f782265b10378d8331201b14704cd8525922fd89bb909fef3e788075`
