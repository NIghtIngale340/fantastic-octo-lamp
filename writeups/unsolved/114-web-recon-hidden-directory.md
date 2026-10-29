# Web Recon — Hidden Directory

**Platform:** PCGCTF · **Challenge ID:** 114 · **Category:** Web Exploitation · **Points:** 150

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A directory isn't linked but still exists.

## Investigation notes

The approach is content discovery — check `robots.txt`, then brute-force common directory names (gobuster/ffuf) to find the unlinked path.

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

- [Original challenge description](../../challenges/unsolved/web-exploitation/114-web-recon-hidden-directory/README.md)
