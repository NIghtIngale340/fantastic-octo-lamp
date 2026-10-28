# Commitment Issues

**Platform:** PCGCTF · **Challenge ID:** 36 · **Category:** General Skills · **Points:** 250

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Recover a flag that was removed from the current message.txt but remains in the Git object history.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/general-skills/036-commitment-issues/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

Deleting a line in a later commit does not immediately erase the earlier blob object. The repository includes a create-flag commit followed by a removal commit. Reading the older version is enough; there is no reason to run project code or restore the old commit into the working tree.

## Step-by-step solution

### 1. Inspect the saved repository history

After extracting challenge.zip into a separate working directory, `-C` runs Git in that repository, `--all` includes every reference and `--oneline` shows concise identifiers and messages. The commit identities below are also independently visible in the decompressed loose objects.

```sh
git -C drop-in log --oneline --all
```

**Recorded output / observation:**

```text
144fdc4 remove sensitive info
7d3aa55 create flag
```

The earlier commit is the relevant version. The messages suggest the intended trail, while the blob’s contents provide the real evidence.

### 2. Read the earlier blob without checking it out

The `commit:path` syntax selects one file at one revision. Unlike checkout, this reads the object without modifying the current working tree. Our independent validation decompressed the loose blob directly and checked its SHA-1 object identifier.

```sh
git -C drop-in show 7d3aa55:message.txt
```

**Recorded output / observation:**

```text
picoCTF{s@n1t1z3_be3dd3da}
```

The supplied source uses the original picoCTF prefix. This challenge does not specify a replacement wrapper, so the recovered string is preserved rather than guessed into a new format.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #36 — actual evidence capture

![036-step-01.png](../screenshots/036-step-01.png)

Read historical Git objects; no checkout or hooks.

Command/action actually executed:

```sh
git -c safe.directory=/home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/git036/drop-in -C /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/git036/drop-in log --oneline --all
```

[Actual command transcript](../screenshots/capture-work/036-step-1.terminal.log) · [Execution record](../screenshots/capture-work/036-step-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #36 — actual evidence capture

![036-step-02.png](../screenshots/036-step-02.png)

Read historical Git objects; no checkout or hooks.

Command/action actually executed:

```sh
git -c safe.directory=/home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/git036/drop-in -C /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/git036/drop-in show 7d3aa55:message.txt
```

[Actual command transcript](../screenshots/capture-work/036-step-2.terminal.log) · [Execution record](../screenshots/capture-work/036-step-2.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved result / candidate:

```text
picoCTF{s@n1t1z3_be3dd3da}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Version control preserves content that ordinary file inspection misses. Read historical blobs and validate the actual object; also remember that unreachable objects can eventually be pruned, so history recovery is not guaranteed forever.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/general-skills/036-commitment-issues/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/general-skills/036-commitment-issues/solution.md>)
- [git-recovered-objects.json](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/git-recovered-objects.json>)
