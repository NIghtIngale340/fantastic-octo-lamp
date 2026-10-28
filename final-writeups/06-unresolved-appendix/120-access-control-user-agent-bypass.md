# Access Control — User-Agent Bypass

**Platform:** PCGCTF · **Challenge ID:** 120 · **Category:** Web Exploitation · **Points:** 200

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

Access is gated on the User-Agent header.

## Investigation notes

The approach is to send the expected User-Agent (`curl -A '...'`) to the restricted path and read the response.

The saved connection attempt used:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://flag.cgcybercom.online/admin-map
```

The connection timed out — no response body.

## Flag

None recovered — target unreachable, and the exact string inside `pcgCTF{...}` isn't known.

## Next step

Once the lab is reachable, test the challenge-specific approach above and record the response and submission result.

## Reference

- [Original challenge description](../../unsolved/web-exploitation/120-access-control-user-agent-bypass/README.md)
