# BAD BLOCKCHAIN — solution

Answer: **192.168.200.48**

The challenge states that the answer is an IP address; it does not specify a flag wrapper. Submit the raw address above unless the platform explicitly requires a wrapper. The equivalent wrapper candidate would be `pcgCTF{192.168.200.48}`, but acceptance is untested.

The hidden bytes are in the payment amounts, not an OP_RETURN output. Inspect the outputs paying the provided address `1CTFzzCwntEm3a6CBGBfgxZdiArwY1HBSD`, ordered by block height:

| Block | Transaction | Output index | Satoshis | Serialized amount (little-endian) | First two bytes |
| ---: | --- | ---: | ---: | --- | --- |
| 696255 | `27bf9358822ef3ae44391950379e9206319e3bb3866d44bd9595a0e7cbdc2ca8` | 0 | 43200 | `c0a8000000000000` | `c0 a8` |
| 696256 | `4a616f943720325cc87611bf4a3bbcf2b5071baf5aab9a0ffbb9297371377c41` | 1 | 12488 | `c830000000000000` | `c8 30` |

Concatenate the nonzero 16-bit value bytes in chronological order:

```text
c0 a8 c8 30 -> 192 . 168 . 200 . 48
```

Both API amounts and raw serialized transaction outputs agree. The raw transaction IDs were recomputed from double-SHA-256 of the non-witness serialization and match the supplied IDs. Neither transaction contains an OP_RETURN output. The result is a private IPv4 address; this is the puzzle's recovered value, not a claim that a public C2 service is reachable at it.

Sources:

- [Older transaction](https://api.blockcypher.com/v1/btc/main/txs/27bf9358822ef3ae44391950379e9206319e3bb3866d44bd9595a0e7cbdc2ca8)
- [Newer transaction](https://api.blockcypher.com/v1/btc/main/txs/4a616f943720325cc87611bf4a3bbcf2b5071baf5aab9a0ffbb9297371377c41)
- [Raw older transaction](https://blockstream.info/api/tx/27bf9358822ef3ae44391950379e9206319e3bb3866d44bd9595a0e7cbdc2ca8/hex)
- [Raw newer transaction](https://blockstream.info/api/tx/4a616f943720325cc87611bf4a3bbcf2b5071baf5aab9a0ffbb9297371377c41/hex)

All source responses and independent verification results are saved in `analysis-blockchain-forensics/`. No platform acceptance is claimed.
