from pathlib import Path
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
ciphertext = Path('/home/nightingale/CTF/PCGCTF/unsolved/cryptography/018-rotation-36/files/cipher.txt').read_text()
def rotate(text, shift):
    return ''.join(alphabet[(alphabet.index(c.upper()) + shift) % 36]
                   if c.upper() in alphabet else c for c in text)
plaintext = rotate(ciphertext, -19)
assert rotate(plaintext, 19) == ciphertext
print(plaintext)
