# Trust the Referer

| Field | Details |
|---|---|
| Platform | OverTheWire Natas, mirrored by PCGCTF |
| Challenge ID | 10 |
| Technical category | Web Exploitation - Natas |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Satisfy a weak Referer check to obtain natas5’s credential. |
| Result | Recovered next-level password — intentionally redacted in this publication draft. |

**Verified on OverTheWire** from the saved live-authentication record; PCGCTF acceptance remains unconfirmed.

## Reading the clues

Here the server gives a useful error: access depends on where the request appears to originate. The important word is “appears.” The HTTP Referer header is supplied by the client and can be changed independently of any actual navigation history.

## Working through the evidence

Commands below reproduce the recorded training procedure; the screenshot pass independently replayed the level-specific method and next-level authentication. `curl --user natasN` prompts for the current level password rather than putting it in shell history. `-sS` hides the progress meter while retaining errors. The output excerpts are redacted from the saved investigation; the redaction is not part of the server response.

### 1. Observe the denial before changing the request

```sh
curl -sS --user natas4 http://natas4.natas.labs.overthewire.org/
```

The saved denial states that authorized users should come from `http://natas5.natas.labs.overthewire.org/`. This tells us the exact value to test. It does not prove that a visit to that site is necessary.

### 2. Supply the expected header

```sh
curl -sS --user natas4 -e http://natas5.natas.labs.overthewire.org/ http://natas4.natas.labs.overthewire.org/index.php
```

Curl's `-e` option sets Referer. The request still goes to **natas4**; the value naming **natas5** is only a header. Confusing these two URLs would test a different authentication boundary.

The recorded response changes to:

```text
Access granted. The password for natas5 is [REDACTED_LEVEL_PASSWORD]
```

### 3. Verify the credential separately

The saved next-host authentication returned HTTP **200** for `natas5`. This proves that the newly revealed string was the next password, while the before/after response establishes which header check was bypassed.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #10 — actual evidence capture

![010-natas-method.png](../screenshots/010-natas-method.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 10 method
```

[Actual command transcript](../screenshots/capture-work/010-natas-method.terminal.log) · [Execution record](../screenshots/capture-work/010-natas-method.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #10 — actual evidence capture

![010-natas-verify.png](../screenshots/010-natas-verify.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 10 verify
```

[Actual command transcript](../screenshots/capture-work/010-natas-verify.terminal.log) · [Execution record](../screenshots/capture-work/010-natas-verify.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved verification at **2026-10-28T22:37:26+08:00** authenticated to **natas5** at `http://natas5.natas.labs.overthewire.org/` and returned **HTTP 200**. Its response SHA-256 is `caa909ae0346016d34d5b62e3eda7b03e0016d80beacec48dd32afc08901023c`. This is a recorded independent OverTheWire check, the earlier authentication record; the screenshot pass also made a fresh successful authentication, documented below.

The demonstration uses the level-specific host and username. Keep the recovered password in a private working copy; the PCGCTF candidate wraps that exact recovered value as `pcgCTF{<RECOVERED_NEXT_LEVEL_PASSWORD>}`. Neither that wrapper nor the PCGCTF solved state was independently confirmed. Redact the password from any browser or terminal capture before publishing it.

## What this challenge taught me

A request header can be a useful signal for analytics, but its presence is not evidence of identity. Authorization must not rely on a client accurately reporting its previous page.

## Evidence and references

[Original archived challenge](../../unsolved/web-exploitation-natas/010-trust-the-referer/README.md)

- [Sanitized live verification ledger](../evidence/ready-natas/natas-verification-redacted.json)

**Provenance:** Rewritten from saved level-specific investigation and the 2026-10-28 live-authentication ledger. The screenshot pass independently repeated the intended level-specific requests and authentication; runtime passwords were redacted before terminal display and logging.
