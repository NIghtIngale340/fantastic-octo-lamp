# EMBEDDED TEXT

**Platform:** PCGCTF · **Challenge ID:** 71 · **Category:** Steganography · **Points:** 100

**Status:** Solved in the old snapshot, but the archive password and hidden text weren't saved, and my bounded cracking attempt here didn't recover them. Honest partial.

## The challenge

Extract a hidden payload from `embedded-text.jpg` — which is itself inside an encrypted ZIP.

## Solving it

The carrier image is locked inside a password-protected ZIP, so that outer layer has to come off before any steghide/metadata claims mean anything. I confirmed the archive's one encrypted member without needing the password:

```sh
zipinfo -v embedded-text.zip
```

```text
embedded-text.jpg — 121896 bytes, encrypted
```

Then tried to crack the ZIP password (rockyou, plus a short digit sweep and common CTF passwords):

```sh
zip2john embedded-text.zip > zip.hash
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
```

```text
Loaded 1 password hash (PKZIP)
0g 0:00:00:00 DONE
Session completed.
```

No luck in those bounded searches. Without the JPEG I can't run the steghide step — that stays a next step, not a result I'm claiming.

## Screenshots

![071-archive-evidence.png](../screenshots/071-archive-evidence.png)

![071-actual-dictionary-attempt.png](../screenshots/071-actual-dictionary-attempt.png)

## Flag

Not recovered. The snapshot records a solve but doesn't keep the string, and I couldn't open the archive here. No flag invented.

## Still to do

- Get the archive password from the original team notes or organizer instructions.
- Once the ZIP opens, run `file` / `exiftool` / `steghide info` on the JPEG and preserve the exact extraction.

## Takeaway

It's fine to stop at a real access boundary (the encrypted archive) rather than inventing the inner payload. Record what was tested and ask for the missing password.

## References

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/steganography/071-embedded-text/README.md>)
