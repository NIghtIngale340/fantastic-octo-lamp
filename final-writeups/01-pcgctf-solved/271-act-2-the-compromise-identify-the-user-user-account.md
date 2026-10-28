# ACT 2 — The Compromise: Identify the User Account

**Platform:** PCGCTF · **Challenge ID:** 271 · **Category:** Network Forensics · **Points:** 100

**Status:** Solved in the authenticated snapshot; reproduced from the Act 2 capture.

## The challenge

Identify the domain user account tied to the infected client.

## Solving it

A SAMR query in the capture exposes the account directly:

```sh
tshark -nr act2.pcap -Y 'samr.samr_UserInfo21.account_name' \
  -T fields -e samr.samr_UserInfo21.account_name -e samr.samr_UserInfo21.full_name
```

```text
brolf   Becka Rolf
```

The account is `brolf` (full name Becka Rolf — that's the follow-up question, #272).

## Screenshot

![271-decisive-evidence.png](../screenshots/271-decisive-evidence.png)

## Flag

```text
pcgCTF{brolf}
```

## Takeaway

SAMR/LSARPC traffic hands you account names and full names in cleartext — a reliable way to attribute a host to a user.

## Reference

- [Original challenge description](../../solved/network-forensics/271-act-2-the-compromise-identify-the-user-user-account/README.md)
