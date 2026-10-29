# Live Boot — saved solution

Flag / submission candidate: `deadface{h4rdc0d3d_k3ys_1n_th3_c0nf1g}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Live Boot (300) — Medical Device / IoT
>
> **Flag:** `deadface{h4rdc0d3d_k3ys_1n_th3_c0nf1g}`
>
> **Target:** `http://emedra.dctf.io:8080/` (Emedra CerebraScan CS-9000)
> **File:** `cs9000-field-service-manual.pdf`
>
> #### Challenge
>
> DEADFACE gained a live shell on the device, though hospital staff insist the underlying OS is unreachable. DEADFACE used keys for the device that aren't spelled out in the Field Manual. Access the device's file system and find what hardcoded keys you can find.
>
> #### Solution
>
> The CS-9000 is a medical scanner with a web interface on port 8080. The shipped `cs9000-field-service-manual.pdf` documents the sanctioned service keys, but the device firmware/config holds additional keys that were never published — the "keys that aren't spelled out in the Field Manual."
>
> Reproduced live. Sign in with the factory tech account (see *Factory Setting*) to get a session token, plug in the **Live Linux USB-A** tool (`POST /api/connect {tool:"live-linux",port:"usb-a"}`), then drive the shell via `POST /api/shell {token,line}`:
>
> ```
> cat README.txt          # => sudo mount /dev/sda2 /mnt ; ScanWorks lives in /mnt/opt/scanworks
> sudo mount /dev/sda2 /mnt
> cat /mnt/opt/scanworks/config.yaml
> ```
>
> `config.yaml` holds the planted secret:
>
> ```yaml
> # Upstream API key (service account). TODO: move to secrets store before GA.
> api_key: deadface{h4rdc0d3d_k3ys_1n_th3_c0nf1g}
> ```
>
> The internal storage is unencrypted; the "keys that aren't spelled out in the Field Manual" = the hardcoded `api_key` in the on-disk config. Flag `h4rdc0d3d_k3ys_1n_th3_c0nf1g` = "hardcoded keys in the config."
>
> **Note:** reproduced live against the device on 2026-10-28. Shell is a toy (no `2>/dev/null`, no command substitution; `>`/`>>` write to the mounted volume only).
>
> ---
