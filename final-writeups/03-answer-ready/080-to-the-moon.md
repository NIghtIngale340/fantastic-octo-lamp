# To the Moon!

**Platform:** PCGCTF · **Challenge ID:** 80 · **Category:** Blockchain / Forensics · **Points:** 100

**Status:** Answer backed by the reproduced chain. Exact PCGCTF submission not re-confirmed.

## The challenge

Follow a hidden image payload through to a Bitcoin OP_RETURN flag.

## Solving it

A multi-stage trail:

1. **Stego** — extract the payload hidden in the image, which yields an encrypted ZIP.
2. **Crack the ZIP** — it's AES-256; John recovers the password `prisonbreak`. Inside is one text member with a wallet address `1NFoSEcGq4XwEbaXmio5yYaakbX5Gtia4R` (keep the Base58 casing exactly).
3. **Read the chain** — that wallet's transaction has an OP_RETURN output. Decoding its script:

```python
script = bytes.fromhex('6a1f666c61677b496e6630533363426c30636b636834316e416e346c797331357d')
# 6a = OP_RETURN, 1f = push 31 bytes → the rest is ASCII
print(script[2:].decode())   # flag{Inf0S3cBl0ckch41nAn4lys15}
```

```text
flag{Inf0S3cBl0ckch41nAn4lys15}
```

## Screenshots

![080-script-1.png](../screenshots/080-script-1.png)

![080-wallet-extraction.png](../screenshots/080-wallet-extraction.png)

![080-actual-stego-extraction.png](../screenshots/080-actual-stego-extraction.png)

## Flag

```text
pcgCTF{Inf0S3cBl0ckch41nAn4lys15}
```

## Takeaway

OP_RETURN outputs can carry arbitrary data on-chain — `6a` then a push length, then ASCII. The chain is the final hiding place after stego → cracked archive → wallet.

## Reference

- [Original challenge description](../../unsolved/blockchain-forensics/080-to-the-moon/README.md)
