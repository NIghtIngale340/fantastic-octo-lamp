# Schedule of Concern — saved solution

Flag / submission candidate: `deadface{9}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### Schedule of Concern (200) — Formulary / SQL
>
> **Flag:** `deadface{9}`
>
> #### Challenge
>
> Count the DEA Schedule II drugs in Aurora's pharmacy formulary.
>
> #### Solution
>
> Group the `drugs` table by schedule rather than guessing the stored format up front — the value could be `II`, `CII`, or `2`:
>
> ```sql
> SELECT dea_schedule, COUNT(*) FROM aurora_pharmacy.drugs GROUP BY dea_schedule;
> ```
>
> ```
> II  | 9      III | 4      IV | 5      V | 2      N | 12
> ```
>
> Schedule is stored as plain Roman numerals. Schedule II count is `9`. (Same baseline relied on in *Heavy Hand*.)
>
> ---
