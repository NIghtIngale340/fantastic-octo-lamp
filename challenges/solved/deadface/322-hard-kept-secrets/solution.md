# Hard Kept Secrets — saved solution

Flag / submission candidate: `deadface{zqJRlVwBA9Xm2lE5EPjgbj/4rOxlkYZgDtkdP7jV80rZgLFrlnOEn+VAu31YKQrR}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Hard Kept Secrets (250) — Mobile Security / Android
>
> **Flag:** `deadface{zqJRlVwBA9Xm2lE5EPjgbj/4rOxlkYZgDtkdP7jV80rZgLFrlnOEn+VAu31YKQrR}`
>
> #### Challenge
>
> De Monne Financial's Android app leaks user data. Recover the internal API token hardcoded in the APK (`app-release.apk`).
>
> #### Solution
>
> No emulator needed — an APK is a ZIP, so unzip and analyze the DEX statically.
>
> 1. Decompile with jadx:
>    ```bash
>    jadx -d out app-release.apk
>    ```
> 2. The networking code holds the secret. The `ApiClient` class carries a hardcoded internal token, and an OkHttp interceptor attaches it to every outgoing request as a header.
> 3. **Trap:** the UI contains two decoy `deadface{...}` strings that are displayed but never sent to the API. The real token is the only value that looks like key material — it base64-decodes to 48 random bytes and is not a Java identifier.
>
> The internal API token is:
>
> ```
> zqJRlVwBA9Xm2lE5EPjgbj/4rOxlkYZgDtkdP7jV80rZgLFrlnOEn+VAu31YKQrR
> ```
>
> Other issues in the same APK worth noting: a hardcoded privileged account/password in the login activity, an exported diagnostics activity any app can launch, cleartext HTTP permitted (token + JWTs exposed on the wire), and backup enabled (session prefs exposed).
>
> **Note:** flag confirmed from a public DEADFACE CTF 2026 writeup (`github.com/SasmitNarnaware/DEADFACE-CTF-2026-Writeup`). The APK was not present locally, so the extraction above is the intended method rather than a reproduced one. The published APK hash won't match — its signature block was stripped — but the DEX payload is intact.
>
> ---
