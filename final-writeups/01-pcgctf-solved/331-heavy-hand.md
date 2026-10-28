# Heavy Hand

**Platform:** PCGCTF · **Challenge ID:** 331 · **Category:** Deadface · **Points:** 500

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Rank prescribers by total quantity of Schedule II drugs dispensed in the final quarter of 2025, then report the leading prescriber’s DEA number.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/331-heavy-hand/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

This query has four distinct entities: dispensing events carry quantity and time; prescriptions connect those events to drugs and prescribers; drugs provide the schedule; prescribers provide the requested identifier. Counting prescriptions would miss the central quantity comparison.

## Step-by-step solution

### 1. Check the relevant schema

In the authorized Aurora SQL shell, confirm table and column names before adapting the query. `information_schema.columns` describes the database; sorting by schema, table and ordinal position groups related fields. This is a read-only discovery query.

```sql
SELECT table_schema, table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema IN ('aurora_ehr','aurora_audit','aurora_trials','aurora_pharmacy')
ORDER BY table_schema, table_name, ordinal_position;
```

**Live schema check:** the shared screenshot below shows the actual database/table inventory and column counts. The full column-list query above remains a reference procedure; that exact listing was not separately captured.

The live query below also checks that its referenced tables and columns exist in the current CTF database. Do not treat a missing or renamed column as a different solved result.

### 2. Apply the challenge-specific query

`SUM(quantity_dispensed)` answers volume, while the joins preserve the identity of the prescribing clinician. The end condition uses 2026-01-01 exclusively so that all of December 31 is included even if `dispensed_at` is a datetime. All nonaggregated selected columns appear in the grouping, making the query work under strict grouping modes. The requested DEA field in the leading row is BR2938471.

```sql
SELECT p.prescriber_id,p.first_name,p.last_name,p.dea_number,
       SUM(d.quantity_dispensed) AS total
FROM aurora_pharmacy.dispenses d
JOIN aurora_pharmacy.prescriptions rx ON rx.rx_id=d.rx_id
JOIN aurora_pharmacy.drugs g ON g.drug_id=rx.drug_id
JOIN aurora_pharmacy.prescribers p ON p.prescriber_id=rx.prescriber_id
WHERE g.dea_schedule='II'
  AND d.dispensed_at >= '2025-10-01'
  AND d.dispensed_at < '2026-01-01'
GROUP BY p.prescriber_id,p.first_name,p.last_name,p.dea_number
ORDER BY total DESC
LIMIT 5;
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
2 | Marcus | Reyes | BR2938471 | 5220
12 | Dorothy | Hill | BR2340466 | 150
Next recorded totals: 90, 90, 90
```

These values are the decisive rows recorded in Garcia’s Day 1 writeup. The original row transcription is attributed to that report. The screenshot pass independently executed the displayed query in Aurora; compare its actual rows in the capture below.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### aurora-live-databases.png

![aurora-live-databases.png](../screenshots/aurora-live-databases.png)

Actual live SHOW DATABASES result.

Command/action actually executed:

```sh
SHOW DATABASES;
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

### aurora-live-schema.png

![aurora-live-schema.png](../screenshots/aurora-live-schema.png)

Actual live read-only schema/table inventory with column counts. This is a compact inventory, not the full column listing.

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

### 331-step-02.png

![331-step-02.png](../screenshots/331-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT p.prescriber_id,p.first_name,p.last_name,p.dea_number,
       SUM(d.quantity_dispensed) AS total
FROM aurora_pharmacy.dispenses d
JOIN aurora_pharmacy.prescriptions rx ON rx.rx_id=d.rx_id
JOIN aurora_pharmacy.drugs g ON g.drug_id=rx.drug_id
JOIN aurora_pharmacy.prescribers p ON p.prescriber_id=rx.prescriber_id
WHERE g.dea_schedule='II'
  AND d.dispensed_at >= '2025-10-01'
  AND d.dispensed_at < '2026-01-01'
GROUP BY p.prescriber_id,p.first_name,p.last_name,p.dea_number
ORDER BY total DESC
LIMIT 5;
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{BR2938471}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Date boundaries and aggregation choice can change a ranking. Write the time window in terms of included instants and aggregate the quantity named by the question.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/331-heavy-hand/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/331-heavy-hand/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
