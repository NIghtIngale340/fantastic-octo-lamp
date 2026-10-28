# ACT 3 - LUMMA IN THE ROOM-AH!: Domain Pivot

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 305 |
| Technical category | OSINT |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Identify the domain used by the malicious C2. |
| Result | `pcgCTF{whitepepper.su}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

DNS can associate names with addresses, while the HTTP Host field identifies which virtual host a request targets. A domain attached to the actual C2 request is more useful than every name ever hosted at that IP.

## Working through the evidence

### 1. Bind the lookup to the supplied indicator

The starting indicator is `153.92.1.49`. Read the original question linked below first: it determines whether the answer is a family, domain, port, organization or year. These are different pivots even when they share a capture.

### 2. Check the source and preserve the decisive record

Frame 24500 is an HTTP GET to153.92.1.49 with Host whitepepper.su and /api/set_agent. All six selected requests agree. The original source asks for the domain at this IOC, and recorded primary threat research separately lists whitepepper.su among Lumma infrastructure.

The observed source/record is preserved below. These are recorded verification results; the drafting pass does not claim a fresh successful website query or a new grader submission.

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/files/2026-01-31-traffic-analysis-exercise.pcap -Y 'ip.dst==153.92.1.49 && http.request' -T fields -e frame.number -e ip.dst -e http.host -e http.request.uri
```

This offline reproduction uses `-r` to read the original capture, `-n` to suppress network name resolution, `-Y` for a display filter, and `-T fields` plus each `-e` to select the displayed packet fields. The filter binds the answer to the supplied IOC. Where present, `-d tcp.port==443,http` tells the dissector to interpret that stream as HTTP; it is a decoding choice, not a change to the stored traffic.

Recorded evidence excerpt (first lines, not a newly fabricated command response):

```text
frame.number	ip.dst	tcp.dstport	http.host	http.request.uri
24500	153.92.1.49	80	whitepepper.su	/api/set_agent?id=3BF67EC05320C5729578BE4C0ADF174C&token=842e2802df0f0a06b4ed51f12f4387e761523b&description=&agent=Chrome
```

### 3. Interpret the result at the requested level

Use the Host field as request context; do not claim every domain resolving to the same server is the C2. The candidate below wraps the recorded answer using the format specified by this challenge; the supporting evidence does not itself prove platform acceptance.

Source: [https://www.malware-traffic-analysis.net/2026/01/31/index.html](https://www.malware-traffic-analysis.net/2026/01/31/index.html).

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #305 — actual evidence capture

![305-saved-evidence.png](../screenshots/305-saved-evidence.png)

Actual terminal inspection of preserved verification record, explicitly historical rather than a new external lookup. This reads preserved evidence; it is not a fresh external IOC lookup.

Command/action actually executed:

```sh
head -n 12 /home/nightingale/CTF/PCGCTF/analysis-team-verification/lumma-domain.tsv
```

[Actual command transcript](../screenshots/capture-work/305-saved-record.terminal.log) · [Execution record](../screenshots/capture-work/305-saved-record.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{whitepepper.su}`**. Use the Host field as request context; do not claim every domain resolving to the same server is the C2. Exact PCGCTF acceptance is not recorded.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

Use the Host field as request context; do not claim every domain resolving to the same server is the C2.

## Evidence and references

[Original archived challenge](../../unsolved/osint/305-act-3-lumma-in-the-room-ah-domain-pivot/README.md)

- [Decisive saved lookup / packet evidence](../../analysis-team-verification/lumma-domain.tsv)
- [Original capture identities and extraction filters](../../analysis-team-verification/packet-checks.json)
- [Preserved investigation notes](../../unsolved/osint/305-act-3-lumma-in-the-room-ah-domain-pivot/solution.md)

**Provenance:** Rewritten from our independently checked original-capture/primary-source verification ledger; raw records linked and acceptance explicitly separated.
