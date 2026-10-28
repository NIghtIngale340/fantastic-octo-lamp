# SQL Skillz

**Platform:** PCGCTF · **Challenge ID:** 311 · **Category:** Aurora Patient Zero · **Points:** 500

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Query the Aurora iOS application’s local medication database for the current patient’s non-Ibuprofen medication.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/aurora-patient-zero/311-sql-skillz/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The prerequisite challenges identify patient ID 847261. A bundled SQLite database can be read without running the iOS app, but the patient ID should still be cross-checked against the medication rows. Exactly one row in the saved database lists Ibuprofen, making that content check useful corroboration.

## Step-by-step solution

### 1. Locate the SQLite member in the nested IPA

An IPA is a ZIP container. The application’s database is an ordinary SQLite file, not an encrypted backup requiring the device keychain. Our earlier verification extracted the original member and saved its SHA-256.

```sh
Inspect AuroraPatientPortal.ipa.zip, then the inner AuroraPatientPortal.ipa, and extract Payload/aurora-patient-portal.app/aurora_meds.sqlite to a working copy.
```

**Recorded output / observation:**

```text
Database member: Payload/aurora-patient-portal.app/aurora_meds.sqlite
Table: medications
Relevant key: pid
```

Open the copied database read-only to avoid changing evidence.

### 2. Read the current patient’s row

This query finds the row by content independently of the prerequisite ID. It then checks that the returned pid agrees with 847261. The OR condition catches Ibuprofen regardless of which medication column holds it. A second targeted `WHERE pid=847261` query should return the same row.

```sql
SELECT * FROM medications
WHERE medication_1 LIKE '%buprofen%'
   OR medication_2 LIKE '%buprofen%';
```

**Recorded output / observation:**

```text
847261 | Ibuprofen | 400 mg | Every 8 hours as needed | Candesartan | 16 mg | Once daily
```

Candesartan is the second medication. Dosage and frequency corroborate the row but are not part of the requested Name field.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #311 — actual evidence capture

![311-readonly-sqlite.png](../screenshots/311-readonly-sqlite.png)

Actual read-only SQLite query for the recovered patient.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/311-capture.py
```

[Actual command transcript](../screenshots/capture-work/311-sqlite.terminal.log) · [Execution record](../screenshots/capture-work/311-sqlite.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved result / candidate:

```text
deadface{Candesartan}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

An application bundle can expose cross-referenced data without any runtime exploit. Validate the linkage between identity and patient key before extracting the requested clinical field.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/aurora-patient-zero/311-sql-skillz/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/aurora-patient-zero/311-sql-skillz/solution.md>)
- [independent-checks.json](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/independent-checks.json>)
- [aurora_meds.sqlite](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/aurora_meds.sqlite>)
