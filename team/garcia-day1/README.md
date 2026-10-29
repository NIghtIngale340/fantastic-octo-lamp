# Garcia Day 1 — imported writeups

Imported: 2026-10-28T23:44:01+08:00. Author: Antonio B. Garcia Jr. Original source preserved byte-for-byte in [source.md](source.md).

**58 previously missing flag/writeup records saved** for challenges already solved in our scoreboard snapshot. Eight existing candidate spellings were corrected from the teammate’s explicit acceptance reports. No new site submissions were made, and no teammate acceptance claim was substituted for our saved scoreboard state.

## Important corrections and distinctions

- Read the actual question before wrapping table values: #87 asks for **IPv4**, #93 asks for **TCP**, and #266 asks for the FQDN **DESKTOP-5NLV63K.firsttolast.tech**. The table’s raw EtherType, numeric IP protocol and bare hostname are not the requested answers.

- EASY PACKET MAC candidates use uppercase letters and dashes; byte counts include “bytes”; IP ID is decimal; flags use “PSH and ACK”; credentials use `usertest/password`.
- Domain Membership uses `pcgCTF{FIRSTTOLAST}` per the teammate’s reported acceptance; captured DNS realm remains FIRSTTOLAST.TECH.
- Capture format is classic pcap, but the teammate reports `pcap` and related strings rejected. #83 moved from flag_ready to answer_only; no accepted spelling has been invented.
- Two Places at Once: database username is `kbhatt`; reported accepted flag is `deadface{kbhat}`. This spelling distinction is retained.
- ACT 3 User Identity remains Clark Collier: our saved LDAP frames 9759/10317 and SAMR frame 1070 contradict the teammate’s claim that the name is unrecoverable.
- Commitment Issues: recovered original `picoCTF{s@n1t1z3_be3dd3da}` from the original archive’s Git blob, filling the missing flag in the teammate’s method. Source prefix is preserved because the challenge does not specify another one.
- Independently reproduced Silent Signal, Base Maze, Multi-Base Layers, Hooked and SQL Skillz from original local files. Carnaby Street was independently read from the original image. [Local checks](independent-checks.json).
- Public-writeup-derived flags and intended methods are attributed to Garcia; they were not all independently reproduced in this import.
- [Signals from the Skull](unmapped-signals-from-the-skull.md) has no matching title/ID in our 192-challenge snapshot; saved separately rather than inventing an inventory entry.

## Newly saved records

