# Small Exponent

**Platform:** PCGCTF · **Challenge ID:** 65 · **Category:** Cryptography · **Points:** 150

**Difficulty:** Medium (stated in supplied artifact).

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Recover an RSA plaintext encrypted with public exponent three when modular reduction never occurs.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/cryptography/065-small-exponent/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

RSA computes `c = m^e mod n`. A small exponent is not automatically a break, but an unpadded short message can satisfy `m^3 < n`. Then the ciphertext is an ordinary perfect cube. Testing an exact integer cube root is much cheaper and more relevant than factoring a 1024-bit modulus.

## Step-by-step solution

### 1. Take and validate an integer cube root

Binary search finds the floor cube root using integers only; floating-point arithmetic would lose precision at this size. The first assertion checks that the cube is exact. The second establishes why the modulus did not change it. Converting the integer to big-endian bytes reverses RSA’s message-to-integer representation.

```sh
python - <<'PY'
from pathlib import Path
import re
t=Path('PCGCTF/solved/cryptography/065-small-exponent/files/03_rsa_small_exponent.txt').read_text()
d={k:int(v) for k,v in re.findall(r'(n|e|ciphertext)\s*=\s*(\d+)',t)}
c=d['ciphertext'];lo=0;hi=1<<((c.bit_length()+2)//3)
while lo+1<hi:
    m=(lo+hi)//2
    if m**3<=c:lo=m
    else:hi=m
assert lo**3==c and lo**3<d['n']
print(lo.to_bytes((lo.bit_length()+7)//8,'big').decode())
PY
```

**Recorded output / observation:**

```text
pcgctf{rsa_small_exponents_are_dangerous}
```

The exact-root assertion and readable plaintext jointly validate the attack. No private key or factorization was required.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #65 — actual evidence capture

![065-step-01.png](../screenshots/065-step-01.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
python - <<'PY'
from pathlib import Path
import re
t=Path('PCGCTF/solved/cryptography/065-small-exponent/files/03_rsa_small_exponent.txt').read_text()
d={k:int(v) for k,v in re.findall(r'(n|e|ciphertext)\s*=\s*(\d+)',t)}
c=d['ciphertext'];lo=0;hi=1<<((c.bit_length()+2)//3)
while lo+1<hi:
    m=(lo+hi)//2
    if m**3<=c:lo=m
    else:hi=m
assert lo**3==c and lo**3<d['n']
print(lo.to_bytes((lo.bit_length()+7)//8,'big').decode())
PY
```

[Actual command transcript](../screenshots/capture-work/065-step-1.terminal.log) · [Execution record](../screenshots/capture-work/065-step-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved result / candidate:

```text
pcgctf{rsa_small_exponents_are_dangerous}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

The vulnerability is unpadded low-exponent RSA with a sufficiently small message, not merely choosing e=3. A solver should test the exact mathematical precondition rather than treating any near-root as plaintext.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/065-small-exponent/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/03_rsa_small_exponent_writeup.md>)
- [crypto-reproduction.json](</home/nightingale/CTF/PCGCTF/final-writeups/evidence-solved/crypto-reproduction.json>)
