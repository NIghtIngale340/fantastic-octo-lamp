# INTERCEPTED

**Platform:** PCGCTF · **Challenge ID:** 78 · **Category:** Forensics / Email Analysis · **Points:** 150

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Find the concealed message in the intercepted email’s custom headers.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/forensics-email-analysis/078-intercepted/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The body contains only a meeting pretext. Most long mail headers are ordinary authentication signatures and should not be treated as ciphertext merely because they look random. The unusual pair is `X-Spam-Signature` and `X-Spam-Validator`: one is Base64-shaped, while the other is hex that decodes to a readable key phrase.

## Step-by-step solution

### 1. Inspect the custom spam headers

The anchored expression selects those exact header names rather than the unrelated ARC and DKIM signature fields. `-E` enables the alternation, and the quotes keep the shell from interpreting the parentheses.

```sh
grep -E '^X-Spam-(Signature|Validator):' PCGCTF/solved/forensics-email-analysis/078-intercepted/files/intercepted.txt
```

**Recorded output / observation:**

```text
X-Spam-Signature: PABZTAYKDRkNAFkCBwlHBRtN...
X-Spam-Validator: 6b65792d746f2d7468652d6b696e67646f6d
```

The signature is abbreviated here for readability; the reproducible script below reads its full value from the original file. The validator bytes spell `key-to-the-kingdom`.

### 2. Undo Base64 and repeating-key XOR

Base64 recovers the encoded bytes. The hex validator yields the key bytes; indexing the key modulo its length repeats it across the message. XOR is its own inverse, so the same operation removes the repeating mask. The entire recovered plaintext is saved as evidence, not inferred from a flag prefix.

```sh
python - <<'PY'
from pathlib import Path
import re,base64
s=Path('PCGCTF/solved/forensics-email-analysis/078-intercepted/files/intercepted.txt').read_text()
c=base64.b64decode(re.search(r'^X-Spam-Signature: (.+)$',s,re.M)[1])
k=bytes.fromhex(re.search(r'^X-Spam-Validator: (.+)$',s,re.M)[1])
p=bytes(b^k[i%len(k)] for i,b in enumerate(c))
print(k.decode());print(p.decode())
PY
```

**Recorded output / observation:**

```text
key-to-the-kingdom
We are meeting at 5 pm opposite the left side trashcan next to the entrance of Fakecity Train Station. Bring the tools.

flag{something_is_about_to_happen}
```

A coherent meeting instruction plus a complete flag validates the relationship between the two custom fields. The explicit challenge wrapper changes only `flag` to `pcgCTF`.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #78 — actual evidence capture

![078-step-01.png](../screenshots/078-step-01.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
grep -E '^X-Spam-(Signature|Validator):' PCGCTF/solved/forensics-email-analysis/078-intercepted/files/intercepted.txt
```

[Actual command transcript](../screenshots/capture-work/078-step-1.terminal.log) · [Execution record](../screenshots/capture-work/078-step-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #78 — actual evidence capture

![078-step-02.png](../screenshots/078-step-02.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
python - <<'PY'
from pathlib import Path
import re,base64
s=Path('PCGCTF/solved/forensics-email-analysis/078-intercepted/files/intercepted.txt').read_text()
c=base64.b64decode(re.search(r'^X-Spam-Signature: (.+)$',s,re.M)[1])
k=bytes.fromhex(re.search(r'^X-Spam-Validator: (.+)$',s,re.M)[1])
p=bytes(b^k[i%len(k)] for i,b in enumerate(c))
print(k.decode());print(p.decode())
PY
```

[Actual command transcript](../screenshots/capture-work/078-step-2.terminal.log) · [Execution record](../screenshots/capture-work/078-step-2.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved result / candidate:

```text
pcgCTF{something_is_about_to_happen}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Header names can camouflage a covert channel as spam-processing metadata. Distinguish arbitrary long signatures from a linked key/ciphertext pair and validate the whole recovered message.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/forensics-email-analysis/078-intercepted/README.md>)
- [078-decoded.txt](</home/nightingale/CTF/PCGCTF/final-writeups/evidence-solved/078-decoded.txt>)