| ID | Challenge | Flag / candidate | Solution |
|---:|---|---|---|
| 5 | Silent Signal | `pcgCTF{CYBER_SECURITY_IS_EVERYONES_RESPONSIBILITY}` | [Solution](../../challenges/solved/cryptography/005-silent-signal/solution.md) |
| 20 | Base Maze | `pcgCTF{ilove_Cyber_Command}` | [Solution](../../challenges/solved/cryptography/020-base-maze/solution.md) |
| 33 | Multi-Base Layers | `pcgCTF{ilove_Cyber_Command}` | [Solution](../../challenges/solved/cryptography/033-multi-base-layers/solution.md) |
| 36 | Commitment Issues | `picoCTF{s@n1t1z3_be3dd3da}` | [Solution](../../challenges/solved/general-skills/036-commitment-issues/solution.md) |
| 84 | EASY PACKET 1 #02  One Packet Wonder | `pcgCTF{1}` | [Solution](../../challenges/solved/network-forensics/084-easy-packet-1-02-one-packet-wonder/solution.md) |
| 87 | EASY PACKET 1 #05  EtherType: IPv4 | `pcgCTF{IPv4}` | [Solution](../../challenges/solved/network-forensics/087-easy-packet-1-05-ethertype-ipv4/solution.md) |
| 88 | EASY PACKET 1 #06  Version Four | `pcgCTF{4}` | [Solution](../../challenges/solved/network-forensics/088-easy-packet-1-06-version-four/solution.md) |
| 92 | EASY PACKET 1 #10  TTL: 64 Hops | `pcgCTF{64}` | [Solution](../../challenges/solved/network-forensics/092-easy-packet-1-10-ttl-64-hops/solution.md) |
| 93 | EASY PACKET 1 #11  Protocol 6 | `pcgCTF{TCP}` | [Solution](../../challenges/solved/network-forensics/093-easy-packet-1-11-protocol-6/solution.md) |
| 94 | EASY PACKET 1 #12  Who Sent It? | `pcgCTF{128.222.228.85}` | [Solution](../../challenges/solved/network-forensics/094-easy-packet-1-12-who-sent-it/solution.md) |
| 95 | EASY PACKET 1 #13  Where Is It Going? | `pcgCTF{128.121.146.100}` | [Solution](../../challenges/solved/network-forensics/095-easy-packet-1-13-where-is-it-going/solution.md) |
| 96 | EASY PACKET 1 #14  Ephemeral Source | `pcgCTF{55872}` | [Solution](../../challenges/solved/network-forensics/096-easy-packet-1-14-ephemeral-source/solution.md) |
| 97 | EASY PACKET 1 #15  Port 80 | `pcgCTF{80}` | [Solution](../../challenges/solved/network-forensics/097-easy-packet-1-15-port-80/solution.md) |
| 98 | EASY PACKET 1 #16  TCP Sequence Marker | `pcgCTF{3111702488}` | [Solution](../../challenges/solved/network-forensics/098-easy-packet-1-16-tcp-sequence-marker/solution.md) |
| 99 | EASY PACKET 1 #17  TCP Acknowledgment Marker | `pcgCTF{1790813139}` | [Solution](../../challenges/solved/network-forensics/099-easy-packet-1-17-tcp-acknowledgment-marker/solution.md) |
| 101 | EASY PACKET 1 #19  TCP Window | `pcgCTF{33088}` | [Solution](../../challenges/solved/network-forensics/101-easy-packet-1-19-tcp-window/solution.md) |
| 104 | EASY PACKET 1 #22  GET the Resource | `pcgCTF{GET}` | [Solution](../../challenges/solved/network-forensics/104-easy-packet-1-22-get-the-resource/solution.md) |
| 105 | EASY PACKET 1 #23  The Requested Path | `pcgCTF{/statuses/replies.xml}` | [Solution](../../challenges/solved/network-forensics/105-easy-packet-1-23-the-requested-path/solution.md) |
| 106 | EASY PACKET 1 #24  HTTP/1.1 | `pcgCTF{HTTP/1.1}` | [Solution](../../challenges/solved/network-forensics/106-easy-packet-1-24-http-1-1/solution.md) |
| 107 | EASY PACKET 1 #25  Know Your Host | `pcgCTF{twitter.com}` | [Solution](../../challenges/solved/network-forensics/107-easy-packet-1-25-know-your-host/solution.md) |
| 108 | EASY PACKET 1 #26  Identify the Client | `pcgCTF{CFNetwork/330}` | [Solution](../../challenges/solved/network-forensics/108-easy-packet-1-26-identify-the-client/solution.md) |
| 109 | EASY PACKET 1 #27  Keep the Connection | `pcgCTF{keep-alive}` | [Solution](../../challenges/solved/network-forensics/109-easy-packet-1-27-keep-the-connection/solution.md) |
| 110 | EASY PACKET 1 #28  Basic Authentication | `pcgCTF{Basic}` | [Solution](../../challenges/solved/network-forensics/110-easy-packet-1-28-basic-authentication/solution.md) |
| 239 | Street-Level Clue | `pcgCTF{Carnaby Street}` | [Solution](../../challenges/solved/osint-imint/239-street-level-clue/solution.md) |
| 262 | ACT 1 - FIRST SIGNAL: Patient Zero | `pcgCTF{172.16.8.49}` | [Solution](../../challenges/solved/network-forensics/262-act-1-first-signal-patient-zero/solution.md) |
| 263 | ACT 1 - FIRST SIGNAL: Hardware Fingerprint | `pcgCTF{00:12:f0:28:d4:34}` | [Solution](../../challenges/solved/network-forensics/263-act-1-first-signal-hardware-fingerprint/solution.md) |
| 264 | ACT 1 - FIRST SIGNAL: Name the Host | `pcgCTF{DESKTOP-5NLV63K.firsttolast.tech}` | [Solution](../../challenges/solved/network-forensics/264-act-1-first-signal-name-the-host/solution.md) |
| 266 | ACT 1 - FIRST SIGNAL: Full Identity | `pcgCTF{DESKTOP-5NLV63K.firsttolast.tech}` | [Solution](../../challenges/solved/network-forensics/266-act-1-first-signal-full-identity/solution.md) |
| 268 | ACT 2 - THE COMPROMISE: Infected IPV4 | `pcgCTF{10.2.28.88}` | [Solution](../../challenges/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/solution.md) |
| 269 | ACT 2 - THE COMPROMISE: VICTIM MAC | `pcgCTF{00:19:d1:b2:4d:ad}` | [Solution](../../challenges/solved/network-forensics/269-act-2-the-compromise-victim-mac/solution.md) |
| 270 | ACT 2 - THE COMPROMISE: VICTIM HOSTNAME | `pcgCTF{DESKTOP-TEYQ2NR}` | [Solution](../../challenges/solved/network-forensics/270-act-2-the-compromise-victim-hostname/solution.md) |
| 271 | ACT 2 - THE COMPROMISE: Identify the User -User Account | `pcgCTF{brolf}` | [Solution](../../challenges/solved/network-forensics/271-act-2-the-compromise-identify-the-user-user-account/solution.md) |
| 311 | SQL Skillz | `deadface{Candesartan}` | [Solution](../../challenges/solved/aurora-patient-zero/311-sql-skillz/solution.md) |
| 313 | Ghost of Squares Past | `deadface{1733-1742-1815-1733-gordon}` | [Solution](../../challenges/solved/deadface/313-ghost-of-squares-past/solution.md) |
| 315 | Bedside Manner | `deadface{v13w_s0urc3_sav3s_l1v3s}` | [Solution](../../challenges/solved/deadface/315-bedside-manner/solution.md) |
| 316 | Factory Setting | `deadface{d3fault_cr3ds_n3v3r_ch4ng3d}` | [Solution](../../challenges/solved/deadface/316-factory-setting/solution.md) |
| 317 | Second Opinion | `deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}` | [Solution](../../challenges/solved/deadface/317-second-opinion/solution.md) |
| 318 | Live Boot | `deadface{h4rdc0d3d_k3ys_1n_th3_c0nf1g}` | [Solution](../../challenges/solved/deadface/318-live-boot/solution.md) |
| 319 | Car Crash | `deadface{08_10_1961}` | [Solution](../../challenges/solved/deadface/319-car-crash/solution.md) |
| 320 | Hooked | `deadface{http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc}` | [Solution](../../challenges/solved/deadface/320-hooked/solution.md) |
| 321 | Art Heist: The Forgery | `deadface{L4MIA_SIGNS_HER_WORK}` | [Solution](../../challenges/solved/deadface/321-art-heist-the-forgery/solution.md) |
| 322 | Hard Kept Secrets | `deadface{zqJRlVwBA9Xm2lE5EPjgbj/4rOxlkYZgDtkdP7jV80rZgLFrlnOEn+VAu31YKQrR}` | [Solution](../../challenges/solved/deadface/322-hard-kept-secrets/solution.md) |
| 323 | Inside Man | `deadface{l3FT_b3Hind!}` | [Solution](../../challenges/solved/deadface/323-inside-man/solution.md) |
| 325 | Diagnosis | `deadface{flaG_ManIfesT3d}` | [Solution](../../challenges/solved/deadface/325-diagnosis/solution.md) |
| 326 | Admitted Under Another Name | `deadface{AH-0044719}` | [Solution](../../challenges/solved/deadface/326-admitted-under-another-name/solution.md) |
| 327 | Schedule of Concern | `deadface{9}` | [Solution](../../challenges/solved/deadface/327-schedule-of-concern/solution.md) |
| 328 | The Attending | `deadface{mreyes}` | [Solution](../../challenges/solved/deadface/328-the-attending/solution.md) |
| 329 | Prying Eyes | `deadface{rborden}` | [Solution](../../challenges/solved/deadface/329-prying-eyes/solution.md) |
| 330 | The Original Reading | `deadface{2.3}` | [Solution](../../challenges/solved/deadface/330-the-original-reading/solution.md) |
| 331 | Heavy Hand | `deadface{BR2938471}` | [Solution](../../challenges/solved/deadface/331-heavy-hand/solution.md) |
| 332 | Upon the Throne | `deadface{REVENANT-7}` | [Solution](../../challenges/solved/deadface/332-upon-the-throne/solution.md) |
| 333 | After the Lock | `deadface{VELT-0137}` | [Solution](../../challenges/solved/deadface/333-after-the-lock/solution.md) |
| 334 | Ghost in the Registry | `deadface{AH-0090001}` | [Solution](../../challenges/solved/deadface/334-ghost-in-the-registry/solution.md) |
| 335 | Too Good to be True | `deadface{VELT-0148}` | [Solution](../../challenges/solved/deadface/335-too-good-to-be-true/solution.md) |
| 336 | Two Places at Once | `deadface{kbhat}` | [Solution](../../challenges/solved/deadface/336-two-places-at-once/solution.md) |
| 337 | Cereal Killer 04 | `deadface{Before_Consenting_to_Med_Exam_Ascertain_Destination_of_Finger!}` | [Solution](../../challenges/solved/deadface/337-cereal-killer-04/solution.md) |
| 338 | Headshot | `deadface{b00m_h34Dsh0TTT}` | [Solution](../../challenges/solved/deadface/338-headshot/solution.md) |
| 339 | File Dump 01 | `deadface{gh0st404}` | [Solution](../../challenges/solved/deadface/339-file-dump-01/solution.md) |

