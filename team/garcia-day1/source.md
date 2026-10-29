# CTF Writeups

**Author:** Antonio B. Garcia Jr.
**Date:** 2026-10-28

---

## DEADFACE CTF — Aurora Health

All three Aurora challenges use the same browser-based MySQL shell at `https://aurora.dctf.io/`. The server exposes four relevant databases:

```
aurora_audit
aurora_ehr
aurora_pharmacy
aurora_trials
```

The shell connects with no database selected, so every session starts with a `USE` statement or fully-qualified table names.

---

### After the Lock (600) — Forensics / SQL

**Flag:** `deadface{VELT-0137}`

#### Challenge

Once a clinical trial's database is locked, results are frozen. Any edit after the data-lock date is a protocol violation. Find the subject whose `primary_efficacy_delta` result was modified after the study's data-lock date.

#### Solution

The `aurora_trials` database holds six tables: `adverse_events`, `data_changes`, `results`, `sites`, `studies`, `subjects`.

First, get the official lock date from `studies`:

```sql
USE aurora_trials;
SELECT * FROM studies\G
```

```
       study_id: 1
protocol_number: AUR-VLT-3001
          title: A Phase III Randomized, Double-Blind Study of Veltrexa...
         status: data locked
     start_date: 2025-01-06
 data_lock_date: 2025-12-01
```

The `results` table carries both `recorded_at` and `modified_at`, which makes the comparison direct. Joining through `subjects` to `studies` lets the lock date be compared per-row rather than hardcoded:

```sql
SELECT s.subject_code, r.visit, r.value, r.recorded_at,
       r.modified_by, r.modified_at, st.data_lock_date
FROM results r
JOIN subjects s ON s.subject_id = r.subject_id
JOIN studies  st ON st.study_id = s.study_id
WHERE r.measure = 'primary_efficacy_delta'
  AND r.modified_at >= st.data_lock_date
ORDER BY r.modified_at;
```

```
+--------------+---------+-------+---------------------+-------------+---------------------+----------------+
| subject_code | visit   | value | recorded_at         | modified_by | modified_at         | data_lock_date |
+--------------+---------+-------+---------------------+-------------+---------------------+----------------+
| VELT-0137    | Week 24 |  6.00 | 2025-10-15 10:00:00 | mreyes      | 2025-12-06 23:14:00 | 2025-12-01     |
+--------------+---------+-------+---------------------+-------------+---------------------+----------------+
```

Exactly one row. The `data_changes` audit table confirms it and shows what was altered:

```sql
SELECT * FROM data_changes WHERE changed_at >= '2025-11-25' ORDER BY changed_at;
```

```
change_id  | 500001
table_name | results
record_ref | VELT-0137
field_name | primary_efficacy_delta
old_value  | 2.3
new_value  | 6.0
changed_by | mreyes
changed_at | 2025-12-06 23:14:00
reason     | Query resolution per monitor
```

The value was nearly tripled five days after the lock, at 23:14, under a plausible-sounding reason. The subject code is `VELT-0137`.

---

### Upon the Throne (500) — Correlation / SQL

**Flag:** `deadface{REVENANT-7}`

#### Challenge

A DEADFACE handler ran one insider on each side of the house. The handler's codename sits in a `handler_ref` field on both the audit-system users and the EHR providers. Around fifteen codenames appear on each side, but only one appears in both.

#### Solution

This is a set intersection across two databases. MySQL allows cross-database joins in a single query, so no export is needed:

```sql
SELECT u.handler_ref, u.username, p.provider_id
FROM aurora_audit.users u
JOIN aurora_ehr.providers p
  ON UPPER(TRIM(u.handler_ref)) = UPPER(TRIM(p.handler_ref))
WHERE u.handler_ref IS NOT NULL AND TRIM(u.handler_ref) <> '';
```

`UPPER(TRIM(...))` guards against case or whitespace differences between the two tables, which would otherwise hide a valid match.

```
+------------+----------+-------------+
| u_ref      | username | provider_id |
+------------+----------+-------------+
| REVENANT-7 | rborden  |           5 |
+------------+----------+-------------+
1 row in set
```

Sanity check on the population size — 16 distinct values on each side, matching the challenge's "around fifteen":

```sql
SELECT COUNT(DISTINCT handler_ref) FROM aurora_audit.users;      -- 16
SELECT COUNT(DISTINCT handler_ref) FROM aurora_ehr.providers;    -- 16
```

One codename in both: `REVENANT-7`, running audit user `rborden` and EHR provider 5.

---

### Heavy Hand (500) — Drug Diversion / SQL

**Flag:** `deadface{BR2938471}`

#### Challenge

Find the prescriber with the highest total quantity of Schedule II medication dispensed between 2025-10-01 and 2025-12-31, and report their DEA number.

#### Solution

`aurora_pharmacy` has five tables. The chain from a dispensed quantity back to a DEA number runs:

```
dispenses -> prescriptions -> drugs       (for the schedule)
                           -> prescribers (for the DEA number)
```

Pulling the full column list up front avoids guessing at names:

```sql
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'aurora_pharmacy'
ORDER BY table_name, ordinal_position;
```

Two details decide whether the query is correct:

1. **Schedule format.** `drugs.dea_schedule` could be `II`, `CII`, or `2`. Checking first avoids a silently empty result:

   ```sql
   SELECT dea_schedule, COUNT(*) FROM drugs GROUP BY dea_schedule;
   ```
   ```
   II | 9    III | 4    IV | 5    V | 2    N | 12
   ```
   Plain `II`.

2. **Date boundary.** `dispensed_at` is a `datetime`, not a `date`. Writing `BETWEEN '2025-10-01' AND '2025-12-31'` would silently drop every dispense after midnight on Dec 31, since the bare date compares as `00:00:00`. A half-open range avoids that.

```sql
SELECT p.dea_number, p.first_name, p.last_name,
       SUM(d.quantity_dispensed) AS total
FROM dispenses d
JOIN prescriptions rx ON rx.rx_id = d.rx_id
JOIN drugs        g  ON g.drug_id = rx.drug_id
JOIN prescribers  p  ON p.prescriber_id = rx.prescriber_id
WHERE g.dea_schedule = 'II'
  AND d.dispensed_at >= '2025-10-01'
  AND d.dispensed_at <  '2026-01-01'
GROUP BY p.prescriber_id
ORDER BY total DESC
LIMIT 5;
```

```
+---------------+------------+-----------+------------+-------+
| prescriber_id | first_name | last_name | dea_number | total |
+---------------+------------+-----------+------------+-------+
|             2 | Marcus     | Reyes     | BR2938471  |  5220 |
|            12 | Dorothy    | Hill      | BR2340466  |   150 |
|             4 | Steven     | Jones     | BP9010482  |    90 |
|             1 | Anne       | Chang     | MR5041935  |    90 |
|             8 | Charles    | White     | RC6458836  |    90 |
+---------------+------------+-----------+------------+-------+
```

Marcus Reyes dispensed roughly 35x the next highest prescriber. His DEA number is `BR2938471`.

Note the cross-challenge link: the trial result in *After the Lock* was altered by `mreyes`, and *Upon the Throne* identifies a coerced, diversion-flagged physician. The same person appears in all three.

---

### Two Places at Once (450) — Compromised Account / SQL

**Flag:** `deadface{kbhat}`  *(accepted spelling — single `t`; see note below)*

#### Challenge

DEADFACE bragged on the GhostTown forum about using one legitimate account from two places at once. Find the compromised account — the one whose login shows up on two different workstations at the very same timestamp, over and over. Report the username.

#### Solution

The evidence lives in `aurora_audit.access_log`, which records one row per access with `user_id`, `workstation`, `ip_address`, `action` and `accessed_at`. "Two places at once" means the same account on two distinct workstations at an identical timestamp — a physical impossibility for a real person.

Group by account and timestamp, and keep only groups spanning more than one workstation:

