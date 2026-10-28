# The Changing Door

**Platform:** PCGCTF · **Challenge ID:** 42 · **Category:** Web Exploitation — DVWA · **Points:** 100

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

Changing an identifier in the request returns someone else's data — an IDOR.

## What I could do

The concept is Insecure Direct Object Reference. The next check is to vary an object id in a request and see whether the app returns records it shouldn't.

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![042-actual-target-response.png](../screenshots/042-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

IDOR is missing authorization on an object reference — the server must check ownership, not trust the id.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/042-the-changing-door/README.md)
