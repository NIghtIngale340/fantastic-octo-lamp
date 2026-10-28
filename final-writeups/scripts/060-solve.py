from pathlib import Path
import ast
import re
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

text = Path("output.txt").read_text()
state = ast.literal_eval(re.search(r"\[[01,\s]+\]", text)[0])
bits = []
for _ in range(128):
    bits.append(state[0])
    feedback = state[63] ^ state[61] ^ state[60] ^ state[58]
    state = state[1:] + [feedback]

key = bytes(int("".join(map(str, bits[i:i + 8])), 2)
            for i in range(0, 128, 8))
print("Key:", key.hex())
ciphertext = bytes.fromhex(re.search(r"[0-9a-f]{80,}", text)[0])
decryptor = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()
padding = plaintext[-1]
assert 1 <= padding <= 16
assert plaintext[-padding:] == bytes([padding]) * padding
print(plaintext[:-padding].decode())
