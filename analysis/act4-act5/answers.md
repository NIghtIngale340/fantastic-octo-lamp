# ACT 4 and ACT 5 answers

17 answers recovered: 7 ACT 4 network-forensics questions, 8 ACT 5 network-forensics questions, and 2 ACT 4 OSINT questions.

**Validation status:** The site returned `PCGCTF is paused` when the evidence-backed victim IP flag was submitted. No acceptance was confirmed and no other answer was submitted. Flag strings below follow the supplied `pcgCTF{...}` format; exact case/space normalization remains unvalidated. Original archive solved/unsolved statuses are preserved.

All network-forensics answers were derived from the local captures. Public research was used for malware-family attribution and the explicitly requested OSINT pivots. No reconstructed payload was executed.

| ID | Challenge | Answer | Flag to submit | Evidence |
| ---: | --- | --- | --- | --- |
| 282 | [ACT 4 - LUMMA IN THE ROOM: Lumma Victim](../../challenges/solved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/solution.md) | `10.1.21.58` | `pcgCTF{10.1.21.58}` | Frames 24500, 25270; TCP streams 99, 111 |
| 283 | [ACT 4 - LUMMA IN THE ROOM: Victim MAC](../../challenges/solved/network-forensics/283-act-4-lumma-in-the-room-victim-mac/solution.md) | `00:21:5d:c8:0e:f2` | `pcgCTF{00:21:5d:c8:0e:f2}` | Frames 24500; TCP streams 99 |
| 284 | [ACT 4 - LUMMA IN THE ROOM: Victim Hostname](../../challenges/solved/network-forensics/284-act-4-lumma-in-the-room-victim-hostname/solution.md) | `DESKTOP-ES9F3ML` | `pcgCTF{DESKTOP-ES9F3ML}` | Frames 1, 2, 3, 4, 5 |
| 285 | [ACT 4 - LUMMA IN THE ROOM: Compromised User](../../challenges/solved/network-forensics/285-act-4-lumma-in-the-room-compromised-user/solution.md) | `gwyatt` | `pcgCTF{gwyatt}` | Frames 214, 358; TCP streams 4, 8 |
| 286 | [ACT 4 - LUMMA IN THE ROOM: Full User Name](../../challenges/solved/network-forensics/286-act-4-lumma-in-the-room-full-user-name/solution.md) | `Gabriel Wyatt` | `pcgCTF{Gabriel Wyatt}` | Frames 358; TCP streams 8 |
| 287 | [ACT 4 - LUMMA IN THE ROOM: Malicious Domain](../../challenges/solved/network-forensics/287-act-4-lumma-in-the-room-malicious-domain/solution.md) | `whitepepper.su` | `pcgCTF{whitepepper.su}` | Frames 23723, 24500; TCP streams 99 |
| 288 | [ACT 4 - LUMMA IN THE ROOM: Fingerprint API](../../challenges/solved/network-forensics/288-act-4-lumma-in-the-room-fingerprint-api/solution.md) | `/api/set_agent` | `pcgCTF{/api/set_agent}` | Frames 24500, 24601, 25270, 25286; TCP streams 99, 111 |
| 289 | [ACT 5 - FINAL INCIDENT: Map the Network](../../challenges/solved/network-forensics/289-act-5-final-incident-map-the-network/solution.md) | `10.3.14.131_10.3.14.134_10.3.14.135` | `pcgCTF{10.3.14.131_10.3.14.134_10.3.14.135}` | Frames 6, 1684, 1771 |
| 290 | [ACT 5 - FINAL INCIDENT: Host One MAC](../../challenges/solved/network-forensics/290-act-5-final-incident-host-one-mac/solution.md) | `00:25:64:18:4c:2a` | `pcgCTF{00:25:64:18:4c:2a}` | Frames 1771 |
| 291 | [ACT 5 - FINAL INCIDENT: Host Two MAC](../../challenges/solved/network-forensics/291-act-5-final-incident-host-two-mac/solution.md) | `14:da:e9:5b:42:1c` | `pcgCTF{14:da:e9:5b:42:1c}` | Frames 1684, 1712 |
| 292 | [ACT 5 - FINAL INCIDENT: Host Three MAC](../../challenges/solved/network-forensics/292-act-5-final-incident-host-three-mac/solution.md) | `00:26:bb:4c:6b:e1` | `pcgCTF{00:26:bb:4c:6b:e1}` | Frames 6 |
| 293 | [ACT 5 - FINAL INCIDENT: Find the Victims](../../challenges/solved/network-forensics/293-act-5-final-incident-find-the-victims/solution.md) | `10.3.14.131_10.3.14.134` | `pcgCTF{10.3.14.131_10.3.14.134}` | Frames 8820, 11043, 16762; TCP streams 179, 299 |
| 294 | [ACT 5 - FINAL INCIDENT: First Ransomware](../../challenges/solved/network-forensics/294-act-5-final-incident-first-ransomware/solution.md) | `Spora` | `pcgCTF{Spora}` | Frames 16762, 16772, 16979; TCP streams 299 |
| 295 | [ACT 5 - FINAL INCIDENT: Second Ransomware](../../challenges/solved/network-forensics/295-act-5-final-incident-second-ransomware/solution.md) | `Cerber` | `pcgCTF{Cerber}` | Frames 8820, 11043, 16354; TCP streams 179, 296 |
| 296 | [ACT 5 - FINAL INCIDENT: Final Assessment](../../challenges/solved/network-forensics/296-act-5-final-incident-final-assessment/solution.md) | `10.3.14.135` | `pcgCTF{10.3.14.135}` | Frames 6, 1350, 2055; TCP streams 8 |
| 307 | [ACT 4 - FIRST TO LAST: Malware Attribution](../../challenges/unsolved/osint/307-act-4-first-to-last-malware-attribution/solution.md) | `FormBook` | `pcgCTF{FormBook}` | Frames 11227, 11714, 21874; TCP streams 242, 249, 421 |
| 308 | [ACT 4 - FIRST TO LAST: Infrastructure Pivot](../../challenges/solved/osint/308-act-4-first-to-last-infrastructure-pivot/solution.md) | `handyman24.eu` | `pcgCTF{handyman24.eu}` | Public DNS/question evidence |

