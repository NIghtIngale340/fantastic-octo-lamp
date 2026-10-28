# The Original Reading — saved solution

Flag / submission candidate: `deadface{2.3}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### The Original Reading (300) — Audit Trail / SQL
>
> **Flag:** `deadface{2.3}`
>
> #### Challenge
>
> Aurora's Phase III trial for Veltrexa keeps a full audit trail of every edit in a `data_changes` table. Most entries are routine source-data corrections, but exactly one rewrote a primary efficacy endpoint to make the drug look like it worked. Recover the original value that was overwritten.
>
> #### Solution
>
> `aurora_trials.data_changes` holds only 9 rows, so the whole table fits on screen:
>
> ```sql
> USE aurora_trials;
> SELECT * FROM data_changes\G
> ```
>
> Eight rows are placeholder corrections — `arm`, `status` and `enrollment_date` edits on `subjects`, all with `old_value` `(prior)` → `new_value` `(corrected)`, all stamped at `09:30:00`, reason `Source data verification`. One row is different:
>
> ```
> change_id:  500001
> table_name: results
> record_ref: VELT-0137
> field_name: primary_efficacy_delta
> old_value:  2.3
> new_value:  6.0
> changed_by: mreyes
> changed_at: 2025-12-06 23:14:00
> reason:     Query resolution per monitor
> ```
>
> Only this row touches a `primary_efficacy_delta`. The value was nearly tripled (2.3 → 6.0) late at night at 23:14 — off from the 09:30 batch stamp of every routine edit — under a plausible-sounding reason. This is the same `VELT-0137` / `mreyes` tamper seen in *After the Lock*; that challenge wanted the subject, this one wants the overwritten value.
>
> The original reading is `2.3`.
>
> ---