## Candidate-format changes

| ID | Previous candidate | Updated candidate |
|---:|---|---|
| 85 | `pcgCTF{00:d0:bc:eb:e0:80}` | `pcgCTF{00-D0-BC-EB-E0-80}` |
| 86 | `pcgCTF{00:1b:63:94:b1:0e}` | `pcgCTF{00-1B-63-94-B1-0E}` |
| 89 | `pcgCTF{20}` | `pcgCTF{20 bytes}` |
| 90 | `pcgCTF{504}` | `pcgCTF{504 bytes}` |
| 91 | `pcgCTF{0xbed2}` | `pcgCTF{48850}` |
| 100 | `pcgCTF{PSH_ACK}` | `pcgCTF{PSH and ACK}` |
| 111 | `pcgCTF{usertest:password}` | `pcgCTF{usertest/password}` |
| 265 | `pcgCTF{FIRSTTOLAST.TECH}` | `pcgCTF{FIRSTTOLAST}` |

**Current inventory:** 81 PCGCTF snapshot solves + 11 verified Natas = 92 solved records; 68 candidates ready, 3 answers needing exact phrasing, 1 rejected candidate, 28 needing work. Total remains 192.

[Current categorized status](../../docs/status.md) · [Ready candidates](../../docs/flags-ready.md) · [Machine-readable import report](import-report.json)
