# Upon the Throne

**Platform:** PCGCTF · **Challenge ID:** 332 · **Category:** Deadface · **Points:** 500

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Find the handler codename present in both audit users and EHR providers, and submit that shared codename.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/332-upon-the-throne/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The prompt describes a set intersection, not the most frequent handler on either side. A cross-database join directly expresses the relationship. Case and incidental whitespace can obscure a match, so normalize them for comparison without changing the original value displayed as evidence.

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

The `ON` condition compares the two stored reference fields after trimming and case normalization. The `WHERE` clause excludes blank placeholders that could otherwise match each other. The returned codename links audit account rborden and provider 5; it is the codename, not either insider’s username, that belongs inside the flag.

```sql
SELECT u.handler_ref,u.username,p.provider_id
FROM aurora_audit.users u
JOIN aurora_ehr.providers p
 ON UPPER(TRIM(u.handler_ref))=UPPER(TRIM(p.handler_ref))
WHERE u.handler_ref IS NOT NULL AND TRIM(u.handler_ref)<>'';
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
REVENANT-7 | rborden | 5
Recorded sanity check: 16 distinct handler references on each side; one shared value.
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

### 332-step-02.png

![332-step-02.png](../screenshots/332-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT u.handler_ref,u.username,p.provider_id
FROM aurora_audit.users u
JOIN aurora_ehr.providers p
 ON UPPER(TRIM(u.handler_ref))=UPPER(TRIM(p.handler_ref))
WHERE u.handler_ref IS NOT NULL AND TRIM(u.handler_ref)<>'';
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{REVENANT-7}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Cross-system correlation works best through deliberate linkage fields. Excluding empty values matters: a blank-to-blank join can masquerade as a meaningful intersection.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/332-upon-the-throne/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/332-upon-the-throne/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
