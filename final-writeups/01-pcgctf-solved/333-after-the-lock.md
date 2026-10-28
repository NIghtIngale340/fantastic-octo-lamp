# After the Lock

**Platform:** PCGCTF · **Challenge ID:** 333 · **Category:** Deadface · **Points:** 600

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Find the subject whose primary efficacy result was modified after its study’s data-lock date.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/333-after-the-lock/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

A lock date freezes the study record for the purpose of this scenario. The comparison should use each result’s modification timestamp and the corresponding study’s lock date, not the initial recording timestamp or a hardcoded date from another trial.

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

The subject-to-study join supplies the correct lock date for each result. The saved query uses `>=`, which also includes an edit exactly at the lock boundary; the decisive row is five days later, so changing that boundary to strict `>` would not change this result. Cross-checking `data_changes` shows 2.3 was replaced by 6.0 for the same subject.

```sql
SELECT s.subject_code,r.visit,r.value,r.recorded_at,r.modified_by,
       r.modified_at,st.data_lock_date
FROM aurora_trials.results r
JOIN aurora_trials.subjects s ON s.subject_id=r.subject_id
JOIN aurora_trials.studies st ON st.study_id=s.study_id
WHERE r.measure='primary_efficacy_delta'
  AND r.modified_at >= st.data_lock_date
ORDER BY r.modified_at;
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
VELT-0137 | Week 24 | 6.00 | 2025-10-15 10:00:00 | mreyes | 2025-12-06 23:14:00 | 2025-12-01
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

### 333-step-02.png

![333-step-02.png](../screenshots/333-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT s.subject_code,r.visit,r.value,r.recorded_at,r.modified_by,
       r.modified_at,st.data_lock_date
FROM aurora_trials.results r
JOIN aurora_trials.subjects s ON s.subject_id=r.subject_id
JOIN aurora_trials.studies st ON st.study_id=s.study_id
WHERE r.measure='primary_efficacy_delta'
  AND r.modified_at >= st.data_lock_date
ORDER BY r.modified_at;
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{VELT-0137}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

A temporal anomaly needs a defensible comparison point. Join to the governing record instead of relying on memory, and document boundary behavior even when it does not affect the winning row.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/333-after-the-lock/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/333-after-the-lock/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
