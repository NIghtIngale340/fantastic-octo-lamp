# Tube Station — Platforms

**Platform:** PCGCTF · **Challenge ID:** 243 · **Category:** OSINT / IMINT · **Points:** 100

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Determine the number of platforms at Piccadilly Circus station.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/osint-imint/243-tube-station-platforms/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The count is not the number of lines. Piccadilly Circus serves two lines, each with two directions and a separate numbered platform. Use the operator’s listed platform identifiers rather than counting only the platforms currently showing live arrivals.

## Step-by-step solution

### 1. Confirm the station from the shared image

The station-name sign ties the follow-up question to Piccadilly Circus. This shared input remains part of the evidence even though this challenge has no separate attachment.

```sh
/home/nightingale/CTF/PCGCTF/solved/osint-imint/240-tube-station-city/files/task3_1602089306375.jpg
```

**Recorded output / observation:**

```text
PICCADILLY CIRCUS STATION
```

With the identity established, inspect the operator’s platform layout rather than a generic Tube map.

### 2. Read both line-specific platform pairs

The Bakerloo listing identifies northbound Platform 1 and southbound Platform 2. The Piccadilly listing identifies eastbound Platform 3 and westbound Platform 4. Count unique platform numbers, not train arrivals or named directions alone.

```sh
Open TfL’s Piccadilly Circus station page with lineId=bakerloo, then with lineId=Piccadilly.
```

**Recorded output / observation:**

```text
Bakerloo: platforms 1 and 2
Piccadilly: platforms 3 and 4
Unique platform count: 4
```

The requested value is four. Arrival times are irrelevant and can change while this fixed layout fact remains the same.

## Visual evidence

![The shared entrance image establishes the station used for platform research.](/home/nightingale/CTF/PCGCTF/solved/osint-imint/240-tube-station-city/files/task3_1602089306375.jpg)

The shared entrance image establishes the station used for platform research.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### 243-actual-browser-image.png

![243-actual-browser-image.png](../screenshots/243-actual-browser-image.png)

Original supplied image displayed in the browser; identification context only, not an independent acceptance record.

## Flag discovery and verification

Saved result / candidate:

```text
pcgCTF{4}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

Primary references: [TfL Bakerloo station view](https://tfl.gov.uk/tube/stop/940GZZLUPCC/piccadilly-circus-underground-station?lineId=bakerloo), [TfL Piccadilly station view](https://tfl.gov.uk/tube/stop/940GZZLUPCC/piccadilly-circus-underground-station?lineId=Piccadilly).

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Operational pages contain both stable infrastructure facts and transient service data. Extract the numbered infrastructure and ignore changing arrival lists.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/osint-imint/243-tube-station-platforms/README.md>)
