# Signals from the Skull — teammate record outside saved inventory

This challenge title has no matching entry in our 192-challenge snapshot. Preserve the teammate’s solution separately; no ID or accepted status has been invented. The reported flag is `deadface{un3ncrypt3d_b4bbl3_fr0m_th3_sku11}`.

## Teammate writeup (quoted)

> ## Signals from the Skull (Medical Device / IoT — BLE)
>
> **Flag:** `deadface{un3ncrypt3d_b4bbl3_fr0m_th3_sku11}`
>
> **Target:** `http://emedra.dctf.io:8080/` (Emedra CerebraScan CS-9000)
>
> #### Challenge
>
> The CS-9000 broadcasts unencrypted BLE maintenance telemetry. Sniff it and recover the leaked flag. (Field manual §5: BLE is unauthenticated/unencrypted; handle `0x2a` = vitals, handle `0x37` = maintenance log, Base64 text chunked across sequence-numbered notifications — reassemble in seq order then Base64-decode.)
>
> #### Solution
>
> Reproduced live. Plug the **BLE Sniffer USB-A** tool (`POST /api/connect {tool:"ble-sniffer",port:"usb-a"}`) for a `ble-capture` token, then `GET /api/capture` with that Bearer token. Packets arrive out of order on two handles. Keep `0x37` (the maintenance log; `0x2a` is 6-byte binary vitals = noise), sort by `seq`, hex→bytes, concatenate, Base64-decode:
>
> ```python
> import json, base64
> pk  = json.load(open('capture.json'))['packets']
> log = sorted([p for p in pk if p['handle']=='0x37'], key=lambda x: x['seq'])
> print(base64.b64decode(bytes.fromhex(''.join(p['payload'] for p in log))).decode())
> ```
>
> ```
> St.Dymphna CS-9000 maint log | site=stdymphna-rmc-01 | tech=emedra-svc
> last_patient: Gideon Marsh (MRN 100413)
> note: telemetry unencrypted per EM-2019 default; flag deadface{un3ncrypt3d_b4bbl3_fr0m_th3_sku11}
> ```
>
> **Note:** reproduced live against the device on 2026-10-28. Full device recon in [EMEDRA_PREP.md](EMEDRA_PREP.md).
>
> ---
