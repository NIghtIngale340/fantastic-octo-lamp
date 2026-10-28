# Silent Witness

**Platform:** PCGCTF · **Challenge ID:** 40 · **Category:** Web Exploitation — DVWA · **Points:** 150

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

Something is hidden in the page but not displayed — i.e. in the HTML source comments.

## What I could do

The concept is an HTML source comment. The next check is to view source (or `curl` the page) and read the comments for the secret.

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![040-actual-target-response.png](../screenshots/040-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

Comments are delivered to the browser even though they're not rendered — view-source exposes them.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/040-silent-witness/README.md)
