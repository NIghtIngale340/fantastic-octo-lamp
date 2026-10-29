# Ghost in the Registry — saved solution

Flag / submission candidate: `deadface{AH-0090001}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### Ghost in the Registry (700) — Cross-Database Join / SQL
>
> **Flag:** `deadface{AH-0090001}`
>
> #### Challenge
>
> Investigators suspect a fabricated patient — one issued controlled-substance prescriptions but never seen for a single clinical encounter. Aurora uses one enterprise `patient_id` across all systems, so records join across databases. Find the patient with at least one Schedule II prescription but zero encounters in `aurora_ehr`, and report their MRN.
>
> #### Solution
>
> Confirm the schedule format first, so the filter can't silently miss a value:
>
> ```sql
> SELECT dea_schedule, COUNT(*) FROM aurora_pharmacy.drugs GROUP BY dea_schedule;
> -- II:9  III:4  IV:5  V:2  N:12   → plain 'II'
> ```
>
> The shared `patient_id` lets a Schedule II prescription in `aurora_pharmacy` be tested against encounter history in `aurora_ehr` with an anti-join. `NOT EXISTS` expresses "zero encounters" directly:
>
> ```sql
> SELECT p.patient_id, p.mrn, p.first_name, p.last_name,
>        COUNT(DISTINCT rx.rx_id) AS rx_count,
>        GROUP_CONCAT(DISTINCT d.brand_name) AS drugs
> FROM aurora_pharmacy.prescriptions rx
> JOIN aurora_pharmacy.drugs d  ON d.drug_id = rx.drug_id
> LEFT JOIN aurora_ehr.patients p ON p.patient_id = rx.patient_id
> WHERE d.dea_schedule = 'II'
>   AND NOT EXISTS (
>     SELECT 1 FROM aurora_ehr.encounters e
>     WHERE e.patient_id = rx.patient_id
>   )
> GROUP BY p.patient_id, p.mrn, p.first_name, p.last_name;
> ```
>
> ```
> +------------+------------+------------+-----------+----------+------------------------------------+
> | patient_id | mrn        | first_name | last_name | rx_count | drugs                              |
> +------------+------------+------------+-----------+----------+------------------------------------+
> |       1060 | AH-0090001 | Dana       | Kessler   |        3 | Amphetamine Salts,Hydrocodone/APAP |
> +------------+------------+------------+-----------+----------+------------------------------------+
> ```
>
> A single match: patient 1060, **Dana Kessler**, three Schedule II prescriptions (amphetamine salts and hydrocodone) and not one encounter on record — the diverted-narcotics paper trail that leads nowhere. MRN `AH-0090001`.
>
> Cross-challenge note: this same MRN appears in `kbhatt`'s log as a lab export on 2025-11-18, so the fabricated patient's records were also pulled through the compromised nurse account from *Two Places at Once*.
>
> ---
