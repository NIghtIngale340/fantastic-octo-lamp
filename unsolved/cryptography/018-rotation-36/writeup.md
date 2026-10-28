# Rotation 36 — solution

Use the alphabet `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`, with indices 0–35. Leave punctuation, whitespace, braces, and underscores unchanged.

The encryption uses a shift of **+19**. Decrypt by subtracting **19 modulo 36** (equivalently, adding 17). For example, `T` (19) becomes `A` (0), and `Y` (24) becomes `F` (5).

```text
AGENT, THIS IS A SCRAMBLED BULLETIN. SHIFT ACROSS A CUSTOM ALPHABET (A-Z AND 0-9).
RECOVER THE HIDDEN CODE TO PROCEED: FLAG{CAESAR_SHIFT_19_ALNUM}

```

The recovered flag is `FLAG{CAESAR_SHIFT_19_ALNUM}`.

The page shows a `pcgCTF{...}` format example, but changing the recovered wrapper to `pcgCTF{CAESAR_SHIFT_19_ALNUM}` was rejected, as shown in the user-provided screenshot. Try the exact flag recovered from the ciphertext:

```text
FLAG{CAESAR_SHIFT_19_ALNUM}
```

Verification: encrypting the plaintext with +19 reproduces the entire original ciphertext exactly. The exact recovered flag has not yet been confirmed accepted. The archive's account-status snapshot remains unchanged.

## Validation status

The user reports that both `pcgCTF{CAESAR_SHIFT_19_ALNUM}` and the literal recovered `FLAG{CAESAR_SHIFT_19_ALNUM}` were rejected. A direct site test of `pcgCTF{caesar_shift_19_alnum}` also returned `Incorrect`.

The decryption is verified, but no accepted submission is known. The case-insensitive encoding cannot establish the author's original capitalization. An expected-answer or source-file mismatch is possible; organizer clarification is needed before asserting another flag.
