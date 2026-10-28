# Who Is Behind the Platform?

**Platform:** PCGCTF · **Challenge ID:** 260 · **Category:** General Skills · **Points:** 20000

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Creator identity supported by primary public profile; earliest-commit command and exact accepted flag spacing remain to be captured.

## Challenge and objective

Identify the creator of the open-source CTF platform by following its earliest public project history.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/general-skills/260-who-is-behind-the-platform/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The platform clues point to CTFd rather than the organizer of this specific event. Its upstream author Kevin Chung uses the public handle ColdHeat, whose own GitHub profile identifies him as CTFd’s creator. The remaining provenance step is to tie that identity to the root commit, since being a current maintainer alone would not satisfy the “started the project” clue.

## Step-by-step solution

### 1. Establish the upstream project and creator identity

The upstream repository is the source of development history; the author’s own profile is a primary identity statement. The official CTFd site also describes the project’s public release timeline.

```sh
Open https://github.com/CTFd/CTFd and https://github.com/ColdHeat
```

**Recorded output / observation:**

```text
Kevin Chung — ColdHeat — Creator of CTFd
```

This is evidence for the answer Kevin Chung, not for the local event organizer’s identity.

### 2. Verify the earliest reachable commit locally

These are exact reproduction commands, with the root identifier filled from actual output. `--max-parents=0` selects root commits, and `--no-patch --format=fuller` shows author and committer metadata without a code diff. The clone/root-commit execution was not performed in this drafting pass.

```sh
git clone https://github.com/CTFd/CTFd.git /tmp/ctfd-history-review
git -C /tmp/ctfd-history-review rev-list --max-parents=0 HEAD
git -C /tmp/ctfd-history-review show --no-patch --format=fuller ROOT_COMMIT_FROM_PREVIOUS_COMMAND
```

**Recorded output / observation:**

```text
[ROOT COMMIT OUTPUT NEEDED: author, date, commit hash and message]
```

Compare the root author with Kevin Chung/ColdHeat and retain both records. If the repository has more than one root, explain which history belongs to the original application rather than choosing the first line blindly.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### 260-primary-profile.png

![260-primary-profile.png](../screenshots/260-primary-profile.png)

Actual public GitHub profile viewed in the browser.

Source viewed: [https://github.com/ColdHeat](https://github.com/ColdHeat).

## Flag discovery and verification

Saved result / candidate:

```text
pcgCTF{Kevin Chung}
```

Creator identity supported by primary public profile; earliest-commit command and exact accepted flag spacing remain to be captured.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

Primary references: [Kevin Chung / ColdHeat](https://github.com/ColdHeat), [CTFd upstream repository](https://github.com/CTFd/CTFd), [official project story](https://ctfd.io/about/).

## Remaining review tasks

- Run the root-commit verification commands and save their real output.
- Recover the historical accepted submission to settle capitalization and spacing without guessing.

## What this challenge taught me

An open-source project’s author is a provenance question. A maintainer list and a project founder are not automatically interchangeable; use original history and a primary identity statement.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/general-skills/260-who-is-behind-the-platform/README.md>)
