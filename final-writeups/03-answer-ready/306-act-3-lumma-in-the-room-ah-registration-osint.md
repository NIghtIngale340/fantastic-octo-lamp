# ACT 3 — Lumma in the Room-ah!: Registration OSINT

**Platform:** PCGCTF · **Challenge ID:** 306 · **Category:** OSINT · **Points:** 100

**Status:** Answer backed by cited WHOIS records (time-sensitive). Exact PCGCTF submission not re-confirmed.

## The challenge

What year was the C2 domain `whitepepper.su` registered?

## Solving it

A WHOIS lookup on the domain gives the creation date:

```sh
whois whitepepper.su | grep -i 'created\|registered'
```

```text
created: 2025-...
```

The registration year is 2025 — consistent with freshly-stood-up malware infrastructure.

## Screenshot

![306-saved-evidence.png](../screenshots/306-saved-evidence.png)

## Flag

```text
pcgCTF{2025}
```

## Takeaway

A recent registration date is itself an IOC — throwaway C2 domains are usually registered right before the campaign. WHOIS data is time-sensitive, so preserve the raw record.

## Reference

- [Original challenge description](../../solved/network-forensics/306-act-3-lumma-in-the-room-ah-registration-osint/README.md)
