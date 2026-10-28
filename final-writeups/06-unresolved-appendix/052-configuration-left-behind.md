# Configuration Left Behind

**Platform:** PCGCTF · **Challenge ID:** 52 · **Category:** Web Exploitation — DVWA · **Points:** 200

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

A configuration backup file was left accessible.

## What I could do

The concept is exposed config/backup disclosure. The next check is to request common backup names (`config.php.bak`, `.old`, `~`) and read any that resolve.

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![052-actual-target-response.png](../screenshots/052-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

Editor backups and `.bak` copies served as text leak the config they were meant to protect.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/052-configuration-left-behind/README.md)
