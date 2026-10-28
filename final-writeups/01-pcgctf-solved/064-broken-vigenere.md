# Broken Vigenere

**Platform:** PCGCTF · **Challenge ID:** 64 · **Category:** Cryptography · **Points:** 100

**Status:** Solved in the last snapshot; decode reproduced locally.

## The challenge

Recover the repeating key and decrypt a Vigenère flag. The ciphertext starts `rtermt{...}`.

## Solving it

We know the plaintext starts `pcgctf`. In Vigenère, ciphertext letter minus plaintext letter (mod 26) gives the key shift at that position, so the first six letters hand us the key:

```sh
python3 -c "print(''.join(chr((ord(c)-ord(p))%26+97) for c,p in zip('rtermt','pcgctf')))"
```

```text
crypto
```

`crypto` is a believable key — now test it on the whole thing, making sure punctuation doesn't consume a key character:

```sh
python3 -c "
ct='rtermt{xzetgstv_gh_gcv_vldnuj}'; key='crypto'; j=0; out=''
for c in ct:
    if c.isalpha(): out+=chr((ord(c)-ord(key[j%6]))%26+97); j+=1
    else: out+=c
print(out)"
```

```text
pcgctf{vigenere_is_not_enough}
```

The whole flag reads out under the same key. This challenge uses lowercase `pcgctf`.

## Screenshots

![064-step-01.png](../screenshots/064-step-01.png)

![064-step-02.png](../screenshots/064-step-02.png)

## Flag

```text
pcgctf{vigenere_is_not_enough}
```

## Takeaway

A repeating key leaks straight through a known plaintext prefix. The one detail that trips people up is keeping the key index aligned across punctuation.

## References

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/cryptography/064-broken-vigenere/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/repeating_key_cipher_writeup.md>)
