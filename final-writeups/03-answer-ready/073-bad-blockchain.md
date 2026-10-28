# BAD BLOCKCHAIN

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 73 |
| Technical category | Blockchain / Forensics |
| Points in saved inventory | 150 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Recover the IP address encoded in Bitcoin transaction data. |
| Result | `192.168.200.48` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

The challenge’s wallet leads to public transactions. The important clue is not a textual IPstring: selected output values encode byte pairs in their serialized little-endian form.

## Working through the evidence

The starting wallet is `1CTFzzCwntEm3a6CBGBfgxZdiArwY1HBSD`, as supplied by the challenge. The saved chain analysis queried its public transaction history and retained raw transaction bytes. A repeatable public discovery request is:

```sh
curl -sS 'https://blockstream.info/api/address/1CTFzzCwntEm3a6CBGBfgxZdiArwY1HBSD/txs'
```

This is a lookup recipe, not a claim that this endpoint was queried again while drafting. Use the returned transaction identifiers and their block heights to inspect the recorded pair below; an explorer may list newest first, while this decode uses chronological order. `-sS` suppresses progress without hiding request errors.

### 1. Preserve transaction order and relevant outputs

The recorded chain analysis identifies transaction 27bf9358822ef3ae44391950379e9206319e3bb3866d44bd9595a0e7cbdc2ca8 in block 696255, output 0, value 43200 satoshis; then 4a616f943720325cc87611bf4a3bbcf2b5071baf5aab9a0ffbb9297371377c41 in 696256, output 1, value 12488. Use chronological order, not whichever result an explorer displays first.

### 2. Decode serialized values

Bitcoin output values are eight-byte little-endian integers. The independent raw-transaction checks verify the amounts and txids, then select the low two serialized bytes from each value:

```python
import ipaddress
raw = (43200).to_bytes(8, 'little')[:2] + (12488).to_bytes(8, 'little')[:2]
print(raw.hex())
print(ipaddress.IPv4Address(raw))
```

Recorded results:

```text
c0a8c830
192.168.200.48
```

The full serialized values are c0a8000000000000 and c830000000000000. Reading decimal digits as IP octets or reversing chronological order would produce a different answer.

### 3. Match the actual requested submission

The original task asks for a raw IP address, so the saved answer is **192.168.200.48**. No pcgCTFwrapper is invented where the task does not specify one. The address is encoded challenge data; it is not an instruction to contact an internal host.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #73 — actual evidence capture

![073-script-1.png](../screenshots/073-script-1.png)

Run the documented self-contained decoder/calculation on original inputs.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/073-capture-1.py
```

[Actual command transcript](../screenshots/capture-work/073-script-1.terminal.log) · [Execution record](../screenshots/capture-work/073-script-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`192.168.200.48`**. Raw transaction IDs/output values and byte order are independently checked. The requested answer is a raw IP; graderacceptance remains unconfirmed.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

Protocol serialization can carry a second message. Verify exact byte order and transaction order before interpreting it.

## Evidence and references

[Original archived challenge](../../unsolved/blockchain-forensics/073-bad-blockchain/README.md)

- [Decisive preserved verification results](../../analysis-blockchain-forensics/verification.json)
- [Preserved investigation notes](../../unsolved/blockchain-forensics/073-bad-blockchain/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
