# Info Leaks

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 309 |
| Technical category | Aurora Patient Zero |
| Points in saved inventory | 250 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Recover the last patient’s name and birth date from the IPA. |
| Result | `deadface{Mara-Voss-1988-04-17}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

An IPA is a package whose plist and bundled resources can be read without running iOS. The challenge asks for patient PII, so a bootstrap configuration is a plausible source; Base64 is only a representation, not encryption.

## Working through the evidence

### 1. Open the nested package

The supplied outer ZIP contains AuroraPatientPortal.ipa; the IPA contains Payload/aurora-patient-portal.app/Info.plist. The recorded extraction preserved the package hashes and REA evidence IDs. It did not install or execute the app.

### 2. Decode the bootstrap value

The Info.plist key **AuroraPatientBootstrap** is a Base64 string. Once the original plist is extracted, reproduce the decoding with:

```python
import plistlib, base64, json
with open('/home/nightingale/CTF/PCGCTF/unsolved/aurora-patient-zero/309-info-leaks/evidence/Info.plist', 'rb') as f:
    info = plistlib.load(f)
patient = json.loads(base64.b64decode(info['AuroraPatientBootstrap']))
print(patient)
```

`plistlib` handles the plist structure rather than treating binary plist data as arbitrary strings. `b64decode` turns the textual representation into bytes, and `json.loads` verifies the resulting object.

The recorded object contains patientName **Mara Voss**, dateOfBirth **1988-04-17**, clinic **Westlake**. The patient name and date—not the clinic—are the fields requested here.

### 3. Follow the original challenge format

The task explicitly requests deadface{firstname-lastname-YYYY-MM-DD}. Hyphenating Mara Voss and retaining the date gives the saved flag. The deadface prefix is intentional; blindly changing every archive answer to pcgCTF would conflict with this challenge’s instructions.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #309 — actual evidence capture

![309-script-1.png](../screenshots/309-script-1.png)

Run the documented self-contained decoder/calculation on original inputs.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/309-capture-1.py
```

[Actual command transcript](../screenshots/capture-work/309-script-1.terminal.log) · [Execution record](../screenshots/capture-work/309-script-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`deadface{Mara-Voss-1988-04-17}`**. Originalplist and decodedJSON confirm PII; no platform acceptance was tested.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

Encoding embedded configuration does not protect private data. Read structured fields and apply the exact task format.

## Evidence and references

[Original archived challenge](../../unsolved/aurora-patient-zero/309-info-leaks/README.md)

- [Decisive preserved verification results](../../analysis-team-verification/aurora-rea-evidence.json)
- [Original shared IPA archive](../../unsolved/aurora-patient-zero/309-info-leaks/files/AuroraPatientPortal.ipa.zip)
- [Decoded bootstrap JSON](../../unsolved/aurora-patient-zero/309-info-leaks/evidence/patient-bootstrap.json)
- [Preserved investigation notes](../../unsolved/aurora-patient-zero/309-info-leaks/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
