# ACT 2 - YOU DIRTY RAT!: Identify the RAT — verified answer evidence

Answer: **STRRAT**

Flag candidate:

```text
pcgCTF{STRRAT}
```

## Independent verification

Freshly inspected the original 2024-07-30 capture. Frame 9119 is client data to 141.98.10.79:12132 and its decoded payload begins ping|STRRAT|. There are 102 matching beacon packets. This is direct captured evidence for STRRAT, with the same IOC as the [original exercise](https://www.malware-traffic-analysis.net/2024/07/30/index.html). A [firsthand public traffic analysis](https://securityposture.medium.com/traffic-analysis-of-strrat-malware-6b9c212c6ae6) independently reports STRRAT and the same C2.

## Reproducible local evidence

- [Verification evidence](../../../analysis-team-verification/strrat-beacons.tsv)
- [Capture identities, filters, counts and first packets](../../../analysis-team-verification/packet-checks.json)
- [Recorded primary public-source observations](../../../analysis-team-verification/public-source-observations.json)

## Limits

The family string and traffic association are directly observed; exact flag acceptance is not tested. This is an evidence-backed answer and saved submission candidate, not a verified PCGCTF acceptance.

Provenance: initially suggested in Antonio B. Garcia Jr.’s potential writeups; independently checked against the sources and original evidence above on 2026-10-28.