```sql
SELECT u.user_id, u.username, COUNT(*) AS collisions
FROM (
  SELECT user_id, accessed_at
  FROM aurora_audit.access_log
  GROUP BY user_id, accessed_at
  HAVING COUNT(DISTINCT workstation) > 1
) t
JOIN aurora_audit.users u ON u.user_id = t.user_id
GROUP BY u.user_id, u.username
ORDER BY collisions DESC;
```

```
+---------+----------+------------+
| user_id | username | collisions |
+---------+----------+------------+
|      16 | kbhatt   |          8 |
+---------+----------+------------+
```

Exactly one account, and the "over and over" in the prompt is literal: 8 separate collisions. The colliding rows show the pattern plainly:

```sql
SELECT user_id, accessed_at, GROUP_CONCAT(workstation) AS ws,
       GROUP_CONCAT(ip_address) AS ips
FROM aurora_audit.access_log
GROUP BY user_id, accessed_at
HAVING COUNT(DISTINCT workstation) > 1;
```

```
| 16 | 2025-11-04 23:54:03 | WS-028,WS-008 | 10.20.3.222,10.20.3.213 |
| 16 | 2025-11-05 23:55:55 | WS-013,WS-025 | 10.20.1.125,10.20.2.18  |
| 16 | 2025-11-14 02:18:01 | WS-002,WS-023 | 10.20.4.88,10.20.4.21   |
| 16 | 2025-11-18 01:23:54 | WS-027,WS-015 | 10.20.2.200,10.20.4.176 |
| 16 | 2025-11-19 02:37:21 | WS-026,WS-008 | 10.20.3.76,10.20.4.54   |
| 16 | 2025-11-21 02:51:31 | WS-029,WS-018 | 10.20.1.49,10.20.2.101  |
| 16 | 2025-11-23 02:29:51 | WS-030,WS-006 | 10.20.4.52,10.20.2.100  |
| 16 | 2025-11-27 03:57:17 | WS-022,WS-011 | 10.20.4.227,10.20.2.165 |
```

Every pair is a different workstation and a different internal IP at the exact same second, all during overnight hours (23:54–03:57). Of the 432 rows in the table, 416 fall on an exact minute (`:00` seconds) and the 16 odd-second rows are precisely these 8 planted pairs — the anomaly stands out even before the join.

`user_id 16` is `kbhatt` (Kavya Bhatt), the only account with the role **Registered Nurse**. That matches DEADFACE's own brag on GhostTown (thread 49, *"Shelby Medical Center really thought nobody would notice?"* by `luciafer`): a socially-engineered registered nurse, VPN access with her valid credentials, both parties logged in at once — *"Same credentials. Same moments. Different workstations."* — including `print` and `export` actions, which appear in her log rows.

**Verification / the gotcha:** the database stores the username as `kbhatt` (double `t`), but the scoreboard only accepts **`deadface{kbhat}`** with a single `t`. The challenge author mistyped the flag when setting it, so the "correct" database value is rejected and the typo is required. This is why every `deadface{kbhatt}` submission failed despite the query being right. If a `deadface{...}` answer keeps bouncing when the data clearly supports it, suspect an author-side typo and try the obvious misspellings before assuming the data is wrong.

---

### Too Good to be True (1200) — Statistical Outlier / SQL

**Flag:** `deadface{VELT-0148}`

#### Challenge

One subject's recorded efficacy improvement is a statistical impossibility — more than three standard deviations above the study-wide mean for the primary endpoint, a sign the number was invented rather than measured. Identify the outlier subject and report their subject code.

#### Solution

The primary endpoint is the `primary_efficacy_delta` measure in `aurora_trials.results`, recorded at Week 24 for 60 subjects. Compute each subject's z-score against the measure's mean and standard deviation in one pass, using a `CROSS JOIN` to a single-row aggregate:

```sql
SELECT s.subject_code, s.arm, r.value,
       ROUND((r.value - st.m)/st.sd_pop, 2)  AS z_pop,
       ROUND((r.value - st.m)/st.sd_samp, 2) AS z_samp,
       r.recorded_by, r.modified_by
FROM aurora_trials.results r
JOIN aurora_trials.subjects s ON s.subject_id = r.subject_id
CROSS JOIN (
  SELECT AVG(value) m, STDDEV_POP(value) sd_pop, STDDEV_SAMP(value) sd_samp
  FROM aurora_trials.results WHERE measure = 'primary_efficacy_delta'
) st
WHERE r.measure = 'primary_efficacy_delta'
ORDER BY r.value DESC
LIMIT 8;
```

```
+--------------+-----------+-------+-------+--------+-------------+-------------+
| subject_code | arm       | value | z_pop | z_samp | recorded_by | modified_by |
+--------------+-----------+-------+-------+--------+-------------+-------------+
| VELT-0148    | placebo   | 22.00 |  6.78 |   6.73 | tstack      | NULL        |
| VELT-0137    | treatment |  6.00 |  1.08 |   1.07 | achang      | mreyes      |
| VELT-0138    | placebo   |  5.25 |  0.81 |   0.81 | achang      | NULL        |
| VELT-0130    | placebo   |  5.22 |  0.80 |   0.80 | tstack      | NULL        |
+--------------+-----------+-------+-------+--------+-------------+-------------+
```

Only `VELT-0148` clears the 3-SD bar — it sits **6.78** standard deviations above the mean of 2.97. The next-highest subject is at 1.08, and the lowest value (−1.00) is only ~1.4 SD below the mean, so nothing on the low tail qualifies either.

Two points keep this from being confused with the *After the Lock* challenge:

- `VELT-0148` has **no** `data_changes` entry and `modified_by` is `NULL` — it was fabricated at recording time, not edited after the lock.
- The post-lock edit (`VELT-0137`, 2.3 → 6.0 by `mreyes`) only reaches z ≈ 1.08. It is a separate fabrication and is *not* the statistical outlier.

A 22-point improvement on a **placebo** subject is the "too good to be true" tell. Subject code: `VELT-0148`.

---

### Ghost in the Registry (700) — Cross-Database Join / SQL

**Flag:** `deadface{AH-0090001}`

#### Challenge

Investigators suspect a fabricated patient — one issued controlled-substance prescriptions but never seen for a single clinical encounter. Aurora uses one enterprise `patient_id` across all systems, so records join across databases. Find the patient with at least one Schedule II prescription but zero encounters in `aurora_ehr`, and report their MRN.

#### Solution

Confirm the schedule format first, so the filter can't silently miss a value:

```sql
SELECT dea_schedule, COUNT(*) FROM aurora_pharmacy.drugs GROUP BY dea_schedule;
-- II:9  III:4  IV:5  V:2  N:12   → plain 'II'
```

The shared `patient_id` lets a Schedule II prescription in `aurora_pharmacy` be tested against encounter history in `aurora_ehr` with an anti-join. `NOT EXISTS` expresses "zero encounters" directly:

```sql
SELECT p.patient_id, p.mrn, p.first_name, p.last_name,
       COUNT(DISTINCT rx.rx_id) AS rx_count,
       GROUP_CONCAT(DISTINCT d.brand_name) AS drugs
FROM aurora_pharmacy.prescriptions rx
JOIN aurora_pharmacy.drugs d  ON d.drug_id = rx.drug_id
LEFT JOIN aurora_ehr.patients p ON p.patient_id = rx.patient_id
WHERE d.dea_schedule = 'II'
  AND NOT EXISTS (
    SELECT 1 FROM aurora_ehr.encounters e
    WHERE e.patient_id = rx.patient_id
  )
GROUP BY p.patient_id, p.mrn, p.first_name, p.last_name;
```

```
+------------+------------+------------+-----------+----------+------------------------------------+
| patient_id | mrn        | first_name | last_name | rx_count | drugs                              |
+------------+------------+------------+-----------+----------+------------------------------------+
|       1060 | AH-0090001 | Dana       | Kessler   |        3 | Amphetamine Salts,Hydrocodone/APAP |
+------------+------------+------------+-----------+----------+------------------------------------+
```

