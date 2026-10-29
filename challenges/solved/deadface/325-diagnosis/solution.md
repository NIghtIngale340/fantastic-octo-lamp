# Diagnosis — saved solution

Flag / submission candidate: `deadface{flaG_ManIfesT3d}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Diagnosis (500) — Mobile Security / Android
>
> **Flag:** `deadface{flaG_ManIfesT3d}`
>
> **File:** `app-release.apk` (De Monne Financial Android app, reused from *Hard Kept Secrets*)
>
> #### Challenge
>
> A De Monne developer suspects hidden activity in the app, possibly from manifest misconfigurations. The challenge reuses the ZIP/APK from *Hard Kept Secrets*.
>
> #### Solution
>
> The flag name ("ManIfesT3d") and the "manifest misconfiguration / hidden activity" wording point to the `AndroidManifest.xml`: an app component left exported that should not be reachable.
>
> Intended approach:
>
> 1. Extract the ZIP into an empty directory, then decode the APK with `apktool d app-release.apk` (or open it in `jadx`).
> 2. Read `AndroidManifest.xml` for exported activities, services, providers and receivers that declare no permission; also check `android:debuggable`, `android:allowBackup`, unusual `intent-filter` entries and `meta-data` values.
>    ```bash
>    grep -i "exported" out/AndroidManifest.xml
>    ```
> 3. Launch the hidden exported activity on a device/emulator to reveal the flag, or follow it into its implementing class:
>    ```bash
>    adb shell am start -n <package>/<hidden.activity>
>    ```
>
> **Note:** flag confirmed by two independent DEADFACE CTF 2026 writeup repos; the APK was not decompiled locally, so the steps above are the intended method rather than a reproduced one.
>
> ---
