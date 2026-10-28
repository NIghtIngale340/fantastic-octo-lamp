# The Changing Door

**Platform:** PCGCTF · **Challenge ID:** 42 · **Category:** Web Exploitation — DVWA · **Points:** 100

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

Changing an identifier in the request returns someone else's data — an IDOR.

## Investigation notes

The concept is Insecure Direct Object Reference. The next check is to vary an object id in a request and see whether the app returns records it shouldn't.

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

- [Original challenge description](../../unsolved/web-exploitation-dvwa/042-the-changing-door/README.md)
