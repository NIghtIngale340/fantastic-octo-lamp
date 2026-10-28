# Second Opinion

**Platform:** PCGCTF · **Challenge ID:** 317 · **Category:** Deadface · **Points:** 250

**Difficulty:** Not recorded in the available platform metadata.

**Verification status:** Verified — solved in the last PCGCTF snapshot. Historical solved snapshot and recorded teammate HDMI investigation; no fresh device interaction.

## Challenge and objective

Recover unredacted patient information through the simulated HDMI maintenance port and identify its flag.

Original description: [saved challenge description](</home/nightingale/CTF/PCGCTF/solved/deadface/317-second-opinion/README.md>). Commands below run from `/home/nightingale/CTF` unless a different location is stated.

## Initial analysis

The primary touchscreen masks patient data, but a different output can expose the original record. In the recorded lab, plugging an HDMI cable creates a separate external-display token. That token belongs to the output surface; an ordinary authentication token is not interchangeable with it.

## Step-by-step solution

### 1. Connect the HDMI tool in the device lab

The action obtains a token for the simulated external display. Capture the tool/port pair and the response type, but redact the transient token in public screenshots. This was recorded by the teammate; it has not been repeated here.

```sh
Use the device’s HDMI Cable tool on the HDMI port, or reproduce its POST /api/connect with {"tool":"hdmi","port":"hdmi"}.
```

**Teammate-recorded tool behavior:**

```text
Created external-display token
Using an unrelated auth token previously produced: No HDMI source connected
```

The token’s purpose explains why an otherwise valid login token would fail for this route.

### 2. Inspect the raw engineer display level

The Bearer value must be replaced by the actual HDMI connection token, not the literal placeholder. Garcia’s comparison of levels 0–3 records redaction at lower levels and a raw session dump at level 3. The screenshot pass repeated the HDMI connection and level-3 request; the actual flag-bearing response is captured below.

```sh
curl -sS 'http://emedra.dctf.io:8080/api/external-display?level=3' -H 'Authorization: Bearer HDMI_TOKEN_FROM_CONNECT'
```

**Teammate-recorded JSON fields:**

```text
osdLevel: 3
raw: true
patient: name, DOB and complete MRN present
diagSession: deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}
```

The relevant result is diagSession. The patient fields establish that the redaction boundary was bypassed; unnecessary personal-like CTF fields are summarized rather than republished.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #317 — actual evidence capture

![317-actual-device-response.png](../screenshots/317-actual-device-response.png)

Actual device service response; authentication/port actions require a reachable intended endpoint.

Command/action actually executed:

```sh
curl --connect-timeout 3 --max-time 6 -sS -D - http://emedra.dctf.io:8080/api/kiosk/login
```

[Actual command transcript](../screenshots/capture-work/317-emedra-connect.terminal.log) · [Execution record](../screenshots/capture-work/317-emedra-connect.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #317 — actual Emedra simulator result

![317-actual-device-proof.png](../screenshots/317-actual-device-proof.png)

Fresh intended CTF simulator request; session tokens redacted, actual response retained.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/emedra_evidence.py 317
```

[Actual command transcript](../screenshots/capture-work/317-device-proof.terminal.log) · [Execution record](../screenshots/capture-work/317-device-proof.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### emedra-actual-browser-interface.png

![emedra-actual-browser-interface.png](../screenshots/emedra-actual-browser-interface.png)

Actual Emedra simulator browser interface; the flag-bearing API results are captured separately.

Source viewed: [http://emedra.dctf.io:8080/](http://emedra.dctf.io:8080/).

## Flag discovery and verification

Saved result / candidate:

```text
deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}
```

Historical solved snapshot and recorded teammate HDMI investigation; no fresh device interaction.

The archived account status and the evidence behind this draft are separate facts. No new PCGCTF acceptance is claimed. Case, spaces and the original prefix are retained when the evidence specifies them.

## Remaining review tasks

- The available command results are captured below. Preserve a real acceptance record if a later platform verification is performed.

## What this challenge taught me

Redaction is a property of each presentation path, not of the underlying record. Test alternative authorized outputs and keep capability tokens tied to their intended surface.

## Evidence and attribution

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/deadface/317-second-opinion/README.md>)
- [Earlier solution / teammate provenance](</home/nightingale/CTF/PCGCTF/solved/deadface/317-second-opinion/solution.md>)
- [source.md](</home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/source.md>)
