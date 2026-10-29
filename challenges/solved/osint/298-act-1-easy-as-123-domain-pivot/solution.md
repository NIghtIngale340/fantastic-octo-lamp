# ACT 1 - EASY AS 123: Domain Pivot — verified answer evidence

Answer: **vadusa.xyz**

Flag candidate:

```text
pcgCTF{vadusa.xyz}
```

## Independent verification

The [exact sample’s MalwareBazaar entry](https://bazaar.abuse.ch/sample/c9e5bb7a368280d771edcfdb33717a3130560d2bb71773ab1aaffe0eb585fd2c/) has both the IP tag 45-131-214-85 and domain tag vadusa-xyz, identifies NetSupport, and lists C2 45.131.214.85:443. A [firsthand analysis of the same capture](https://rvmchua.com/posts/mta-easy-as-123/) explicitly associates vadusa.xyz with this IOC. This corroborates the teammate’s domain pivot against the threat database rather than relying only on their document.

## Reproducible local evidence

- [Verification evidence](../../../../analysis/team-verification/public-source-observations.json)
- [Capture identities, filters, counts and first packets](../../../../analysis/team-verification/packet-checks.json)
- [Recorded primary public-source observations](../../../../analysis/team-verification/public-source-observations.json)

## Limits

This is a historical malicious infrastructure association, not a claim about its current DNS or ownership. No lookup/contact to the malicious host was needed. This is an evidence-backed answer and saved submission candidate, not a verified PCGCTF acceptance.

Provenance: initially suggested in Antonio B. Garcia Jr.’s potential writeups; independently checked against the sources and original evidence above on 2026-10-28.
