# ELLIOT'S SECRET STASH — solution

Recovered visual flag: **`flag{hello_Elliot}`**.

Submission candidate in the challenge's requested format:

```text
pcgCTF{hello_Elliot}
```

Preserve the capital **E** in `Elliot`.

## Extraction

The supplied ZIP contains `Dubwreckerz - Digital Revolution (Anonymous VIP).wav`. Its WAV `data` chunk starts at file offset **46**. The installed John the Ripper helper recognizes a DeepSound header there:

```sh
deepsound2john -v 'evidence/Dubwreckerz - Digital Revolution (Anonymous VIP).wav'
```

The helper reports normal-quality encoding and **no encryption**. Its lack of a password hash does not mean that the file lacks hidden data.

Normal-quality DeepSound encodes each hidden byte using the low nibbles of two consecutive 16-bit audio samples:

```python
hidden_byte = ((carrier[i] & 0x0f) << 4) | (carrier[i + 2] & 0x0f)
```

Decoding the audio data reveals:

- Header `DSCF 04 00`: normal-quality mode, unencrypted.
- File-record marker `DSSF`.
- A 20-byte filename field containing `digital revolut.mp4`.
- A big-endian file length of **8,857,850 bytes**.
- Four zero initialization bytes, followed by the MP4, alignment padding, and the closing `DSSF` marker.

[solve.py](solve.py) reproduces the extraction from the original ZIP, checks the ZIP member's CRC, record markers, payload length and recovered MP4 SHA-256, then writes the video and [verification record](evidence/verification.json).

```sh
python solve.py
```

The extracted video decodes successfully with FFmpeg. The flag appears beneath the scrolling manifesto at approximately **39 seconds**. Inspecting only a frame every three seconds missed it; the one-frame-per-second contact sheet exposed the brief overlay.

To reproduce the saved visual evidence, from this challenge directory:

```sh
ffmpeg -i 'evidence/digital revolut.mp4' -vf 'fps=1,select=eq(n\,39)' -frames:v 1 evidence/flag-frame-39s.png
```

![Recovered flag in the hidden video](evidence/flag-frame-39s.png)

## Evidence

- [Extracted hidden video](evidence/digital%20revolut.mp4)
- [Flag frame](evidence/flag-frame-39s.png)
- [Video contact sheet](evidence/video-contact-sheet-every-second.jpg)
- [Video stream and container metadata](evidence/video-probe.json)
- [Hashes and extraction checks](evidence/verification.json)

The decoder's nibble layout is independently consistent with the installed `/usr/share/john/deepsound2john.py`, written by [Ryan Govostes](https://ryan.govost.es/2018/deepsound/). [DeepSound's official project](https://github.com/Jpinsoft/DeepSound) documents hiding and extracting files from audio. The actual flag comes from the supplied artifact, not a public walkthrough.

Status: locally recovered and evidence-backed; **PCGCTF acceptance has not been tested**. The source video uses `flag{...}` while this challenge explicitly asks for `pcgCTF{...}`.
