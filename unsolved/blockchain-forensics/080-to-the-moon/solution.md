# TO THE MOON! — solution

Exact recovered blockchain flag:

```text
flag{Inf0S3cBl0ckch41nAn4lys15}
```

The challenge page separately specifies a `pcgCTF{...}` wrapper. Translating only that wrapper gives the **unvalidated submission candidate**:

```text
pcgCTF{Inf0S3cBl0ckch41nAn4lys15}
```

Preserve the payload's exact capitalization and digits. The two wrappers must not be confused with confirmed platform acceptance.

## Image to wallet

The original JPEG has no useful EXIF clue, appended bytes, or embedded archive detectable by ordinary signature scanning. StegSeek recovered a steghide payload using passphrase `iloveyou`. Its original embedded filename is `To_the_moon.zip` (266 bytes).

The ZIP uses AES-256 encryption and contains `To_the_moon.txt`. A local dictionary check with John recovered its separate passphrase `prisonbreak`. ZIP extraction and integrity verification succeeded.

The 34-byte plaintext is the wallet address:

```text
1NFoSEcGq4XwEbaXmio5yYaakbX5Gtia4R
```

Only the supplied challenge image and recovered archive were analyzed; no executable or script payload was run.

## Wallet to flag

The wallet's funding transaction is `ca944563cd4ddeb920423f324cdf0329665a80bd04017bfd4a72ae44f3146a16` (block 693054). Its next transaction, `e22990a8494a2c22c8ab68c6288164fb084885ca3dad68b149da9e296ec67af5` (block 693055), has the hidden message in output index 1:

```text
6a1f666c61677b496e6630533363426c30636b636834316e416e346c797331357d
```

`6a` is OP_RETURN. `1f` pushes 31 bytes. Decode the remaining bytes as ASCII to recover `flag{Inf0S3cBl0ckch41nAn4lys15}`. The flag was independently checked against the complete raw transaction from a second explorer, including recomputation of its transaction ID.

Sources:

- [Recovered wallet history](https://api.blockcypher.com/v1/btc/main/addrs/1NFoSEcGq4XwEbaXmio5yYaakbX5Gtia4R?limit=200)
- [Transaction with the flag](https://api.blockcypher.com/v1/btc/main/txs/e22990a8494a2c22c8ab68c6288164fb084885ca3dad68b149da9e296ec67af5)
- [Raw transaction](https://blockstream.info/api/tx/e22990a8494a2c22c8ab68c6288164fb084885ca3dad68b149da9e296ec67af5/hex)

Original JPEG SHA-256: `b9cd9778240ce4ea023a4b0c09b8a6a821e87da8012858c09a3f621aa85a7217`.

All downloaded transaction responses, raw bytes, and verification results are saved in `analysis-blockchain-forensics/`. No platform acceptance is claimed.
