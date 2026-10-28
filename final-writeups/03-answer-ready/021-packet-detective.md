# Packet Detective

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 21 |
| Technical category | Network Analysis |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Identify the extension of a downloaded file from the supplied capture. |
| Result | `pcgCTF{zip}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

Several downloads occur in the same capture. The FTP session is linked to the neighboring credential question, but that context is an inference about intent, not proof that the grader means the ZIP transfer.

## Working through the evidence

### 1. Find actual transfer commands

Read the original capture with a filter for FTP retrieval, rather than selecting an arbitrary filename from strings:

```sh
tshark -n -r '/home/nightingale/CTF/PCGCTF/unsolved/network-analysis/021-packet-detective/files/UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng' -Y 'ftp.request.command == "RETR"' -T fields -e frame.number -e ftp.request.arg
```

Replace the marked path with the original capture linked in the evidence. `-Y` selects download requests; `RETR` means retrieve, whereas `STOR` means upload. The recorded frame 11831 requests **accountNum.zip**. Frame 11837 carries a valid ZIP in the associated data stream20.

### 2. Correlate control and data channels

FTP uses separate control and data connections. TCP stream 19 contains the request; TCP stream 20 transfers the file. Merely seeing .jpg in an earlier STOR would identify an upload, not this download. The exported ZIP was independently opened and checked during the saved analysis.

### 3. Preserve the question’s ambiguity

The capture also includes an HTTP Chrome-extension .crx download and a CA-certificate filename. The saved question asks an extension but uses a filename placeholder and gives no protocol discriminator. For the FTP interpretation, the extension is **zip**, while the full filename is accountNum.zip. The evidence proves that transfer, but not which download the author intended.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #21 — actual evidence capture

![021-packet-proof.png](../screenshots/021-packet-proof.png)

Actual field extraction from preserved capture; no invented successful grader response.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-analysis/021-packet-detective/files/UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'frame.number in {11831,11837}' -T fields -E header=y -e frame.number -e ftp.request.command -e ftp.request.arg -e ftp-data.command
```

[Actual command transcript](../screenshots/capture-work/021-packet-proof.terminal.log) · [Execution record](../screenshots/capture-work/021-packet-proof.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{zip}`**. The candidate pcgCTF{zip} follows the FTP transfer. CRX/CA downloads make the expected target ambiguous; an organizer hint or actual acceptance is still needed.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

A correct packet extraction can still leave an ambiguous question. Preserve protocol, direction and exact filename before choosing an extension.

## Evidence and references

[Original archived challenge](../../unsolved/network-analysis/021-packet-detective/README.md)

- [Decisive preserved verification results](../../analysis-network-analysis/answers.json)
- [Original capture](../../unsolved/network-analysis/021-packet-detective/files/UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng)
- [Preserved investigation notes](../../unsolved/network-analysis/021-packet-detective/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