## Evidence and filters

### 282 — ACT 4 - LUMMA IN THE ROOM: Lumma Victim

Answer: `10.1.21.58`

Filter: `ip.dst == 153.92.1.49 && http.request`

The source of both Chrome and Edge victim-fingerprinting requests is 10.1.21.58.

### 283 — ACT 4 - LUMMA IN THE ROOM: Victim MAC

Answer: `00:21:5d:c8:0e:f2`

Filter: `ip.src == 10.1.21.58 && ip.dst == 153.92.1.49`

Ethernet source address on the infected host's C2 request.

### 284 — ACT 4 - LUMMA IN THE ROOM: Victim Hostname

Answer: `DESKTOP-ES9F3ML`

Filter: `dhcp || (nbns && eth.src == 00:21:5d:c8:0e:f2)`

DHCP Host Name is DESKTOP-ES9F3ML; DHCP offers/acknowledges 10.1.21.58. NBNS independently advertises the same hostname.

### 285 — ACT 4 - LUMMA IN THE ROOM: Compromised User

Answer: `gwyatt`

Filter: `kerberos.CNameString == "gwyatt" || samr.samr_UserInfo21.account_name == "gwyatt"`

Kerberos names gwyatt; the SAMR user-information response confirms the account.

### 286 — ACT 4 - LUMMA IN THE ROOM: Full User Name

Answer: `Gabriel Wyatt`

Filter: `samr.samr_UserInfo21.full_name`

The same SAMR UserInfo21 response pairs account gwyatt with full name Gabriel Wyatt. Preserve the space in the raw answer; the challenge does not specify underscore normalization.

### 287 — ACT 4 - LUMMA IN THE ROOM: Malicious Domain

Answer: `whitepepper.su`

Filter: `dns.a == 153.92.1.49 || (ip.dst == 153.92.1.49 && http.request)`

DNS maps whitepepper.su to 153.92.1.49; HTTP Host confirms the same domain.

### 288 — ACT 4 - LUMMA IN THE ROOM: Fingerprint API

Answer: `/api/set_agent`

Filter: `ip.dst == 153.92.1.49 && http.request.uri contains "/api/set_agent"`

The API endpoint is /api/set_agent. Query strings supply victim ID, token, agent=Chrome/Edge, and optionally act=log; they are not part of the requested path.

### 289 — ACT 5 - FINAL INCIDENT: Map the Network

Answer: `10.3.14.131_10.3.14.134_10.3.14.135`

Filter: `ip.src == 10.3.14.131 || ip.src == 10.3.14.134 || ip.src == 10.3.14.135`

These three client IPv4 addresses are ordered numerically. The gateway is 10.3.14.1. Despite the question describing all three as Windows, .135 exhibits Apple/macOS traffic.

### 290 — ACT 5 - FINAL INCIDENT: Host One MAC

Answer: `00:25:64:18:4c:2a`

Filter: `ip.src == 10.3.14.131`

Ethernet source on an IPv4 packet sent by 10.3.14.131.

