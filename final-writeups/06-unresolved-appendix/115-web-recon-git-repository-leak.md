# Web Recon — Git Repository Leak

**Platform:** PCGCTF · **Challenge ID:** 115 · **Category:** Web Exploitation · **Points:** 700

**Status:** Unresolved. The technique is clear from the clue, but the target (http://flag1.cgcybercom.online/repo/.git/) wasn't reachable from here, so there's no response to work with and no confirmed flag. Honest stub.

## The challenge

The site exposes its `.git` directory.

## What I could do

The approach is to confirm `/repo/.git/HEAD` resolves, then dump the repo (e.g. git-dumper) to reconstruct the source and recover the flag from history.

I probed the target read-only:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://flag1.cgcybercom.online/repo/.git/
```

The connection timed out — no response body. Reporting a working exploit here would be inventing evidence.

## Screenshot

![115-web-recon-git-repository-leak-actual-target-response.png](../screenshots/115-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered — target unreachable, and the exact string inside `pcgCTF{...}` isn't known.

## Still to do

- Reach the target from an authorized network, run the check above, and record one justified candidate with its real submission result.

## Takeaway

A web-served `.git` directory leaks full source and history — block it at the server.

## Reference

- [Original challenge description](../../unsolved/web-exploitation/115-web-recon-git-repository-leak/README.md)
