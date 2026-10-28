# Too Good to be True

**Platform:** PCGCTF · **Challenge ID:** 335 · **Category:** Deadface · **Points:** 1200

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

## Challenge and objective

Identify the primary endpoint value more than three standard deviations above the study mean and report the subject code.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/335-too-good-to-be-true/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The prompt provides a statistical criterion, so there is no need to guess a “large” threshold. Compute the mean and standard deviation over the same endpoint population, then express each value as a z-score: its distance from the mean divided by the standard deviation.

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

The subquery returns one row of summary statistics; `CROSS JOIN` attaches those constants to every endpoint result. The outer filter uses the same measure as the aggregate, keeping the reference population consistent. The saved report also checked sample standard deviation, yielding 6.73 for the same subject; the classification does not depend on that convention. The post-lock edited subject VELT-0137 is a separate case.

```sql
SELECT s.subject_code,s.arm,r.value,
 ROUND((r.value-st.m)/st.sd,2) AS z_score
FROM aurora_trials.results r
JOIN aurora_trials.subjects s ON s.subject_id=r.subject_id
CROSS JOIN (SELECT AVG(value) AS m,STDDEV_POP(value) AS sd
            FROM aurora_trials.results
            WHERE measure='primary_efficacy_delta') st
WHERE r.measure='primary_efficacy_delta'
ORDER BY z_score DESC;
```

**Originally teammate-recorded result; the query was independently repeated during the screenshot pass:**

```text
VELT-0148 | placebo | 22.00 | 6.78
VELT-0137 | treatment | 6.00 | 1.08
Recorded mean: approximately 2.97; only VELT-0148 exceeds +3 standard deviations.
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

### 335-step-02.png

![335-step-02.png](../screenshots/335-step-02.png)

Actual live read-only Aurora query result; compare the returned rows with step 2. This is not a new PCGCTF acceptance.

Command/action actually executed:

```sql
SELECT s.subject_code,s.arm,r.value,
 ROUND((r.value-st.m)/st.sd,2) AS z_score
FROM aurora_trials.results r
JOIN aurora_trials.subjects s ON s.subject_id=r.subject_id
CROSS JOIN (SELECT AVG(value) AS m,STDDEV_POP(value) AS sd
            FROM aurora_trials.results
            WHERE measure='primary_efficacy_delta') st
WHERE r.measure='primary_efficacy_delta'
ORDER BY z_score DESC;
```

Source viewed: [https://aurora.dctf.io/](https://aurora.dctf.io/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{VELT-0148}
```

Solved in our saved PCGCTF snapshot; SQL procedure and decisive rows are recorded by Antonio B. Garcia Jr., independently repeated in the live Aurora shell during the screenshot pass.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Statistical and audit-trail anomalies can point to different records. Explain the reference population and scale rather than assuming every suspicious endpoint belongs to the same incident.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/335-too-good-to-be-true/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/335-too-good-to-be-true/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)

## Leading outliers — compact live result

The full query returns 60 rows, so its earlier screenshot shows the tail of the output. I repeated the same read-only query with `LIMIT 5` to keep the highest z-scores visible. The actual result shows VELT-0148 at **6.78**, and the separate post-lock subject VELT-0137 at **1.08**.

```sql
SELECT s.subject_code,s.arm,r.value,
 ROUND((r.value-st.m)/st.sd,2) AS z_score
FROM aurora_trials.results r
JOIN aurora_trials.subjects s ON s.subject_id=r.subject_id
CROSS JOIN (SELECT AVG(value) AS m,STDDEV_POP(value) AS sd
            FROM aurora_trials.results
            WHERE measure='primary_efficacy_delta') st
WHERE r.measure='primary_efficacy_delta'
ORDER BY z_score DESC LIMIT 5;
```

![Actual leading outliers](../screenshots/335-leading-outliers.png)

Notice the subject code, placebo arm and 22.00 endpoint value in the first row. This confirms the statistical finding; it is not a new grader acceptance.
