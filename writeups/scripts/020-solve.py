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
