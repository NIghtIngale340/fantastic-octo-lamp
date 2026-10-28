from pathlib import Path

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ciphertext = Path("cipher.txt").read_text()

def rotate(text, shift):
    result = []
    for character in text:
        letter = character.upper()
        if letter in alphabet:
            result.append(alphabet[(alphabet.index(letter) + shift) % 36])
        else:
            result.append(character)
    return "".join(result)

plaintext = rotate(ciphertext, -19)
assert rotate(plaintext, 19) == ciphertext
print(plaintext)