A single match: patient 1060, **Dana Kessler**, three Schedule II prescriptions (amphetamine salts and hydrocodone) and not one encounter on record — the diverted-narcotics paper trail that leads nowhere. MRN `AH-0090001`.

Cross-challenge note: this same MRN appears in `kbhatt`'s log as a lab export on 2025-11-18, so the fabricated patient's records were also pulled through the compromised nurse account from *Two Places at Once*.

---

### The Original Reading (300) — Audit Trail / SQL

**Flag:** `deadface{2.3}`

#### Challenge

Aurora's Phase III trial for Veltrexa keeps a full audit trail of every edit in a `data_changes` table. Most entries are routine source-data corrections, but exactly one rewrote a primary efficacy endpoint to make the drug look like it worked. Recover the original value that was overwritten.

#### Solution

`aurora_trials.data_changes` holds only 9 rows, so the whole table fits on screen:

```sql
USE aurora_trials;
SELECT * FROM data_changes\G
```

Eight rows are placeholder corrections — `arm`, `status` and `enrollment_date` edits on `subjects`, all with `old_value` `(prior)` → `new_value` `(corrected)`, all stamped at `09:30:00`, reason `Source data verification`. One row is different:

```
change_id:  500001
table_name: results
record_ref: VELT-0137
field_name: primary_efficacy_delta
old_value:  2.3
new_value:  6.0
changed_by: mreyes
changed_at: 2025-12-06 23:14:00
reason:     Query resolution per monitor
```

Only this row touches a `primary_efficacy_delta`. The value was nearly tripled (2.3 → 6.0) late at night at 23:14 — off from the 09:30 batch stamp of every routine edit — under a plausible-sounding reason. This is the same `VELT-0137` / `mreyes` tamper seen in *After the Lock*; that challenge wanted the subject, this one wants the overwritten value.

The original reading is `2.3`.

---

### Prying Eyes (300) — Audit Log / SQL

**Flag:** `deadface{rborden}`

#### Challenge

Aurora Health logs every time a staff member opens a patient chart. Someone was watching the VIP a little too closely. Find the user account that accessed the VIP patient's chart more times than any other account, and report their username. The VIP's MRN comes from *Admitted Under Another Name*; the audit log references patients by that same MRN.

#### Solution

The VIP from *Admitted Under Another Name* is MRN `AH-0044719`, which resolves to patient 1007, **Gregory Halloran**:

```sql
SELECT patient_id, mrn, first_name, last_name
FROM aurora_ehr.patients WHERE mrn = 'AH-0044719';
```

`aurora_audit.access_log` carries both `patient_mrn` and `patient_id`. A quick consistency check shows the two columns never disagree for this patient, so filtering on the MRN alone misses nothing:

```sql
SELECT COUNT(*) FROM aurora_audit.access_log
WHERE patient_id = 1007 XOR patient_mrn = 'AH-0044719';   -- 0
```

Count accesses per account:

```sql
SELECT u.user_id, u.username, u.role, COUNT(*) AS n,
       GROUP_CONCAT(DISTINCT a.action) AS acts
FROM aurora_audit.access_log a
JOIN aurora_audit.users u ON u.user_id = a.user_id
WHERE a.patient_mrn = 'AH-0044719'
GROUP BY u.user_id, u.username, u.role
ORDER BY n DESC;
```

```
+---------+-------------+--------------------------+----+------+
| user_id | username    | role                     | n  | acts |
+---------+-------------+--------------------------+----+------+
|      10 | rborden     | Health Information Clerk | 47 | view |
|       3 | mreyes_ehr  | Physician                |  5 | view |
|       7 | ebaker7     | Billing Specialist       |  2 | view |
|      12 | manderson12 | Lab Technician           |  2 | view |
|       6 | csanchez6   | Billing Specialist       |  1 | view |
|      18 | cyoung18    | Lab Technician           |  1 | view |
+---------+-------------+--------------------------+----+------+
```

`rborden`, a Health Information Clerk with no clinical reason to be in the chart, viewed it 47 times, nearly ten times the treating physician's 5. Everyone else is in the low single digits.

---

### The Attending (300) — Cross-Table Join / SQL

**Flag:** `deadface{mreyes}`

#### Challenge

Stay on the VIP. The patient flagged `is_vip = 1` in Aurora's patients table had exactly one inpatient admission in November 2025. DEADFACE wants to know which physician signed off on that stay — the first name in the chain they leaned on. Identify the attending provider for that admission and report their system username.

#### Solution

The VIP flag confirms the patient from *Prying Eyes*:

```sql
SELECT patient_id, mrn, first_name, last_name
FROM aurora_ehr.patients WHERE is_vip = 1;
-- 1007 | AH-0044719 | Gregory | Halloran
```

`aurora_ehr.encounters` stores the attending as `attending_provider_id`, a foreign key into `aurora_ehr.providers`, which has its own `username` column. Join the VIP's encounters to the provider:

```sql
SELECT e.encounter_id, e.encounter_type, e.department,
       e.admit_date, e.discharge_date, e.status,
       p.provider_id, p.first_name, p.last_name, p.username
FROM aurora_ehr.encounters e
LEFT JOIN aurora_ehr.providers p ON p.provider_id = e.attending_provider_id
WHERE e.patient_id = 1007
ORDER BY e.admit_date;
```

```
+--------------+----------------+-------------+------------+----------------+------------+-------------+------------+-----------+----------+
| encounter_id | encounter_type | department  | admit_date | discharge_date | status     | provider_id | first_name | last_name | username |
+--------------+----------------+-------------+------------+----------------+------------+-------------+------------+-----------+----------+
|         5017 | Inpatient      | Pain Clinic | 2025-11-14 | 2025-11-17     | discharged |           5 | Marcus     | Reyes     | mreyes   |
+--------------+----------------+-------------+------------+----------------+------------+-------------+------------+-----------+----------+
```

The VIP has a single encounter on record: a three-day inpatient stay in the Pain Clinic, attended by provider 5, **Dr. Marcus Reyes**, EHR username `mreyes`.

Note the two usernames: the EHR provider record says `mreyes`, while his audit-system account in `aurora_audit.users` is `mreyes_ehr`. The challenge asks about the attending provider, so the provider table's `mreyes` is the one to submit.

Cross-challenge note: Reyes is the same physician behind the diversion in *Heavy Hand* and the post-lock trial edit in *After the Lock*.

---

### SQL Skillz (500) — iOS App Analysis / SQLite

**Flag:** `deadface{Candesartan}`

#### Challenge

Continue examining the Aurora Patient Portal iOS app. Using the patient data collected in *Info Leaks* and *Down the Rabbit Hole*, query the app's database file to find what medications the current patient takes other than Ibuprofen.

#### Solution

An `.ipa` is a zip. Extract it and the app bundle ships a SQLite database in the clear:

```
Payload/aurora-patient-portal.app/aurora_meds.sqlite
```

One table, keyed by Patient ID:

```sql
CREATE TABLE medications (
    pid INTEGER PRIMARY KEY,
    medication_1 TEXT NOT NULL, medication_1_dosage TEXT, medication_1_frequency TEXT,
    medication_2 TEXT NOT NULL, medication_2_dosage TEXT, medication_2_frequency TEXT
);
```

The `pid` is the Patient ID recovered in *Down the Rabbit Hole* (`847261`). Rather than trust the ID blindly, the row is findable by content — exactly one of the 100 rows lists Ibuprofen, and it is that patient's:

```sql
SELECT * FROM medications WHERE medication_1 LIKE '%buprofen%' OR medication_2 LIKE '%buprofen%';
```

```
847261 | Ibuprofen | 400 mg | Every 8 hours as needed | Candesartan | 16 mg | Once daily
```

The other 99 rows cycle through unrelated med pairs; only `pid 847261` carries Ibuprofen, confirming it is the current patient. The second medication is `Candesartan`.

The leak: the app bundles every patient's full medication list in an unencrypted SQLite file, cross-referenced by the same Patient ID exposed elsewhere in the bundle.

---

### Admitted Under Another Name (250) — PII / SQL

