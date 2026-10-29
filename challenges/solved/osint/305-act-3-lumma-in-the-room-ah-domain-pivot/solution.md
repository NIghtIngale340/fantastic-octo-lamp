# ACT 3 - LUMMA IN THE ROOM-AH!: Domain Pivot — verified answer evidence

Answer: **whitepepper.su**

Flag candidate:

```text
pcgCTF{whitepepper.su}
```

## Independent verification

The [original incident source](https://www.malware-traffic-analysis.net/2026/01/31/index.html) asks for the domain associated with the Lumma IOC 153.92.1.49. A fresh local check confirms six HTTP requests to that IP with Host whitepepper.su; frame 24500 is GET /api/set_agent. The analyst performing the original public [WhoisXML research](https://circleid.com/posts/dns-deep-dive-lummastealer-castleloader-larger-threat) separately lists whitepepper.su among Lumma infrastructure.

## Reproducible local evidence

- [Verification evidence](../../../../analysis/team-verification/lumma-domain.tsv)
- [Capture identities, filters, counts and first packets](../../../../analysis/team-verification/packet-checks.json)
- [Recorded primary public-source observations](../../../../analysis/team-verification/public-source-observations.json)

## Limits

Historical C2 association is established; current DNS/ownership is not implied. This is an evidence-backed answer and saved submission candidate, not a verified PCGCTF acceptance.

Provenance: initially suggested in Antonio B. Garcia Jr.’s potential writeups; independently checked against the sources and original evidence above on 2026-10-28.
