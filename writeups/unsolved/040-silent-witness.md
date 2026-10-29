# Silent Witness

**Platform:** PCGCTF · **Challenge ID:** 40 · **Category:** Web Exploitation — DVWA · **Points:** 150

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

Something is hidden in the page but not displayed — i.e. in the HTML source comments.

## Investigation notes

The concept is an HTML source comment. The next check is to view source (or `curl` the page) and read the comments for the secret.

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

- [Original challenge description](../../challenges/unsolved/web-exploitation-dvwa/040-silent-witness/README.md)