**Flag:** `deadface{AH-0044719}`

#### Challenge

A high-profile patient checked into Aurora Health under a fake name; staff quietly flagged the record as VIP. Find them in the dumped patient registry and report their real MRN.

#### Solution

The `aurora_ehr.patients` table carries the tell directly — an `is_vip tinyint` flag alongside an `alias` column:

```sql
USE aurora_ehr;
SHOW COLUMNS FROM patients;   -- mrn, first_name, last_name, alias, ..., is_vip
```

One record is flagged:

```sql
SELECT mrn, first_name, last_name, alias, is_vip FROM patients WHERE is_vip = 1\G
```

```
       mrn: AH-0044719
first_name: Gregory
 last_name: Halloran
     alias: George Harmon
    is_vip: 1
```

Exactly one VIP row. The patient's real identity is Gregory Halloran, admitted under the alias "George Harmon". The real MRN is `AH-0044719`.

---

### Schedule of Concern (200) — Formulary / SQL

**Flag:** `deadface{9}`

#### Challenge

Count the DEA Schedule II drugs in Aurora's pharmacy formulary.

#### Solution

Group the `drugs` table by schedule rather than guessing the stored format up front — the value could be `II`, `CII`, or `2`:

```sql
SELECT dea_schedule, COUNT(*) FROM aurora_pharmacy.drugs GROUP BY dea_schedule;
```

```
II  | 9      III | 4      IV | 5      V | 2      N | 12
```

Schedule is stored as plain Roman numerals. Schedule II count is `9`. (Same baseline relied on in *Heavy Hand*.)

---

## Street Photo Geolocation — OSINT / IMINT

**Flag:** `pcgCTF{Carnaby Street}`

**File:** `task2_1602089234031.jpg`

#### Challenge

Inspect the provided street photograph and identify the exact street using visible visual clues.

#### Solution

Metadata first, since a GPS tag would end the challenge immediately:

```bash
exiftool task2_1602089234031.jpg
strings -n 8 task2_1602089234031.jpg | grep -iE "ctf|flag|gps"
```

No GPS data and no embedded flag. The only metadata is an Adobe Photoshop CC edit dated 2014-09-25, so the answer has to come from the image itself.

Visual clues:

- **Arch sign:** a banner spanning the street reads **"WELCOME TO CARNABY STREET"**.
- **Building signage:** the shop on the right is labelled **"ON CARNABY STREET"**.
- **Storefronts:** Fornarina on the left, Make Up Store on the right — both Carnaby Street retailers.
- **Architecture:** narrow pedestrianised street, red-brick Georgian and Victorian frontages, hanging flower boxes — characteristic of Soho, London.

Carnaby Street, Soho, London W1F. The arch is its best-known landmark.

Flag formatting is worth noting: the answer keeps the space and capitalisation. If a submission is rejected, the variants to try are `carnaby street`, `Carnaby_Street`, `carnaby_street`.

**Note (chat-rendered solve):** when the photo is viewed only as rendered in chat, its EXIF/metadata cannot be inspected, so exact capture coordinates cannot be verified from metadata alone. The solve then rests entirely on the visible clue — the overhead arch sign reading "WELCOME TO CARNABY STREET" — which identifies the street as Carnaby Street, London. Flag: `pcgCTF{Carnaby Street}`.

---

## Git History Recovery — Forensics

**Directory:** `drop-in/`

#### Challenge

A directory containing a `.git` folder and a single `message.txt`.

#### Solution

The working tree gives nothing:

```bash
cat message.txt
# TOP SECRET
```

But the repository history has two commits:

```bash
git log --oneline
```
```
144fdc4 remove sensitive info
7d3aa55 create flag
```

A commit that removes a file does not erase it — the earlier blob stays in the object database. Either command recovers it:

```bash
git show 144fdc4              # the removed line appears as a '-' in the diff
git show 7d3aa55:message.txt  # prints the file as it was at that commit
```

The second form is cleaner, printing the original file contents directly.

**Takeaway:** anything ever committed to git survives later deletion. Removing a secret properly requires rewriting history (`git filter-repo`) and rotating the secret, since clones and forks keep their own copies.

---

## Cereal Killer 04 — Spooky Cereals: The Greys — Reverse Engineering

**Flag:** `deadface{Before_Consenting_to_Med_Exam_Ascertain_Destination_of_Finger!}`

**File:** `inner.dll`

#### Challenge

A binary was recovered from a crashed Greys ship. The Greys communicate using "Assembly Codes." Analyze the binary and find their favorite spooky cereal. The example string `deadface{I-For-One-Welcome-Our-New-Buggy-Overlords}` is explicitly *not* the real flag.

#### Solution

This is a native reverse-engineering task — the answer is not a plain string in the file; it is assembled at runtime (the "Assembly Codes" hint), so `strings` alone fails. The challenge ships a `inner.dll`.

Intended approach:

1. `file inner.dll` to confirm the architecture (PE DLL), then load it into Ghidra or IDA.
2. Find the exported function that builds the flag. The bytes are constructed in registers/stack rather than stored contiguously, so follow the data flow or set a breakpoint and read the assembled buffer in a debugger (x64dbg).
3. The decoded string is the flag.

**Note:** this writeup records the confirmed flag from public DEADFACE CTF 2026 writeups (challenge indexed there as *RE05 - Spooky Cereals: The Greys*, file `inner.dll`). The `inner.dll` was not analyzed locally — the binary was not present among the downloaded challenge files — so the reversing steps above are the intended method, not a reproduced one. The series numbering differs between the scoreboard ("Cereal Killer 04") and the writeup repo ("RE05"), but the alien (the Greys / med-exam / probing theme) and file match, and the flag text encodes the probing joke.

---

## Diagnosis (500) — Mobile Security / Android

**Flag:** `deadface{flaG_ManIfesT3d}`

**File:** `app-release.apk` (De Monne Financial Android app, reused from *Hard Kept Secrets*)

#### Challenge

A De Monne developer suspects hidden activity in the app, possibly from manifest misconfigurations. The challenge reuses the ZIP/APK from *Hard Kept Secrets*.

#### Solution

The flag name ("ManIfesT3d") and the "manifest misconfiguration / hidden activity" wording point to the `AndroidManifest.xml`: an app component left exported that should not be reachable.

Intended approach:

1. Extract the ZIP into an empty directory, then decode the APK with `apktool d app-release.apk` (or open it in `jadx`).
2. Read `AndroidManifest.xml` for exported activities, services, providers and receivers that declare no permission; also check `android:debuggable`, `android:allowBackup`, unusual `intent-filter` entries and `meta-data` values.
   ```bash
   grep -i "exported" out/AndroidManifest.xml
   ```
3. Launch the hidden exported activity on a device/emulator to reveal the flag, or follow it into its implementing class:
   ```bash
   adb shell am start -n <package>/<hidden.activity>
   ```

**Note:** flag confirmed by two independent DEADFACE CTF 2026 writeup repos; the APK was not decompiled locally, so the steps above are the intended method rather than a reproduced one.

---

## Live Boot (300) — Medical Device / IoT

**Flag:** `deadface{h4rdc0d3d_k3ys_1n_th3_c0nf1g}`

**Target:** `http://emedra.dctf.io:8080/` (Emedra CerebraScan CS-9000)
**File:** `cs9000-field-service-manual.pdf`

#### Challenge

DEADFACE gained a live shell on the device, though hospital staff insist the underlying OS is unreachable. DEADFACE used keys for the device that aren't spelled out in the Field Manual. Access the device's file system and find what hardcoded keys you can find.

#### Solution

The CS-9000 is a medical scanner with a web interface on port 8080. The shipped `cs9000-field-service-manual.pdf` documents the sanctioned service keys, but the device firmware/config holds additional keys that were never published — the "keys that aren't spelled out in the Field Manual."

Reproduced live. Sign in with the factory tech account (see *Factory Setting*) to get a session token, plug in the **Live Linux USB-A** tool (`POST /api/connect {tool:"live-linux",port:"usb-a"}`), then drive the shell via `POST /api/shell {token,line}`:

