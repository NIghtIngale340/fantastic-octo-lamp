# Bitcoin Trail

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 69 |
| Technical category | Network Analysis |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Identify the Bitcoin address appearing in transfer RPC data. |
| Result | `pcgCTF{bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

The network capture includes JSON-RPC requests. An address in a sendtoaddress call is stronger evidence of the transfer destination than a wallet-looking string found without method context.

## Working through the evidence

### 1. Inspect the transfer conversation

```sh
tshark -n -r '/home/nightingale/CTF/PCGCTF/unsolved/network-analysis/069-bitcoin-trail/files/cryptocurrency_transfer_tracking.pcap' -Y 'frame.number == 196 || frame.number == 187 || frame.number == 218' -V
```

These are the decisive frames recorded by the original analysis. The filter includes the transfer and corroborating responses instead of asserting that all RPC traffic describes a single action.

### 2. Read the method and its parameter

Frame 196, TCP stream 17, contains JSON-RPC **sendtoaddress** with destination **bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh**. Frames 187 and 218, including stream18, independently carry the same address in related RPC data.

### 3. Preserve what the observation proves

The capture establishes which address was used in the RPC exchange. It does not identify a real-world owner and does not independently prove a mined on-chain transaction. No blockchain search or contact with the address owner is needed for the requested packet-derived answer.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #69 — actual evidence capture

![069-packet-proof.png](../screenshots/069-packet-proof.png)

Actual field extraction from preserved capture; no invented successful grader response.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-analysis/069-bitcoin-trail/files/cryptocurrency_transfer_tracking.pcap -Y 'frame.number in {187,196,218}' -T fields -E header=y -e frame.number -e tcp.payload
```

[Actual command transcript](../screenshots/capture-work/069-packet-proof.terminal.log) · [Execution record](../screenshots/capture-work/069-packet-proof.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh}`**. Address and RPCrole are locally evidenced; ownership and final PCGCTF acceptance are not inferred.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

A semantic method name distinguishes an address’s role from its mere presence in traffic.

## Evidence and references

[Original archived challenge](../../unsolved/network-analysis/069-bitcoin-trail/README.md)

- [Decisive preserved verification results](../../analysis-network-analysis/verification.json)
- [Original capture](../../unsolved/network-analysis/069-bitcoin-trail/files/cryptocurrency_transfer_tracking.pcap)
- [Preserved investigation notes](../../unsolved/network-analysis/069-bitcoin-trail/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
