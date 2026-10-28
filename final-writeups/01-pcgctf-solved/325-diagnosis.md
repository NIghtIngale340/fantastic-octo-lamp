# Diagnosis

**Platform:** PCGCTF · **Challenge ID:** 325 · **Category:** Deadface · **Points:** 500

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Historical site-solved snapshot; flag retained from teammate’s explicitly unreproduced public-writeup notes. Original APK missing.

## Challenge and objective

Identify the hidden Android activity implicated by the manifest configuration and recover its flag.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/325-diagnosis/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The manifest is a map of application components. An exported activity may be reachable by another app or explicit intent, but exporting a component alone is not proof that it exposes a flag. The implementing class and any permission checks must be traced as well.

## Step-by-step solution

### 1. Check the shared package boundary

The original direct-attachment inventory and related challenge folders were reviewed. No app-release.apk or original Hard Kept Secrets ZIP was present in the saved primary payloads. The answer is sourced to the teammate’s report; this is a bounded local absence, not a claim that the organizer never supplied a package.

```sh
find '/home/nightingale/CTF/PCGCTF' -iname '*.apk' -o -iname '*hard*kept*'
```

**Recorded output / observation:**

```text
Primary APK absent from local challenge attachments
Shared source: Hard Kept Secrets
```

Recover the shared original package once and use its hash to connect all three investigations. Garcia records flaG_ManIfesT3d from two public writeups but did not decompile the APK locally. The intended manifest review remains a plan until the package and actual component names are recovered.

### 2. Trace the relevant code after obtaining the APK

These tools decode the APK resources or DEX into an inspectable representation. The listed search terms are starting points, not an observed set of matching classes. The exact flags and their program roles must be established from the actual package before describing a successful local extraction.

```sh
apktool d app-release.apk -o decoded-apk
rg -n "activity|exported|permission" decoded-apk/AndroidManifest.xml
jadx -d decompiled app-release.apk
```

**Unexecuted artifact-specific procedure:**

```text
[OUTPUT NEEDED: actual manifest/decompiler matches and relevant surrounding code]
```

Identify the exported diagnostic component and inspect its implementation. If runtime confirmation is needed, construct the explicit activity intent using the package/component names actually observed, not placeholders disguised as real names.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #325 — actual evidence capture

![325-actual-artifact-inventory.png](../screenshots/325-actual-artifact-inventory.png)

Actual inventory confirms which original challenge artifact is absent; does not invent a reverse-engineering/stego result. The inventory documents the missing payload; no extraction or decompilation of that absent payload is claimed.

Command/action actually executed:

```sh
find /home/nightingale/CTF/PCGCTF/solved/deadface/325-diagnosis -maxdepth 2 -type f -printf '%P
'
```

[Actual command transcript](../screenshots/capture-work/325-artifact-inventory.terminal.log) · [Execution record](../screenshots/capture-work/325-artifact-inventory.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

**Blocked evidence:** the original challenge payload is absent. The inventory was captured; the proposed extraction or code inspection cannot be truthfully reproduced until that original file is recovered.

## Flag discovery and verification

Saved result / candidate:

```text
deadface{flaG_ManIfesT3d}
```

Historical site-solved snapshot; flag retained from teammate’s explicitly unreproduced public-writeup notes. Original APK missing.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- Obtain the original shared APK/ZIP and record its SHA-256.
- Identify the exported diagnostic component and inspect its implementation. If runtime confirmation is needed, construct the explicit activity intent using the package/component names actually observed, not placeholders disguised as real names.
- Capture the decisive code/manifest evidence and any runtime observation separately.

## What this challenge taught me

The same application can leak different secrets through different code paths. Establish the role of the recovered value instead of submitting whichever flag-shaped string appears first.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/325-diagnosis/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/325-diagnosis/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
