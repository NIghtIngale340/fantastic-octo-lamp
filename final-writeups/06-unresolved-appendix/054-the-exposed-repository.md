# The Exposed Repository

**Platform:** PCGCTF · **Challenge ID:** 54 · **Category:** Web Exploitation — DVWA · **Points:** 250

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

The site's `.git` directory is web-accessible — source-code disclosure.

## What I could do

The concept is an exposed Git repo. The next check is to request `/.git/` and, if present, dump the repo (e.g. git-dumper) to recover source and secrets.

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![054-actual-target-response.png](../screenshots/054-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

A served `.git` directory hands an attacker your full source and history — block it at the web server.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/054-the-exposed-repository/README.md)
