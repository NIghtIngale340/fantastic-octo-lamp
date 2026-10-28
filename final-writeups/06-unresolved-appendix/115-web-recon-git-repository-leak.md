# Web Recon — Git Repository Leak

**Platform:** PCGCTF · **Challenge ID:** 115 · **Category:** Web Exploitation · **Points:** 700

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

The site exposes its `.git` directory.

## Investigation notes

The approach is to confirm `/repo/.git/HEAD` resolves, then dump the repo (e.g. git-dumper) to reconstruct the source and recover the flag from history.

The saved connection attempt used:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://flag1.cgcybercom.online/repo/.git/
```

The connection timed out — no response body.

## Flag

None recovered — target unreachable, and the exact string inside `pcgCTF{...}` isn't known.

## Next step

Once the lab is reachable, test the challenge-specific approach above and record the response and submission result.

## Reference

- [Original challenge description](../../unsolved/web-exploitation/115-web-recon-git-repository-leak/README.md)
