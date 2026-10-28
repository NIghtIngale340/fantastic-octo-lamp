# Commented Out Secrets

**Platform:** PCGCTF · **Challenge ID:** 50 · **Category:** Web Exploitation — DVWA · **Points:** 150

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

A secret was left in an HTML comment.

## What I could do

The concept is sensitive-info disclosure in HTML comments. The next check is to view source and read the comments.

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![050-actual-target-response.png](../screenshots/050-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

Commenting out a secret doesn't remove it — it still ships to every visitor in the source.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/050-commented-out-secrets/README.md)
