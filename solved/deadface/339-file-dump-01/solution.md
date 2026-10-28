# File Dump 01 — saved solution

Flag / submission candidate: `deadface{gh0st404}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## File Dump 01 (200) — Steganography
>
> **Flag:** `deadface{gh0st404}`
>
> **File:** `File_Dump_Challenge.zip`
>
> #### Challenge
>
> A DEADFACE hacker's laptop was intercepted; he had stolen a man named Daniel's entire identity. First challenge in the series: identify which DEADFACE member is responsible. Submit as `deadface{deadface alias}`.
>
> #### Solution
>
> Steganography/forensics task. The ZIP holds the files pulled off the intercepted laptop. Hidden in the dumped files (metadata, embedded data, or a stego-carrying image) is the attacker's handle on the DEADFACE crew — alias `gh0st404`.
>
> Intended approach:
>
> 1. Extract `File_Dump_Challenge.zip` into an empty directory.
> 2. Triage the contents: `exiftool` on every image/document for authorship and comment fields, `strings`/`binwalk` for appended or embedded data, and a stego extractor (`steghide`, `zsteg`) on the carriers.
> 3. The recovered artifact ties the identity theft to DEADFACE member `gh0st404`.
>
> **Note:** flag confirmed from public DEADFACE CTF 2026 writeups (Steganography category, file `File_Dump_Challenge.zip`). The archive was not analyzed locally, so the steps above are the intended method, not a reproduced one.
>
> ---
