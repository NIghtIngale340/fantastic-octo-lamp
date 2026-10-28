# The Cracked Seal

**Platform:** PCGCTF · **Challenge ID:** 41 · **Category:** Web Exploitation — DVWA · **Points:** 150

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A weak password hash is meant to be cracked (MD5 is the plausible intended example, though no hash is supplied here).

## Investigation notes

The concept is weak password hashing. With the actual hash, the next step would be to identify the algorithm and crack it (e.g. hashcat/John against a wordlist).

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

- [Original challenge description](../../unsolved/web-exploitation-dvwa/041-the-cracked-seal/README.md)
