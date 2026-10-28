# Art Heist: The Forgery

**Platform:** PCGCTF · **Challenge ID:** 321 · **Category:** Deadface · **Points:** 200

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Historical site-solved snapshot; flag is retained from Garcia’s attributed public-writeup report, while the original payload and decisive extraction are missing.

## Challenge and objective

Identify the forged painting among five scans and recover the forger’s signature.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/321-art-heist-the-forgery/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The prompt emphasizes digital archive records as well as visual similarity. Garcia’s notes suggest metadata as the intended channel and record a Lamia-themed flag, but no original painting archive was downloaded in this snapshot. The forged filename and decisive metadata field therefore remain evidence gaps.

## Step-by-step solution

### 1. Audit the available primary evidence

The challenge README and imported source were inspected. The attachment directory does not contain the primary payload named in the teammate’s report, which bounds what can be independently reconstructed here.

```sh
find '/home/nightingale/CTF/PCGCTF/solved/deadface/321-art-heist-the-forgery' -maxdepth 2 -type f -print
```

**Recorded output / observation:**

```text
Available: saved README and imported solution
Missing primary artifact: CTF_Forgery_Paintings.zip
```

The solved snapshot remains valid historical status. It does not establish a new artifact extraction or make the intended method a recorded local execution.

### 2. Reproduce the first artifact-specific triage after recovery

Compare author, comment, software and PNG textual-chunk fields across the five files. Chunk-name presence is only a locator: decode the actual chunk data with a format-aware reader before claiming its contents are the flag.

```sh
exiftool -a -G1 -s paintings/*
python - <<'PY'
from pathlib import Path
for p in Path("paintings").glob("*.png"):
    b=p.read_bytes();print(p.name,[t for t in [b"tEXt",b"iTXt",b"zTXt"] if t in b])
PY
```

**Unexecuted reproduction plan:**

```text
[OUTPUT NEEDED: actual CTF_Forgery_Paintings.zip analysis; no terminal output was fabricated.]
```

Capture the forged file, anomalous field and exact decoded value. The current report does not preserve which PNG chunk or metadata tag was decisive.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #321 — actual evidence capture

![321-actual-artifact-inventory.png](../screenshots/321-actual-artifact-inventory.png)

Actual inventory confirms which original challenge artifact is absent; does not invent a reverse-engineering/stego result. The inventory documents the missing payload; no extraction or decompilation of that absent payload is claimed.

Command/action actually executed:

```sh
find /home/nightingale/CTF/PCGCTF/solved/deadface/321-art-heist-the-forgery -maxdepth 2 -type f -printf '%P
'
```

[Actual command transcript](../screenshots/capture-work/321-artifact-inventory.terminal.log) · [Execution record](../screenshots/capture-work/321-artifact-inventory.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

**Blocked evidence:** the original challenge payload is absent. The inventory was captured; the proposed extraction or code inspection cannot be truthfully reproduced until that original file is recovered.

## Flag discovery and verification

Saved result / candidate:

```text
deadface{L4MIA_SIGNS_HER_WORK}
```

Historical site-solved snapshot; flag is retained from Garcia’s attributed public-writeup report, while the original payload and decisive extraction are missing.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- Obtain the original CTF_Forgery_Paintings.zip and verify its identity before following the proposed procedure.
- Capture the forged file, anomalous field and exact decoded value. The current report does not preserve which PNG chunk or metadata tag was decisive.
- Capture the decisive extraction and, if available, the original accepted submission screenshot.

## What this challenge taught me

A metadata discrepancy can expose a forged digital record even when the visible artwork looks consistent.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/321-art-heist-the-forgery/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/321-art-heist-the-forgery/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
