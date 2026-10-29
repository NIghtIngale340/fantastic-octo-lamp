from math import gcd, isqrt
from sympy import isprime
from pathlib import Path
import re
source = Path('/home/nightingale/CTF/PCGCTF/unsolved/cryptography/067-weak-rsa/files/05_weak_rsa.txt').read_text()
n, e, c = [int(re.search(r'\b' + key + r'\s*=\s*(\d+)', source)[1])
           for key in ('n', 'e', 'c')]
print(n.bit_length(), e)
print(isprime(n), isqrt(n) ** 2 == n)
print(gcd(c, n), 0 < c < n)
