# Cereal Killer 04

**Platform:** PCGCTF · **Challenge ID:** 337 · **Category:** Deadface · **Points:** 600

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Historical site-solved snapshot; flag is retained from Garcia’s attributed public-writeup report, while the original payload and decisive extraction are missing.

## Challenge and objective

Analyze the recovered Greys binary and recover the spooky-cereal flag.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/337-cereal-killer-04/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

“Assembly Codes” points toward native code, and Garcia’s reference names inner.dll. The source material explicitly admits that the DLL was unavailable locally. Its published flag can be preserved, but an export name, disassembly address, register sequence or runtime buffer cannot be invented. The series numbering differs between the local title and the cited public notes.

## Step-by-step solution

### 1. Audit the available primary evidence

The challenge README and imported source were inspected. The attachment directory does not contain the primary payload named in the teammate’s report, which bounds what can be independently reconstructed here.

```sh
find '/home/nightingale/CTF/PCGCTF/solved/deadface/337-cereal-killer-04' -maxdepth 2 -type f -print
```

**Recorded output / observation:**

```text
Available: saved README and imported solution
Missing primary artifact: inner.dll
```

The solved snapshot remains valid historical status. It does not establish a new artifact extraction or make the intended method a recorded local execution.

### 2. Reproduce the first artifact-specific triage after recovery

First identify the actual PE architecture and exports from the file rather than assuming x86 or x64 from its extension. Printable strings are a first pass, not proof that a runtime-assembled flag is absent. Load the verified binary in the available native analysis tool and follow the flag-building code only once its entry point is known.

```sh
file inner.dll
objdump -p inner.dll
strings -n 6 inner.dll | rg -i "deadface|cereal|grey"
```

**Unexecuted reproduction plan:**

```text
[OUTPUT NEEDED: actual inner.dll analysis; no terminal output was fabricated.]
```

Obtain inner.dll, record its SHA-256, identify the actual export/function and preserve the decoded buffer or a decompiler-backed reconstruction. No function address is known in the local notes.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #337 — actual evidence capture

![337-actual-artifact-inventory.png](../screenshots/337-actual-artifact-inventory.png)

Actual inventory confirms which original challenge artifact is absent; does not invent a reverse-engineering/stego result. The inventory documents the missing payload; no extraction or decompilation of that absent payload is claimed.

Command/action actually executed:

```sh
find /home/nightingale/CTF/PCGCTF/solved/deadface/337-cereal-killer-04 -maxdepth 2 -type f -printf '%P
'
```

[Actual command transcript](../screenshots/capture-work/337-artifact-inventory.terminal.log) · [Execution record](../screenshots/capture-work/337-artifact-inventory.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

**Blocked evidence:** the original challenge payload is absent. The inventory was captured; the proposed extraction or code inspection cannot be truthfully reproduced until that original file is recovered.

## Flag discovery and verification

Saved result / candidate:

```text
deadface{Before_Consenting_to_Med_Exam_Ascertain_Destination_of_Finger!}
```

Historical site-solved snapshot; flag is retained from Garcia’s attributed public-writeup report, while the original payload and decisive extraction are missing.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- Obtain the original inner.dll and verify its identity before following the proposed procedure.
- Obtain inner.dll, record its SHA-256, identify the actual export/function and preserve the decoded buffer or a decompiler-backed reconstruction. No function address is known in the local notes.
- Capture the decisive extraction and, if available, the original accepted submission screenshot.

## What this challenge taught me

A published flag and a reproduced reverse-engineering procedure are different deliverables. Keep addresses and runtime claims tied to a real analyzed binary.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/337-cereal-killer-04/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/337-cereal-killer-04/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
