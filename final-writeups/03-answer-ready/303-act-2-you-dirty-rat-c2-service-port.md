# ACT 2 - YOU DIRTY RAT!: C2 Service Port

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 303 |
| Technical category | OSINT |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Recover the C2 service port for the STRRAT incident. |
| Result | `pcgCTF{12132}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

A victim may make many benign requests while infected. I restricted the packet selection to the known C2 address and the STRRAT marker, then read the destination port, not the client’s ephemeral source port.

## Working through the evidence

### 1. Bind the lookup to the supplied indicator

The starting indicator is `141.98.10.79`. Read the original question linked below first: it determines whether the answer is a family, domain, port, organization or year. These are different pivots even when they share a capture.

### 2. Check the source and preserve the decisive record

All102 matching outbound beacon packets use destination TCP 12132, including frame 9119. The firsthand public STRRAT analysis reports the same address and port. This directly supports12132 without guessing a default RAT port.

The observed source/record is preserved below. These are recorded verification results; the drafting pass does not claim a fresh successful website query or a new grader submission.

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/274-act-3-malware-investigation-compromised-endpoint/files/2024-07-30-traffic-analysis-exercise.pcap -Y 'ip.dst==141.98.10.79 && tcp contains "STRRAT"' -T fields -e frame.number -e ip.dst -e tcp.dstport
```

This offline reproduction uses `-r` to read the original capture, `-n` to suppress network name resolution, `-Y` for a display filter, and `-T fields` plus each `-e` to select the displayed packet fields. The filter binds the answer to the supplied IOC. Where present, `-d tcp.port==443,http` tells the dissector to interpret that stream as HTTP; it is a decoding choice, not a change to the stored traffic.

Recorded evidence excerpt (first lines, not a newly fabricated command response):

```text
frame.number	ip.dst	tcp.dstport	data.data
9119	141.98.10.79	12132	70696e677c5354525241547c31424538323932437c4445534b544f502d534b42523235467c63636f6c6c6965727c4d6963726f736f66742057696e646f77732031312050726f7c36342d6269747c57696e646f777320446566656e6465727c7c312e367c55533a556e69746564205374617465737c4e6f7420496e7374616c6c65647c3120536563
```

### 3. Interpret the result at the requested level

Ports are incident-specific configuration. Another STRRAT sample can use a different port, so keep the IOC and packet context attached to the number. The candidate below wraps the recorded answer using the format specified by this challenge; the supporting evidence does not itself prove platform acceptance.

Source: [https://securityposture.medium.com/traffic-analysis-of-strrat-malware-6b9c212c6ae6](https://securityposture.medium.com/traffic-analysis-of-strrat-malware-6b9c212c6ae6).

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #303 — actual evidence capture

![303-saved-evidence.png](../screenshots/303-saved-evidence.png)

Actual terminal inspection of preserved verification record, explicitly historical rather than a new external lookup. This reads preserved evidence; it is not a fresh external IOC lookup.

Command/action actually executed:

```sh
head -n 12 /home/nightingale/CTF/PCGCTF/analysis-team-verification/strrat-beacons.tsv
```

[Actual command transcript](../screenshots/capture-work/303-saved-record.terminal.log) · [Execution record](../screenshots/capture-work/303-saved-record.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{12132}`**. Ports are incident-specific configuration. Another STRRAT sample can use a different port, so keep the IOC and packet context attached to the number. Exact PCGCTF acceptance is not recorded.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

Ports are incident-specific configuration. Another STRRAT sample can use a different port, so keep the IOC and packet context attached to the number.

## Evidence and references

[Original archived challenge](../../unsolved/osint/303-act-2-you-dirty-rat-c2-service-port/README.md)

- [Decisive saved lookup / packet evidence](../../analysis-team-verification/strrat-beacons.tsv)
- [Original capture identities and extraction filters](../../analysis-team-verification/packet-checks.json)
- [Preserved investigation notes](../../unsolved/osint/303-act-2-you-dirty-rat-c2-service-port/solution.md)

**Provenance:** Rewritten from our independently checked original-capture/primary-source verification ledger; raw records linked and acceptance explicitly separated.
