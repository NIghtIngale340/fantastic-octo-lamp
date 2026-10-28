# Prying Eyes

**Platform:** PCGCTF · **Challenge ID:** 329 · **Category:** Deadface · **Points:** 300

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Count accesses to the VIP’s chart and identify the account with the highest count.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/329-prying-eyes/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

With MRN AH-0044719 established, the problem becomes an audit-log aggregation. The ranking should count individual accesses to that chart, not every event performed by the account across the hospital. Joining `users` gives a readable username after grouping the log.

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

`WHERE` chooses the target patient before aggregation. `GROUP BY` creates one row per account, and descending count puts the highest accessor first. The saved result makes `rborden` the clear leader at 47. This identifies a usage anomaly; the challenge narrative supplies the malicious context, rather than the SQL count alone proving intent.

```sql
SELECT u.user_id, u.username, u.role, COUNT(*) AS accesses
FROM aurora_audit.access_log a
JOIN aurora_audit.users u ON u.user_id=a.user_id
WHERE a.patient_mrn='AH-0044719'
GROUP BY u.user_id,u.username,u.role
ORDER BY accesses DESC;
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
10 | rborden | Health Information Clerk | 47
3  | mreyes_ehr | Physician | 5
Other listed accounts: 1–2 accesses each
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

### 329-step-02.png

![329-step-02.png](../screenshots/329-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT u.user_id, u.username, u.role, COUNT(*) AS accesses
FROM aurora_audit.access_log a
JOIN aurora_audit.users u ON u.user_id=a.user_id
WHERE a.patient_mrn='AH-0044719'
GROUP BY u.user_id,u.username,u.role
ORDER BY accesses DESC;
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{rborden}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

A suspicious count needs the right denominator and target. Filter the relevant object first, then compare users; do not infer guilt solely from a job title or a large number.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/329-prying-eyes/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/329-prying-eyes/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