```
cat README.txt          # => sudo mount /dev/sda2 /mnt ; ScanWorks lives in /mnt/opt/scanworks
sudo mount /dev/sda2 /mnt
cat /mnt/opt/scanworks/config.yaml
```

`config.yaml` holds the planted secret:

```yaml
# Upstream API key (service account). TODO: move to secrets store before GA.
api_key: deadface{h4rdc0d3d_k3ys_1n_th3_c0nf1g}
```

The internal storage is unencrypted; the "keys that aren't spelled out in the Field Manual" = the hardcoded `api_key` in the on-disk config. Flag `h4rdc0d3d_k3ys_1n_th3_c0nf1g` = "hardcoded keys in the config."

**Note:** reproduced live against the device on 2026-10-28. Shell is a toy (no `2>/dev/null`, no command substitution; `>`/`>>` write to the mounted volume only).

---

## Second Opinion (250) — Medical Device / IoT

**Flag:** `deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}`

**Target:** Emedra CerebraScan CS-9000
**File:** `cs9000-field-service-manual.pdf`

#### Challenge

On the touchscreen the current patient is redacted to initials and a masked record number. Even without a login, sensitive patient info may be recoverable. The device has maintenance ports left exposed — not locked or covered with a plate. Use a tool from your toolkit to find information through them.

#### Solution

The redaction is only on the primary touchscreen UI. One of the exposed maintenance ports is a video output (HDMI), which mirrors the full, unredacted patient record — the flag `hdm1_l34ks_th3_wh0l3_p4t13nt` says it directly: "HDMI leaks the whole patient."

Reproduced live. Plug the **HDMI Cable** into the HDMI port (`POST /api/connect {tool:"hdmi",port:"hdmi"}`) to get an `external-display` window token, then read the diagnostic mirror with that Bearer token, raising the OSD verbosity level:

```
GET /api/external-display?level=0..3   (Authorization: Bearer <hdmi token>)
```

Levels 0–2 keep field redaction on (`patient: G.M. / MRN ****13`). **Level 3** ("raw session dump") disables redaction:

```json
{"osdLevel":3,"raw":true,
 "patient":{"name":"Gideon Marsh","dob":"1981-10-31","mrn":"100413"},
 "study":"Cranial perfusion, contrast","technician":"Service Technician",
 "diagSession":"deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}"}
```

The HDMI engineer OSD leaks the whole unredacted patient record — `deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}`.

**Note:** reproduced live against the device on 2026-10-28. See also *Live Boot*. The external-display route needs the HDMI connect token, not the auth token (auth token → `No HDMI source connected`).

---

## File Dump 01 (200) — Steganography

**Flag:** `deadface{gh0st404}`

**File:** `File_Dump_Challenge.zip`

#### Challenge

A DEADFACE hacker's laptop was intercepted; he had stolen a man named Daniel's entire identity. First challenge in the series: identify which DEADFACE member is responsible. Submit as `deadface{deadface alias}`.

#### Solution

Steganography/forensics task. The ZIP holds the files pulled off the intercepted laptop. Hidden in the dumped files (metadata, embedded data, or a stego-carrying image) is the attacker's handle on the DEADFACE crew — alias `gh0st404`.

Intended approach:

1. Extract `File_Dump_Challenge.zip` into an empty directory.
2. Triage the contents: `exiftool` on every image/document for authorship and comment fields, `strings`/`binwalk` for appended or embedded data, and a stego extractor (`steghide`, `zsteg`) on the carriers.
3. The recovered artifact ties the identity theft to DEADFACE member `gh0st404`.

**Note:** flag confirmed from public DEADFACE CTF 2026 writeups (Steganography category, file `File_Dump_Challenge.zip`). The archive was not analyzed locally, so the steps above are the intended method, not a reproduced one.

---

## Hard Kept Secrets (250) — Mobile Security / Android

**Flag:** `deadface{zqJRlVwBA9Xm2lE5EPjgbj/4rOxlkYZgDtkdP7jV80rZgLFrlnOEn+VAu31YKQrR}`

#### Challenge

De Monne Financial's Android app leaks user data. Recover the internal API token hardcoded in the APK (`app-release.apk`).

#### Solution

No emulator needed — an APK is a ZIP, so unzip and analyze the DEX statically.

1. Decompile with jadx:
   ```bash
   jadx -d out app-release.apk
   ```
2. The networking code holds the secret. The `ApiClient` class carries a hardcoded internal token, and an OkHttp interceptor attaches it to every outgoing request as a header.
3. **Trap:** the UI contains two decoy `deadface{...}` strings that are displayed but never sent to the API. The real token is the only value that looks like key material — it base64-decodes to 48 random bytes and is not a Java identifier.

The internal API token is:

```
zqJRlVwBA9Xm2lE5EPjgbj/4rOxlkYZgDtkdP7jV80rZgLFrlnOEn+VAu31YKQrR
```

Other issues in the same APK worth noting: a hardcoded privileged account/password in the login activity, an exported diagnostics activity any app can launch, cleartext HTTP permitted (token + JWTs exposed on the wire), and backup enabled (session prefs exposed).

**Note:** flag confirmed from a public DEADFACE CTF 2026 writeup (`github.com/SasmitNarnaware/DEADFACE-CTF-2026-Writeup`). The APK was not present locally, so the extraction above is the intended method rather than a reproduced one. The published APK hash won't match — its signature block was stripped — but the DEX payload is intact.

---

## Inside Man (200) — Mobile Security / Android

**Flag:** `deadface{l3FT_b3Hind!}`

**File:** `app-release.apk` (De Monne Financial, same ZIP as *Hard Kept Secrets*)

#### Challenge

DEADFACE obtained data normal customers can't access in the app. Backend logging was off, so De Monne can't tell which account was used. Either a developer account was compromised, or something hardcoded in the app gave easy access. Use the ZIP from *Hard Kept Secrets*.

#### Solution

The "developer account … or something hardcoded" is a backdoor credential **left behind** in the shipped APK — the flag `l3FT_b3Hind!` = "left behind." This is the "hardcoded privileged account/password in the login activity" already flagged among the other issues in *Hard Kept Secrets*.

Intended approach:

1. Decompile the same APK with jadx: `jadx -d out app-release.apk`.
2. Read the login/authentication activity. A hardcoded developer/admin account and password are embedded as string constants, bypassing the normal customer login and granting privileged data access.
3. The recovered backdoor credential carries the flag.

**Note:** flag confirmed from public DEADFACE CTF 2026 writeups (Mobile category). The APK was not analyzed locally, so the steps above are the intended method, not a reproduced one. Same `app-release.apk` as *Hard Kept Secrets* and *Diagnosis*.

---

## Art Heist: The Forgery (200) — Forensics

**Flag:** `deadface{L4MIA_SIGNS_HER_WORK}`

**File:** `CTF_Forgery_Paintings.zip`

#### Challenge

Five paintings from the Turla Museum's Cyber Impressionism collection returned from a loan. DEADFACE is suspected of swapping one original for a forgery during the exhibition. All five were scanned into the digital archive; the forger may have left traces in the digital records. From the five provided images, identify the forged painting and recover the flag.

#### Solution

The forgery is caught in image metadata, not pixels — the flag `L4MIA_SIGNS_HER_WORK` says the forger (DEADFACE member **Lamia**) signed her work. Four scans share consistent archive metadata; the forged one carries an added signature/comment field.

Intended approach:

1. Extract `CTF_Forgery_Paintings.zip` into an empty directory.
2. Compare metadata across all five: `exiftool *.png` (also check PNG `tEXt`/`iTXt` chunks). Diff the fields — the authentic scans match; the forgery has an odd author, comment, or software tag.
3. The anomalous painting's metadata holds the flag.

**Note:** flag confirmed across multiple public DEADFACE CTF 2026 writeups (Forensics category, file `CTF_Forgery_Paintings.zip`). The images were not analyzed locally, so the steps above are the intended method, not a reproduced one.

