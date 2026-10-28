# FTP Credential Leak

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 22 |
| Technical category | Network Analysis |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Recover the password used for a successful FTP login. |
| Result | `pcgCTF{AfricaCTF2021}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

This question has no separate attachment. The parent Packet Detective capture supplies the FTP control channel, so absence of a download link does not mean the evidence is unavailable.

## Working through the evidence

### 1. Reuse the parent capture

```sh
tshark -n -r '/home/nightingale/CTF/PCGCTF/unsolved/network-analysis/021-packet-detective/files/UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng' -Y 'ftp.request.command == "PASS" || ftp.response.code == 230' -T fields -e frame.number -e ftp.request.arg -e ftp.response.code -e ftp.response.arg
```

This offline recipe reads the original linked capture. `PASS` selects supplied passwords; FTP response 230 confirms a successful login. `-T fields` avoids flooding the result with unrelated packet details.

### 2. Associate the password with success

The preserved dissection shows USER kali at frame 496, PASS **AfricaCTF2021** at 500, then Login successful at 502. Repeated sessions carry the same password at 587 and 11816. The matching response is important: a string sent in a password field could simply be a failed guess.

### 3. Transcribe the answer

The requested value is the password, not the username, a whole USER/PASS conversation, or a hash. Keep the uppercase A, CTF and digits exactly. FTP sent these credentials in cleartext; this recovery does not involve cracking encryption.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #22 — actual evidence capture

![022-packet-proof.png](../screenshots/022-packet-proof.png)

Actual field extraction from preserved capture; no invented successful grader response.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-analysis/021-packet-detective/files/UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'frame.number in {500,502,587,11816}' -T fields -E header=y -e frame.number -e ftp.request.command -e ftp.request.arg -e ftp.response.code -e ftp.response.arg
```

[Actual command transcript](../screenshots/capture-work/022-packet-proof.terminal.log) · [Execution record](../screenshots/capture-work/022-packet-proof.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{AfricaCTF2021}`**. The FTP login is confirmed by the recorded230 response. That is separate from whether PCGCTF accepts the wrapper.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

Correlate a submitted credential with its authentication result before reporting it as working.

## Evidence and references

[Original archived challenge](../../unsolved/network-analysis/022-ftp-credential-leak/README.md)

- [Decisive preserved verification results](../../analysis-network-analysis/answers.json)
- [Original capture](../../unsolved/network-analysis/021-packet-detective/files/UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng)
- [Preserved investigation notes](../../unsolved/network-analysis/022-ftp-credential-leak/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
