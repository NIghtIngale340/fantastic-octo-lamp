# Hooked — saved solution

Flag / submission candidate: `deadface{http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc}`

Our original PCGCTF snapshot already marks this challenge solved. Answer independently corroborated from our original local evidence; teammate writeup preserved below. Existing solved snapshot unchanged.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Independent check

See [local decode / database results](../../../../team/garcia-day1/independent-checks.json).

## Teammate’s writeup (quoted)

> ## Hooked (150) — Forensics / Browser Artifacts
>
> **Flag:** `deadface{http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc}`
>
> **File:** Chrome profile imaged from `DEMONNE-WS04` (`Chrome/User Data/Default/` — `History`, `Login Data`, `Cookies`, `Cache`)
>
> #### Challenge
>
> De Monne workstation DEMONNE-WS04 (employee Fletcher Kampeter) logged a credential submission to an unknown external host at 10:23 AM on March 14, 2025. From the imaged browser artifacts, recover the phishing URL the employee clicked.
>
> #### Solution
>
> Solved locally against the artifacts. Chrome's `History` is a SQLite DB; the `urls` and `visits` tables reconstruct the click chain.
>
> ```python
> import sqlite3, shutil
> shutil.copy('History','hist_copy.db')
> c = sqlite3.connect('hist_copy.db')
> for r in c.execute('SELECT id,url,title,last_visit_time FROM urls ORDER BY id'):
>     print(r)
> for r in c.execute('SELECT id,url,from_visit,transition,visit_time FROM visits ORDER BY visit_time'):
>     print(r)
> ```
>
> The visit chain (`from_visit` links each hop):
>
> ```
> url 4  [URGENT] De Monne VPN Migration - Action Required (Gmail)
>   -> url 5  Gmail inbox
>   -> url 6  http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc   (De Monne "Secure Employee Portal")
>   -> url 7  http://demonne-secure-portal.net/auth/redirect?session=9f3a22cd&status=ok  (auto-redirect after credential capture)
> ```
>
> The phishing landing page clicked from the email is **url 6**. Its Chrome timestamp `13386421424000000` converts to 2025-03-14 10:23:44 (Chrome epoch = microseconds since 1601; `/1e6 - 11644473600`), matching the logged 10:23 AM credential submission. url 7 is the post-submit redirect, not the clicked link.
>
> Flag: `deadface{http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc}`.
>
> **Note:** reproduced locally from the provided `ctf_artifacts` Chrome profile.
>
> ---
