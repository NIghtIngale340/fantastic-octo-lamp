# CryptoMaze

**Platform:** PCGCTF · **Challenge ID:** 60 · **Category:** Cryptography · **Points:** 250

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Reproduce the provided LFSR output, derive a 128-bit AES key and decrypt the ciphertext.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/cryptography/060-cryptomaze/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The supplied state and tap positions fully determine a linear feedback shift register. The missing implementation choices are output position, shift direction and bit packing. The earlier solver identified the consistent convention: output state[0], shift left, append the XOR of taps, and pack bytes most-significant-bit first. AES is then tested with that derived key, not with a guessed dictionary password.

## Step-by-step solution

### 1. Generate and pack the first 128 output bits

`ast.literal_eval` reads the supplied list without executing code. XOR combines the four taps into the next feedback bit. Sixteen groups of eight output bits produce the 16-byte AES-128 key. The initial state is used before each shift.

```sh
python - <<'PY'
from pathlib import Path
import ast,re
t=Path('PCGCTF/solved/cryptography/060-cryptomaze/files/output.txt').read_text()
s=ast.literal_eval(re.search(r'\[[01,\s]+\]',t)[0]);bits=[]
for _ in range(128):
    bits.append(s[0]);s=s[1:]+[s[63]^s[61]^s[60]^s[58]]
k=bytes(int(''.join(map(str,bits[i:i+8])),2) for i in range(0,128,8))
print(k.hex())
PY
```

**Recorded output / observation:**

```text
912e6fe0b77afbd3f41c246cb5de62a7
```

The key matches the earlier recorded solver and was independently regenerated in this pass.

### 2. Decrypt ECB and validate all padding bytes

The ciphertext is three AES blocks and no IV is supplied. ECB is the convention that yields a coherent plaintext and valid PKCS#7 padding. The assertion checks the length and every padding byte before removing them; blindly cutting the last-byte count would be weaker validation.

```sh
python - <<'PY'
from pathlib import Path
import re
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
t=Path('PCGCTF/solved/cryptography/060-cryptomaze/files/output.txt').read_text()
c=bytes.fromhex(re.search(r'[0-9a-f]{80,}',t)[0])
d=Cipher(algorithms.AES(bytes.fromhex('912e6fe0b77afbd3f41c246cb5de62a7')),modes.ECB()).decryptor()
p=d.update(c)+d.finalize();n=p[-1]
assert 1<=n<=16 and p[-n:]==bytes([n])*n
print(p[:-n].decode())
PY
```

**Recorded output / observation:**

```text
pcgCTF{scr8mbledt_flvg_79d68fe0}
```

The entire plaintext and valid padding support the selected LFSR and AES conventions. The ciphertext length alone would not have proved ECB.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #60 — actual evidence capture

![060-step-01.png](../screenshots/060-step-01.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
python - <<'PY'
from pathlib import Path
import ast,re
t=Path('PCGCTF/solved/cryptography/060-cryptomaze/files/output.txt').read_text()
s=ast.literal_eval(re.search(r'\[[01,\s]+\]',t)[0]);bits=[]
for _ in range(128):
    bits.append(s[0]);s=s[1:]+[s[63]^s[61]^s[60]^s[58]]
k=bytes(int(''.join(map(str,bits[i:i+8])),2) for i in range(0,128,8))
print(k.hex())
PY
```

[Actual command transcript](../screenshots/capture-work/060-step-1.terminal.log) · [Execution record](../screenshots/capture-work/060-step-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #60 — actual evidence capture

![060-step-02.png](../screenshots/060-step-02.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
python - <<'PY'
from pathlib import Path
import re
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
t=Path('PCGCTF/solved/cryptography/060-cryptomaze/files/output.txt').read_text()
c=bytes.fromhex(re.search(r'[0-9a-f]{80,}',t)[0])
d=Cipher(algorithms.AES(bytes.fromhex('912e6fe0b77afbd3f41c246cb5de62a7')),modes.ECB()).decryptor()
p=d.update(c)+d.finalize();n=p[-1]
assert 1<=n<=16 and p[-n:]==bytes([n])*n
print(p[:-n].decode())
PY
```

[Actual command transcript](../screenshots/capture-work/060-step-2.terminal.log) · [Execution record](../screenshots/capture-work/060-step-2.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved result / candidate:

```text
pcgCTF{scr8mbledt_flvg_79d68fe0}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

A strong block cipher cannot protect a key derived from fully public deterministic inputs. Record generator conventions explicitly and validate the decrypted bytes rather than trusting a plausible prefix.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/060-cryptomaze/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/06_lfsr_aes_writeup.md>)
- [crypto-reproduction.json](</home/nightingale/CTF/PCGCTF/final-writeups/evidence-solved/crypto-reproduction.json>)
