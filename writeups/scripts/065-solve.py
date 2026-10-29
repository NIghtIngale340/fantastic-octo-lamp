from pathlib import Path
import re

text = Path("03_rsa_small_exponent.txt").read_text()
values = {name: int(value) for name, value in
          re.findall(r"(n|e|ciphertext)\s*=\s*(\d+)", text)}
c = values["ciphertext"]
low, high = 0, 1 << ((c.bit_length() + 2) // 3)

while low + 1 < high:
    middle = (low + high) // 2
    if middle ** 3 <= c:
        low = middle
    else:
        high = middle

assert values["e"] == 3
assert low ** 3 == c < values["n"]
message = low.to_bytes((low.bit_length() + 7) // 8, "big")
print(message.decode())
