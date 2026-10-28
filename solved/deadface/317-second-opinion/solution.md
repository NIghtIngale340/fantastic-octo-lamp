# Second Opinion — saved solution

Flag / submission candidate: `deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Second Opinion (250) — Medical Device / IoT
>
> **Flag:** `deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}`
>
> **Target:** Emedra CerebraScan CS-9000
> **File:** `cs9000-field-service-manual.pdf`
>
> #### Challenge
>
> On the touchscreen the current patient is redacted to initials and a masked record number. Even without a login, sensitive patient info may be recoverable. The device has maintenance ports left exposed — not locked or covered with a plate. Use a tool from your toolkit to find information through them.
>
> #### Solution
>
> The redaction is only on the primary touchscreen UI. One of the exposed maintenance ports is a video output (HDMI), which mirrors the full, unredacted patient record — the flag `hdm1_l34ks_th3_wh0l3_p4t13nt` says it directly: "HDMI leaks the whole patient."
>
> Reproduced live. Plug the **HDMI Cable** into the HDMI port (`POST /api/connect {tool:"hdmi",port:"hdmi"}`) to get an `external-display` window token, then read the diagnostic mirror with that Bearer token, raising the OSD verbosity level:
>
> ```
> GET /api/external-display?level=0..3   (Authorization: Bearer <hdmi token>)
> ```
>
> Levels 0–2 keep field redaction on (`patient: G.M. / MRN ****13`). **Level 3** ("raw session dump") disables redaction:
>
> ```json
> {"osdLevel":3,"raw":true,
>  "patient":{"name":"Gideon Marsh","dob":"1981-10-31","mrn":"100413"},
>  "study":"Cranial perfusion, contrast","technician":"Service Technician",
>  "diagSession":"deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}"}
> ```
>
> The HDMI engineer OSD leaks the whole unredacted patient record — `deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}`.
>
> **Note:** reproduced live against the device on 2026-10-28. See also *Live Boot*. The external-display route needs the HDMI connect token, not the auth token (auth token → `No HDMI source connected`).
>
> ---
