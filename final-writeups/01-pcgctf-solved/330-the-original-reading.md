# The Original Reading

**Platform:** PCGCTF · **Challenge ID:** 330 · **Category:** Deadface · **Points:** 300

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Recover the original primary efficacy value overwritten in the trial audit trail.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/330-the-original-reading/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

Current results show the value after an edit, while the `data_changes` table preserves old and new values. The strongest starting filter is the endpoint name, `primary_efficacy_delta`, because the prompt says exactly one edit changed that measure.

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

Selecting `old_value` and `new_value` side by side prevents the common mistake of reporting 6.0, the replacement. Garcia’s record has one matching audit row, attributed to `mreyes`. The requested original value is the exact stored text `2.3`; rounding or adding zeros is unnecessary.

```sql
SELECT change_id, record_ref, field_name, old_value, new_value,
       changed_by, changed_at, reason
FROM aurora_trials.data_changes
WHERE field_name='primary_efficacy_delta'
ORDER BY changed_at;
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
500001 | VELT-0137 | primary_efficacy_delta | 2.3 | 6.0 | mreyes | 2025-12-06 23:14:00 | Query resolution per monitor
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

### 330-step-02.png

![330-step-02.png](../screenshots/330-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT change_id, record_ref, field_name, old_value, new_value,
       changed_by, changed_at, reason
FROM aurora_trials.data_changes
WHERE field_name='primary_efficacy_delta'
ORDER BY changed_at;
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{2.3}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

For tampering investigations, the current table and the audit trail answer different questions. Preserve the original representation when a challenge explicitly requests the value as recorded.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/330-the-original-reading/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/330-the-original-reading/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
