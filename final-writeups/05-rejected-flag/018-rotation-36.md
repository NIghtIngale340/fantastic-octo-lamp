# Rotation 36

**Platform:** PCGCTF · **Challenge ID:** 18 · **Category:** Cryptography · **Points:** 100

**Status:** Rejected Flag — under investigation. The decode is proven by a full round-trip, but every obvious wrapper/case variant was rejected, and no accepted string is known. Honest writeup.

## The challenge

A Caesar shift over a custom 36-character alphabet (`A–Z` plus `0–9`). Recover the hidden code.

## Solving it

The attachment defines the ring as `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789` — so the position after `Z` is `0`, and digits rotate too. I decoded by rotating back 19 and verified by re-encrypting (`+19`) and checking the whole file matches:

```python
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
rot = lambda t,s: ''.join(alphabet[(alphabet.index(c.upper())+s)%36] if c.upper() in alphabet else c for c in t)
pt = rot(ciphertext, -19)
assert rot(pt, 19) == ciphertext   # full round-trip
print(pt)
```

```text
AGENT, THIS IS A SCRAMBLED BULLETIN. SHIFT ACROSS A CUSTOM ALPHABET (A-Z AND 0-9).
RECOVER THE HIDDEN CODE TO PROCEED: FLAG{CAESAR_SHIFT_19_ALNUM}
```

The round-trip assertion over the whole file (whitespace included) is strong proof the transform is right — there's no second encoded suffix.

## Screenshot

![018-script-1.png](../screenshots/018-script-1.png)

## Flag — rejected, unresolved

The decoded payload is `FLAG{CAESAR_SHIFT_19_ALNUM}`, but submissions failed:

| Candidate | Outcome | Evidence |
|---|---|---|
| `pcgCTF{CAESAR_SHIFT_19_ALNUM}` | Incorrect | user screenshot in chat (original image no longer on disk) |
| `FLAG{CAESAR_SHIFT_19_ALNUM}` | Rejected | user report |
| `pcgCTF{caesar_shift_19_alnum}` | Incorrect | prior assistant test |

The cipher is case-insensitive, so the original capitalization can't be recovered from the math alone — that may be the issue, or the served attachment may differ from the archived one.

## Still to do

- Re-run the script against the *currently served* attachment and compare its SHA-256 with the archived round-trip record.
- Pull the live hint / required format, and ask the organizer for clarification rather than guessing more variants.

## Takeaway

A correct transformation and an accepted submission are two different checks. Here the decode is proven by a full round-trip; the submission isn't accepted. The honest result is a diagnostic record, not an invented flag.

## Reference

- [Original challenge description](../../unsolved/cryptography/018-rotation-36/README.md)
