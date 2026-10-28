# Common Modulus

**Platform:** PCGCTF · **Challenge ID:** 66 · **Category:** Cryptography · **Points:** 250

**Difficulty:** Medium (stated in supplied artifact).

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Recover the identical plaintext encrypted under one RSA modulus and two coprime exponents.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/cryptography/066-common-modulus/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The shared modulus is the key clue. With e1=3 and e2=5, Bézout’s identity gives `2·3 − 1·5 = 1`. Multiplying the first ciphertext squared by the inverse of the second cancels the exponents and leaves the message modulo n. This is a common-modulus attack; it does not require recovering either private exponent.

## Step-by-step solution

### 1. Combine the ciphertexts and re-encrypt the result

Three-argument `pow` performs modular arithmetic efficiently. The exponent −1 requests a modular inverse, which exists here because the ciphertext is invertible modulo n. Both assertions re-encrypt the recovered integer with the original public parameters; they test the result against two independent ciphertext equations.

```sh
python - <<'PY'
from pathlib import Path
import re
t=Path('PCGCTF/solved/cryptography/066-common-modulus/files/04_rsa_common_modulus.txt').read_text()
d={k:int(v) for k,v in re.findall(r'(n|e1|e2|c1|c2)\s*=\s*(\d+)',t)}
n=d['n'];m=pow(d['c1'],2,n)*pow(d['c2'],-1,n)%n
assert pow(m,d['e1'],n)==d['c1']
assert pow(m,d['e2'],n)==d['c2']
print(m.to_bytes((m.bit_length()+7)//8,'big').decode())
PY
```

**Recorded output / observation:**

```text
pcgctf{common_modulus_common_mistake}
```

The same recovered message reproduces both ciphertexts, confirming that the shared-modulus algebra was applied correctly.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #66 — actual evidence capture

![066-step-01.png](../screenshots/066-step-01.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
python - <<'PY'
from pathlib import Path
import re
t=Path('PCGCTF/solved/cryptography/066-common-modulus/files/04_rsa_common_modulus.txt').read_text()
d={k:int(v) for k,v in re.findall(r'(n|e1|e2|c1|c2)\s*=\s*(\d+)',t)}
n=d['n'];m=pow(d['c1'],2,n)*pow(d['c2'],-1,n)%n
assert pow(m,d['e1'],n)==d['c1']
assert pow(m,d['e2'],n)==d['c2']
print(m.to_bytes((m.bit_length()+7)//8,'big').decode())
PY
```

[Actual command transcript](../screenshots/capture-work/066-step-1.terminal.log) · [Execution record](../screenshots/capture-work/066-step-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved result / candidate:

```text
pcgctf{common_modulus_common_mistake}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Reusing RSA’s modulus across distinct exponents can turn separate encryptions into a solvable linear relation in the exponents. Re-encryption is a stronger validation than recognizing a flag prefix.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/066-common-modulus/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/04_rsa_common_modulus_writeup.md>)
- [crypto-reproduction.json](</home/nightingale/CTF/PCGCTF/final-writeups/evidence-solved/crypto-reproduction.json>)
