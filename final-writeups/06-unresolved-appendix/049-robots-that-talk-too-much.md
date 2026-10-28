# Robots That Talk Too Much

**Platform:** PCGCTF · **Challenge ID:** 49 · **Category:** Web Exploitation — DVWA · **Points:** 200

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

`robots.txt` discloses sensitive paths (same file as #39, different question).

## What I could do

The concept is information disclosure via `robots.txt`. The next check is to read the `Disallow` entries and follow the sensitive ones.

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![049-actual-target-response.png](../screenshots/049-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

Listing a secret path in `robots.txt` to 'hide' it just publishes a map to it.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/049-robots-that-talk-too-much/README.md)
