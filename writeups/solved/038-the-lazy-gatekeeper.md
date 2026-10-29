# The Lazy Gatekeeper

**Platform:** PCGCTF · **Challenge ID:** 38 · **Category:** Web Exploitation — DVWA · **Points:** 50

**Status:** Solved in the old snapshot, but the lab host is unreachable now and the exact accepted flag wasn't saved. The login method remains unconfirmed on this deployment.

## The challenge

Which account did the unchanged DVWA gatekeeper still trust? The "original keys" wording points at default credentials, not an injection.

## Solving it

DVWA ships with a documented default web login of `admin` / `password`, so that's the obvious thing to try. I tried to reach the lab host to confirm on the actual deployment:

```sh
curl --connect-timeout 3 --max-time 6 -sS -D - http://10.56.102.240:4280/
```

The connection failed — the private lab host isn't reachable from here, so I can't show the authenticated page or capture the exact flag. The reasoning (admin via unchanged defaults) holds, but I'm not going to present an unconfirmed login as a captured solve.

## Screenshot

The terminal image below displays a retained verification transcript.

![038-actual-target-response.png](../screenshots/038-actual-target-response.png)

(The capture shows the failed connection attempt — not a working exploit.)

## Flag

Not recovered. The snapshot records a solve but not the submitted string, and the host is down, so there's nothing to re-verify.

## Still to do

- Reach the lab host from the authorized network and capture the actual login result.
- Recover the exact accepted flag text — the snapshot alone doesn't keep it.

## Takeaway

A known default credential isn't the same as a confirmed login on a specific deployment. When reconstructing an old solve, keep "this is the likely answer" separate from "I verified it here."

## References

- [Original challenge and attachments](<../../home/nightingale/CTF/PCGCTF/solved/web-exploitation-dvwa/038-the-lazy-gatekeeper/README.md>)
- [DVWA default credentials](https://github.com/digininja/DVWA/blob/master/README.md#default-credentials)
