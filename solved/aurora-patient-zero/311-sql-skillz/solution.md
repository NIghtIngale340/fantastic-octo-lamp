# SQL Skillz — saved solution

Flag / submission candidate: `deadface{Candesartan}`

Our original PCGCTF snapshot already marks this challenge solved. Answer independently corroborated from our original local evidence; teammate writeup preserved below. Existing solved snapshot unchanged.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Independent check

See [local decode / database results](../../../team-writeups/garcia-day1/independent-checks.json).

## Teammate’s writeup (quoted)

> ### SQL Skillz (500) — iOS App Analysis / SQLite
>
> **Flag:** `deadface{Candesartan}`
>
> #### Challenge
>
> Continue examining the Aurora Patient Portal iOS app. Using the patient data collected in *Info Leaks* and *Down the Rabbit Hole*, query the app's database file to find what medications the current patient takes other than Ibuprofen.
>
> #### Solution
>
> An `.ipa` is a zip. Extract it and the app bundle ships a SQLite database in the clear:
>
> ```
> Payload/aurora-patient-portal.app/aurora_meds.sqlite
> ```
>
> One table, keyed by Patient ID:
>
> ```sql
> CREATE TABLE medications (
>     pid INTEGER PRIMARY KEY,
>     medication_1 TEXT NOT NULL, medication_1_dosage TEXT, medication_1_frequency TEXT,
>     medication_2 TEXT NOT NULL, medication_2_dosage TEXT, medication_2_frequency TEXT
> );
> ```
>
> The `pid` is the Patient ID recovered in *Down the Rabbit Hole* (`847261`). Rather than trust the ID blindly, the row is findable by content — exactly one of the 100 rows lists Ibuprofen, and it is that patient's:
>
> ```sql
> SELECT * FROM medications WHERE medication_1 LIKE '%buprofen%' OR medication_2 LIKE '%buprofen%';
> ```
>
> ```
> 847261 | Ibuprofen | 400 mg | Every 8 hours as needed | Candesartan | 16 mg | Once daily
> ```
>
> The other 99 rows cycle through unrelated med pairs; only `pid 847261` carries Ibuprofen, confirming it is the current patient. The second medication is `Candesartan`.
>
> The leak: the app bundles every patient's full medication list in an unencrypted SQLite file, cross-referenced by the same Patient ID exposed elsewhere in the bundle.
>
> ---
