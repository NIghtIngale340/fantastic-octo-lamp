# ACT 2 - YOU DIRTY RAT!: C2 Service Port — verified answer evidence

Answer: **12132**

Flag candidate:

```text
pcgCTF{12132}
```

## Independent verification

Fresh original-capture check finds 102 packets with STRRAT payloads destined to 141.98.10.79; the destination TCP port is 12132, starting at frame 9119. The [firsthand public traffic analysis](https://securityposture.medium.com/traffic-analysis-of-strrat-malware-6b9c212c6ae6) also names this exact IOC and port.

## Reproducible local evidence

- [Verification evidence](../../../analysis-team-verification/strrat-beacons.tsv)
- [Capture identities, filters, counts and first packets](../../../analysis-team-verification/packet-checks.json)
- [Recorded primary public-source observations](../../../analysis-team-verification/public-source-observations.json)

## Limits

Port verified for this incident; other STRRAT samples can use different ports. This is an evidence-backed answer and saved submission candidate, not a verified PCGCTF acceptance.

Provenance: initially suggested in Antonio B. Garcia Jr.’s potential writeups; independently checked against the sources and original evidence above on 2026-10-28.
