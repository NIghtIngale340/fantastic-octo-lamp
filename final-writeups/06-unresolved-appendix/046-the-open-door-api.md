# The Open Door API

**Platform:** PCGCTF · **Challenge ID:** 46 · **Category:** Web Exploitation — DVWA · **Points:** 250

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

An API endpoint has no authentication — anyone can call it.

## What I could do

The concept is missing API authentication. The next check is to call the endpoint directly and see whether it returns data with no credentials.

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![046-actual-target-response.png](../screenshots/046-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

An unauthenticated API is open to everyone — auth has to be enforced server-side on every endpoint.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/046-the-open-door-api/README.md)
