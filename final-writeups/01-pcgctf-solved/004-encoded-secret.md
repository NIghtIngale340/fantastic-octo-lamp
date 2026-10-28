# Encoded Secret

**Platform:** PCGCTF · **Challenge ID:** 4 · **Category:** Cryptography · **Points:** 100

**Status:** Solved in the last snapshot; decode reproduced locally.

## The challenge

Decode an intercepted Base64 string. The "once is enough?" hint is a tell that it's nested.

## Solving it

Base64 is encoding, not encryption — you just peel it. After each decode I looked at the result instead of guessing how many layers there were:

```sh
python3 -c "import base64; x=b'VVRGU1IyVXlOV3hrYlZaNVdETk9NR0l6UW1aaVIxWm9ZMjAxY0dKdFpEaz0='
for i in range(3): x=base64.b64decode(x); print(x.decode())"
```

```text
UTFSR2UyNWxkbVZ5WDNOMGIzQmZiR1ZoY201cGJtZDk=
Q1RGe25ldmVyX3N0b3BfbGVhcm5pbmd9
CTF{never_stop_learning}
```

Layers one and two are still valid Base64; layer three is the flag. A fourth decode fails because `{` and `}` aren't Base64 characters — that failure is the natural "you're done" signal.

## Screenshot

![004-step-01.png](../screenshots/004-step-01.png)

## Flag

```text
CTF{never_stop_learning}
```

The decoded prefix is `CTF`, and this challenge's saved description doesn't record a `pcgCTF` wrapper, so I left the raw result rather than normalizing it.

## Takeaway

You can recognize each encoding from its output alphabet, and a structured result (or a clean failure) tells you when to stop. More decoding isn't more certainty.

## References

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/004-encoded-secret/README.md>)
