"""Decrypt the challenge once a verified prime factor is available.

Usage: python solve.py <prime-factor-of-n>
"""
import math
import re
import sys
from pathlib import Path
from sympy import isprime

root = Path(__file__).resolve().parent
source = (root / 'files' / '05_weak_rsa.txt').read_text()
n, e, c = [int(re.search(r'\b' + k + r'\s*=\s*(\d+)', source)[1]) for k in ('n', 'e', 'c')]
if len(sys.argv) != 2:
    sys.exit('Usage: python solve.py <prime-factor-of-n>')
p = int(sys.argv[1])
if p <= 1 or p >= n or n % p:
    sys.exit('The supplied number is not a nontrivial factor of n.')
q = n // p
if not (isprime(p) and isprime(q)):
    sys.exit('Both factors must be prime for this two-prime RSA solver.')
phi = (p - 1) * (q - 1)
if math.gcd(e, phi) != 1:
    sys.exit('The exponent has no inverse modulo phi(n).')
d = pow(e, -1, phi)
m = pow(c, d, n)
assert p * q == n
assert pow(m, e, n) == c
plaintext = m.to_bytes((m.bit_length() + 7) // 8, 'big')
(root / 'decrypted.bin').write_bytes(plaintext)
print(plaintext.decode('utf-8', errors='backslashreplace'))