### 291 — ACT 5 - FINAL INCIDENT: Host Two MAC

Answer: `14:da:e9:5b:42:1c`

Filter: `ip.src == 10.3.14.134`

Ethernet source on packets from 10.3.14.134; DHCP also identifies this host as Knutson-PC.

### 292 — ACT 5 - FINAL INCIDENT: Host Three MAC

Answer: `00:26:bb:4c:6b:e1`

Filter: `ip.src == 10.3.14.135`

Ethernet source on a DNS query sent by 10.3.14.135.

### 293 — ACT 5 - FINAL INCIDENT: Find the Victims

Answer: `10.3.14.131_10.3.14.134`

Filter: `(ip.src == 10.3.14.131 && http.host == "spora.biz") || (ip.src == 10.3.14.134 && (http.host contains "p27dokhpz2n7nvgr" || udp.dstport == 6892))`

The .131 host accesses the Spora payment domain; .134 emits Cerber-pattern UDP/6892 traffic and visits the Cerber payment portal. These are the two infected endpoints in ascending order.

### 294 — ACT 5 - FINAL INCIDENT: First Ransomware

Answer: `Spora`

Filter: `ip.src == 10.3.14.131 && http.host == "spora.biz"`

The first host accesses spora.biz, the ransomware-specific domain. The HTTP stream includes redirects and DDoS-Guard interstitials; those pages alone are not proof of executable delivery. Family attribution combines this ransomware-specific domain, the challenge's infection context, and primary Spora research.

### 295 — ACT 5 - FINAL INCIDENT: Second Ransomware

Answer: `Cerber`

Filter: `ip.src == 10.3.14.134 && (http.host contains "p27dokhpz2n7nvgr" || udp.dstport == 6892)`

UDP destination port 6892 and p27dokhpz2n7nvgr.1nmrtq.top match independently published Cerber post-infection behavior. The portal paths include a victim identifier, language selection, captcha, and bitcoin resources.

### 296 — ACT 5 - FINAL INCIDENT: Final Assessment

Answer: `10.3.14.135`

Filter: `ip.src == 10.3.14.135`

The third client exhibits ordinary Apple services and Reddit browsing, with neither ransomware-specific pattern attributed to .131 and .134. Clean means no observed evidence of infection in this capture, not a forensic guarantee about the endpoint.

### 307 — ACT 4 - FIRST TO LAST: Malware Attribution

Answer: `FormBook`

Filter: `ip.dst == 146.59.71.167 && http.request`

The FIRST TO LAST capture shows short-path POST requests and GET check-ins to /irpw/ with 2kn1=..., Connection: close, no Referer, and the fixed Firefox/39.0 User-Agent. This matches the structure of official ET Open FormBook signature SID 2050745. The rule was inspected and matched structurally; an IDS engine was not run. Public report corroboration is listed below. Do not infer a malware family solely from a shared hosting IP.

### 308 — ACT 4 - FIRST TO LAST: Infrastructure Pivot

Answer: `handyman24.eu`

Filter: `dns.qry.name == "handyman24.eu"`

The question explicitly specifies this domain. A live public DNS lookup also returned 146.59.71.167. This is the requested public DNS pivot, while the captured C2 HTTP Host is www.grinswakebthu.info; shared IP hosting does not mean all hosted sites are malicious.

## Source captures

- `ACT12026-08-09-traffic-analysis-exercise.pcap` — SHA-256 `0ea6b597732a9ce6af9a7e3adff4512c9a91b4bce27184c8fdeb746f05cce170`
- `2026-01-31-traffic-analysis-exercise.pcap` — SHA-256 `f755444d0b6eac847e07b73dea0774084b232d8577f536547a12f39b959d7833`
- `2017-02-11-traffic-analysis-exercise.pcap` — SHA-256 `6971ca45f782265b10378d8331201b14704cd8525922fd89bb909fef3e788075`

## Public research and OSINT sources

- [FormBook official ET Open signature](https://rules.emergingthreats.net/open/suricata-7.0/rules/emerging-malware.rules)
- [FormBook firsthand investigation and matching C2 IOC](https://github.com/chadibazzi/wireshark-formbook-soc-investigation)
- [Cerber firsthand network research](https://isc.sans.edu/diary/Blank%2BSlate%2Bmalspam%2Bstill%2Bpushing%2BCerber%2Bransomware/22215/)
- [Spora primary malware analysis](https://www.malwarebytes.com/blog/news/2017/03/spora-ransomware)
- [Google public DNS result](https://dns.google/resolve?name=handyman24.eu&type=A)

Packet numbers and TCP stream indices refer to the exact captures above. Supporting TSV files and text stream reconstructions are saved beside this report.
