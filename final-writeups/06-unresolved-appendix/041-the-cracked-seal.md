# The Cracked Seal

**Platform:** PCGCTF · **Challenge ID:** 41 · **Category:** Web Exploitation — DVWA · **Points:** 150

**Status:** Unresolved. The clue points at a clear concept, but the lab host (http://10.56.102.240:4280/) wasn't reachable from here, so there's no response to exploit and no confirmed flag. Honest stub.

## The challenge

A weak password hash is meant to be cracked (MD5 is the plausible intended example, though no hash is supplied here).

## What I could do

The concept is weak password hashing. With the actual hash, the next step would be to identify the algorithm and crack it (e.g. hashcat/John against a wordlist).

I probed the target read-only, with redirects disabled so an unrelated landing page couldn't masquerade as the lab:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect. Claiming a working exploit here would be inventing evidence.

## Screenshot

![041-actual-target-response.png](../screenshots/041-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Still to do

- Reach the lab from an authorized network, capture the live prompt/hint, and record one justified candidate plus its actual submission result.

## Takeaway

A fast, unsalted hash like MD5 is crackable offline — the fix is a slow, salted KDF.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/041-the-cracked-seal/README.md)
