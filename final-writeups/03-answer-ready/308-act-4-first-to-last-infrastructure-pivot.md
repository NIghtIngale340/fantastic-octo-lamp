# ACT 4 - FIRST TO LAST: Infrastructure Pivot

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 308 |
| Technical category | OSINT |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Identify the public DNS/reverse-host domain named in the investigation. |
| Result | `pcgCTF{handyman24.eu}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

The original challenge explicitly identifies handyman24.eu as resolving to the IOC. That is stronger task-specific guidance than choosing a captured decoy domain from a different part of the infection.

## Working through the evidence

### 1. Bind the lookup to the supplied indicator

The starting indicator is `146.59.71.167`. Read the original question linked below first: it determines whether the answer is a family, domain, port, organization or year. These are different pivots even when they share a capture.

### 2. Check the source and preserve the decisive record

The saved public DNS JSON also returns146.59.71.167 for handyman24.eu. The current candidate follows the name stated by the question. Captured HTTP uses www.grinswakebthu.info, which is a different observation and should not silently replace the requested infrastructure pivot.

The observed source/record is preserved below. These are recorded verification results; the drafting pass does not claim a fresh successful website query or a new grader submission.

Open the linked primary/reference page for the exact indicator, retain its URL, and read the field described above. This step is browser-based: no malware execution, domain visitation or invented terminal output is necessary. The saved JSON observations distinguish what the page actually stated from a later interpretation.

### 3. Interpret the result at the requested level

Reverse-host names, DNS A records and captured HTTP Host values can differ. Keep each source and the question’s requested relationship explicit. The candidate below wraps the recorded answer using the format specified by this challenge; the supporting evidence does not itself prove platform acceptance.

Source: [https://dns.google/resolve?name=handyman24.eu&type=A](https://dns.google/resolve?name=handyman24.eu&type=A).

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #308 — actual evidence capture

![308-saved-evidence.png](../screenshots/308-saved-evidence.png)

Actual display of retained packet/DNS evidence; source date remains the recorded verification date. This reads preserved evidence; it is not a fresh external IOC lookup.

Command/action actually executed:

```sh
head -n 12 /home/nightingale/CTF/PCGCTF/analysis-act4-act5/handyman24-dns.json
```

[Actual command transcript](../screenshots/capture-work/308-saved-record.terminal.log) · [Execution record](../screenshots/capture-work/308-saved-record.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{handyman24.eu}`**. Reverse-host names, DNS A records and captured HTTP Host values can differ. Keep each source and the question’s requested relationship explicit. Exact PCGCTF acceptance is not recorded.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

Reverse-host names, DNS A records and captured HTTP Host values can differ. Keep each source and the question’s requested relationship explicit.

## Evidence and references

[Original archived challenge](../../unsolved/osint/308-act-4-first-to-last-infrastructure-pivot/README.md)

- [Decisive saved lookup / packet evidence](../../analysis-act4-act5/handyman24-dns.json)
- [Original capture identities and extraction filters](../../analysis-team-verification/packet-checks.json)
- [Preserved investigation notes](../../unsolved/osint/308-act-4-first-to-last-infrastructure-pivot/solution.md)

**Provenance:** Rewritten from our independently checked original-capture/primary-source verification ledger; raw records linked and acceptance explicitly separated.
