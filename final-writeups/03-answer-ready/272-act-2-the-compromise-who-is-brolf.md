# ACT 2 — The Compromise: Who Is brolf?

**Platform:** PCGCTF · **Challenge ID:** 272 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the Act 2 capture. Exact PCGCTF submission not independently re-confirmed.

## The challenge

Resolve the account `brolf` to its full name.

## Solving it

The SAMR user-info record carries both fields, so this is a direct read:

```sh
tshark -nr act2.pcap -Y 'samr.samr_UserInfo21.account_name=="brolf"' \
  -T fields -e samr.samr_UserInfo21.full_name
```

```text
Becka Rolf
```

## Screenshot

![272-decisive-evidence.png](../screenshots/272-decisive-evidence.png)

## Flag

```text
pcgCTF{Becka Rolf}
```

## Takeaway

`brolf` = Becka Rolf — the SAMR record pairs the login name with the display name, so no guessing at the expansion.

## Reference

- [Original challenge description](../../solved/network-forensics/272-act-2-the-compromise-who-is-brolf/README.md)
