# Back to Basics

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 312 |
| Technical category | Aurora Patient Zero |
| Points in saved inventory | 150 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Identify the gateway named in the hidden diagnostic data. |
| Result | `deadface{gw-westlake-int-03}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

Finding a gateway-looking string alone would be weaker than proving its role. The relevant question is which value the app associates with a gateway diagnostic label.

## Working through the evidence

### 1. Inspect the original executable statically

The package executable is Aurora Health Mobile. Initial strings include AuroraDiagnostics and gw-westlake-int-03, but strings by themselves cannot establish that the latter is actually used as the gateway. The saved analysis therefore followed the diagnostic initializer.

### 2. Link label and value in code

REA/Ghidra’s recorded dossier for DiagnosticInfo.items at address 0x100009a68 shows construction of seven diagnostic rows. The second row pairs the label **Sync Gateway** with **gw-westlake-int-03**, decoded from constants at 0x100009b78 and0x100009b90. The same initializer contains Clinic Route=westlake and a Last Gateway Check value. This ties the candidate to the role requested by the challenge instead of merely finding nearby strings.

A focused initial triage command is:

```sh
strings -n 4 'Aurora Health Mobile'
```

`-n 4` sets the minimum printable-run length. Its role is navigation to relevant strings, not proof of the SwiftUI page’s live behavior. Reproducing the stronger result requires opening the original hash-identified executable in the analysis tool and following DiagnosticInfo.items using the preserved dossier.

### 3. State the scope of verification

The code establishes the diagnostic data relationship. The iOS app was not run, so this draft does not claim that a long-press gesture was actually exercised or that a live network connection to the gateway succeeded. The task’s explicit deadface{gateway-name} wrapper determines the candidate spelling.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #312 — actual evidence capture

![312-actual-binary-strings.png](../screenshots/312-actual-binary-strings.png)

Actual original executable string triage; label/value code role remains grounded in retained static-analysis dossier. This is a printable-string inspection, not a new decompiler or runtime screenshot.

Command/action actually executed:

```sh
strings -n 4 '/home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/Aurora Health Mobile' | rg -i 'gw-westlake|gateway|Aurora Diagnostics'
```

[Actual command transcript](../screenshots/capture-work/312-strings.terminal.log) · [Execution record](../screenshots/capture-work/312-strings.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`deadface{gw-westlake-int-03}`**. Staticlabel/value association is confirmed by the retained dossier; runtime UI andplatform acceptance remain unobserved.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

A role-linked constant is stronger evidence than an isolated string, but static code inspection should not be presented as runtime observation.

## Evidence and references

[Original archived challenge](../../unsolved/aurora-patient-zero/312-back-to-basics/README.md)

- [Decisive preserved verification results](../../analysis-team-verification/aurora-rea-evidence.json)
- [Original shared IPA archive](../../unsolved/aurora-patient-zero/309-info-leaks/files/AuroraPatientPortal.ipa.zip)
- [Preserved investigation notes](../../unsolved/aurora-patient-zero/312-back-to-basics/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
