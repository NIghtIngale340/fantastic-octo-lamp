# Hash Me If You Can

**Platform:** PCGCTF · **Challenge ID:** 1 · **Category:** Cryptography · **Points:** 100

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Historical solved snapshot only; no password recovered in the saved materials or the new bounded dictionary attempt.

## Challenge and objective

Recover the password whose supplied 40-character digest is `530d378bd60243f41d169aad7cd238ae816a6ee3`.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/cryptography/001-hash-me-if-you-can/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The length and hexadecimal alphabet are consistent with a SHA-1 digest, but that shape alone does not prove the algorithm. A digest is one-way: decoding it as hex does not reveal the password. A defensible first test is to hash plausible candidates and compare their full digest to the supplied value.

## Step-by-step solution

### 1. Identify and save the candidate digest

`printf` writes exactly one candidate hash with a terminating newline. It avoids shell interpretation of the digest and gives the password-testing tool a reproducible input file. The 40 hex characters represent 20 bytes, matching SHA-1’s output size.

```sh
printf '%s\n' '530d378bd60243f41d169aad7cd238ae816a6ee3' > /tmp/pcgctf-hashme.sha1
```

**Recorded output / observation:**

```text
530d378bd60243f41d169aad7cd238ae816a6ee3
```

This supports testing SHA-1, while leaving the hash-family assumption explicit.

### 2. Test a bounded dictionary

`--format=raw-sha1` chooses unsalted SHA-1. `--wordlist` supplies candidate passwords; the temporary session and pot paths avoid writing into unrelated user state. This exact full dictionary pass was run during drafting.

```sh
john --session=/tmp/pcgctf-solved-hash --format=raw-sha1 --wordlist=/usr/share/wordlists/rockyou.txt --pot=/tmp/pcgctf-solved.pot /tmp/pcgctf-hashme.sha1
```

**Recorded output / observation:**

```text
Loaded 1 password hash (Raw-SHA1)
0g ... DONE
Session completed.
```

Zero guesses recovered a matching password in this wordlist. A separate focused test of platform names and common suffixes also failed. Neither result proves that the digest is not SHA-1 or that the password is strong.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #1 — actual evidence capture

![001-digest-evidence.png](../screenshots/001-digest-evidence.png)

Inspect original hash, without pretending the unknown plaintext was recovered.

Command/action actually executed:

```sh
python -c "h='530d378bd60243f41d169aad7cd238ae816a6ee3';print('Digest:',h);print('Hex length:',len(h));print('SHA-1 candidate: 160 bits; preimage remains unrecovered')"
```

[Actual command transcript](../screenshots/capture-work/001-hash-check.terminal.log) · [Execution record](../screenshots/capture-work/001-hash-check.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #1 — actual bounded dictionary attempt

![001-actual-dictionary-attempt.png](../screenshots/001-actual-dictionary-attempt.png)

Actual fresh dictionary recovery attempt with explicit20-secondbound; no inventedplaintext.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/dictionary_evidence.py 1
```

[Actual command transcript](../screenshots/capture-work/001-dictionary-proof.terminal.log) · [Execution record](../screenshots/capture-work/001-dictionary-proof.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

**Exact recovered flag not available.** The solved snapshot establishes a historical solve, but it does not retain the submitted string. No flag has been invented for this draft.

Historical solved snapshot only; no password recovered in the saved materials or the new bounded dictionary attempt.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- Recover the original accepted password from team submission history, or obtain a challenge hint that constrains the dictionary.
- If another hash family or salted construction is suggested, record that evidence before changing the algorithm assumption.
- Verify any recovered candidate by recomputing the full supplied digest, then capture the exact accepted flag spelling.

## What this challenge taught me

A hash-shaped value needs an algorithm hypothesis and a verified match, not an online “decoder” answer. Negative dictionary results are bounded evidence and must remain bounded.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/001-hash-me-if-you-can/README.md>)

## Fresh dictionary check

The screenshot pass ran John against the supplied digest/archive and the local RockYou dictionary. The actual run reached `DONE` / `Session completed` with `0g`: this dictionary produced no recovered password. The configured 20-second bound was not reached. The historical solved snapshot is retained, but no plaintext or new accepted flag was recovered.
