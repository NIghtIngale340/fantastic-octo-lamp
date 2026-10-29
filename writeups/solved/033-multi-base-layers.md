# Multi-Base Layers

**Platform:** PCGCTF · **Challenge ID:** 33 · **Category:** Cryptography · **Points:** 100

**Status:** Solved in the last snapshot; decode reproduced locally.

## The challenge

Same shape as Base Maze (#20) — in fact it reuses the identical hex blob. Peel it back through hex, Ascii85, Base32 and Base64.

## Solving it

Hex digits, even length → start with hex → bytes. The output's punctuation alphabet points at Ascii85, then Base32 (uppercase + `=` padding), then a final Base64 decode:

Save this as `solve.py` and run `python3 solve.py`. [Download the script](../scripts/033-solve.py).

```python
from pathlib import Path
import base64

value = bytes.fromhex(Path("encoded.txt").read_text().strip())
print("Hex decoded:", value.decode())
value = base64.a85decode(value)
print("Ascii85 decoded:", value.decode())
value = base64.b32decode(value)
print("Base32 decoded:", value.decode())
value = base64.b64decode(value)
print("Base64 decoded:", value.decode())
```

```text
Hex decoded: 91;ua78bp27nQiR7p/_h9M/AU;,'DR7oi>c10.@X9L2fM1c86"9/KdQ;-?jn91^s;4Ztqk
Ascii85 decoded: KEYVER3FGJWHGYRTLJWFQMCOGVMW2VTZLAYE45TCK4YWQYTNKI4Q====
Base32 decoded: Q1RGe2lsb3ZlX0N5YmVyX0NvbW1hbmR9
Base64 decoded: CTF{ilove_Cyber_Command}
```

Source prefix is `CTF`; the challenge wrapper is `pcgCTF`. Keep `ilove_Cyber_Command` verbatim.

## Screenshots

Fresh local reproduction using the command described above.

![Command and result](../screenshots/033-final-method.png)

## Flag

```text
pcgCTF{ilove_Cyber_Command}
```

## Takeaway

When two challenges share an artifact, solve it once and note the reuse — but still decode layer by layer so a wrong guess shows up right away.

## References

- [Original challenge and attachments](<../../home/nightingale/CTF/PCGCTF/solved/cryptography/033-multi-base-layers/README.md>)
- [Earlier solution / teammate provenance](<../../home/nightingale/CTF/PCGCTF/solved/cryptography/033-multi-base-layers/solution.md>)
