# Headshot — saved solution

Flag / submission candidate: `deadface{b00m_h34Dsh0TTT}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Headshot (150) — Steganography / Forensics
>
> **Flag:** `deadface{b00m_h34Dsh0TTT}`
>
> **File:** `headshot.zip`
>
> #### Challenge
>
> DEADFACE compromised a fileshare of corporate headshots for Aurora Health employees and is tagging one photo to mark a future target. Figure out which image was tampered with.
>
> #### Solution
>
> One headshot among the set carries hidden/added data the others don't — the tag identifying the target. The flag `b00m_h34Dsh0TTT` ("boom headshot") is recovered from that image.
>
> Intended approach:
>
> 1. Extract `headshot.zip` into an empty directory.
> 2. Triage every image: compare file sizes, run `exiftool *` for odd author/comment fields, `binwalk`/`strings` for appended or embedded data, and an LSB/stego check on carriers.
> 3. The single anomalous headshot yields the flag.
>
> **Note:** flag confirmed from a public DEADFACE CTF 2026 writeup (Steganography category, file `headshot.zip`, `github.com/SasmitNarnaware/DEADFACE-CTF-2026-Writeup`). The archive was not analyzed locally, so the steps above are the intended method, not a reproduced one.
>
> ---
