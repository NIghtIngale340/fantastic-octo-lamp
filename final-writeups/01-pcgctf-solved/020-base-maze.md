# Base Maze

**Platform:** PCGCTF · **Challenge ID:** 20 · **Category:** Cryptography · **Points:** 250

**Status:** Solved in the last snapshot; decode reproduced locally.

## The challenge

Peel a message back through hex, Ascii85, Base32 and Base64.

## Solving it

The outer string is all hex digits with an even length, so the first move is hex → bytes. The result is punctuation-heavy text that isn't hex anymore — its character set looks like Ascii85. From there the next output has Base32's uppercase alphabet and `=` padding, then a final Base64 layer. Each step is driven by what the previous one looks like, not by the title:

Save this as `solve.py` and run `python3 solve.py`. [Download the script](../scripts/020-solve.py).

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

The source flag is prefixed `CTF`; the challenge uses `pcgCTF`, so keep the payload `ilove_Cyber_Command` exactly when wrapping it.

## Screenshots

Fresh local reproduction using the command described above.

![Command and result](../screenshots/020-final-method.png)

## Flag

```text
pcgCTF{ilove_Cyber_Command}
```

## Takeaway

Stacked encodings are still just reversible representation, not protection. Printing every intermediate string keeps the chain auditable and flags a wrong decoder immediately.

## References

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/020-base-maze/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/cryptography/020-base-maze/solution.md>)
