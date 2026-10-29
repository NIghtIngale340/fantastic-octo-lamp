# ACT 3 - LUMMA IN THE ROOM-AH!: Identify the Stealer — verified answer evidence

Answer: **Lumma Stealer**

Flag candidate:

```text
pcgCTF{Lumma Stealer}
```

## Independent verification

The [original exercise background](https://www.malware-traffic-analysis.net/2026/01/31/index.html) explicitly names a Lumma Stealer fingerprinting alert triggered by 153.92.1.49 over TCP 80. Our original capture corroborates six HTTP requests to this IOC with host whitepepper.su and /api/set_agent requests, starting frame 24500.

## Reproducible local evidence

- [Verification evidence](../../../../analysis/team-verification/lumma-domain.tsv)
- [Capture identities, filters, counts and first packets](../../../../analysis/team-verification/packet-checks.json)
- [Recorded primary public-source observations](../../../../analysis/team-verification/public-source-observations.json)

## Limits

The family is directly named by the original incident source; exact grader normalization remains untested. This is an evidence-backed answer and saved submission candidate, not a verified PCGCTF acceptance.

Provenance: initially suggested in Antonio B. Garcia Jr.’s potential writeups; independently checked against the sources and original evidence above on 2026-10-28.