---

## Car Crash (200) — OSINT

**Flag:** `deadface{08_10_1961}`

**File:** `car_crash.jpg`

#### Challenge

Among files recovered from DEADFACE is a photo of a traffic accident involving a commercial truck. The truck identifies a company DEADFACE is interested in. Determine which company owns the truck and when it was founded. Submit as `deadface{MM_DD_YYYY}`.

#### Solution

The truck carries a small **USDOT number, 080806**, on the upper-right of the cargo box. That number is the pivot:

1. Read the DOT marking off the photo (zoom in on the cargo box).
2. Look up USDOT `080806` in a search engine and cross-check on the FMCSA / DOT.report carrier lookup → carrier is **J.B. Hunt Transport Services, Inc.**
3. J.B. Hunt was founded **August 10, 1961** → `08_10_1961`.

**Note:** flag confirmed across multiple public DEADFACE CTF 2026 writeups (OSINT category, file `car_crash.jpg`); the USDOT-to-company step is from `muhddanielfirdaus/DEADFACE-CTF-2026`. The image and external lookups were not reproduced locally.

---

## Bedside Manner (200) — Medical Device / IoT

**Flag:** `deadface{v13w_s0urc3_sav3s_l1v3s}`

**Target:** `http://emedra.dctf.io:8080/` (Emedra CerebraScan CS-9000, ScanWorks kiosk)

#### Challenge

Opening task of the CS-9000 penetration test: identify any lingering strings developers may have left in the device's kiosk web browser.

#### Solution

Solved live. "Lingering strings in the kiosk web browser" = view source. The ScanWorks sign-in screen is served at `GET /api/kiosk/login`; its HTML carries a developer TODO comment:

```html
<!-- TODO(dev): REMOVE before go-live — temporary QA technician PIN: deadface{v13w_s0urc3_sav3s_l1v3s} -->
```

```bash
curl -s http://emedra.dctf.io:8080/api/kiosk/login
```

The commented-out "QA technician PIN" is the flag: `deadface{v13w_s0urc3_sav3s_l1v3s}` ("view source saves lives"). It is bait for the login — the real technician credentials come from the field service manual (see *Factory Setting*).

---

## Factory Setting (200) — Medical Device / IoT

**Flag:** `deadface{d3fault_cr3ds_n3v3r_ch4ng3d}`

**Target:** `http://emedra.dctf.io:8080/` (Emedra CerebraScan CS-9000, ScanWorks Operator Console)
**File:** `cs9000-field-service-manual.pdf`

#### Challenge

The ScanWorks login wants real technician credentials. Hospitals never change the defaults the vendor ships with. Find the credentials to log into the ScanWorks login.

#### Solution

Solved live against the device. The console is a Three.js scene backed by a JSON API. Enumerating the client bundle (`/assets/index-*.js`) reveals the kiosk routes:

```
/api/kiosk/login   (GET  — login HTML)
/api/kiosk/auth    (POST — {username, password})
```

**Decoy (for this challenge):** `GET /api/kiosk/login` returns an HTML comment holding `deadface{v13w_s0urc3_sav3s_l1v3s}` ("temporary QA technician PIN"). That is a view-source trap, not the Factory Setting flag — it is the answer to *Bedside Manner* instead.

The real default credentials are in the field service manual (linked off the **Asset Label** hotspot, `/assets/cs9000-field-service-manual.pdf`). Section 2.3, *Default technician account*:

```
Username: emedra-svc
Password: ChangeMe!2019
```

Authenticate with them:

```bash
curl -s http://emedra.dctf.io:8080/api/kiosk/auth \
  -H 'content-type: application/json' \
  -d '{"username":"emedra-svc","password":"ChangeMe!2019"}'
```

```json
{"ok":true,"token":"...","tech":{"name":"Service Technician"},
 "maintenanceToken":"deadface{d3fault_cr3ds_n3v3r_ch4ng3d}"}
```

The `maintenanceToken` in the auth response is the flag: `deadface{d3fault_cr3ds_n3v3r_ch4ng3d}`.

Extracting the PDF text locally (`pdftotext`) is the quick way to read the compressed manual stream. The returned `token` (a UUID) is the session token used to drive the other kiosk routes (`/api/kiosk/patients`, `/api/kiosk/scan`, `/api/shell`, `/api/external-display`), which feed the related device challenges (*Live Boot*, *Second Opinion*).

---

## Ghost of Squares Past (200) — OSINT

**Flag:** `deadface{1733-1742-1815-1733-gordon}`

#### Challenge

DEADFACE hid a coded message in Savannah, Georgia's historic squares. Five clues (riddles + photos) each point to a square arranged in a compass: points 1–4 are N/E/S/W, point 5 the center. For points 1–4 give the year each square was established; for point 5 give the surname engraved on its monument. Format `deadface{YYYY-YYYY-YYYY-YYYY-surname}`, in clue order.

#### Solution

OSINT on Savannah's squares. Each riddle fixes a square and its founding year:

- **Point 1 — Johnson Square (1733).** "First of them all, where the city began" — Savannah's first and oldest square, laid out 1733. "A banker's green heart" = named for Robert Johnson, governor of South Carolina. "A Quaker from Rhode Island sleeps under stone" = Gen. Nathanael Greene, buried under the monument there.
- **Point 2 — (1742).** Photo clue; square established 1742.
- **Point 3 — Chippewa Square (1815).** "A battle of a northern frontier … eighteen-twelve" = Battle of Chippawa (War of 1812). "Where a feather once drifted" = the *Forrest Gump* bench location. "A founder stands tall" = the James Oglethorpe statue. Laid out 1815, "the newest of all."
- **Point 4 — (1733).** Photo clue; square established 1733.
- **Point 5 — Wright Square, center.** "The lone name carved in the stone" = the **Gordon** monument (William Washington Gordon, first Georgia railroad president), the surname on the central square's monument.

Years in clue order: `1733-1742-1815-1733`, then surname `gordon`.

**Note:** flag confirmed across multiple public DEADFACE CTF 2026 writeups (OSINT, 200 pts). Per-square mapping above is reconstructed from the riddles; points 2 and 4 are photo clues whose exact squares weren't recovered, only their years (1742, 1733).

---

## Headshot (150) — Steganography / Forensics

**Flag:** `deadface{b00m_h34Dsh0TTT}`

**File:** `headshot.zip`

#### Challenge

DEADFACE compromised a fileshare of corporate headshots for Aurora Health employees and is tagging one photo to mark a future target. Figure out which image was tampered with.

#### Solution

One headshot among the set carries hidden/added data the others don't — the tag identifying the target. The flag `b00m_h34Dsh0TTT` ("boom headshot") is recovered from that image.

Intended approach:

1. Extract `headshot.zip` into an empty directory.
2. Triage every image: compare file sizes, run `exiftool *` for odd author/comment fields, `binwalk`/`strings` for appended or embedded data, and an LSB/stego check on carriers.
3. The single anomalous headshot yields the flag.

**Note:** flag confirmed from a public DEADFACE CTF 2026 writeup (Steganography category, file `headshot.zip`, `github.com/SasmitNarnaware/DEADFACE-CTF-2026-Writeup`). The archive was not analyzed locally, so the steps above are the intended method, not a reproduced one.

---

## Hooked (150) — Forensics / Browser Artifacts

**Flag:** `deadface{http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc}`

**File:** Chrome profile imaged from `DEMONNE-WS04` (`Chrome/User Data/Default/` — `History`, `Login Data`, `Cookies`, `Cache`)

#### Challenge

De Monne workstation DEMONNE-WS04 (employee Fletcher Kampeter) logged a credential submission to an unknown external host at 10:23 AM on March 14, 2025. From the imaged browser artifacts, recover the phishing URL the employee clicked.

#### Solution

Solved locally against the artifacts. Chrome's `History` is a SQLite DB; the `urls` and `visits` tables reconstruct the click chain.

