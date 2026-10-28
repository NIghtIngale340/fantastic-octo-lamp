# Admitted Under Another Name — saved solution

Flag / submission candidate: `deadface{AH-0044719}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### Admitted Under Another Name (250) — PII / SQL
>
> **Flag:** `deadface{AH-0044719}`
>
> #### Challenge
>
> A high-profile patient checked into Aurora Health under a fake name; staff quietly flagged the record as VIP. Find them in the dumped patient registry and report their real MRN.
>
> #### Solution
>
> The `aurora_ehr.patients` table carries the tell directly — an `is_vip tinyint` flag alongside an `alias` column:
>
> ```sql
> USE aurora_ehr;
> SHOW COLUMNS FROM patients;   -- mrn, first_name, last_name, alias, ..., is_vip
> ```
>
> One record is flagged:
>
> ```sql
> SELECT mrn, first_name, last_name, alias, is_vip FROM patients WHERE is_vip = 1\G
> ```
>
> ```
>        mrn: AH-0044719
> first_name: Gregory
>  last_name: Halloran
>      alias: George Harmon
>     is_vip: 1
> ```
>
> Exactly one VIP row. The patient's real identity is Gregory Halloran, admitted under the alias "George Harmon". The real MRN is `AH-0044719`.
>
> ---
