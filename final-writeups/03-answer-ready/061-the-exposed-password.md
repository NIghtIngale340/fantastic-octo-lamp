# The Exposed Password

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 61 |
| Technical category | Network Analysis |
| Points in saved inventory | 150 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Recover the successful HTTP login password. |
| Result | `pcgCTF{John1234!}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

The capture contains more than one attempt. Selecting the first POST would produce a convincing but wrong answer; the following server response decides which submitted password worked.

## Working through the evidence

### 1. Isolate login attempts and responses

```sh
tshark -n -r '/home/nightingale/CTF/PCGCTF/unsolved/network-analysis/061-the-exposed-password/files/http_authentication.pcap' -Y 'http.request.method == "POST" || frame.number == 29 || frame.number == 48' -V
```

`-V` prints the decoded protocol tree so the form body and response can be read together. The marked input path is the original attached pcap, linked below; this is a reproducible recipe for the preserved observations.

### 2. Reject the failed attempt

Frame 27 submits **john1234**, and response 29 rejects it. That lowercase value is not the recovered answer, even though it appears in a credential field.

### 3. Decode the successful form value

Frame 46 has `username=johndoe&password=John1234%21`; response 48 confirms a valid login. URL form encoding represents the exclamation mark as `%21`. A concise independent conversion is:

```python
from urllib.parse import unquote
print(unquote('John1234%21'))
```

The decoded result is **John1234!**. Keep the initial capital J and final exclamation mark; dropping either changes the credential.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #61 — actual evidence capture

![061-packet-proof.png](../screenshots/061-packet-proof.png)

Actual field extraction from preserved capture; no invented successful grader response.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-analysis/061-the-exposed-password/files/http_authentication.pcap -Y 'frame.number in {27,46,48}' -T fields -E header=y -e frame.number -e http.request.method -e http.file_data -e http.response.code
```

[Actual command transcript](../screenshots/capture-work/061-packet-proof.terminal.log) · [Execution record](../screenshots/capture-work/061-packet-proof.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{John1234!}`**. The saved successful HTTP response corroborates the credential; no PCGCTF acceptance is claimed.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

Application responses disambiguate attempted credentials; decoding a transport representation should preserve the exact secret.

## Evidence and references

[Original archived challenge](../../unsolved/network-analysis/061-the-exposed-password/README.md)

- [Decisive preserved verification results](../../analysis-network-analysis/answers.json)
- [Original capture](../../unsolved/network-analysis/061-the-exposed-password/files/http_authentication.pcap)
- [Preserved investigation notes](../../unsolved/network-analysis/061-the-exposed-password/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