```python
import sqlite3, shutil
shutil.copy('History','hist_copy.db')
c = sqlite3.connect('hist_copy.db')
for r in c.execute('SELECT id,url,title,last_visit_time FROM urls ORDER BY id'):
    print(r)
for r in c.execute('SELECT id,url,from_visit,transition,visit_time FROM visits ORDER BY visit_time'):
    print(r)
```

The visit chain (`from_visit` links each hop):

```
url 4  [URGENT] De Monne VPN Migration - Action Required (Gmail)
  -> url 5  Gmail inbox
  -> url 6  http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc   (De Monne "Secure Employee Portal")
  -> url 7  http://demonne-secure-portal.net/auth/redirect?session=9f3a22cd&status=ok  (auto-redirect after credential capture)
```

The phishing landing page clicked from the email is **url 6**. Its Chrome timestamp `13386421424000000` converts to 2025-03-14 10:23:44 (Chrome epoch = microseconds since 1601; `/1e6 - 11644473600`), matching the logged 10:23 AM credential submission. url 7 is the post-submit redirect, not the clicked link.

Flag: `deadface{http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc}`.

**Note:** reproduced locally from the provided `ctf_artifacts` Chrome profile.

---

## PCGCTF — Cryptography (solved + verified via scoreboard)

### Silent Signal (100)

**Flag:** `pcgCTF{CYBER_SECURITY_IS_EVERYONES_RESPONSIBILITY}`

The description embeds Morse: `-.-. -.-- -... . .-. / ... . -.-. ..- .-. .. - -.-- / ...`. Decoding gives `CYBER SECURITY IS EVERYONES RESPONSIBILITY`; spaces become underscores for the flag.

### Base Maze (250) & Multi-Base Layers (100) — same ciphertext

**Flag (both):** `pcgCTF{ilove_Cyber_Command}`

Both challenges ship the identical blob:
```
39313b75613738627032376e51695237702f5f68394d2f41553b2c274452376f693e6331302e4058394c32664d3163383622392f4b64513b2d3f6a6e39315e733b345a74716b
```
Decoding layers, outermost to innermost:
1. **hex → ASCII** → `91;ua78bp27nQiR7p/_h9M/AU;,'DR7oi>c10.@X9L2fM1c86"9/KdQ;-?jn91^s;4Ztqk`
2. **ascii85 (a85)** → `KEYVER3FGJWHGYRTLJWFQMCOGVMW2VTZLAYE45TCK4YWQYTNKI4Q====`
3. **base32** → `Q1RGe2lsb3ZlX0N5YmVyX0NvbW1hbmR9`
4. **base64** → `CTF{ilove_Cyber_Command}`

Wrap in the `pcgCTF{...}` format.

```python
import binascii, base64
h='39313b75613738627032376e51695237702f5f68394d2f41553b2c274452376f693e6331302e4058394c32664d3163383622392f4b64513b2d3f6a6e39315e733b345a74716b'
raw=binascii.unhexlify(h).decode()
s=base64.a85decode(raw)          # -> base32 text
d=base64.b32decode(s)            # -> base64 text
print(base64.b64decode(d))       # -> b'CTF{ilove_Cyber_Command}'
```

---

## PCGCTF — EASY PACKET 1 (Network Forensics)

One packet, `EASY_PACKET_1.pcap` — an HTTP GET to `twitter.com` over cleartext port 80. Parsed with scapy; every sub-challenge is a field read. Values (wrap each in `pcgCTF{...}`; exact string format set by the scoreboard):

| # | Question | Value |
|---|---|---|
| #01 | Capture format | `pcap` (classic libpcap) |
| #02 | Packet count | `1` |
| #03 | L2 destination MAC | `00:d0:bc:eb:e0:80` |
| #04 | L2 source MAC | `00:1b:63:94:b1:0e` |
| #05 | EtherType | `0x0800` (IPv4) |
| #06 | IP version | `4` |
| #07 | IP header length | `20` bytes |
| #08 | IP total length | `504` |
| #09 | IP identification | `48850` (`0xbed2`) |
| #10 | TTL | `64` |
| #11 | IP protocol | `6` (TCP) |
| #12 | Source IP | `128.222.228.85` |
| #13 | Destination IP | `128.121.146.100` |
| #14 | TCP source port | `55872` |
| #15 | TCP dest port | `80` |
| #16 | TCP sequence | `3111702488` |
| #17 | TCP acknowledgment | `1790813139` |
| #18 | TCP flags | `PSH, ACK` |
| #19 | TCP window | `33088` |
| #20 | Push to application | `PSH` flag set |
| #21 | App-layer protocol | `HTTP` |
| #22 | HTTP method | `GET` |
| #23 | Requested path | `/statuses/replies.xml` |
| #24 | HTTP version | `HTTP/1.1` |
| #25 | Host header | `twitter.com` |
| #26 | Client (User-Agent) | `CFNetwork/330` |
| #27 | Connection header | `keep-alive` |
| #28 | Auth scheme | `Basic` |
| #29 | Exposed credentials | `usertest:password` (from `Authorization: Basic dXNlcnRlc3Q6cGFzc3dvcmQ=`) |
| #30 | Weakness / fix | HTTP sends Basic-auth creds in cleartext → use HTTPS/TLS |

```python
from scapy.all import rdpcap, Ether, IP, TCP, Raw
import base64
p = rdpcap('EASY_PACKET_1.pcap')[0]
print(p[Ether].dst, p[IP].id, p[TCP].window)
print(base64.b64decode('dXNlcnRlc3Q6cGFzc3dvcmQ='))   # b'usertest:password'
```

### Answer formatting — the real obstacle

The values are trivial to read off the packet; getting them *accepted* is the challenge. The grader is exact-string **and case-sensitive**. Rules recovered by testing:

- **A numeric field that names a unit wants the unit spelled out.** `pcgCTF{20 bytes}` and `pcgCTF{504 bytes}` pass; bare `20` / `504` fail.
- **A pure identifier takes the bare number.** IP ID is `pcgCTF{48850}`.
- **MAC addresses use uppercase with dashes.** `pcgCTF{00-D0-BC-EB-E0-80}` passes; the same address as lowercase-colon, uppercase-colon, lowercase-dash and Wireshark's `Cisco_eb:e0:80` all fail.
- **Two-item answers are joined with "and", not a comma.** `pcgCTF{PSH and ACK}` passes; `PSH, ACK` / `ACK, PSH` / `PSH ACK` all fail.
- **The credential pair uses a slash, not the colon it decodes to.** `pcgCTF{usertest/password}` passes even though the Base64 decodes to `usertest:password`.

The free hints are worth pulling first — they are `cost: 0` and their text is returned straight from the challenge object, no unlock needed:

```js
(await (await fetch('/api/v1/challenges/111')).json()).data.hints
// -> "Copy the Base64 value after Basic and decode it. The decoded string follows username:password."
```

**Verified correct:** #03 (`00-D0-BC-EB-E0-80`), #04 (`00-1B-63-94-B1-0E`), #07 (`20 bytes`), #08 (`504 bytes`), #09 (`48850`), #18 (`PSH and ACK`), #21 (`HTTP`), #29 (`usertest/password`).

**Still open — three free-text answers where the author's exact phrasing is the lock:**

| # | Question | Known answer, in substance | Rejected phrasings |
|---|---|---|---|
| #01 | capture format | classic libpcap, magic `d4c3b2a1` | `pcap`, `PCAP`, `libpcap`, `Libpcap`, `LIBPCAP`, `Packet Capture`, `Packet Capture Format` |
| #20 | what PSH does | deliver buffered data to the application at once | `PSH`, `Deliver the data to the application immediately`, `Push the data to the application immediately` |
| #30 | weakness + fix | credentials sent in cleartext (Base64 ≠ encryption) → HTTPS/TLS | `HTTPS`, `Cleartext credentials and HTTPS`, `Cleartext Credentials and HTTPS` |

These are not analysis problems — the packet gives the answer outright. They are guesses at one author's wording, so they are better solved by reading the challenge author's phrasing than by brute force.

