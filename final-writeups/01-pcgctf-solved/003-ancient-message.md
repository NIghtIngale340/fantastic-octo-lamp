# Ancient Message

**Platform:** PCGCTF · **Challenge ID:** 3 · **Category:** Cryptography · **Points:** 100

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Decrypt `Frdvw Jxdug Fbehu Frppdqg` using the description’s three-position alphabet shift.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/cryptography/003-ancient-message/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The ciphertext preserves word lengths and capitalization. The prompt explicitly supplies the alphabet and shift, so frequency analysis or a large brute force is unnecessary. Caesar encryption moves each letter by a fixed number of positions; decryption reverses that movement modulo 26.

## Step-by-step solution

### 1. Reverse the stated shift

The code chooses the correct alphabet base for each letter, subtracts three, and uses `% 26` to wrap around. Spaces are copied untouched. This directly implements the hint without changing the word boundaries.

```sh
python - <<'PY'
s='Frdvw Jxdug Fbehu Frppdqg'
out=[]
for c in s:
    if c.isalpha():
        a=ord('A' if c.isupper() else 'a')
        out.append(chr((ord(c)-a-3)%26+a))
    else:
        out.append(c)
print(''.join(out))
PY
```

**Recorded output / observation:**

```text
Coast Guard Cyber Command
```

Readable plaintext across every word confirms the direction of the shift. Adding three to each plaintext letter reproduces the original ciphertext.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #3 — actual evidence capture

![003-step-01.png](../screenshots/003-step-01.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
python - <<'PY'
s='Frdvw Jxdug Fbehu Frppdqg'
out=[]
for c in s:
    if c.isalpha():
        a=ord('A' if c.isupper() else 'a')
        out.append(chr((ord(c)-a-3)%26+a))
    else:
        out.append(c)
print(''.join(out))
PY
```

[Actual command transcript](../screenshots/capture-work/003-step-1.terminal.log) · [Execution record](../screenshots/capture-work/003-step-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved result / candidate:

```text
pcgCTF{Coast Guard Cyber Command}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

The plaintext is independently recovered. The challenge does not specify replacing spaces with underscores; this draft therefore preserves spaces in the candidate and does not claim that its exact spelling was the historical accepted submission.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

A supplied Caesar shift is a transformation rule, not a password. Preserve punctuation and case while testing both the plaintext and its reversible mapping.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/003-ancient-message/README.md>)
