# Robots Know Everything

**Platform:** OverTheWire Natas (mirrored by PCGCTF) · **Challenge ID:** 9 · **Category:** Web Exploitation — Natas · **Points:** 100

**Status:** Verified on OverTheWire from the saved live-auth record. Next-level password redacted.

## The challenge

Use `robots.txt` to find a hidden directory and recover natas4's password.

## Solving it

`robots.txt` is a request to crawlers, not a lock — a `Disallow` just names a path politely, and I can still fetch it:

```sh
curl -sS --user natas3 http://natas3.natas.labs.overthewire.org/robots.txt
# Disallow: /s3cr3t/
```

So I went straight there:

```sh
curl -sS --user natas3 http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
```

That file holds natas4's password, which logs into the next level.

## Verification record

The [saved authentication ledger](../evidence/ready-natas/natas-verification-redacted.json) records the method check and next-level authentication. Runtime passwords are redacted in that ledger.

## Flag

Recovered natas4 password (kept private); PCGCTF candidate is `pcgCTF{<natas4 password>}`.

## Takeaway

`robots.txt` advertises the paths you wanted hidden. It's a map for anyone curious, not an access control.

## References

- [Original archived challenge](../../challenges/solved/web-exploitation-natas/009-robots-know-everything/README.md)
