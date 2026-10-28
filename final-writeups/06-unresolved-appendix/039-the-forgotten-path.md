# The Forgotten Path

**Platform:** PCGCTF · **Challenge ID:** 39 · **Category:** Web Exploitation — DVWA · **Points:** 150

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A page is omitted from navigation; which file reveals directories? That's `robots.txt`.

## Investigation notes

The concept is clear — `robots.txt` lists `Disallow` paths that anyone can read (it's a crawler hint, not an access control). The next check is to fetch `/robots.txt` and read the listed directories.

The saved connection attempt used:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect.

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Next step

Once the lab is reachable, test the challenge-specific approach above and record the response and submission result.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/039-the-forgotten-path/README.md)
