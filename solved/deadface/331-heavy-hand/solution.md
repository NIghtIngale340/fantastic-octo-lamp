# Heavy Hand — saved solution

Flag / submission candidate: `deadface{BR2938471}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### Heavy Hand (500) — Drug Diversion / SQL
>
> **Flag:** `deadface{BR2938471}`
>
> #### Challenge
>
> Find the prescriber with the highest total quantity of Schedule II medication dispensed between 2025-10-01 and 2025-12-31, and report their DEA number.
>
> #### Solution
>
> `aurora_pharmacy` has five tables. The chain from a dispensed quantity back to a DEA number runs:
>
> ```
> dispenses -> prescriptions -> drugs       (for the schedule)
>                            -> prescribers (for the DEA number)
> ```
>
> Pulling the full column list up front avoids guessing at names:
>
> ```sql
> SELECT table_name, column_name, data_type
> FROM information_schema.columns
> WHERE table_schema = 'aurora_pharmacy'
> ORDER BY table_name, ordinal_position;
> ```
>
> Two details decide whether the query is correct:
>
> 1. **Schedule format.** `drugs.dea_schedule` could be `II`, `CII`, or `2`. Checking first avoids a silently empty result:
>
>    ```sql
>    SELECT dea_schedule, COUNT(*) FROM drugs GROUP BY dea_schedule;
>    ```
>    ```
>    II | 9    III | 4    IV | 5    V | 2    N | 12
>    ```
>    Plain `II`.
>
> 2. **Date boundary.** `dispensed_at` is a `datetime`, not a `date`. Writing `BETWEEN '2025-10-01' AND '2025-12-31'` would silently drop every dispense after midnight on Dec 31, since the bare date compares as `00:00:00`. A half-open range avoids that.
>
> ```sql
> SELECT p.dea_number, p.first_name, p.last_name,
>        SUM(d.quantity_dispensed) AS total
> FROM dispenses d
> JOIN prescriptions rx ON rx.rx_id = d.rx_id
> JOIN drugs        g  ON g.drug_id = rx.drug_id
> JOIN prescribers  p  ON p.prescriber_id = rx.prescriber_id
> WHERE g.dea_schedule = 'II'
>   AND d.dispensed_at >= '2025-10-01'
>   AND d.dispensed_at <  '2026-01-01'
> GROUP BY p.prescriber_id
> ORDER BY total DESC
> LIMIT 5;
> ```
>
> ```
> +---------------+------------+-----------+------------+-------+
> | prescriber_id | first_name | last_name | dea_number | total |
> +---------------+------------+-----------+------------+-------+
> |             2 | Marcus     | Reyes     | BR2938471  |  5220 |
> |            12 | Dorothy    | Hill      | BR2340466  |   150 |
> |             4 | Steven     | Jones     | BP9010482  |    90 |
> |             1 | Anne       | Chang     | MR5041935  |    90 |
> |             8 | Charles    | White     | RC6458836  |    90 |
> +---------------+------------+-----------+------------+-------+
> ```
>
> Marcus Reyes dispensed roughly 35x the next highest prescriber. His DEA number is `BR2938471`.
>
> Note the cross-challenge link: the trial result in *After the Lock* was altered by `mreyes`, and *Upon the Throne* identifies a coerced, diversion-flagged physician. The same person appears in all three.
>
> ---
