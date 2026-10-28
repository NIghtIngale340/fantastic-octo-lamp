# Multi-Base Layers

**Platform:** PCGCTF · **Challenge ID:** 33 · **Category:** Cryptography · **Points:** 100

**Status:** Solved in the last snapshot; decode reproduced locally.

## The challenge

Same shape as Base Maze (#20) — in fact it reuses the identical hex blob. Peel it back through hex, Ascii85, Base32 and Base64.

## Solving it

Hex digits, even length → start with hex → bytes. The output's punctuation alphabet points at Ascii85, then Base32 (uppercase + `=` padding), then a final Base64 decode:

```sh
python3 -c "
import base64
h=open('encoded.txt').read().strip()
a=base64.a85decode(bytes.fromhex(h))
b=base64.b32decode(a)
print(base64.b64decode(b).decode())"
```

```text
CTF{ilove_Cyber_Command}
```

Source prefix is `CTF`; the challenge wrapper is `pcgCTF`. Keep `ilove_Cyber_Command` verbatim.

## Screenshots

![033-step-01.png](../screenshots/033-step-01.png)

![033-step-02.png](../screenshots/033-step-02.png)

## Flag

```text
pcgCTF{ilove_Cyber_Command}
```

## Takeaway

When two challenges share an artifact, solve it once and note the reuse — but still decode layer by layer so a wrong guess shows up right away.

## References

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/033-multi-base-layers/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/cryptography/033-multi-base-layers/solution.md>)
