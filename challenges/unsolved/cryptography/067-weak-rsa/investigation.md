# Weak RSA — investigation status

No flag has been recovered. The original challenge files are unchanged.

The modulus is 512 bits. The public exponent is 65537; that number is an exponent, not the RSA key length. The modulus is composite and is not a perfect power.

Checks completed without a factor:

- Fermat factorization: 1,000,000 increments.
- SymPy factorint with a limit of 1,000,000.
- GCD against other downloaded RSA moduli; no shared prime.
- GCD of ciphertext and modulus; result 1.
- Near-square multiples 1 through 10,000, ten candidates each.
- Pollard p−1 with bound 10,000,000 and base 2.
- ECM: 100 curves, B1=10,000, B2=100,000.
- FactorDB reports C (composite), with no known nontrivial factors.

The stronger ECM run also completed without a factor: 500 curves, B1=50,000, B2=500,000, seed 5678 (227 seconds).

The linked article describes the correct general RSA workflow, but its numerical example is inconsistent: its printed p and q do not multiply to its displayed n. Its displayed n is 534 bits, rather than the stated 150–200 bits. Its numbers must not be reused for this challenge.

Reference: https://dev.to/ctfdojo/picoctf-mind-your-ps-and-qs-writeup-factor-a-weak-rsa-modulus-38bo

`solve.py` accepts a prime factor of this challenge's n, checks both factors, reconstructs the private exponent, decrypts, and verifies the plaintext by re-encrypting it. It does not yet have the required factor.
