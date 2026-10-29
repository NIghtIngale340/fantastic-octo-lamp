# Elliot's Secret Stash

**Platform:** PCGCTF · **Challenge ID:** 74 · **Category:** Steganography / Forensics · **Points:** 100

**Status:** Answer backed by the extracted payload. Exact PCGCTF submission not re-confirmed.

## The challenge

Recover the hidden message in the supplied audio.

## Solving it

The ZIP contains a WAV file. The saved extraction identifies a DeepSound header in its audio data, using normal-quality mode without encryption.

The [saved decoder](../../challenges/solved/steganography-forensics/074-elliot-s-secret-stash/solve.py) recovers each hidden byte from the low nibbles of two consecutive 16-bit audio samples. It checks the DeepSound record markers and the recovered MP4 hash before writing `digital revolut.mp4`.

Run it from the original challenge directory:

```sh
python3 solve.py
```

The hidden video briefly displays `flag{hello_Elliot}` at about 39 seconds. The recovered frame below shows the result. The challenge requests the `pcgCTF` wrapper, with the capital `E` preserved.

## Screenshot

Recovered video frame at approximately 39 seconds:

![Flag visible in the recovered video](../../challenges/solved/steganography-forensics/074-elliot-s-secret-stash/evidence/flag-frame-39s.png)

## Flag

```text
pcgCTF{hello_Elliot}
```

## Takeaway

A missing password doesn't mean there's no payload — DeepSound can carry unencrypted files, so check for its header before concluding the audio is clean.

## Reference

- [Original challenge description](../../challenges/solved/steganography-forensics/074-elliot-s-secret-stash/README.md)
