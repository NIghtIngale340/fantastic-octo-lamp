# Commented Out Secrets

**Platform:** PCGCTF · **Challenge ID:** 50 · **Category:** Web Exploitation — DVWA · **Points:** 150

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A secret was left in an HTML comment.

## Investigation notes

The concept is sensitive-info disclosure in HTML comments. The next check is to view source and read the comments.

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

- [Original challenge description](../../challenges/unsolved/web-exploitation-dvwa/050-commented-out-secrets/README.md)
