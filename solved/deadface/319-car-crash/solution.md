# Car Crash — saved solution

Flag / submission candidate: `deadface{08_10_1961}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Car Crash (200) — OSINT
>
> **Flag:** `deadface{08_10_1961}`
>
> **File:** `car_crash.jpg`
>
> #### Challenge
>
> Among files recovered from DEADFACE is a photo of a traffic accident involving a commercial truck. The truck identifies a company DEADFACE is interested in. Determine which company owns the truck and when it was founded. Submit as `deadface{MM_DD_YYYY}`.
>
> #### Solution
>
> The truck carries a small **USDOT number, 080806**, on the upper-right of the cargo box. That number is the pivot:
>
> 1. Read the DOT marking off the photo (zoom in on the cargo box).
> 2. Look up USDOT `080806` in a search engine and cross-check on the FMCSA / DOT.report carrier lookup → carrier is **J.B. Hunt Transport Services, Inc.**
> 3. J.B. Hunt was founded **August 10, 1961** → `08_10_1961`.
>
> **Note:** flag confirmed across multiple public DEADFACE CTF 2026 writeups (OSINT category, file `car_crash.jpg`); the USDOT-to-company step is from `muhddanielfirdaus/DEADFACE-CTF-2026`. The image and external lookups were not reproduced locally.
>
> ---
