# ACT 1 - EASY AS 123: Threat Identity — verified answer evidence

Answer: **NetSupport Manager RAT**

Flag candidate:

```text
pcgCTF{NetSupport Manager RAT}
```

## Independent verification

The [original exercise](https://www.malware-traffic-analysis.net/2026/02/28/index.html) directly associates 45.131.214.85 over TCP 443 with NetSupport Manager RAT. [ThreatFox](https://threatfox.abuse.ch/ioc/1755776/) independently labels that IOC NetSupportManager RAT, alias NetSupport. Our original packet capture independently has 264 HTTP requests to this IOC, with NetSupport Manager/1.3 in the user agent; first request is frame 2638.

## Reproducible local evidence

- [Verification evidence](../../../../analysis/team-verification/netsupport-http.tsv)
- [Capture identities, filters, counts and first packets](../../../../analysis/team-verification/packet-checks.json)
- [Recorded primary public-source observations](../../../../analysis/team-verification/public-source-observations.json)

## Limits

The family is established; the platform’s accepted capitalization/spacing is not tested. The longer family label follows the original exercise. This is an evidence-backed answer and saved submission candidate, not a verified PCGCTF acceptance.

Provenance: initially suggested in Antonio B. Garcia Jr.’s potential writeups; independently checked against the sources and original evidence above on 2026-10-28.
