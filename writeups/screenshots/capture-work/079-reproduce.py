import re
from pathlib import Path
text = Path('/home/nightingale/CTF/PCGCTF/unsolved/cryptography-encoding/079-sequence/files/sequence.txt').read_text()
json_text = text[text.index('{'):text.rindex('}') + 1]
keys = re.findall(r'^\s*"([^"\n]+)"\s*:', json_text, re.M)
positions = [1, 2, 3, 5, 8, 13, 21, 34]
print(''.join(keys[i-1][0] for i in positions))
