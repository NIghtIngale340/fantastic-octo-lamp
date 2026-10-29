from pathlib import Path
import base64
import re

email = Path("intercepted.txt").read_text()
signature = re.search(r"^X-Spam-Signature: (.+)$", email, re.M)[1]
validator = re.search(r"^X-Spam-Validator: (.+)$", email, re.M)[1]
ciphertext = base64.b64decode(signature)
key = bytes.fromhex(validator)
plaintext = bytes(value ^ key[i % len(key)]
                  for i, value in enumerate(ciphertext))
print(plaintext.decode())
