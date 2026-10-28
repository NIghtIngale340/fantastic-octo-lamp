# Web Recon — Read the Headers

**Platform:** PCGCTF · **Challenge ID:** 116 · **Category:** Web Exploitation · **Points:** 300

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

The flag is in the HTTP response headers.

## Investigation notes

The approach is to read the full response headers (`curl -D -` or `-I`) and look for a custom header carrying the flag.

The saved connection attempt used:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://flag1.cgcybercom.online/
```

The connection timed out — no response body.

## Flag

None recovered — target unreachable, and the exact string inside `pcgCTF{...}` isn't known.

## Next step

Once the lab is reachable, test the challenge-specific approach above and record the response and submission result.

## Reference

- [Original challenge description](../../unsolved/web-exploitation/116-web-recon-read-the-headers/README.md)
