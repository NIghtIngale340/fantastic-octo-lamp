# Hash Me If You Can

**Platform:** PCGCTF · **Challenge ID:** 1 · **Category:** Cryptography · **Points:** 100

**Status:** Marked solved in the old snapshot, but the saved materials don't keep the password, and my dictionary run here didn't recover it either.

## The challenge

Recover the password behind this digest:

```text
530d378bd60243f41d169aad7cd238ae816a6ee3
```

## Working it

The digest has 40 hexadecimal characters, which is consistent with SHA-1. That gives a starting point for password guessing, although the length alone does not identify the algorithm.

The saved dictionary run used John with the Raw-SHA1 format and RockYou. The screenshot includes the full command and run settings. This is a shorter version of that command, assuming the digest has been saved in `hash.txt`:

```sh
john --format=raw-sha1 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

The recorded run completed without recovering a password. An additional check of platform names and common suffixes also found no match. These results only cover the guesses tested.

## Verification record

The [saved dictionary-run transcript](../screenshots/capture-work/001-dictionary-proof.terminal.log) records the command, its limits, and the unsuccessful result.

## Flag

Not recovered. The saved scoreboard marks this challenge as solved, but the accepted password is missing from the archive.

## Still to do

- Dig the original password out of the team's submission history, or get a hint that narrows the wordlist.
- If a different hash family or a salt turns up, record that before changing the SHA-1 assumption.
- Confirm any candidate by recomputing the full digest before trusting it.

## Takeaway

A hash-shaped string needs an algorithm guess plus a verified match — not an online "decoder." And a dictionary miss is only ever a miss, not proof the password is strong.

## Reference

- [Original challenge and attachments](<../../home/nightingale/CTF/PCGCTF/solved/cryptography/001-hash-me-if-you-can/README.md>)
