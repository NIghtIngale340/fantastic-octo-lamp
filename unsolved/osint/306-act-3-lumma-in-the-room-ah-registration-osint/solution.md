# ACT 3 - LUMMA IN THE ROOM-AH!: Registration OSINT — verified answer evidence

Answer: **2025**

Flag candidate:

```text
pcgCTF{2025}
```

## Independent verification

Queried the .su registry WHOIS server whois.tcinet.ru directly. It returns WHITEPEPPER.SU, source TCI, created 2025-12-19T20:37:42Z. Therefore the year in the current registration record is 2025. Raw registry output is saved. [Registry WHOIS service](https://tcinet.ru/) and [public WHOIS lookup](https://www.whois.com/whois/whitepepper.su).

## Reproducible local evidence

- [Verification evidence](../../../analysis-team-verification/whitepepper-whois.txt)
- [Capture identities, filters, counts and first packets](../../../analysis-team-verification/packet-checks.json)
- [Recorded primary public-source observations](../../../analysis-team-verification/public-source-observations.json)

## Limits

The current registration date is confirmed. Historical DNS observations go back before 2025, so this does not establish the first-ever registration date across lapsed registrations. The challenge does not specify a historical WHOIS snapshot; exact platform acceptance remains untested. This is an evidence-backed answer and saved submission candidate, not a verified PCGCTF acceptance.

Provenance: initially suggested in Antonio B. Garcia Jr.’s potential writeups; independently checked against the sources and original evidence above on 2026-10-28.
