<div align="center">

# PCGCTF — Team ChickenWings Archive

### A Fully Documented Capture-the-Flag Campaign: 175 Solves, Evidence-Backed Writeups

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Wireshark](https://img.shields.io/badge/Wireshark-tshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)](https://www.wireshark.org)
[![Burp Suite](https://img.shields.io/badge/Burp_Suite-Proxy-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white)](https://portswigger.net/burp)
[![OWASP Juice Shop](https://img.shields.io/badge/OWASP-Juice_Shop-000000?style=for-the-badge&logo=owasp&logoColor=white)](https://owasp.org/www-project-juice-shop/)
[![CTFd](https://img.shields.io/badge/CTFd-Platform-FF0000?style=for-the-badge&logo=flag&logoColor=white)](https://ctfd.io)

<br/>

**A complete working archive of a Philippine Cyber Guardians CTF run — every solved challenge, the commands that produced each answer, the packet and filesystem evidence behind it, and an honest account of what is still undocumented.**

[Coverage](#-coverage-at-a-glance) •
[Structure](#-repository-structure) •
[Categories](#-what-we-solved) •
[Toolchain](#-toolchain) •
[Navigating](#-navigating-the-archive) •
[Contributors](#-contributors)

</div>

---

## Project Overview

This repository is the full record of **Team ChickenWings** at [PCGCTF](https://cgcybercom.online/challenges). It is built to be read by someone who was not there:

1. **Preserves** the original challenge inventory — descriptions and attachments exactly as published
2. **Documents** each solve as a walkthrough with the real commands, filters and artifacts used
3. **Separates** what was verified from what is an evidence-backed but unconfirmed answer
4. **Admits** its own gaps, down to the individual challenge, in a generated audit

> **Why this matters:** A scoreboard screenshot proves a number. It does not teach anyone the method. This archive is the method — 198 drafts, 757 captured images and the raw analysis working sets that produced the answers.

---

## Coverage at a Glance

Audited 29 October 2026. The audit is generated from the solve list, not written by hand: see **[docs/coverage.md](docs/coverage.md)** for the challenge-by-challenge map.

| Metric | Result |
| --- | --- |
| **Problems solved** | **175** across 24 categories |
| **Points earned** | 63,025 (43,025 excluding one 20,000-point outlier) |
| **Solves with a writeup** | **167 of 175** |
| **Solves with no writeup** | **8** — enumerated below, nothing hidden |
| **Writeup drafts in total** | 199 (156 solved, 43 unsolved or unconfirmed) |
| **Captured evidence images** | 757 screenshots, plus 128 evidence artifacts |

### The 8 gaps

Stated plainly rather than rounded away:

- **2 Juice Shop solves** — *Error Handling* and *Score Board*. Solved live against the instance; never written up.
- **6 OSINT / IMINT solves** — the *Country*, *City*, *Street*, *Email*, *Photographer* and *Location* sub-answers. These were added to the scoreboard after the 28 October inventory snapshot, so no challenge folder or draft was ever created for them.

The four *Broken Anti Automation* solves were undocumented until 29 October 2026, when they were recovered from a loose bundle and written up in [writeups/solved/broken-anti-automation.md](writeups/solved/broken-anti-automation.md).

### A note on what "solved" means here

`writeups/solved/` and `challenges/solved/` follow the **team scoreboard**. Each individual draft carries its own verification status, and those statuses are deliberately not all the same:

| Status inside a draft | Meaning |
| --- | --- |
| Verified | A saved scoreboard state, or an independently re-checked authentication |
| Needs flag verification | The answer is evidence-supported; the submission string was never confirmed |
| Partial | The method is documented but an original artifact or exact wording is missing |

A draft filed under `solved/` is therefore a solved *problem*, not a claim that every command was re-run today. The distinction is kept on purpose — see [docs/writeup-index.md](docs/writeup-index.md).

---

## Repository Structure

```
fantastic-octo-lamp/
│
├── README.md                     # This file
│
├── 📂 writeups/                  # The walkthroughs
│   ├── 📂 solved/                #   155 drafts for scoreboard solves
│   ├── 📂 unsolved/              #   43 drafts: unconfirmed, rejected or open
│   ├── 📂 screenshots/           #   757 captured images, by challenge
│   ├── 📂 evidence/              #   Extracted artifacts backing the drafts
│   ├── 📂 evidence-solved/       #   Artifacts tied to confirmed solves
│   └── 📂 scripts/               #   Helper scripts used during capture
│
├── 📂 challenges/                # The preserved original inventory
│   ├── 📂 solved/                #   152 challenge folders + attachments
│   └── 📂 unsolved/              #   45 challenge folders + attachments
│
├── 📂 analysis/                  # Raw working sets that produced the answers
│   ├── 📂 network-forensics/     #   tshark exports, beacon tables, identities
│   ├── 📂 network-analysis/      #   Stream dumps, credential extractions
│   ├── 📂 act4-act5/             #   Lumma and ransomware act evidence
│   ├── 📂 blockchain-forensics/  #   Decoded transactions and wallets
│   ├── 📂 natas/                 #   Per-level verification records
│   └── 📂 team-verification/     #   Cross-checks and public-source lookups
│
├── 📂 docs/                      # Reports and indexes
│   ├── coverage.md               #   Generated solve-to-writeup audit
│   ├── writeup-index.md          #   Master index with per-draft status
│   ├── status.md                 #   Full status list for all challenges
│   ├── flags-ready.md            #   Answers ready for submission
│   ├── network-evidence.md       #   Packet and stream evidence index
│   ├── quality-report.md         #   Draft quality review
│   └── ...                       #   Editorial, visuals, missing-evidence reports
│
├── 📂 data/                      # Machine-readable records
│   ├── solved-list.txt           #   Scoreboard solves — the audit's input
│   ├── challenges.json           #   192-challenge inventory snapshot
│   ├── status.json               #   Structured status export
│   └── 📂 juice-shop/            #   Live Juice Shop inventory and scrape
│
├── 📂 scripts/                   # Archive maintenance
│   ├── audit_coverage.py         #   Regenerates docs/coverage.md
│   └── check_links.py            #   Fails if broken links increase
│
└── 📂 team/                      # Per-member working records
```

---

## What We Solved

| Category | Solves | Documented |
| --- | ---: | ---: |
| Network Forensics | 62 | 62 |
| Deadface | 25 | 25 |
| OSINT / IMINT | 17 | 11 |
| Cryptography | 13 | 13 |
| Web Exploitation — Natas | 11 | 11 |
| Vulnerable Components | 9 | 9 |
| OSINT | 8 | 8 |
| Network Analysis | 4 | 4 |
| Broken Anti-Automation | 4 | 4 |
| Insecure Deserialization | 3 | 3 |
| Steganography | 2 | 2 |
| XXE | 2 | 2 |
| Aurora Patient Zero | 2 | 2 |
| Blockchain / Forensics | 2 | 2 |
| General Skills | 2 | 2 |
| *Nine single-challenge categories* | 9 | 7 |
| **Total** | **175** | **167** |

Full per-category figures, including the exact missing entries, are in [docs/coverage.md](docs/coverage.md).

---

## Toolchain

<table>
<tr>
<th>Area</th>
<th>Tooling</th>
<th>Used for</th>
</tr>
<tr>
<td><b>Packet analysis</b></td>
<td>Wireshark / tshark</td>
<td>Field extraction, stream reassembly, beacon timing across five incident acts</td>
</tr>
<tr>
<td><b>Web exploitation</b></td>
<td>Burp Suite, curl</td>
<td>Request tampering, header and cookie manipulation, JWT forgery</td>
</tr>
<tr>
<td><b>Target application</b></td>
<td>OWASP Juice Shop</td>
<td>Vulnerable-component, XXE and deserialization tracks</td>
</tr>
<tr>
<td><b>Cryptanalysis</b></td>
<td>Python, CyberChef</td>
<td>Classical ciphers, multi-layer encodings, RSA small-exponent and common-modulus attacks</td>
</tr>
<tr>
<td><b>Forensics</b></td>
<td>Autopsy, binwalk, exiftool, sqlite3</td>
<td>Disk and registry artifacts, carved files, application databases</td>
</tr>
<tr>
<td><b>Steganography</b></td>
<td>zsteg, steghide, stegsolve</td>
<td>Embedded payloads and layered carriers</td>
</tr>
<tr>
<td><b>OSINT</b></td>
<td>WHOIS, RIPE, reverse image search, MalwareBazaar</td>
<td>Infrastructure pivots, malware attribution, image geolocation</td>
</tr>
<tr>
<td><b>Capture automation</b></td>
<td>Playwright</td>
<td>Reproducible screenshots of challenge and solve states</td>
</tr>
</table>

---

## Navigating the Archive

### Read a single solve

Start from the index and follow the link:

```bash
# Master index, grouped with per-draft verification status
less docs/writeup-index.md

# Or go straight to a challenge by its ID
ls writeups/solved/ | grep 262
cat writeups/solved/262-act-1-first-signal-patient-zero.md
```

Each draft follows the same shape: the challenge as published, the approach, the exact commands, the evidence, and the answer.

### Trace an answer back to its raw evidence

```bash
# The original challenge, exactly as it was published
cat challenges/solved/network-forensics/262-act-1-first-signal-patient-zero/README.md

# The working set the answer came from
ls analysis/network-forensics/
```

### Re-run the coverage audit

The audit is generated from [data/solved-list.txt](data/solved-list.txt), so it cannot silently drift from the scoreboard:

```bash
python scripts/audit_coverage.py           # rewrite docs/coverage.md
python scripts/audit_coverage.py --check   # non-zero exit if it is stale
```

Add a line to `data/solved-list.txt` for a new solve and the audit will name it as undocumented until a draft exists.

### Verify the documentation links

```bash
python scripts/check_links.py --max 48
```

48 relative links were already broken when the archive was reorganised on 29 October 2026 — mostly evidence artifacts that were never copied in. The `--max` ceiling holds that number so a future move cannot quietly add more. Run with `-v` to list them.

---

## Documentation Index

| Document | Contents |
| --- | --- |
| [docs/coverage.md](docs/coverage.md) | Generated audit: all 175 solves mapped to their writeup, gaps named |
| [docs/writeup-index.md](docs/writeup-index.md) | Master index of all 198 drafts with verification status |
| [docs/submission-log.md](docs/submission-log.md) | The nine flags the platform confirmed `correct`, and how they were submitted |
| [docs/status.md](docs/status.md) | Full status list across the 192-challenge snapshot |
| [docs/flags-ready.md](docs/flags-ready.md) | Answers ready for submission |
| [docs/network-evidence.md](docs/network-evidence.md) | Packet and stream evidence index |
| [docs/by-technical-category.md](docs/by-technical-category.md) | Drafts grouped by technique rather than scoreboard category |
| [docs/quality-report.md](docs/quality-report.md) | Draft quality review |
| [docs/missing-evidence.md](docs/missing-evidence.md) | Known gaps and remaining work |
| [docs/visuals.md](docs/visuals.md) | Captured visual evidence |

---

## Scope and Ethics

Every target in this archive is a deliberately vulnerable training system: the PCGCTF platform, OWASP Juice Shop, DVWA and OverTheWire Natas. Nothing here was run against a system we were not authorised to test.

Runtime credentials recovered during the OverTheWire levels are redacted in the published drafts. Downloaded archives were preserved without executing their contents. Third-party material from the original challenges is retained only as needed to explain a solve.

---

## Still Open

- [ ] **Write up *Error Handling* and *Score Board*** — the gap with the clearest fix; the instance work is already done
- [ ] **Recover the 6 late IMINT sub-answers** — needs the post-snapshot scoreboard state
- [ ] **Close the 48 pre-existing broken evidence links** — mostly artifacts that were never copied into the archive
- [ ] **Confirm submission strings** for drafts currently marked *needs flag verification*
- [ ] **Re-capture partial drafts** whose original artifacts were lost

---

## Contributors

<table>
<tr>
<td align="center">
<img src="https://github.com/2nieGarcia.png" width="100" style="border-radius: 50%"><br>
<b>Antonio B. Garcia Jr.</b><br>
<a href="https://github.com/2nieGarcia">@2nieGarcia</a><br>
<sub>Cryptography · Network forensics · Web exploitation</sub>
</td>
<td align="center">
<b>Mark Christian Anub</b><br>
<sub>Deadface · OSINT · Forensics</sub>
</td>
</tr>
</table>

---

<div align="center">

### Team ChickenWings

*Every answer here has a command behind it, and every gap here is named.*

</div>
