# Access Denied? Think Again

**Platform:** OverTheWire Natas (mirrored by PCGCTF) · **Challenge ID:** 7 · **Category:** Web Exploitation — Natas · **Points:** 100

**Status:** Verified on OverTheWire from the saved live-auth record. Next-level password redacted.

## The challenge

natas1 blocks right-click. Get natas2's password anyway.

## Solving it

Disabling the context menu is a browser-only trick — it changes one interaction and nothing on the server. `curl` doesn't run the page's JavaScript, so the handler never fires and the secret is just sitting in the response body:

```sh
curl -sS --user natas1 http://natas1.natas.labs.overthewire.org/
```

The natas2 password is in an HTML comment in that output. Confirmed it against the next level:

```sh
curl -sS --user natas2 -o /dev/null -w '%{http_code}\n' http://natas2.natas.labs.overthewire.org/
# → 200
```

## Verification record

The [saved authentication ledger](../evidence/ready-natas/natas-verification-redacted.json) records the method check and next-level authentication. Runtime passwords are redacted in that ledger.

## Flag

Recovered natas2 password: `vsDOxoXyq3wckCP1ZmTZ71ngIA606odB`, so the flag is:

```text
pcgCTF{vsDOxoXyq3wckCP1ZmTZ71ngIA606odB}
```

## Takeaway

A client-side UI restriction isn't an access control. If the secret reached the browser, blocking right-click protects nothing.

## References

- [Original archived challenge](../../unsolved/web-exploitation-natas/007-access-denied-think-again/README.md)
