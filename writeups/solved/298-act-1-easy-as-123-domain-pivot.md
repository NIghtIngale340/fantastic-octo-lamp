# ACT 1 — Easy as 123: Domain Pivot

**Platform:** PCGCTF · **Challenge ID:** 298 · **Category:** Network Forensics / OSINT · **Points:** 100

**Status:** Answer backed by cited public sources. Exact PCGCTF submission not re-confirmed.

**Evidence:** Source: [MalwareBazaar IP/domain tags and the cited incident report](../../analysis/team-verification/public-source-observations.json). Packet/stream: not applicable to this OSINT lookup.

## The challenge

Pivot from C2 IP `45.131.214.85` to its associated domain.

## Solving it

I looked for an *explicit* IP↔domain link, not just a domain that happened to share hosting. The matching MalwareBazaar sample carries both the `45-131-214-85` and `vadusa-xyz` tags and identifies NetSupport, and the analyst writeup for this exercise names `vadusa.xyz` on that IP:

```text
MalwareBazaar sample tags: 45-131-214-85, vadusa-xyz → NetSupport
Analyst report: vadusa.xyz ↔ 45.131.214.85
```

Refanged, the domain is `vadusa.xyz`.

## Supporting record

The lookup observations are preserved in the [saved verification records](../../analysis/team-verification/public-source-observations.json).

## Flag

```text
pcgCTF{vadusa.xyz}
```

## Takeaway

A database's dash-separated tag (`vadusa-xyz`) is a normalized label — resolve it to the real punctuation (`vadusa.xyz`) using an explicit report, and treat it as a historical link, not current ownership.

## References

- [Analyst writeup (Easy as 123)](https://rvmchua.com/posts/mta-easy-as-123/)
- [Original challenge description](../../challenges/solved/osint/298-act-1-easy-as-123-domain-pivot/README.md)
