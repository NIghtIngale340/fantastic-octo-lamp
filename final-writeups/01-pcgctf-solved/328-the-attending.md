# The Attending

**Platform:** PCGCTF · **Challenge ID:** 328 · **Category:** Deadface · **Points:** 300

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Find the attending provider for the VIP’s November 2025 inpatient encounter and report that provider’s system username.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/328-the-attending/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

This continues the VIP investigation rather than restarting it. The patient table establishes the identity, while the encounter table contains the foreign key naming the attending. A person’s audit account can differ from the provider account, so the join must end at `providers.username`.

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

The joins follow patient → encounter → provider. The half-open month range includes every November time without relying on midnight at the end of the month. Garcia’s recorded encounter is a three-day Pain Clinic admission. Its attending provider has username `mreyes`; the related audit-system username `mreyes_ehr` is not the field requested here.

```sql
SELECT e.encounter_id, e.encounter_type, e.admit_date, e.discharge_date,
       p.provider_id, p.first_name, p.last_name, p.username
FROM aurora_ehr.encounters e
JOIN aurora_ehr.patients v ON v.patient_id=e.patient_id
JOIN aurora_ehr.providers p ON p.provider_id=e.attending_provider_id
WHERE v.is_vip=1 AND e.encounter_type='Inpatient'
  AND e.admit_date >= '2025-11-01' AND e.admit_date < '2025-12-01';
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
5017 | Inpatient | 2025-11-14 | 2025-11-17 | 5 | Marcus | Reyes | mreyes
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

### 328-step-02.png

![328-step-02.png](../screenshots/328-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT e.encounter_id, e.encounter_type, e.admit_date, e.discharge_date,
       p.provider_id, p.first_name, p.last_name, p.username
FROM aurora_ehr.encounters e
JOIN aurora_ehr.patients v ON v.patient_id=e.patient_id
JOIN aurora_ehr.providers p ON p.provider_id=e.attending_provider_id
WHERE v.is_vip=1 AND e.encounter_type='Inpatient'
  AND e.admit_date >= '2025-11-01' AND e.admit_date < '2025-12-01';
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{mreyes}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Following foreign keys is more dependable than matching people by name. Similar usernames in different systems are separate values until the evidence connects them.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/328-the-attending/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/328-the-attending/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
