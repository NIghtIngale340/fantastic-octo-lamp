# Multi-Base Layers — saved solution

Flag / submission candidate: `pcgCTF{ilove_Cyber_Command}`

Our original PCGCTF snapshot already marks this challenge solved. Answer independently corroborated from our original local evidence; teammate writeup preserved below. Existing solved snapshot unchanged.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Independent check

See [local decode / database results](../../../team-writeups/garcia-day1/independent-checks.json).

## Teammate’s writeup (quoted)

> ### Base Maze (250) & Multi-Base Layers (100) — same ciphertext
>
> **Flag (both):** `pcgCTF{ilove_Cyber_Command}`
>
> Both challenges ship the identical blob:
> ```
> 39313b75613738627032376e51695237702f5f68394d2f41553b2c274452376f693e6331302e4058394c32664d3163383622392f4b64513b2d3f6a6e39315e733b345a74716b
> ```
> Decoding layers, outermost to innermost:
> 1. **hex → ASCII** → `91;ua78bp27nQiR7p/_h9M/AU;,'DR7oi>c10.@X9L2fM1c86"9/KdQ;-?jn91^s;4Ztqk`
> 2. **ascii85 (a85)** → `KEYVER3FGJWHGYRTLJWFQMCOGVMW2VTZLAYE45TCK4YWQYTNKI4Q====`
> 3. **base32** → `Q1RGe2lsb3ZlX0N5YmVyX0NvbW1hbmR9`
> 4. **base64** → `CTF{ilove_Cyber_Command}`
>
> Wrap in the `pcgCTF{...}` format.
>
> ```python
> import binascii, base64
> h='39313b75613738627032376e51695237702f5f68394d2f41553b2c274452376f693e6331302e4058394c32664d3163383622392f4b64513b2d3f6a6e39315e733b345a74716b'
> raw=binascii.unhexlify(h).decode()
> s=base64.a85decode(raw)          # -> base32 text
> d=base64.b32decode(s)            # -> base64 text
> print(base64.b64decode(d))       # -> b'CTF{ilove_Cyber_Command}'
> ```
>
> ---
