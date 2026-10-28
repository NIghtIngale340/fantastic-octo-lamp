# HIT A BRICK WALL

## Challenge information

Platform: **PCGCTF**, challenge **77**, **Forensics / Steganography**, **100 points**. No difficulty badge was supplied. [Original description and PNG](../../unsolved/forensics-steganography/077-hit-a-brick-wall/README.md).

The description moves the usual hidden-key locations aside and points to a wall: “The clue may be hiding in the writing itself.” The attachment is `bricks.png`, a small drawing of a wall and door. The objective is to recover its hidden message.

**New result from this documentation pass:** directly decoded `flag{b1nary}`. The submission candidate under the stated wrapper is **`pcgCTF{b1nary}`**. It has not been submitted or accepted. The original inventory marked this challenge unresolved; the evidence below justifies documenting a newly recovered answer without rewriting that original snapshot.

## Initial inspection

The drawing has twelve horizontal rows of bricks. The first eight complete bricks in each row use two recurring pale colors. Those color changes are not random texture: they repeat in groups that can represent binary digits. The half brick at the left edge of alternating rows must be excluded, otherwise the bit grouping shifts.

Before using that interpretation, the independent triage inspected the PNG chunks, metadata and pixel colors. `exiftool` reported a 1232 × 694 RGBA PNG created with GIMP, including a thumbnail and color profile. The file has no appended bytes beyond IEND. No literal flag was obtained from metadata. These checks made it reasonable to examine the visible design rather than claim an unseen appended archive.

```sh
exiftool '/home/nightingale/CTF/PCGCTF/unsolved/forensics-steganography/077-hit-a-brick-wall/files/bricks.png'
```

`exiftool` reads structured metadata rather than merely searching compressed bytes. The recorded properties identify the carrier, not the answer. A thumbnail or editor name is not proof of hidden text.

## Reading the wall as bytes

A byte contains eight bits. Treat the lighter brick RGB `(240, 227, 213)` as **0** and the slightly darker brick RGB `(224, 212, 199)` as **1**. Read eight complete bricks left to right, then move down one row. Sampling near brick centers avoids mortar lines and the door shadow.

The actual decoder sampled y-coordinates `38 + 56 * row` for zero-based rows 0–11. Alternating rows begin with a complete brick center at x=115 or x=62, and subsequent centers are approximately 108.5 pixels apart. These are measured coordinates for this supplied image, not universal PNG constants.

```python
from PIL import Image
im = Image.open('/home/nightingale/CTF/PCGCTF/unsolved/forensics-steganography/077-hit-a-brick-wall/files/bricks.png').convert('RGB')
message = ''
for row in range(12):
    y = 38 + 56 * row
    first_x = 115 if row % 2 == 0 else 62
    colors = [im.getpixel((round(first_x + 108.5 * c), y))
              for c in range(8)]
    bits = ''.join('0' if c == (240, 227, 213) else
                   '1' if c == (224, 212, 199) else '?'
                   for c in colors)
    assert '?' not in bits
    message += chr(int(bits, 2))
print(message)
```

`convert('RGB')` makes color comparisons explicit. `getpixel` samples a measured brick center; the conditional maps the two observed colors to bits. `int(bits, 2)` interprets a row as a base-two number, and `chr` maps that number to a character. The assertion rejects an unexpected color instead of silently treating door pixels as data.

Actual output:

```text
flag{b1nary}
```

| Wall row | Bits | Decimal | Character |
|---:|---|---:|---|
| 1 | `01100110` | 102 | `f` |
| 2 | `01101100` | 108 | `l` |
| 3 | `01100001` | 97 | `a` |
| 4 | `01100111` | 103 | `g` |
| 5 | `01111011` | 123 | `{` |
| 6 | `01100010` | 98 | `b` |
| 7 | `00110001` | 49 | `1` |
| 8 | `01101110` | 110 | `n` |
| 9 | `01100001` | 97 | `a` |
| 10 | `01110010` | 114 | `r` |
| 11 | `01111001` | 121 | `y` |
| 12 | `01111101` | 125 | `}` |

The readable braces and flag prefix make the grouping self-consistent. The character after `b` is the digit **1**, not a lowercase letter `i`.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #77 — actual offline reproduction

![077-decisive-result.png](../screenshots/077-decisive-result.png)

Run the exact independently checked decoder/check.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/077-reproduce.py
```

[Actual command transcript](../screenshots/capture-work/077-decode.terminal.log) · [Execution record](../screenshots/capture-work/077-decode.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### 077-brick-ascii-decode.png

![077-brick-ascii-decode.png](../screenshots/077-brick-ascii-decode.png)

Actual terminal execution of the measured brick-color ASCII decoder.

## Cross-check, flag formatting and verification

The [original challenge creator’s publication](https://www.paulhempshall.com/blog/free-dfir-steganography-ctf-challenges/) independently gives the same raw flag and describes the writing-on-the-wall idea. That source was useful corroboration; the row-by-row extraction above independently establishes it from our attachment.

The artifact spells `flag{b1nary}`; the saved PCGCTF task explicitly requests `pcgCTF{theflaghere.......}`. Preserving the payload and applying that required wrapper gives `pcgCTF{b1nary}`. No successful submission is asserted. Final confirmation requires submitting that exact candidate when the platform is available and recording its real response.

## Lesson

The carrier’s ordinary visual structure was the encoding. Counting eight complete bricks and preserving row alignment mattered more than running a large collection of steganography tools. Metadata triage ruled out easy alternatives, but the decisive operation was converting two visible colors into ASCII bytes.
