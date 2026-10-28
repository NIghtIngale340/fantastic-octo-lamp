# Web Recon — View Source

**Platform:** PCGCTF · **Challenge ID:** 113 · **Category:** Web Exploitation · **Points:** 150

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A flag is hidden in the page's HTML source.

## Investigation notes

The approach is to view source (or `curl` the page) and read it — comments and hidden elements included.

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

- [Original challenge description](../../unsolved/web-exploitation/113-web-recon-view-source/README.md)
