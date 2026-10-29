# Infrastructure — Unsecured Reverse Proxy

**Platform:** PCGCTF · **Challenge ID:** 117 · **Category:** Web / Infrastructure Security · **Points:** 300

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A reverse proxy forwards to an internal service it shouldn't expose.

## Investigation notes

The approach is to probe proxy routes / Host headers that reach the backend the proxy was meant to shield, then read the internal response.

The saved connection attempt used:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://flag.cgcybercom.online/
```

The connection timed out — no response body.

## Flag

None recovered — target unreachable, and the exact string inside `pcgCTF{...}` isn't known.

## Next step

Once the lab is reachable, test the challenge-specific approach above and record the response and submission result.

## Reference

- [Original challenge description](../../challenges/unsolved/web-infrastructure-security/117-infrastructure-unsecured-reverse-proxy/README.md)
