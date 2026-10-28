# The Invisible Crown

**Platform:** PCGCTF · **Challenge ID:** 43 · **Category:** Web Exploitation — DVWA · **Points:** 200

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

A client-controlled value decides your role (a cookie is the likely spot, but it could be a token or local storage).

## What I could do

The concept is client-controlled role data. The next check is to inspect the cookie/token and flip the role field, then confirm the server trusts it.

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![043-actual-target-response.png](../screenshots/043-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

Never trust the client for authorization state — a role in a cookie the server doesn't verify is yours to change.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/043-the-invisible-crown/README.md)
