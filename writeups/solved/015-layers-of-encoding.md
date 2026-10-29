# Layers of Encoding

**Platform:** OverTheWire Natas (mirrored by PCGCTF) · **Challenge ID:** 15 · **Category:** Web Exploitation — Natas · **Points:** 100

**Status:** Verified on OverTheWire from the saved live-auth record. Next-level password redacted.

## The challenge

natas8 compares your input, after a published transform, against a constant. Work backwards.

## Solving it

The source shows the transform: Base64-encode, reverse the string, then hex-encode — compared against a stored value. All three are reversible with no key, so I just undo them in the opposite order (un-hex → un-reverse → un-Base64):

```sh
python3 -c "
import base64
enc='3d3d516343746d4d6d6c315669563362'
print(base64.b64decode(bytes.fromhex(enc)[::-1]).decode())"
# → oubWYf2kBq
```

Then submit the recovered secret:

```sh
curl -sS --user natas8 --data-urlencode 'secret=oubWYf2kBq' -d 'submit=Submit' \
  http://natas8.natas.labs.overthewire.org/index.php
```

The page returns natas9's password.

## Verification record

The [saved authentication ledger](../evidence/ready-natas/natas-verification-redacted.json) records the method check and next-level authentication. Runtime passwords are redacted in that ledger.

## Flag

Recovered natas9 password: `UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9`, so the flag is:

```text
pcgCTF{UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9}
```

## Takeaway

Stacked encodings aren't protection — the only care needed is reversing the steps in the right order.

## References

- [Original archived challenge](../../challenges/solved/web-exploitation-natas/015-layers-of-encoding/README.md)
