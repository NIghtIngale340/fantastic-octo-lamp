# Team writeup comparison

**Follow-up:** all 21 additional candidates below have now been independently supported and merged into our candidate list. Sequence was corrected to `FLAG LANGUAGE`, adding a 22nd result. See the [verification report](analysis-team-verification/README.md) and [current status](STATUS.md). The comparison below records the state before that merge.

Compared 2026-10-28 against `STATUS.json` and saved local evidence.

Source: [Antonio B. Garcia Jr. — Potential Writeups](../POTENTIAL_WRITEUPS%28GARCIA%20V1%29.md). The source explicitly says every flag is a candidate and none has been submitted or accepted. Section headings saying “SOLVED” do not establish platform acceptance.

## Findings

- 28 distinct main candidate answers, excluding the explicitly weak Viral Name lead.
- 21 are additional candidates for challenges currently marked `needs_work` in our inventory.
- Five duplicate our saved answers: #61, #62, #69, #307 and #308.
- One repeats our rejected Rotation 36 submission (#18).
- One is explicitly speculative: Sequence (#79).
- Five of the 21 additional candidates have local evidence independently checked during this comparison; the exact limits are recorded below.
- This comparison does not change the solved list or promote unsubmitted candidates to accepted answers.

## Additional candidates from teammate

| ID | Challenge | Candidate | Comparison / verification |
|---|---|---|---|
| 297 | [ACT 1 - EASY AS 123: Threat Identity](unsolved/osint/297-act-1-easy-as-123-threat-identity/README.md) | `pcgCTF{NetSupport Manager RAT}` | Teammate candidate; exact expected malware name/wrapper not verified. |
| 298 | [ACT 1 - EASY AS 123: Domain Pivot](unsolved/osint/298-act-1-easy-as-123-domain-pivot/README.md) | `pcgCTF{vadusa.xyz}` | Teammate candidate; historical infrastructure attribution needs source verification. |
| 299 | [ACT 1 - EASY AS 123: Protocol Deception](unsolved/osint/299-act-1-easy-as-123-protocol-deception/README.md) | `pcgCTF{HTTP}` | Teammate candidate supported by their packet discussion; exact submission unverified. |
| 300 | [ACT 1 - EASY AS 123: Malware Hash Pivot](unsolved/osint/300-act-1-easy-as-123-malware-hash-pivot/README.md) | `pcgCTF{NetSupport}` | Teammate candidate; hash-to-family attribution and exact label need verification. |
| 301 | [ACT 2 - YOU DIRTY RAT!: Identify the RAT](unsolved/osint/301-act-2-you-dirty-rat-identify-the-rat/README.md) | `pcgCTF{STRRAT}` | Teammate candidate supported by their beacon discussion; unsubmitted. |
| 302 | [ACT 2 - YOU DIRTY RAT!: Infrastructure Owner](unsolved/osint/302-act-2-you-dirty-rat-infrastructure-owner/README.md) | `pcgCTF{UAB Host Baltic}` | Teammate candidate; provider versus organization/ASN wording needs verification. |
| 303 | [ACT 2 - YOU DIRTY RAT!: C2 Service Port](unsolved/osint/303-act-2-you-dirty-rat-c2-service-port/README.md) | `pcgCTF{12132}` | Teammate candidate supported by their packet discussion; unsubmitted. |
| 304 | [ACT 3 - LUMMA IN THE ROOM-AH!: Identify the Stealer](unsolved/osint/304-act-3-lumma-in-the-room-ah-identify-the-stealer/README.md) | `pcgCTF{Lumma Stealer}` | Teammate candidate; precise expected family spelling unverified. |
| 305 | [ACT 3 - LUMMA IN THE ROOM-AH!: Domain Pivot](unsolved/osint/305-act-3-lumma-in-the-room-ah-domain-pivot/README.md) | `pcgCTF{whitepepper.su}` | Teammate candidate supported by their packet discussion; unsubmitted. |
| 306 | [ACT 3 - LUMMA IN THE ROOM-AH!: Registration OSINT](unsolved/osint/306-act-3-lumma-in-the-room-ah-registration-osint/README.md) | `pcgCTF{2025}` | Teammate candidate; current registration can differ from historical registration. Verify relevant registration record. |
| 244 | [Airport Context — Building](unsolved/osint-imint/244-airport-context-building/README.md) | `pcgCTF{Vancouver International Airport}` | Teammate candidate; visible YVR branding is supporting evidence, not acceptance. |
| 247 | [Coffee Shop — City](unsolved/osint-imint/247-coffee-shop-city/README.md) | `pcgCTF{Blairgowrie}` | Teammate candidate derived from a Searchlight walkthrough; independently match the supplied image. |
| 253 | [Reverse Image — Editor](unsolved/osint-imint/253-reverse-image-editor/README.md) | `pcgCTF{Andrew Knowlton}` | Teammate candidate derived from a matching video/walkthrough; independently verify the image and requested role. |
| 254 | [Sculpture — Identification](unsolved/osint-imint/254-sculpture-identification/README.md) | `pcgCTF{Rudolph the Chrome Nosed Reindeer}` | Teammate candidate; artwork identification and exact title spelling need independent checking. |
| 256 | [Justice — Character](unsolved/osint-imint/256-justice-character/README.md) | `pcgCTF{Lady Justice}` | Teammate candidate; Lady Justice, Themis and Justitia may not be interchangeable to the grader. |
| 259 | [Hotel From the Past](unsolved/osint-imint/259-hotel-from-the-past/README.md) | `pcgCTF{Novotel Singapore Clarke Quay}` | Teammate candidate; distinguish the requested historical hotel name from later names. |
| 309 | [Info Leaks](unsolved/aurora-patient-zero/309-info-leaks/README.md) | `deadface{Mara-Voss-1988-04-17}` | Independently confirmed: original IPA Info.plist bootstrap decodes to patientName Mara Voss, dateOfBirth 1988-04-17. Flag formatting follows the challenge. |
| 310 | [Down the Rabbit Hole](unsolved/aurora-patient-zero/310-down-the-rabbit-hole/README.md) | `deadface{847261}` | Independently confirmed: original IPA chest X-ray XMP metadata contains dc:identifier PID-847261. |
| 312 | [Back to Basics](unsolved/aurora-patient-zero/312-back-to-basics/README.md) | `deadface{gw-westlake-int-03}` | Independently confirmed: gateway string exists in the original app executable. Hidden diagnostics screen was not run in this comparison. |
| 122 | [PCGCTF Juice Shop Gateway](unsolved/reconnaissance/122-pcgctf-juice-shop-gateway/README.md) | `pcgCTF{73dbb9f2bac263e70119eb5e22d79e029e03a27e}` | Recomputed HMAC-SHA1 of Score Board with the ASCII CTF_KEY in our supplied docker-compose.yml; matches teammate. This confirms the calculation, not the running app or platform acceptance. |
| 75 | [HIDDEN](unsolved/forensics/075-hidden/README.md) | `pcgCTF{me0w_hia!}` | Independently carved JPEG from original winsock32.dll at offset 294912, length 24023; visually read embedded flag{me0w_hia!}. pcgCTF wrapper remains a candidate. |

## Answers that agree

| ID | Challenge | Shared candidate |
|---|---|---|
| 61 | [The Exposed Password](unsolved/network-analysis/061-the-exposed-password/README.md) | `pcgCTF{John1234!}` |
| 62 | [THE HIDDEN DOWNLOAD](unsolved/network-analysis/062-the-hidden-download/README.md) | `pcgCTF{Cx689iO7Fu4G}` |
| 69 | [Bitcoin Trail](unsolved/network-analysis/069-bitcoin-trail/README.md) | `pcgCTF{bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh}` |
| 307 | [ACT 4 - FIRST TO LAST: Malware Attribution](unsolved/osint/307-act-4-first-to-last-malware-attribution/README.md) | `pcgCTF{FormBook}` |
| 308 | [ACT 4 - FIRST TO LAST: Infrastructure Pivot](unsolved/osint/308-act-4-first-to-last-infrastructure-pivot/README.md) | `pcgCTF{handyman24.eu}` |

These are agreement between writeups, not additional accepted solves.

## Disagreements and unresolved answers

| ID | Challenge | Comparison |
|---|---|---|
| 18 | Rotation 36 | Both recover `FLAG{CAESAR_SHIFT_19_ALNUM}` mathematically. The teammate proposes `pcgCTF{CAESAR_SHIFT_19_ALNUM}`, which was already rejected in our attempts. Keep `flag_rejected`; do not call it solved. |
| 57 | The Viral Name | Teammate explicitly lists Jhepoy Dizon as a weak lead. Your supplied screenshot directly shows **Renz Angeles** above the IP-address/anime comment. Our evidence-backed candidate is `pcgCTF{Renz Angeles}`; still not accepted. |
| 79 | Sequence | Teammate proposes `pcgCTF{FLAG FIBONACCI}` but says word two is unconfirmed. Their shown Fibonacci-position initials begin `FLAGI`, which does not establish `FLAG FIBONACCI`. Keep investigating. |
| 21 | Packet Detective | Teammate notes CRX and CA downloads; our writeup documents an FTP `RETR accountNum.zip` with actual ZIP transfer and candidate `pcgCTF{zip}`. Multiple file types occur in the capture, so the short question remains ambiguous. Our candidate is not definitive. |
| 67 | Weak RSA | Neither writeup has recovered the factors or a flag. Remains unsolved. |
| 77 / 74 | Hit a Brick Wall / Elliot’s Secret Stash | Teammate has investigation notes but no recovered flags; our inventory also remains unresolved. |
| 261 | Password Hash Leak | No completed solution in either compared source. |

## Completed local work missing from teammate’s document

| ID / group | Our saved result |
|---|---|
| 22 — FTP Credential Leak | `pcgCTF{AfricaCTF2021}`. Credentials recovered from the shared #21 capture; teammate says local evidence is missing. |
| 73 — BAD BLOCKCHAIN | Raw answer `192.168.200.48`, derived from on-chain output values. Teammate has no recovered answer. |
| 80 — TO THE MOON! | Recovered on-chain `flag{Inf0S3cBl0ckch41nAn4lys15}`; platform-format candidate `pcgCTF{Inf0S3cBl0ckch41nAn4lys15}`. Teammate lists it as unfinished. |
| 57 — The Viral Name | Screenshot-backed Renz Angeles identification, as explained above. |
| Network Forensics | Our analysis covers all 38 originally unsolved challenges: 36 flag candidates and two conceptual answers (#102 and #112) whose exact accepted wording is unresolved. Teammate’s IOC pivots are separate OSINT questions and should not replace these network answers. |
| Natas | Our 11 levels have credentials verified against the next live OverTheWire level. These are locally verified solves, separate from acceptance on PCGCTF. |

See [Network Forensics](analysis-network-forensics/answers.md), [Network Analysis](analysis-network-analysis/answers.md), [Blockchain](analysis-blockchain-forensics/answers.md), and [Natas verification](analysis-natas/verification.md).

## Current inventory remains unchanged

| State | Count |
|---|---:|
| Solved in saved PCGCTF scoreboard snapshot | 81 |
| Independently verified Natas solves | 11 |
| Flag candidates ready | 46 |
| Answer known; exact submission unresolved | 2 |
| Rejected flag candidate | 1 |
| Needs work | 51 |
| Total | 192 |

The 21 new teammate candidates overlap the 51 needs-work entries. They are not 21 extra accepted solves. A later merge should preserve their provenance and verification limits, save individual solutions, and update candidate status separately from scoreboard acceptance.
