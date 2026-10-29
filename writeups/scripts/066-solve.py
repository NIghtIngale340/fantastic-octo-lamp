from pathlib import Path
import re

text = Path("04_rsa_common_modulus.txt").read_text()
values = {name: int(value) for name, value in
          re.findall(r"(n|e1|e2|c1|c2)\s*=\s*(\d+)", text)}
n, c1, c2 = values["n"], values["c1"], values["c2"]
assert 2 * values["e1"] - values["e2"] == 1
message = pow(c1, 2, n) * pow(c2, -1, n) % n
assert pow(message, values["e1"], n) == c1
assert pow(message, values["e2"], n) == c2
print(message.to_bytes((message.bit_length() + 7) // 8, "big").decode())
