# Through the Wrong Door

**Platform:** PCGCTF · **Challenge ID:** 53 · **Category:** Web Exploitation — DVWA · **Points:** 250

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A parameter lets you read arbitrary files via path traversal (`../`) — distinct from LFI.

## Investigation notes

The concept is path traversal. The next check is to feed `../../../../etc/passwd` to the file parameter and confirm arbitrary file read.

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

- [Original challenge description](../../unsolved/web-exploitation-dvwa/053-through-the-wrong-door/README.md)