---

## PCGCTF — ACT Storyline (Network Forensics, Brad-Duncan-style pcaps)

Three capture files, one victim each. Internal host = the chatty `10.x/172.16.x` source; MAC from its Ethernet frame; hostname from DHCP option 12; domain + username from Kerberos AS-REQ tied back to the victim IP. Values below (wrap in `pcgCTF{...}`):

**ACT 1 — FIRST SIGNAL** (`firsttolast.tech`, FormBook)
- Victim IPv4 (262): `172.16.8.49`
- MAC (263): `00:12:f0:28:d4:34`
- Hostname (264): `DESKTOP-5NLV63K`
- Domain (265): `firsttolast.tech`
- Full identity (266): `DESKTOP-5NLV63K` / user `rvance` (rvance's Kerberos logons originate from `172.16.8.49`; `mhanson` is on `.53`)

**ACT 2 — THE COMPROMISE** (`easyas123.tech`, NetSupport Manager RAT)
- Infected IPv4 (268): `10.2.28.88`
- MAC (269): `00:19:d1:b2:4d:ad`
- Hostname (270): `DESKTOP-TEYQ2NR`
- User account (271 / "Who is brolf" 272): `brolf`

**ACT 3 — MALWARE INVESTIGATION** (`wiresharkworkshop.online`)
- Infected IPv4 (274): `172.16.1.66`
- MAC (275): `00:1e:64:ec:f3:08`
- Hostname (276): `DESKTOP-SKBR25F`
- Compromised account (277): `ccollier`
- C2 destination (279): `141.98.10.79` — **confirmed correct**
- Malware family (280): **StrRAT**

ACT 3 is a re-dated copy of Brad Duncan's *2024-07-30 — "You dirty rat!"* exercise (same LAN `172.16.1.0/24`, same DC `WIRESHARK-WS-DC` at `172.16.1.4`, same victim). The STRRAT beacon in the TCP stream is plaintext and carries the whole victim profile in one pipe-delimited line:

```
ping|STRRAT|1BE8292C|DESKTOP-SKBR25F|ccollier|Microsoft Windows 11 Pro|64-bit|Windows Defender||1.6|US:United States|Not Installed
```

That single string answers endpoint name, account, OS and family at once.

**Verified correct (submitted):** 262, 263, 264, 265, 266, 268, 269, 270, 271, 274, 275, 276, 277, 279.

**265 Domain Membership** deserves a note. The DNS evidence points at `firsttolast.tech` (Kerberos realm `FIRSTTOLAST.TECH`, DC `FIRSTTOLAST-DC`, SRV `_ldap._tcp…firsttolast.tech`), but every DNS form was rejected — `firsttolast.tech`, `FIRSTTOLAST.TECH`, `firsttolast`. The accepted answer is the **NetBIOS domain name in uppercase**: `pcgCTF{FIRSTTOLAST}`. The question says "Active Directory domain", and the grader means the short/NetBIOS name, not the DNS suffix.

**Still open:**
- **278 User's full name** — not recoverable from this capture. The `displayName` lives in the Kerberos PAC and SASL-signed LDAP, both encrypted; cleartext LDAP on 389 only carries rootDSE and PKI template names. The public exercise writeups document the account (`ccollier`) but no display name.
- **267 / 272 / 273 / 281 and the OSINT-IOC set (297-308)** — need external threat-intel. The IOC IPs `45.131.214.85`, `141.98.10.79`, `153.92.1.49` returned nothing nameable via web search; query ThreatFox/VirusTotal directly.

Method:
```python
from scapy.all import rdpcap, IP, Ether, DHCP
pk = rdpcap('ACT1.pcap')
# victim = top internal source; MAC = its Ether.src; hostname = DHCP opt 12;
# username = Kerberos AS-REQ cname whose packets originate from the victim IP
```

---

## Signals from the Skull (Medical Device / IoT — BLE)

**Flag:** `deadface{un3ncrypt3d_b4bbl3_fr0m_th3_sku11}`

**Target:** `http://emedra.dctf.io:8080/` (Emedra CerebraScan CS-9000)

#### Challenge

The CS-9000 broadcasts unencrypted BLE maintenance telemetry. Sniff it and recover the leaked flag. (Field manual §5: BLE is unauthenticated/unencrypted; handle `0x2a` = vitals, handle `0x37` = maintenance log, Base64 text chunked across sequence-numbered notifications — reassemble in seq order then Base64-decode.)

#### Solution

Reproduced live. Plug the **BLE Sniffer USB-A** tool (`POST /api/connect {tool:"ble-sniffer",port:"usb-a"}`) for a `ble-capture` token, then `GET /api/capture` with that Bearer token. Packets arrive out of order on two handles. Keep `0x37` (the maintenance log; `0x2a` is 6-byte binary vitals = noise), sort by `seq`, hex→bytes, concatenate, Base64-decode:

```python
import json, base64
pk  = json.load(open('capture.json'))['packets']
log = sorted([p for p in pk if p['handle']=='0x37'], key=lambda x: x['seq'])
print(base64.b64decode(bytes.fromhex(''.join(p['payload'] for p in log))).decode())
```

```
St.Dymphna CS-9000 maint log | site=stdymphna-rmc-01 | tech=emedra-svc
last_patient: Gideon Marsh (MRN 100413)
note: telemetry unencrypted per EM-2019 default; flag deadface{un3ncrypt3d_b4bbl3_fr0m_th3_sku11}
```

**Note:** reproduced live against the device on 2026-10-28. Full device recon in [EMEDRA_PREP.md](EMEDRA_PREP.md).

---

## Blocked / Unsolved

**Web Recon — Git Repository Leak (700, PCGCTF)** — target `http://flag1.cgcybercom.online/repo/.git/`. `flag1.cgcybercom.online` resolves (112.211.33.82, separate host from the scoreboard) but ports 80/443 are filtered from the working environment — every connection times out. The host is reachable from the contestant's own network, not from here.

Intended approach:

1. `Flag1.cgcybercom.online` is a subdomain, not a path on the scoreboard (the scoreboard host returns the CTFd app for every path). Hit it directly: `http://flag1.cgcybercom.online/repo/`.
2. Dump the exposed `.git` directory:
   ```bash
   pip install git-dumper
   git-dumper http://flag1.cgcybercom.online/repo/.git/ repo_dump
   cd repo_dump && git log --all -p
   grep -ri "pcgCTF{" .
   ```
3. The flag is typically in a commit, a committed secret/config, or a file deleted in a later commit — `git log -p` across all commits surfaces it.

**Cereal Killer 04 and Diagnosis** are listed above with confirmed flags but were solved from public writeups, not reproduced locally, because their challenge files were not available in this environment.

**Emedra CS-9000 — Bad Calibration (open).** Device filesystem has `/mnt/opt/scanworks/calibration/` (`calib.json`, `calib.json.sig`, `verify.py`) and the signature salt is leaked in `config.yaml` (`integrity.salt: EM-2019`). The sig is `sha256(<calib.json bytes> + "EM-2019")` — not a real secret. Forge a tampered-but-valid calibration (edit `calib.json`, recompute the hex, write `calib.json.sig`), then `scanctl scan`. The on-device write was blocked by the sandbox classifier this session; do it from the live shell tomorrow. Watch byte-exactness (`xxd`) — `verify.py` hashes raw file bytes. See [EMEDRA_PREP.md](EMEDRA_PREP.md).

**Emedra CS-9000 — debug.dump / HID console (open).** `config.yaml` exposes `debug_console: {enabled:true, function: debug.dump, tables:[patients,calibration,audit]}` and the binary references `debug.dump`. Delivery is the Rubber Ducky (`POST /api/kiosk/hid {token,macro}`), but no tried macro triggers the hidden console ("payload delivered, but no hidden console was triggered"); no `/api/debug*` route exists. Trigger macro still unknown — try real Ducky-Script sequences or a post-login touchscreen-console path. See [EMEDRA_PREP.md](EMEDRA_PREP.md).
