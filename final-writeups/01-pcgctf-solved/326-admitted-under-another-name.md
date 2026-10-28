# Admitted Under Another Name

**Platform:** PCGCTF · **Challenge ID:** 326 · **Category:** Deadface · **Points:** 250

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Identify the patient registry’s VIP record and report its real Medical Record Number, not the alias or display name.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/326-admitted-under-another-name/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The prompt gives a reliable discriminator: staff marked the record as VIP. That is a stronger filter than guessing which patient name sounds important. The alias matters as context, but the requested identifier is the MRN in the same row.

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

`WHERE is_vip = 1` limits the query to the planted VIP record. Selecting `mrn` alongside the real name and alias keeps the identity fields distinguishable. The teammate records one matching row, so no tie-breaking rule is required. Although the description calls the service MSSQL, the saved working procedure uses MySQL syntax; verify the actual shell rather than assuming a dialect from that label.

```sql
SELECT patient_id, mrn, first_name, last_name, alias, is_vip
FROM aurora_ehr.patients
WHERE is_vip = 1;
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
1007 | AH-0044719 | Gregory | Halloran | George Harmon | 1
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

### 326-step-02.png

![326-step-02.png](../screenshots/326-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT patient_id, mrn, first_name, last_name, alias, is_vip
FROM aurora_ehr.patients
WHERE is_vip = 1;
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{AH-0044719}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

An alias is not the same as an internal identifier. Query the explicit flag and return the exact field named by the challenge; do not submit the most visually memorable value.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/326-admitted-under-another-name/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/326-admitted-under-another-name/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
