# Path Traversal — Off by Slash

**Platform:** PCGCTF · **Challenge ID:** 118 · **Category:** Web Exploitation · **Points:** 300

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A path filter is bypassable with a slash trick — path traversal.

## Investigation notes

The approach is to try traversal payloads that defeat a naive `../` filter (encoded slashes, extra slashes) and read a file outside the web root.

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

- [Original challenge description](../../challenges/unsolved/web-exploitation/118-path-traversal-off-by-slash/README.md)
