# ACT 2 - YOU DIRTY RAT!: Infrastructure Owner — verified answer evidence

Answer: **UAB Host Baltic**

Flag candidate:

```text
pcgCTF{UAB Host Baltic}
```

## Independent verification

Fetched current primary RIPE records independently. The route object for 141.98.10.0/24 has origin AS209605. The aut-num object has as-name hostbaltic. RIPEstat prefix-overview reports announced=true and the holder hostbaltic UAB Host Baltic. [RIPEstat](https://stat.ripe.net/data/prefix-overview/data.json?resource=141.98.10.0/24) and [RIPE route record](https://rest.db.ripe.net/search.json?query-string=141.98.10.0/24&type-filter=route) support the announcing organization; [IPinfo](https://ipinfo.io/ips/141.98.10.0/24) agrees.

## Reproducible local evidence

- [Verification evidence](../../../analysis-team-verification/routing-status.json)
- [Capture identities, filters, counts and first packets](../../../analysis-team-verification/packet-checks.json)
- [Recorded primary public-source observations](../../../analysis-team-verification/public-source-observations.json)

## Limits

The question asks the current announcing organization, not the attacker or end customer. AS209605 identifies the ASN; UAB Host Baltic supplies the requested organization. This is an evidence-backed answer and saved submission candidate, not a verified PCGCTF acceptance.

Provenance: initially suggested in Antonio B. Garcia Jr.’s potential writeups; independently checked against the sources and original evidence above on 2026-10-28.
