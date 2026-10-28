# Elliot's Secret Stash

**Platform:** PCGCTF · **Challenge ID:** 74 · **Category:** Steganography / Forensics · **Points:** 100

**Status:** Answer backed by the extracted payload. Exact PCGCTF submission not re-confirmed.

## The challenge

Recover the hidden message in the supplied audio.

## Solving it

The Mr. Robot / Elliot theme points at DeepSound — a tool that hides files inside audio. The carrier has the DeepSound header, and it doesn't require a password here, so I extracted the embedded file:

```sh
# DeepSound carrier → extract embedded file(s)
```

The recovered payload (a short video/message) contains:

```text
hello_Elliot
```

## Screenshot

![074-terminal-extraction.png](../screenshots/074-terminal-extraction.png)

## Flag

```text
pcgCTF{hello_Elliot}
```

## Takeaway

A missing password doesn't mean there's no payload — DeepSound can carry unencrypted files, so check for its header before concluding the audio is clean.

## Reference

- [Original challenge description](../../unsolved/steganography/074-elliot-s-secret-stash/README.md)
