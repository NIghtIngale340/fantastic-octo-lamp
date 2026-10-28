# The Attending — saved solution

Flag / submission candidate: `deadface{mreyes}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### The Attending (300) — Cross-Table Join / SQL
>
> **Flag:** `deadface{mreyes}`
>
> #### Challenge
>
> Stay on the VIP. The patient flagged `is_vip = 1` in Aurora's patients table had exactly one inpatient admission in November 2025. DEADFACE wants to know which physician signed off on that stay — the first name in the chain they leaned on. Identify the attending provider for that admission and report their system username.
>
> #### Solution
>
> The VIP flag confirms the patient from *Prying Eyes*:
>
> ```sql
> SELECT patient_id, mrn, first_name, last_name
> FROM aurora_ehr.patients WHERE is_vip = 1;
> -- 1007 | AH-0044719 | Gregory | Halloran
> ```
>
> `aurora_ehr.encounters` stores the attending as `attending_provider_id`, a foreign key into `aurora_ehr.providers`, which has its own `username` column. Join the VIP's encounters to the provider:
>
> ```sql
> SELECT e.encounter_id, e.encounter_type, e.department,
>        e.admit_date, e.discharge_date, e.status,
>        p.provider_id, p.first_name, p.last_name, p.username
> FROM aurora_ehr.encounters e
> LEFT JOIN aurora_ehr.providers p ON p.provider_id = e.attending_provider_id
> WHERE e.patient_id = 1007
> ORDER BY e.admit_date;
> ```
>
> ```
> +--------------+----------------+-------------+------------+----------------+------------+-------------+------------+-----------+----------+
> | encounter_id | encounter_type | department  | admit_date | discharge_date | status     | provider_id | first_name | last_name | username |
> +--------------+----------------+-------------+------------+----------------+------------+-------------+------------+-----------+----------+
> |         5017 | Inpatient      | Pain Clinic | 2025-11-14 | 2025-11-17     | discharged |           5 | Marcus     | Reyes     | mreyes   |
> +--------------+----------------+-------------+------------+----------------+------------+-------------+------------+-----------+----------+
> ```
>
> The VIP has a single encounter on record: a three-day inpatient stay in the Pain Clinic, attended by provider 5, **Dr. Marcus Reyes**, EHR username `mreyes`.
>
> Note the two usernames: the EHR provider record says `mreyes`, while his audit-system account in `aurora_audit.users` is `mreyes_ehr`. The challenge asks about the attending provider, so the provider table's `mreyes` is the one to submit.
>
> Cross-challenge note: Reyes is the same physician behind the diversion in *Heavy Hand* and the post-lock trial edit in *After the Lock*.
>
> ---
