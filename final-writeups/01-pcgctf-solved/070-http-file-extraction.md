# HTTP File Extraction

**Platform:** PCGCTF · **Challenge ID:** 70 · **Category:** Network Analysis · **Points:** 150

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Export the ZIP downloaded over captured HTTP and recover the password in its text member.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/network-analysis/070-http-file-extraction/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The capture is a saved HTTP transaction, so the file is reconstructible from response bytes without visiting the hostname. This challenge’s capture is byte-identical to the one used for Hidden Download (#62); reusing a verified extraction is appropriate, but the duplicate relationship must be stated instead of pretending a second independent incident occurred.

## Step-by-step solution

### 1. Find the download request and response

`-r` reads a recording, `-n` disables name resolution, and `-Y http` selects HTTP messages. The chosen fields show which frame requests the ZIP and which response labels the content type.

```sh
tshark -n -r PCGCTF/solved/network-analysis/070-http-file-extraction/files/http_file_extraction.pcap -Y http -T fields -e frame.number -e http.request.uri -e http.content_type
```

**Recorded output / observation:**

```text
Frame 11: GET /password.zip
Frame 13: application/zip
```

The response body is the recoverable object; a filename in a request alone would not prove that the download completed.

### 2. Export and inspect the ZIP member

`--export-objects` reassembles HTTP object bodies. `unzip -t` validates the archive CRCs before `-p` prints only the named member to standard output. The saved extraction and integrity check are preserved in the earlier network analysis evidence.

```sh
mkdir -p /tmp/pcgctf-http70
tshark -r PCGCTF/solved/network-analysis/070-http-file-extraction/files/http_file_extraction.pcap --export-objects http,/tmp/pcgctf-http70
unzip -t /tmp/pcgctf-http70/password.zip
unzip -p /tmp/pcgctf-http70/password.zip password.txt
```

**Recorded output / observation:**

```text
my password is:
Cx689iO7Fu4G
```

This text is the requested password; it is not the ZIP encryption password or an HTTP authentication credential. Case and digits are significant.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #70 — actual evidence capture

![070-step-01.png](../screenshots/070-step-01.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
tshark -n -r PCGCTF/solved/network-analysis/070-http-file-extraction/files/http_file_extraction.pcap -Y http -T fields -e frame.number -e http.request.uri -e http.content_type
```

[Actual command transcript](../screenshots/capture-work/070-step-1.terminal.log) · [Execution record](../screenshots/capture-work/070-step-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #70 — actual evidence capture

![070-step-02.png](../screenshots/070-step-02.png)

Fresh execution of the documented offline step.

Command/action actually executed:

```sh
mkdir -p /tmp/pcgctf-http70
tshark -r PCGCTF/solved/network-analysis/070-http-file-extraction/files/http_file_extraction.pcap --export-objects http,/tmp/pcgctf-http70
unzip -t /tmp/pcgctf-http70/password.zip
unzip -p /tmp/pcgctf-http70/password.zip password.txt
```

[Actual command transcript](../screenshots/capture-work/070-step-2.terminal.log) · [Execution record](../screenshots/capture-work/070-step-2.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved result / candidate:

```text
pcgCTF{Cx689iO7Fu4G}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Reconstruct application objects instead of searching raw packet strings alone. Validate the exported container and distinguish the secret inside it from transport metadata.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/network-analysis/070-http-file-extraction/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/network-analysis/070-http-file-extraction/solution.md>)
- [password.zip](</home/nightingale/CTF/PCGCTF/analysis-network-analysis/hidden-download-objects/password.zip>)
- [hidden-download-contents.txt](</home/nightingale/CTF/PCGCTF/analysis-network-analysis/hidden-download-contents.txt>)
- [verification.json](</home/nightingale/CTF/PCGCTF/analysis-network-analysis/verification.json>)
