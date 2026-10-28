# The Open Warehouse

**Platform:** PCGCTF · **Challenge ID:** 45 · **Category:** Web Exploitation — DVWA · **Points:** 250

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

The server lists a directory's contents — directory indexing is on.

## What I could do

The concept is directory listing. The next check is to request a directory with no index page and read the exposed file list.

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![045-actual-target-response.png](../screenshots/045-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

Directory indexing turns one known path into the whole folder — disable autoindex.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/045-the-open-warehouse/README.md)
