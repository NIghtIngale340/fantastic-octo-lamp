# Weak RSA

## Challenge information

**PCGCTF #67 · Cryptography · 300 points.** The supplied text labels difficulty **Medium / Hard**; no separate platform badge is recorded. [Original description](../../unsolved/cryptography/067-weak-rsa/README.md) and [public key/ciphertext](../../unsolved/cryptography/067-weak-rsa/files/05_weak_rsa.txt).

The administrator calls the setup “RSA-65537,” but the hint says the mathematics is strong and the key generation is not. The objective is explicit: factor `n`, reconstruct the private exponent, and decrypt `c`. The requested source format is lowercase **`pcgctf{...}`**. **Status: unresolved; no plaintext or flag has been recovered.**

## What the parameters actually mean

RSA publishes a modulus `n` and exponent `e`. The common exponent 65537 is not the key length: our modulus is **512 bits**. For ordinary two-prime RSA, `n = p*q`; knowing both factors permits computing `phi(n) = (p-1)*(q-1)` and the inverse `d = e^-1 mod phi(n)`. Decryption is `m = c^d mod n`.

The hint points at factor generation, but it does not identify a specific weak-prime pattern. A small modulus can still resist simple local attacks when neither factor has the tested special structure. The correct workflow must validate a real factor before claiming the private key exists.

## Reproduced structural checks

The independent pass parsed the three numbers directly from the supplied text and evaluated:

```python
from math import gcd, isqrt
from sympy import isprime
from pathlib import Path
import re
source = Path('/home/nightingale/CTF/PCGCTF/unsolved/cryptography/067-weak-rsa/files/05_weak_rsa.txt').read_text()
n, e, c = [int(re.search(r'\b' + key + r'\s*=\s*(\d+)', source)[1])
           for key in ('n', 'e', 'c')]
print(n.bit_length(), e)
print(isprime(n), isqrt(n) ** 2 == n)
print(gcd(c, n), 0 < c < n)
```

Actual results:

```text
512 65537
False False
1 True
```

`bit_length` measures the modulus rather than the exponent. `isprime` confirms the integer is composite; the square check rules out equal factors. `gcd(c,n)=1` means the ciphertext does not trivially reveal a factor through a common divisor. The range check confirms the ciphertext is a valid residue. These observations narrow the problem but do not factor it. [Machine-readable results](../evidence/067/independent-checks.json).

A fresh read-only [FactorDB](https://factordb.com/) API lookup returned status **C** and only the original modulus, exponent 1, in its factors array. [Actual response](../evidence/067/factordb.json). C means the service records the number as composite; repeating the modulus in that array is not a nontrivial factorization.

## Earlier bounded attacks and their limits

The preserved [investigation log](../../unsolved/cryptography/067-weak-rsa/investigation.md) records unsuccessful Fermat increments, bounded SymPy factoring, pairwise GCD against other challenge moduli, near-square multiples, Pollard p−1 and ECM curves. In particular, the stronger ECM run used 500 curves with B1=50,000 and B2=500,000 and found no factor. Those historical parameters come from the saved log; their full terminal output is not preserved and this draft does not invent a transcript or rerun every expensive search.

Fermat is useful when p and q are close because it seeks `n=a²-b²`. Pollard p−1 targets a factor whose predecessor is smooth. ECM can discover a relatively small factor. Failure within a bound only excludes what that particular search tested; it does not prove the key was securely generated or that every factoring strategy has failed.

The public article linked in earlier notes illustrates the RSA workflow, but its example numbers do not belong to this modulus. Substituting someone else’s factors would produce an unrelated private key. Any proposed factor must satisfy `n % p == 0` before proceeding.

## Decryption procedure once a factor is found

The existing [solve.py](../../unsolved/cryptography/067-weak-rsa/solve.py) is a prepared verifier, not a completed factorization:

```sh
python '/home/nightingale/CTF/PCGCTF/unsolved/cryptography/067-weak-rsa/solve.py' '<verified-prime-factor-of-this-n>'
```

This is a **pending command**: the factor placeholder has no known value. The script rejects trivial/nondividing factors, checks both p and q are prime, computes phi and the modular inverse, and decrypts with Python’s three-argument `pow`. It then verifies `p*q == n` and re-encrypts the message to require `pow(m,e,n)==c`. This makes a later success auditable rather than merely accepting printable output.

```python
q = n // p
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
assert p * q == n
assert pow(m, e, n) == c
```

These are the solver’s mathematical steps, not observed plaintext. The integer must finally be converted to big-endian bytes and interpreted according to the supplied challenge format.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #67 — actual offline reproduction

![067-decisive-result.png](../screenshots/067-decisive-result.png)

Run the exact independently checked decoder/check.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/067-reproduce.py
```

[Actual command transcript](../screenshots/capture-work/067-decode.terminal.log) · [Execution record](../screenshots/capture-work/067-decode.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Result and lesson

The structural work is reproducible, but the required factor remains missing. A sensible continuation is a properly bounded general factoring effort or a newly available factor record, preserving parameters and output. The key lesson is that knowing the RSA equations does not replace recovering the key material, and that an exponent of 65537 says nothing about a 512-bit modulus’s strength.
