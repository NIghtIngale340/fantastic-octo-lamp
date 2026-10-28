# Ghost in the Registry

**Platform:** PCGCTF · **Challenge ID:** 334 · **Category:** Deadface · **Points:** 700

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Find a patient with a Schedule II prescription but no recorded encounter, and return that patient’s MRN.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/334-ghost-in-the-registry/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The challenge is defined by both presence and absence. An ordinary inner join to encounters would eliminate exactly the patient we want. Start from controlled-substance prescriptions, then use an anti-join condition to keep patients with no matching encounter.

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

`NOT EXISTS` tests the absence of any encounter for the shared enterprise patient ID. The formulary join restricts the prescriptions to Schedule II. Counting distinct prescription IDs prevents an accidental future one-to-many join from multiplying the recorded prescription count. Garcia’s result has one qualifying patient, with MRN AH-0090001.

```sql
SELECT p.patient_id,p.mrn,p.first_name,p.last_name,
       COUNT(DISTINCT rx.rx_id) AS rx_count
FROM aurora_pharmacy.prescriptions rx
JOIN aurora_pharmacy.drugs d ON d.drug_id=rx.drug_id
JOIN aurora_ehr.patients p ON p.patient_id=rx.patient_id
WHERE d.dea_schedule='II'
  AND NOT EXISTS (SELECT 1 FROM aurora_ehr.encounters e
                  WHERE e.patient_id=rx.patient_id)
GROUP BY p.patient_id,p.mrn,p.first_name,p.last_name;
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
1060 | AH-0090001 | Dana | Kessler | 3
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

### 334-step-02.png

![334-step-02.png](../screenshots/334-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT p.patient_id,p.mrn,p.first_name,p.last_name,
       COUNT(DISTINCT rx.rx_id) AS rx_count
FROM aurora_pharmacy.prescriptions rx
JOIN aurora_pharmacy.drugs d ON d.drug_id=rx.drug_id
JOIN aurora_ehr.patients p ON p.patient_id=rx.patient_id
WHERE d.dea_schedule='II'
  AND NOT EXISTS (SELECT 1 FROM aurora_ehr.encounters e
                  WHERE e.patient_id=rx.patient_id)
GROUP BY p.patient_id,p.mrn,p.first_name,p.last_name;
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{AH-0090001}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Absence is a real query condition. In forensic SQL, choose the join type to preserve the anomaly rather than inadvertently filtering it out.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/334-ghost-in-the-registry/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/334-ghost-in-the-registry/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
