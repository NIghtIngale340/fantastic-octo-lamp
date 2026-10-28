# PCGCTF Juice Shop Gateway

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 122 |
| Technical category | Reconnaissance |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Find the hidden Score Board and derive its shared CTF flag. |
| Result | `pcgCTF{73dbb9f2bac263e70119eb5e22d79e029e03a27e}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

The supplied compose file configures CTF mode and a common CTF_KEY. That makes the per-challenge flag deterministic, but the exact challenge name and app-side calculation still need verification rather than guessing from a route name.

## Working through the evidence

### 1. Read the deployment configuration

The compose file sets NODE_ENV=ctf and a shared CTF_KEY. The hidden Angular route is `http://localhost:3000/#/score-board`. This local instance is the intended training environment; a scoreboard on another service is not interchangeable.

### 2. Verify the app’s flag construction

The recorded official-source check identifies `Score Board` with key scoreBoardChallenge in challenges.yml. challengeUtils.ts sends the challenge’s name into utils.ctfFlag. utils.ts computes hexadecimal **HMAC-SHA1** using the CTF_KEY string. The literal ASCII key is used; it is not hex-decoded into bytes.

```python
import hashlib, hmac, yaml
cfg = yaml.safe_load(open('/home/nightingale/CTF/PCGCTF/unsolved/reconnaissance/122-pcgctf-juice-shop-gateway/files/docker-compose.yml'))
key = cfg['services']['juice-shop']['environment']['CTF_KEY']
print(hmac.new(key.encode(), b'Score Board', hashlib.sha1).hexdigest())
```

Read the key from the supplied compose file rather than copying unrelated credentials into a public terminal command. HMAC authenticates a message with a key; here the message is the exact challenge name, including its space and capitals.

Actual independently recomputed digest:

```text
73dbb9f2bac263e70119eb5e22d79e029e03a27e
```

### 3. Keep derivation distinct from application execution

The source and calculation establish the deterministic code. Docker was not run during this verification; the teammate’s report that the route marked the challenge solved is attributed to them. The supplied image tag is not pinned, so a future runtime should record its actual version or digest and compare its implementation.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #122 — actual evidence capture

![122-script-1.png](../screenshots/122-script-1.png)

Run the documented self-contained decoder/calculation on original inputs.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/122-capture-1.py
```

[Actual command transcript](../screenshots/capture-work/122-script-1.terminal.log) · [Execution record](../screenshots/capture-work/122-script-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{73dbb9f2bac263e70119eb5e22d79e029e03a27e}`**. Officialsource and independent HMAC calculation agree. Applicationruntime and platform acceptance remain unobserved.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

A reproducible deterministic derivation still needs exact inputs and version context; it is not the same evidence as observing a running challenge solve.

## Evidence and references

[Original archived challenge](../../unsolved/reconnaissance/122-pcgctf-juice-shop-gateway/README.md)

- [Decisive preserved verification results](../../analysis-team-verification/artifacts.json)
- [Original compose configuration](../../unsolved/reconnaissance/122-pcgctf-juice-shop-gateway/files/docker-compose.yml)
- [Preserved investigation notes](../../unsolved/reconnaissance/122-pcgctf-juice-shop-gateway/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
