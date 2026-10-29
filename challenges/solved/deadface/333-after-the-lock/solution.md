# After the Lock — saved solution

Flag / submission candidate: `deadface{VELT-0137}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### After the Lock (600) — Forensics / SQL
>
> **Flag:** `deadface{VELT-0137}`
>
> #### Challenge
>
> Once a clinical trial's database is locked, results are frozen. Any edit after the data-lock date is a protocol violation. Find the subject whose `primary_efficacy_delta` result was modified after the study's data-lock date.
>
> #### Solution
>
> The `aurora_trials` database holds six tables: `adverse_events`, `data_changes`, `results`, `sites`, `studies`, `subjects`.
>
> First, get the official lock date from `studies`:
>
> ```sql
> USE aurora_trials;
> SELECT * FROM studies\G
> ```
>
> ```
>        study_id: 1
> protocol_number: AUR-VLT-3001
>           title: A Phase III Randomized, Double-Blind Study of Veltrexa...
>          status: data locked
>      start_date: 2025-01-06
>  data_lock_date: 2025-12-01
> ```
>
> The `results` table carries both `recorded_at` and `modified_at`, which makes the comparison direct. Joining through `subjects` to `studies` lets the lock date be compared per-row rather than hardcoded:
>
> ```sql
> SELECT s.subject_code, r.visit, r.value, r.recorded_at,
>        r.modified_by, r.modified_at, st.data_lock_date
> FROM results r
> JOIN subjects s ON s.subject_id = r.subject_id
> JOIN studies  st ON st.study_id = s.study_id
> WHERE r.measure = 'primary_efficacy_delta'
>   AND r.modified_at >= st.data_lock_date
> ORDER BY r.modified_at;
> ```
>
> ```
> +--------------+---------+-------+---------------------+-------------+---------------------+----------------+
> | subject_code | visit   | value | recorded_at         | modified_by | modified_at         | data_lock_date |
> +--------------+---------+-------+---------------------+-------------+---------------------+----------------+
> | VELT-0137    | Week 24 |  6.00 | 2025-10-15 10:00:00 | mreyes      | 2025-12-06 23:14:00 | 2025-12-01     |
> +--------------+---------+-------+---------------------+-------------+---------------------+----------------+
> ```
>
> Exactly one row. The `data_changes` audit table confirms it and shows what was altered:
>
> ```sql
> SELECT * FROM data_changes WHERE changed_at >= '2025-11-25' ORDER BY changed_at;
> ```
>
> ```
> change_id  | 500001
> table_name | results
> record_ref | VELT-0137
> field_name | primary_efficacy_delta
> old_value  | 2.3
> new_value  | 6.0
> changed_by | mreyes
> changed_at | 2025-12-06 23:14:00
> reason     | Query resolution per monitor
> ```
>
> The value was nearly tripled five days after the lock, at 23:14, under a plausible-sounding reason. The subject code is `VELT-0137`.
>
> ---
