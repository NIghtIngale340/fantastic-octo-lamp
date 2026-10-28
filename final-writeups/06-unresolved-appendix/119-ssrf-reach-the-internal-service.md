# SSRF — Reach the Internal Service

**Platform:** PCGCTF · **Challenge ID:** 119 · **Category:** Web Exploitation · **Points:** 200

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A server-side fetch can be pointed at an internal service — SSRF.

## Investigation notes

The approach is to supply an internal URL (e.g. `http://127.0.0.1/` or a metadata endpoint) to the parameter the server fetches, and read the internal response.

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

- [Original challenge description](../../unsolved/web-exploitation/119-ssrf-reach-the-internal-service/README.md)
