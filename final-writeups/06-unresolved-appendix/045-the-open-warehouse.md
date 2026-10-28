# The Open Warehouse

**Platform:** PCGCTF · **Challenge ID:** 45 · **Category:** Web Exploitation — DVWA · **Points:** 250

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

The server lists a directory's contents — directory indexing is on.

## Investigation notes

The concept is directory listing. The next check is to request a directory with no index page and read the exposed file list.

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

- [Original challenge description](../../unsolved/web-exploitation-dvwa/045-the-open-warehouse/README.md)
