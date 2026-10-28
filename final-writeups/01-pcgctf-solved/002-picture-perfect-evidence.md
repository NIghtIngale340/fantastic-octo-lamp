# Picture Perfect Evidence

**Platform:** PCGCTF · **Challenge ID:** 2 · **Category:** Cryptography · **Points:** 100

**Status:** Solved in the last snapshot; I re-read the metadata for this writeup.

## The challenge

Find the camera "make" hidden in a JPEG's metadata. The thing in the picture isn't the answer — the device that took it is.

## Solving it

If the question is about the device, EXIF metadata is where to look. I pulled the make, model and software fields with exiftool:

```sh
exiftool -Make -Model -Software 'cydex (1).jpg'
```

```text
Make     : Iphone17PROMaxFULLYPAID
Model    : --
Software : MediaTek Camera Application
```

The make is `Iphone17PROMaxFULLYPAID`. Obviously that's not a real camera string — an iPhone make with a MediaTek software field is nonsense — so it's clearly been planted for the challenge. The answer is that exact string, odd capitalization and all; don't "tidy" it into a real brand name.

## Screenshots

![002-step-01.png](../screenshots/002-step-01.png)

![002-step-02.png](../screenshots/002-step-02.png)

## Flag

```text
pcgCTF{Iphone17PROMaxFULLYPAID}
```

## Takeaway

Metadata can be the whole challenge, and it can be edited. Read the exact field the question asks for instead of inferring the device from the other tags.

## References

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/002-picture-perfect-evidence/README.md>)
- [Saved EXIF dump](</home/nightingale/CTF/PCGCTF/final-writeups/evidence-solved/002-exif.txt>)
