# HIDDEN

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 75 |
| Technical category | Forensics |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Recover the hidden message from the misleading DLL artifact. |
| Result | `pcgCTF{me0w_hia!}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

A .dll suffix does not establish a PE executable. The supplied winsock32.dll is a disk image, which redirects the investigation toward partitions and NTFS streams instead of disassembly.

## Working through the evidence

### 1. Identify the carrier layout

The original ZIP member is a 10,486,272-byte disk image. Sleuth Kit mmls identifies an NTFS partition beginning at sector 128. With 512-byte sectors, the filesystem starts at offset 65536.

```sh
mmls winsock32.dll
fls -r -o 128 winsock32.dll
```

`fls -r` recursively lists filesystem entries. `-o 128` supplies a sector offset, not the byte offset 65536. The preserved listing identifies the named data stream **passwords.txt:flag.jpg**, attribute 40-128-3.

### 2. Export the named stream

```sh
icat -o 128 winsock32.dll 40-128-3 > flag.jpg
```

`icat` reads the specified filesystem attribute; shell redirection writes the recovered bytes to a local file. This is not the ordinary passwords.txt data stream. The independent export produces 24,023 bytes and matches the raw carve at absolute offset 294912.

### 3. Read the JPEG

The extracted image is a cat hiding beneath a blanket with visible text **flag{me0w_hia!}**. Its JPEG structure and saved SHA256 corroborate the extraction. The PCGCTF prompt explicitly specifies its own wrapper, so preserve the payload while using pcgCTF braces.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Visual evidence

![Recovered NTFS named-stream image.](../../unsolved/forensics/075-hidden/evidence/flag.jpg)

*Recovered NTFS named-stream image.* Box the visible flag; this is actual extracted content, not a fabricated terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #75 — actual evidence capture

![075-ntfs-stream-list.png](../screenshots/075-ntfs-stream-list.png)

Actual partition/NTFS stream listing from original archive.

Command/action actually executed:

```sh
mmls /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/winsock32.dll; fls -r -o 128 /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/winsock32.dll
```

[Actual command transcript](../screenshots/capture-work/075-ntfs.terminal.log) · [Execution record](../screenshots/capture-work/075-ntfs.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #75 — actual evidence capture

![075-ntfs-export.png](../screenshots/075-ntfs-export.png)

Actual named stream export and original-payload hash.

Command/action actually executed:

```sh
icat -o 128 /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/winsock32.dll 40-128-3 > /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/recovered-flag.jpg && file /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/recovered-flag.jpg && sha256sum /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/recovered-flag.jpg
```

[Actual command transcript](../screenshots/capture-work/075-export.terminal.log) · [Execution record](../screenshots/capture-work/075-export.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{me0w_hia!}`**. The NTFS stream and visible raw flag are recovered. Applying the stated wrapper is a candidate until the site accepts it.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

A filesystem attribute can hide content outside the ordinary file stream. Check the actual carrier type before following its extension.

## Evidence and references

[Original archived challenge](../../unsolved/forensics/075-hidden/README.md)

- [Decisive preserved verification results](../../analysis-team-verification/artifacts.json)
- [Actual partition table](../../unsolved/forensics/075-hidden/evidence/partition-table.txt)
- [Actual NTFS named-stream listing](../../unsolved/forensics/075-hidden/evidence/ntfs-files.txt)
- [Preserved investigation notes](../../unsolved/forensics/075-hidden/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
