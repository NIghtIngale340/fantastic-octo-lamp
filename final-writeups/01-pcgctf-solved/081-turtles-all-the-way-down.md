# TURTLES ALL THE WAY DOWN

**Platform:** PCGCTF · **Challenge ID:** 81 · **Category:** Steganography · **Points:** 100

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Find the altered turtle image and recover the flag concealed below its displayed height.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/steganography/081-turtles-all-the-way-down/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The archive contains nineteen JPEGs and one PNG. The last image is also visibly unhappy, which matches the wording. Rather than assuming LSB steganography, compare its declared dimensions with its decompressed pixel data. PNG stores width and height in IHDR and compressed scanlines in IDAT; those two representations should agree.

## Step-by-step solution

### 1. Compare the image dimensions

The archive was extracted locally with Python’s ZipFile. Pillow reads format and geometry for each member, making a modified canvas easier to spot. The images vary naturally, so the file type and unhappy subject are clues, not proof on their own.

```sh
python - <<'PY'
from pathlib import Path
from PIL import Image
p=Path('PCGCTF/final-writeups/evidence-solved/81/ctf')
for f in p.iterdir():
    im=Image.open(f);print(f.name,im.size,im.format)
PY
```

**Recorded output / observation:**

```text
19.jpg (1000, 1000) JPEG
20.png (1000, 848) PNG
```

The PNG’s cropped-looking bottom and explicit dimension hint justify checking how many scanlines its IDAT data actually contains.

### 2. Count the stored RGBA rows and repair only the copy

The original IHDR specifies 8-bit RGBA, so each 1000-pixel scanline needs 4000 data bytes plus one PNG filter byte. The 4,001,000 decompressed bytes therefore contain exactly 1000 rows. Height 848 hides the bottom 152 rows. The script changes the height to 1000 and recomputes the IHDR CRC over its chunk type and data, leaving the original file untouched.

```sh
python - <<'PY'
from pathlib import Path
import struct,zlib
p=Path('PCGCTF/final-writeups/evidence-solved/81/ctf/20.png');b=p.read_bytes();o=8;data=b''
while o<len(b):
    n=struct.unpack('>I',b[o:o+4])[0];kind=b[o+4:o+8]
    if kind==b'IDAT':data+=b[o+8:o+8+n]
    o+=n+12
raw=zlib.decompress(data);print('decompressed bytes:',len(raw))
assert len(raw)==1000*(1+1000*4)
c=bytearray(b);c[20:24]=struct.pack('>I',1000)
c[29:33]=struct.pack('>I',zlib.crc32(c[12:29])&0xffffffff)
p.with_name('20-restored.png').write_bytes(c)
PY
```

**Recorded output / observation:**

```text
decompressed bytes: 4001000
Restored visual text: flag{coffee_first_then_smiles}
```

Opening the repaired copy reveals the flag below the original visible canvas. It is not necessary to alter pixel data or guess an XOR key.

## Visual evidence

![Original image: declared height 848 hides the text.](/home/nightingale/CTF/PCGCTF/final-writeups/evidence-solved/81/ctf/20.png)

Original image: declared height 848 hides the text.

![Restored height 1000: the original stored bottom rows reveal the flag.](/home/nightingale/CTF/PCGCTF/final-writeups/evidence-solved/81/20-restored.png)

Restored height 1000: the original stored bottom rows reveal the flag.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #81 — actual evidence capture

![081-step-01.png](../screenshots/081-step-01.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
python - <<'PY'
from pathlib import Path
from PIL import Image
p=Path('PCGCTF/final-writeups/evidence-solved/81/ctf')
for f in p.iterdir():
    im=Image.open(f);print(f.name,im.size,im.format)
PY
```

[Actual command transcript](../screenshots/capture-work/081-step-1.terminal.log) · [Execution record](../screenshots/capture-work/081-step-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #81 — actual evidence capture

![081-step-02.png](../screenshots/081-step-02.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
python - <<'PY'
from pathlib import Path
import struct,zlib
p=Path('PCGCTF/final-writeups/evidence-solved/81/ctf/20.png');b=p.read_bytes();o=8;data=b''
while o<len(b):
    n=struct.unpack('>I',b[o:o+4])[0];kind=b[o+4:o+8]
    if kind==b'IDAT':data+=b[o+8:o+8+n]
    o+=n+12
raw=zlib.decompress(data);print('decompressed bytes:',len(raw))
assert len(raw)==1000*(1+1000*4)
c=bytearray(b);c[20:24]=struct.pack('>I',1000)
c[29:33]=struct.pack('>I',zlib.crc32(c[12:29])&0xffffffff)
p.with_name('20-restored.png').write_bytes(c)
PY
```

[Actual command transcript](../screenshots/capture-work/081-step-2.terminal.log) · [Execution record](../screenshots/capture-work/081-step-2.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved result / candidate:

```text
pcgCTF{coffee_first_then_smiles}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

The script writes its repaired copy alongside `ctf/20.png`; the displayed evidence was independently generated and saved at `evidence-solved/81/20-restored.png`. Both contain the same corrected IHDR and pixel data.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

A file header can conceal existing content by describing an incomplete canvas. Cross-check lengths against the actual pixel encoding and repair a copy with the proper checksum.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/steganography/081-turtles-all-the-way-down/README.md>)
