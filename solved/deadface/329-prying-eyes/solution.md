# Prying Eyes — saved solution

Flag / submission candidate: `deadface{rborden}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### Prying Eyes (300) — Audit Log / SQL
>
> **Flag:** `deadface{rborden}`
>
> #### Challenge
>
> Aurora Health logs every time a staff member opens a patient chart. Someone was watching the VIP a little too closely. Find the user account that accessed the VIP patient's chart more times than any other account, and report their username. The VIP's MRN comes from *Admitted Under Another Name*; the audit log references patients by that same MRN.
>
> #### Solution
>
> The VIP from *Admitted Under Another Name* is MRN `AH-0044719`, which resolves to patient 1007, **Gregory Halloran**:
>
> ```sql
> SELECT patient_id, mrn, first_name, last_name
> FROM aurora_ehr.patients WHERE mrn = 'AH-0044719';
> ```
>
> `aurora_audit.access_log` carries both `patient_mrn` and `patient_id`. A quick consistency check shows the two columns never disagree for this patient, so filtering on the MRN alone misses nothing:
>
> ```sql
> SELECT COUNT(*) FROM aurora_audit.access_log
> WHERE patient_id = 1007 XOR patient_mrn = 'AH-0044719';   -- 0
> ```
>
> Count accesses per account:
>
> ```sql
> SELECT u.user_id, u.username, u.role, COUNT(*) AS n,
>        GROUP_CONCAT(DISTINCT a.action) AS acts
> FROM aurora_audit.access_log a
> JOIN aurora_audit.users u ON u.user_id = a.user_id
> WHERE a.patient_mrn = 'AH-0044719'
> GROUP BY u.user_id, u.username, u.role
> ORDER BY n DESC;
> ```
>
> ```
> +---------+-------------+--------------------------+----+------+
> | user_id | username    | role                     | n  | acts |
> +---------+-------------+--------------------------+----+------+
> |      10 | rborden     | Health Information Clerk | 47 | view |
> |       3 | mreyes_ehr  | Physician                |  5 | view |
> |       7 | ebaker7     | Billing Specialist       |  2 | view |
> |      12 | manderson12 | Lab Technician           |  2 | view |
> |       6 | csanchez6   | Billing Specialist       |  1 | view |
> |      18 | cyoung18    | Lab Technician           |  1 | view |
> +---------+-------------+--------------------------+----+------+
> ```
>
> `rborden`, a Health Information Clerk with no clinical reason to be in the chart, viewed it 47 times, nearly ten times the treating physician's 5. Everyone else is in the low single digits.
>
> ---
