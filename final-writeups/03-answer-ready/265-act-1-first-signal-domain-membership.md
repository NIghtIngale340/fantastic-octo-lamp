# ACT 1 - FIRST SIGNAL: Domain Membership

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 265 |
| Category | Network Forensics |
| Points | 100 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Determine the Active Directory domain associated with the compromised workstation.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/265-act-1-first-signal-domain-membership/README.md). The supplied evidence is `ACT12026-08-09-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

A workstation’s hostname alone does not identify its Active Directory environment. Kerberos authentication requests expose the realm used with the machine account.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `0ea6b597732a9ce6af9a7e3adff4512c9a91b4bce27184c8fdeb746f05cce170`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
ip.addr == 172.16.8.49 && kerberos
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/262-act-1-first-signal-patient-zero/files/ACT12026-08-09-traffic-analysis-exercise.pcap \
  -Y '(ip.addr == 172.16.8.49 && kerberos) && frame.number in {1939, 1961}' \
  -T fields -E header=y -e frame.number -e ip.src -e kerberos.CNameString -e kerberos.realm
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	ip.src	kerberos.CNameString	kerberos.realm
1939	172.16.8.49	desktop-5nlv63k$	FIRSTTOLAST.TECH
1961	172.16.8.8	DESKTOP-5NLV63K$	FIRSTTOLAST.TECH
```

### 2. Interpret the result

The focused records show desktop-5nlv63k$ and realm FIRSTTOLAST.TECH. The trailing dollar sign identifies a computer account. This establishes the DNS/Kerberos realm; the short NetBIOS domain FIRSTTOLAST is a distinct representation of that environment.

### Keep the raw value separate from the submission

Kerberos realm `FIRSTTOLAST.TECH` and short NetBIOS domain `FIRSTTOLAST` are both useful, but answer different representations. Garcia’s recorded acceptance explains the selected short-name candidate; it does not invalidate the DNS realm. The DNS suffix is still required when constructing the FQDN in #266.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #265 — offline packet evidence

![265-decisive-evidence.png](../screenshots/265-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/262-act-1-first-signal-patient-zero/files/ACT12026-08-09-traffic-analysis-exercise.pcap -Y '(ip.addr == 172.16.8.49 && kerberos) && frame.number in {1939, 1961}' -T fields -E header=y -e frame.number -e ip.src -e kerberos.CNameString -e kerberos.realm
```

[Actual command transcript](../screenshots/capture-work/265-network.terminal.log) · [Execution record](../screenshots/capture-work/265-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{FIRSTTOLAST}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. Garcia’s Day 1 document explicitly reports this submission spelling accepted; it was not independently retested in our account. The observed DNS realm is FIRSTTOLAST.TECH, while the teammate-reported accepted short name is FIRSTTOLAST. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

Keep the DNS realm and short domain name separate. The correct captured realm can differ from the particular representation a grader accepts. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/265-act-1-first-signal-domain-membership/README.md)
- [Actual TShark field output](../evidence/network/265-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/265-act-1-first-signal-domain-membership/solution.md)

- [Garcia Day 1 report — attributed formatting/acceptance evidence](../../team-writeups/garcia-day1/source.md)
