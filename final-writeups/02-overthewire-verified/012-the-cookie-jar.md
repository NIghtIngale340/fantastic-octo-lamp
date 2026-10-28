# The Cookie Jar

**Platform:** OverTheWire Natas (mirrored by PCGCTF) · **Challenge ID:** 12 · **Category:** Web Exploitation — Natas · **Points:** 100

**Status:** Verified on OverTheWire from the saved live-auth record. Next-level password redacted.

## The challenge

natas5 says "you're not logged in." The only "session state" is a plain cookie.

## Solving it

The default response denies access because of a `loggedin=0` cookie. It's unsigned, and the server trusts it at face value, so the next step is to flip it:

```sh
curl -sS --user natas5 -b 'loggedin=1' http://natas5.natas.labs.overthewire.org/
```

With `loggedin=1` the page reveals natas6's password.

## Verification record

The [saved authentication ledger](../evidence/ready-natas/natas-verification-redacted.json) records the method check and next-level authentication. Runtime passwords are redacted in that ledger.

## Flag

Recovered natas6 password: `7mhjtShJAcld2NYbKHEadnhEwRn2P8VT`, so the flag is:

```text
pcgCTF{7mhjtShJAcld2NYbKHEadnhEwRn2P8VT}
```

## Takeaway

A cookie is client-supplied. If the server doesn't sign or verify it, a bare boolean "logged in" flag is yours to set.

## References

- [Original archived challenge](../../unsolved/web-exploitation-natas/012-the-cookie-jar/README.md)
