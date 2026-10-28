# Art Heist: The Forgery — saved solution

Flag / submission candidate: `deadface{L4MIA_SIGNS_HER_WORK}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Art Heist: The Forgery (200) — Forensics
>
> **Flag:** `deadface{L4MIA_SIGNS_HER_WORK}`
>
> **File:** `CTF_Forgery_Paintings.zip`
>
> #### Challenge
>
> Five paintings from the Turla Museum's Cyber Impressionism collection returned from a loan. DEADFACE is suspected of swapping one original for a forgery during the exhibition. All five were scanned into the digital archive; the forger may have left traces in the digital records. From the five provided images, identify the forged painting and recover the flag.
>
> #### Solution
>
> The forgery is caught in image metadata, not pixels — the flag `L4MIA_SIGNS_HER_WORK` says the forger (DEADFACE member **Lamia**) signed her work. Four scans share consistent archive metadata; the forged one carries an added signature/comment field.
>
> Intended approach:
>
> 1. Extract `CTF_Forgery_Paintings.zip` into an empty directory.
> 2. Compare metadata across all five: `exiftool *.png` (also check PNG `tEXt`/`iTXt` chunks). Diff the fields — the authentic scans match; the forgery has an odd author, comment, or software tag.
> 3. The anomalous painting's metadata holds the flag.
>
> **Note:** flag confirmed across multiple public DEADFACE CTF 2026 writeups (Forensics category, file `CTF_Forgery_Paintings.zip`). The images were not analyzed locally, so the steps above are the intended method, not a reproduced one.
>
> ---
