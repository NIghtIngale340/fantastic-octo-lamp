# Two Places at Once

**Platform:** PCGCTF · **Challenge ID:** 336 · **Category:** Deadface · **Points:** 1500

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Identify the legitimate account appearing on two different workstations at identical timestamps, repeatedly.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/336-two-places-at-once/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The anomaly is simultaneity, not simply a high activity count. Group accesses by user and exact timestamp, require more than one workstation, and only then count how often that collision occurs for each account. An IP difference supports the finding but is not a replacement for the workstation condition.

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

`HAVING` filters grouped timestamps rather than individual log rows. `COUNT(DISTINCT workstation)` avoids counting duplicate events on one machine as two physical locations. The outer count shows eight recurring collisions for kbhatt. This determines the database answer; it does not independently establish the scoreboard spelling.

```sql
SELECT u.user_id,u.username,COUNT(*) AS collisions
FROM (SELECT user_id,accessed_at
      FROM aurora_audit.access_log
      GROUP BY user_id,accessed_at
      HAVING COUNT(DISTINCT workstation)>1) t
JOIN aurora_audit.users u ON u.user_id=t.user_id
GROUP BY u.user_id,u.username
ORDER BY collisions DESC;
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
16 | kbhatt | 8
Example recorded collision: 2025-11-04 23:54:03, WS-028 and WS-008.
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

### 336-step-02.png

![336-step-02.png](../screenshots/336-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT u.user_id,u.username,COUNT(*) AS collisions
FROM (SELECT user_id,accessed_at
      FROM aurora_audit.access_log
      GROUP BY user_id,accessed_at
      HAVING COUNT(DISTINCT workstation)>1) t
JOIN aurora_audit.users u ON u.user_id=t.user_id
GROUP BY u.user_id,u.username
ORDER BY collisions DESC;
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{kbhat}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Database value versus reported accepted flag

The query returns **kbhatt**, with two final `t` characters. Garcia reports that `deadface{kbhatt}` was rejected and `deadface{kbhat}` was accepted. Our saved submission string therefore uses `kbhat`, but that acceptance is a teammate report, not a new observation. Before publishing this as an organizer typo, retain the acceptance screenshot or organizer confirmation.

**Evidence status:** see the actual captures below; any missing original artifact, unavailable target or unrecorded grader response remains explicitly unverified.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Evidence and grading are separate layers. Keep the exact database value even when a teammate reports that a misspelled flag was required.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/336-two-places-at-once/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/336-two-places-at-once/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
