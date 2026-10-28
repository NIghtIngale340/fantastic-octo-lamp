# The Exposed Repository

**Platform:** PCGCTF · **Challenge ID:** 54 · **Category:** Web Exploitation — DVWA · **Points:** 250

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

The site's `.git` directory is web-accessible — source-code disclosure.

## Investigation notes

The concept is an exposed Git repo. The next check is to request `/.git/` and, if present, dump the repo (e.g. git-dumper) to recover source and secrets.

The saved connection attempt used:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://10.56.102.240:4280/
```

The result was a **connect timeout** — no response body to inspect.

## Flag

None recovered. The lab is unreachable from this environment, and the grader's exact wording inside `pcgCTF{...}` isn't known either.

## Next step

Once the lab is reachable, test the challenge-specific approach above and record the response and submission result.

## Reference

- [Original challenge description](../../unsolved/web-exploitation-dvwa/054-the-exposed-repository/README.md)
