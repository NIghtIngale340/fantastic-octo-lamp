# Inside Man — saved solution

Flag / submission candidate: `deadface{l3FT_b3Hind!}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Inside Man (200) — Mobile Security / Android
>
> **Flag:** `deadface{l3FT_b3Hind!}`
>
> **File:** `app-release.apk` (De Monne Financial, same ZIP as *Hard Kept Secrets*)
>
> #### Challenge
>
> DEADFACE obtained data normal customers can't access in the app. Backend logging was off, so De Monne can't tell which account was used. Either a developer account was compromised, or something hardcoded in the app gave easy access. Use the ZIP from *Hard Kept Secrets*.
>
> #### Solution
>
> The "developer account … or something hardcoded" is a backdoor credential **left behind** in the shipped APK — the flag `l3FT_b3Hind!` = "left behind." This is the "hardcoded privileged account/password in the login activity" already flagged among the other issues in *Hard Kept Secrets*.
>
> Intended approach:
>
> 1. Decompile the same APK with jadx: `jadx -d out app-release.apk`.
> 2. Read the login/authentication activity. A hardcoded developer/admin account and password are embedded as string constants, bypassing the normal customer login and granting privileged data access.
> 3. The recovered backdoor credential carries the flag.
>
> **Note:** flag confirmed from public DEADFACE CTF 2026 writeups (Mobile category). The APK was not analyzed locally, so the steps above are the intended method, not a reproduced one. Same `app-release.apk` as *Hard Kept Secrets* and *Diagnosis*.
>
> ---
