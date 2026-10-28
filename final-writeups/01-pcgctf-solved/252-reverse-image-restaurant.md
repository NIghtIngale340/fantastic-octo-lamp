# Reverse Image — Restaurant

**Platform:** PCGCTF · **Challenge ID:** 252 · **Category:** OSINT / IMINT · **Points:** 100

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Answer supported by the earlier image investigation and Bon Appétit’s original video; exact historical accepted punctuation is not recorded.

## Challenge and objective

Identify the restaurant shown in the supplied interior photograph.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/osint-imint/252-reverse-image-restaurant/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The photograph’s arrangement and interior signage are the starting point. This restaurant image is also the prerequisite evidence for the editor question (#253). The existing image investigation matched it to Katz’s Delicatessen and corroborated that link with Bon Appétit’s own video filmed at the restaurant; the latter names the editor working a 24-hour shift there.

## Step-by-step solution

### 1. Inspect the restaurant interior

Compare the visible counters, interior signs and wall arrangement to the matching restaurant evidence saved for #253. The source image is the actual challenge input, not a newly generated illustration.

```sh
Open PCGCTF/solved/osint-imint/252-reverse-image-restaurant/files/task6_1602348602115.jpg.
```

**Recorded output / observation:**

```text
Identified restaurant: Katz’s Delicatessen, New York City
```

A recognizable restaurant name is an answer hypothesis; a corroborating first-party recording links the image context to the named location.

### 2. Cross-check the restaurant context

Bon Appétit’s own video page identifies Katz’s Delicatessen and Andrew Knowlton’s shift there. This is the primary media source used by the related editor challenge, and it supports the named restaurant rather than an unrelated lookalike.

```sh
Open https://www.bonappetit.com/video/watch/working-24-hours-straight-at-new-york-most-iconic-deli
```

**Recorded output / observation:**

```text
Katz’s Delicatessen
```

The restaurant name belongs in this question’s answer; Andrew Knowlton belongs in the separate editor question.

## Visual evidence

![Original restaurant photograph; compare its distinctive counter and signage to the primary video.](/home/nightingale/CTF/PCGCTF/solved/osint-imint/252-reverse-image-restaurant/files/task6_1602348602115.jpg)

Original restaurant photograph; compare its distinctive counter and signage to the primary video.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### 252-actual-browser-image.png

![252-actual-browser-image.png](../screenshots/252-actual-browser-image.png)

Original supplied image displayed in the browser; identification context only, not an independent acceptance record.

## Flag discovery and verification

Saved result / candidate:

```text
pcgCTF{Katz's Delicatessen}
```

Answer supported by the earlier image investigation and Bon Appétit’s original video; exact historical accepted punctuation is not recorded.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

The original source writes Katz’s with an apostrophe. This draft’s ASCII apostrophe is a submission candidate, not a newly checked accepted spelling. See the [related editor evidence](/home/nightingale/CTF/PCGCTF/unsolved/osint-imint/253-reverse-image-editor/evidence/verification.json).

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Reverse-image work is strongest when a visual match is tied to a named original source. Keep the restaurant and the person associated with it as separate answers.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/osint-imint/252-reverse-image-restaurant/README.md>)
