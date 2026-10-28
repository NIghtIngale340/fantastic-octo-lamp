# ACT 2 - YOU DIRTY RAT!: Infrastructure Owner

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 302 |
| Technical category | OSINT |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Identify the organization currently announcing the prefix. |
| Result | `pcgCTF{UAB Host Baltic}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

Registration, route origin and customer ownership are different facts. The question asks for the announcing organization, so I followed the route origin ASN rather than reverse DNS branding.

## Working through the evidence

### 1. Bind the lookup to the supplied indicator

The starting indicator is `141.98.10.0/24`. Read the original question linked below first: it determines whether the answer is a family, domain, port, organization or year. These are different pivots even when they share a capture.

### 2. Check the source and preserve the decisive record

The saved primary RIPE route object has origin AS209605. The aut-num record names hostbaltic, and RIPEstat reports announced=true with holder hostbaltic UAB Host Baltic. IPinfo independently agrees. The requested organization is UAB Host Baltic.

The observed source/record is preserved below. These are recorded verification results; the drafting pass does not claim a fresh successful website query or a new grader submission.

```sh
curl -sS "https://stat.ripe.net/data/prefix-overview/data.json?resource=141.98.10.0/24"
```

This is a repeatable public lookup recipe; `-sS` keeps errors while hiding the progress meter. The saved actual response has `announced: true`, ASN209605 and holder `hostbaltic UAB Host Baltic`. Cross-check the preserved route/aut-num JSON rather than treating a reverse hostname as an organization name.

### 3. Interpret the result at the requested level

The route identifies an announcing network operator, not the attacker or a particular hosted customer. The finding is time-sensitive and the raw query response is preserved. The candidate below wraps the recorded answer using the format specified by this challenge; the supporting evidence does not itself prove platform acceptance.

Source: [https://stat.ripe.net/data/prefix-overview/data.json?resource=141.98.10.0/24](https://stat.ripe.net/data/prefix-overview/data.json?resource=141.98.10.0/24).

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #302 — actual evidence capture

![302-saved-evidence.png](../screenshots/302-saved-evidence.png)

Actual terminal inspection of preserved verification record, explicitly historical rather than a new external lookup. This reads preserved evidence; it is not a fresh external IOC lookup.

Command/action actually executed:

```sh
head -n 12 /home/nightingale/CTF/PCGCTF/analysis-team-verification/routing-status.json
```

[Actual command transcript](../screenshots/capture-work/302-saved-record.terminal.log) · [Execution record](../screenshots/capture-work/302-saved-record.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{UAB Host Baltic}`**. The route identifies an announcing network operator, not the attacker or a particular hosted customer. The finding is time-sensitive and the raw query response is preserved. Exact PCGCTF acceptance is not recorded.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

The route identifies an announcing network operator, not the attacker or a particular hosted customer. The finding is time-sensitive and the raw query response is preserved.

## Evidence and references

[Original archived challenge](../../unsolved/osint/302-act-2-you-dirty-rat-infrastructure-owner/README.md)

- [Decisive saved lookup / packet evidence](../../analysis-team-verification/routing-status.json)
- [Original capture identities and extraction filters](../../analysis-team-verification/packet-checks.json)
- [RIPE route object](../../analysis-team-verification/ripe-route.json)
- [RIPE ASN object](../../analysis-team-verification/ripe-asn.json)
- [Preserved investigation notes](../../unsolved/osint/302-act-2-you-dirty-rat-infrastructure-owner/solution.md)

**Provenance:** Rewritten from our independently checked original-capture/primary-source verification ledger; raw records linked and acceptance explicitly separated.
