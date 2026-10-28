# Bedside Manner — saved solution

Flag / submission candidate: `deadface{v13w_s0urc3_sav3s_l1v3s}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Bedside Manner (200) — Medical Device / IoT
>
> **Flag:** `deadface{v13w_s0urc3_sav3s_l1v3s}`
>
> **Target:** `http://emedra.dctf.io:8080/` (Emedra CerebraScan CS-9000, ScanWorks kiosk)
>
> #### Challenge
>
> Opening task of the CS-9000 penetration test: identify any lingering strings developers may have left in the device's kiosk web browser.
>
> #### Solution
>
> Solved live. "Lingering strings in the kiosk web browser" = view source. The ScanWorks sign-in screen is served at `GET /api/kiosk/login`; its HTML carries a developer TODO comment:
>
> ```html
> <!-- TODO(dev): REMOVE before go-live — temporary QA technician PIN: deadface{v13w_s0urc3_sav3s_l1v3s} -->
> ```
>
> ```bash
> curl -s http://emedra.dctf.io:8080/api/kiosk/login
> ```
>
> The commented-out "QA technician PIN" is the flag: `deadface{v13w_s0urc3_sav3s_l1v3s}` ("view source saves lives"). It is bait for the login — the real technician credentials come from the field service manual (see *Factory Setting*).
>
> ---
