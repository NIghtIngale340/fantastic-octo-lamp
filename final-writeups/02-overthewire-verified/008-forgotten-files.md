# Forgotten Files

| Field | Details |
|---|---|
| Platform | OverTheWire Natas, mirrored by PCGCTF |
| Challenge ID | 8 |
| Technical category | Web Exploitation - Natas |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Follow an exposed asset directory to natas3’s credential. |
| Result | Recovered next-level password — intentionally redacted in this publication draft. |

**Verified on OverTheWire** from the saved live-authentication record; PCGCTF acceptance remains unconfirmed.

## Reading the clues

The page refers to a small image under `files/`. That is a useful path clue rather than an invitation to guess arbitrary filenames. If the web server lists the directory, the asset path can reveal unrelated files stored beside the image.

## Working through the evidence

Commands below reproduce the recorded training procedure; the screenshot pass independently replayed the level-specific method and next-level authentication. `curl --user natasN` prompts for the current level password rather than putting it in shell history. `-sS` hides the progress meter while retaining errors. The output excerpts are redacted from the saved investigation; the redaction is not part of the server response.

### 1. Follow the page’s asset path to its parent directory

```sh
curl -sS --user natas2 http://natas2.natas.labs.overthewire.org/files/
```

A trailing slash requests the directory, not the image. The saved response contains a directory index with `users.txt`:

```html
<h1>Index of /files</h1>
<a href="users.txt">users.txt</a>
```

These are relevant excerpts rather than a complete transcript. Their value is that the server itself reveals the next filename; no wordlist enumeration is needed.

### 2. Read the disclosed file and choose the right account

```sh
curl -sS --user natas2 http://natas2.natas.labs.overthewire.org/files/users.txt
```

The file contains several colon-separated account entries. The investigation records the `natas3` entry as:

```text
natas3:[REDACTED_LEVEL_PASSWORD]
```

The other sample users are irrelevant and are omitted here. A colon separates the username from its password; the whole line should not be pasted into a password field.

### 3. Verify the extracted credential

Authenticate to `http://natas3.natas.labs.overthewire.org/` as `natas3` using the recovered value. The saved verification produced HTTP **200**. That check ties the directory-leaked text to a working next-level credential.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #8 — actual evidence capture

![008-natas-method.png](../screenshots/008-natas-method.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 8 method
```

[Actual command transcript](../screenshots/capture-work/008-natas-method.terminal.log) · [Execution record](../screenshots/capture-work/008-natas-method.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #8 — actual evidence capture

![008-natas-verify.png](../screenshots/008-natas-verify.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 8 verify
```

[Actual command transcript](../screenshots/capture-work/008-natas-verify.terminal.log) · [Execution record](../screenshots/capture-work/008-natas-verify.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved verification at **2026-10-28T22:37:26+08:00** authenticated to **natas3** at `http://natas3.natas.labs.overthewire.org/` and returned **HTTP 200**. Its response SHA-256 is `1f756fa9f80ae7d93ef30a99d3a55759de68eca872fb510384b47a41088c8eaa`. This is a recorded independent OverTheWire check, the earlier authentication record; the screenshot pass also made a fresh successful authentication, documented below.

The demonstration uses the level-specific host and username. Keep the recovered password in a private working copy; the PCGCTF candidate wraps that exact recovered value as `pcgCTF{<RECOVERED_NEXT_LEVEL_PASSWORD>}`. Neither that wrapper nor the PCGCTF solved state was independently confirmed. Redact the password from any browser or terminal capture before publishing it.

## What this challenge taught me

An ordinary resource path can expose the layout of a deployment. Directory indexing becomes a disclosure problem when sensitive files are placed beside public assets.

## Evidence and references

[Original archived challenge](../../unsolved/web-exploitation-natas/008-forgotten-files/README.md)

- [Sanitized live verification ledger](../evidence/ready-natas/natas-verification-redacted.json)

**Provenance:** Rewritten from saved level-specific investigation and the 2026-10-28 live-authentication ledger. The screenshot pass independently repeated the intended level-specific requests and authentication; runtime passwords were redacted before terminal display and logging.
