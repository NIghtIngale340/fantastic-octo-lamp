ciphertext = "rtermt{xzetgstv_gh_gcv_vldnuj}"
known_prefix = "pcgctf"
key = "".join(chr((ord(c) - ord(p)) % 26 + ord("a"))
              for c, p in zip(ciphertext, known_prefix))
print("Key:", key)

message = []
position = 0
for letter in ciphertext:
    if "a" <= letter <= "z":
        shift = ord(key[position % len(key)]) - ord("a")
        message.append(chr((ord(letter) - ord("a") - shift) % 26 + ord("a")))
        position += 1
    else:
        message.append(letter)
print("".join(message))
