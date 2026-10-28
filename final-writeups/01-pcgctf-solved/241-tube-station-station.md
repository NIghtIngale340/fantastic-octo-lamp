# Tube Station — Station

**Platform:** PCGCTF · **Challenge ID:** 241 · **Category:** OSINT / IMINT · **Points:** 100

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Local evidence independently reproduced; exact historical platform submission is not newly tested.

## Challenge and objective

Identify the exact station shown in the same entrance photograph.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/osint-imint/241-tube-station-station/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The city and station questions share one image. I would separate generic network branding from the actual station name: “Underground” identifies the transport system, while the lower sign identifies the individual stop. The surrounding advertising screens fit the same location, but they are supporting context rather than the primary proof.

## Step-by-step solution

### 1. Read the station entrance lettering

Inspect the original image, especially the sign immediately above the staircase. No OCR output has been invented; this was a direct visual inspection.

```sh
/home/nightingale/CTF/PCGCTF/solved/osint-imint/240-tube-station-city/files/task3_1602089306375.jpg
```

**Recorded output / observation:**

```text
PICCADILLY CIRCUS STATION
```

The station label is the anchor for both questions. The name is visible on the blue sign above the stairs, not on the generic red roundel. Read Piccadilly Circus Station, then corroborate it against the operator’s station listing.

### 2. Corroborate with the transport operator

The operator’s own station page supplies the station name and postal city. This avoids confusing a similar-looking Underground entrance elsewhere with the named stop. The page was consulted during drafting.

```sh
Open https://tfl.gov.uk/tube/stop/940GZZLUPCC/piccadilly-circus-underground-station
```

**Recorded output / observation:**

```text
Station: Piccadilly Circus Underground Station
Address city: London
```

Return only the field asked for by this particular challenge: Piccadilly Circus.

## Visual evidence

![Original shared photograph; highlight the lower station-name sign.](/home/nightingale/CTF/PCGCTF/solved/osint-imint/240-tube-station-city/files/task3_1602089306375.jpg)

Original shared photograph; highlight the lower station-name sign.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### 241-actual-browser-image.png

![241-actual-browser-image.png](../screenshots/241-actual-browser-image.png)

Original supplied image displayed in the browser; identification context only, not an independent acceptance record.

## Flag discovery and verification

Saved result / candidate:

```text
pcgCTF{Piccadilly Circus}
```

Local evidence independently reproduced; exact historical platform submission is not newly tested.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

Primary source: [Transport for London station page](https://tfl.gov.uk/tube/stop/940GZZLUPCC/piccadilly-circus-underground-station).

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Shared evidence can answer different questions at different levels of specificity. Keep the city and station submissions separate.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/osint-imint/241-tube-station-station/README.md>)
