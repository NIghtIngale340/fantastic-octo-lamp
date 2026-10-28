# The Exposed Script

| Field | Details |
|---|---|
| Platform | OverTheWire Natas, mirrored by PCGCTF |
| Challenge ID | 13 |
| Technical category | Web Exploitation - Natas |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Read an exposed include file, submit its secret and obtain natas7’s credential. |
| Result | Recovered next-level password — intentionally redacted in this publication draft. |

**Verified on OverTheWire** from the saved live-authentication record; PCGCTF acceptance remains unconfirmed.

## Reading the clues

The source-view route makes the server-side comparison visible. It includes a file from `includes/secret.inc`, so the next question is whether that file is protected from direct HTTP access. An include suffix can be served as text if it is not mapped to the PHP interpreter.

## Working through the evidence

Commands below reproduce the recorded training procedure; the screenshot pass independently replayed the level-specific method and next-level authentication. `curl --user natasN` prompts for the current level password rather than putting it in shell history. `-sS` hides the progress meter while retaining errors. The output excerpts are redacted from the saved investigation; the redaction is not part of the server response.

### 1. Identify the include from the source view

```sh
curl -sS --user natas6 http://natas6.natas.labs.overthewire.org/index-source.html
```

The important source statement is the include of `includes/secret.inc`. It identifies the file supplying the comparison secret, rather than leaving us to brute-force the form.

### 2. Request that exact file

```sh
curl -sS --user natas6 http://natas6.natas.labs.overthewire.org/includes/secret.inc
```

The saved response exposes PHP text containing a `$secret` assignment. In a public capture, redact the assignment's value; its role is to satisfy this level's form, not to serve as the next level's login password. Direct disclosure is the evidence that the include was accessible as source.

### 3. Submit the observed secret

```sh
curl -sS --user natas6 --data-urlencode 'secret=<VALUE_FROM_SECRET_INC>' -d 'submit=Submit' http://natas6.natas.labs.overthewire.org/index.php
```

Replace the bracketed placeholder locally with the actual observed value. `--data-urlencode` encodes the form field correctly; `-d` supplies the submit field and makes this a POST. The saved successful response begins `Access granted` and reveals the password for `natas7`, omitted here.

### 4. Confirm the next-level login

The authentication ledger records HTTP **200** for `natas7`, confirming the disclosed password without needing to publish it.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #13 — actual evidence capture

![013-natas-method.png](../screenshots/013-natas-method.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 13 method
```

[Actual command transcript](../screenshots/capture-work/013-natas-method.terminal.log) · [Execution record](../screenshots/capture-work/013-natas-method.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #13 — actual evidence capture

![013-natas-verify.png](../screenshots/013-natas-verify.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 13 verify
```

[Actual command transcript](../screenshots/capture-work/013-natas-verify.terminal.log) · [Execution record](../screenshots/capture-work/013-natas-verify.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved verification at **2026-10-28T22:37:26+08:00** authenticated to **natas7** at `http://natas7.natas.labs.overthewire.org/` and returned **HTTP 200**. Its response SHA-256 is `5a2622b73e2246c9bc621141da384be168589ff5b20ed88b08aa0a4f939b9ad8`. This is a recorded independent OverTheWire check, the earlier authentication record; the screenshot pass also made a fresh successful authentication, documented below.

The demonstration uses the level-specific host and username. Keep the recovered password in a private working copy; the PCGCTF candidate wraps that exact recovered value as `pcgCTF{<RECOVERED_NEXT_LEVEL_PASSWORD>}`. Neither that wrapper nor the PCGCTF solved state was independently confirmed. Redact the password from any browser or terminal capture before publishing it.

## What this challenge taught me

Source disclosure can occur through an auxiliary file even when the main script is interpreted correctly. Keeping secrets outside the public document tree avoids relying on filename extensions for confidentiality.

## Evidence and references

[Original archived challenge](../../unsolved/web-exploitation-natas/013-the-exposed-script/README.md)

- [Sanitized live verification ledger](../evidence/ready-natas/natas-verification-redacted.json)

**Provenance:** Rewritten from saved level-specific investigation and the 2026-10-28 live-authentication ledger. The screenshot pass independently repeated the intended level-specific requests and authentication; runtime passwords were redacted before terminal display and logging.
