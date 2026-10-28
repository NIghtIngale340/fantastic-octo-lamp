# Headshot

**Platform:** PCGCTF · **Challenge ID:** 338 · **Category:** Deadface · **Points:** 150

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Historical site-solved snapshot; flag is retained from Garcia’s attributed public-writeup report, while the original payload and decisive extraction are missing.

## Challenge and objective

Identify the one employee headshot tampered with and recover its hidden tag.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/338-headshot/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The challenge is comparative: one image differs from the rest, so dimensions, metadata and container structure should be compared before trying a random extraction password. The original snapshot contains no headshot.zip attachment. The saved flag comes from Garcia’s public-writeup report, not a retained local extraction.

## Step-by-step solution

### 1. Audit the available primary evidence

The challenge README and imported source were inspected. The attachment directory does not contain the primary payload named in the teammate’s report, which bounds what can be independently reconstructed here.

```sh
find '/home/nightingale/CTF/PCGCTF/solved/deadface/338-headshot' -maxdepth 2 -type f -print
```

**Recorded output / observation:**

```text
Available: saved README and imported solution
Missing primary artifact: headshot.zip
```

The solved snapshot remains valid historical status. It does not establish a new artifact extraction or make the intended method a recorded local execution.

### 2. Reproduce the first artifact-specific triage after recovery

Compare metadata and structure across all actual headshots. `-a` keeps duplicate tags, `-G1` names their metadata groups and `-s` uses concise tag labels. Searching printable strings is useful triage, but a negative result would not rule out compressed or pixel-encoded data.

```sh
exiftool -a -G1 -s headshots/*
file headshots/*
strings -n 6 headshots/* | rg -i "deadface|comment|author"
```

**Unexecuted reproduction plan:**

```text
[OUTPUT NEEDED: actual headshot.zip analysis; no terminal output was fabricated.]
```

Identify the exact anomalous filename and extraction method; do not call a large file or unusual comment malicious without comparing its peers.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #338 — actual evidence capture

![338-actual-artifact-inventory.png](../screenshots/338-actual-artifact-inventory.png)

Actual inventory confirms which original challenge artifact is absent; does not invent a reverse-engineering/stego result. The inventory documents the missing payload; no extraction or decompilation of that absent payload is claimed.

Command/action actually executed:

```sh
find /home/nightingale/CTF/PCGCTF/solved/deadface/338-headshot -maxdepth 2 -type f -printf '%P
'
```

[Actual command transcript](../screenshots/capture-work/338-artifact-inventory.terminal.log) · [Execution record](../screenshots/capture-work/338-artifact-inventory.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

**Blocked evidence:** the original challenge payload is absent. The inventory was captured; the proposed extraction or code inspection cannot be truthfully reproduced until that original file is recovered.

## Flag discovery and verification

Saved result / candidate:

```text
deadface{b00m_h34Dsh0TTT}
```

Historical site-solved snapshot; flag is retained from Garcia’s attributed public-writeup report, while the original payload and decisive extraction are missing.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- Obtain the original headshot.zip and verify its identity before following the proposed procedure.
- Identify the exact anomalous filename and extraction method; do not call a large file or unusual comment malicious without comparing its peers.
- Capture the decisive extraction and, if available, the original accepted submission screenshot.

## What this challenge taught me

A comparative set can reveal tampering more reliably than looking at one file in isolation.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/338-headshot/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/338-headshot/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
