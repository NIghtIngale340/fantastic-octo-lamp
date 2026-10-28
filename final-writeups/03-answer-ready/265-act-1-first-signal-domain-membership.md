# ACT 1 — First Signal: Domain Membership

**Platform:** PCGCTF · **Challenge ID:** 265 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the Act 1 capture. Exact PCGCTF submission not independently re-confirmed.

## The challenge

What Active Directory domain is the compromised workstation joined to?

## Solving it

The Kerberos realm is the domain, straight from the AS-REQ:

```sh
tshark -nr act1.pcap -Y 'kerberos.CNameString' -T fields -e kerberos.realm
```

```text
FIRSTTOLAST.TECH
```

The realm is `FIRSTTOLAST.TECH`; the NetBIOS/short domain name is `FIRSTTOLAST`.

## Screenshot

![265-decisive-evidence.png](../screenshots/265-decisive-evidence.png)

## Flag

```text
pcgCTF{FIRSTTOLAST}
```

(If the grader wanted the full realm it'd be `FIRSTTOLAST.TECH` — worth noting since both appear.)

## Takeaway

The Kerberos realm names the domain. Watch whether a challenge wants the short name or the full DNS realm.

## Reference

- [Original challenge description](../../solved/network-forensics/265-act-1-first-signal-domain-membership/README.md)
