# Command Me

| Field | Details |
|---|---|
| Platform | OverTheWire Natas, mirrored by PCGCTF |
| Challenge ID | 16 |
| Technical category | Web Exploitation - Natas |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Exploit unquoted shell input to read natas10’s password file. |
| Result | Recovered next-level password — intentionally redacted in this publication draft. |

**Verified on OverTheWire** from the saved live-authentication record; PCGCTF acceptance remains unconfirmed.

## Reading the clues

The search feature is implemented by passing user input into a shell command. The source makes the dangerous boundary visible: a value intended to be a grep pattern can instead become shell syntax because it is inserted unquoted.

## Working through the evidence

Commands below reproduce the recorded training procedure; the screenshot pass independently replayed the level-specific method and next-level authentication. `curl --user natasN` prompts for the current level password rather than putting it in shell history. `-sS` hides the progress meter while retaining errors. The output excerpts are redacted from the saved investigation; the redaction is not part of the server response.

### 1. Inspect the command construction

```sh
curl -sS --user natas9 http://natas9.natas.labs.overthewire.org/index-source.html
```

The relevant recorded line is:

```php
passthru("grep -i $key dictionary.txt");
```

`grep -i` searches without case sensitivity. Its legitimate role does not make the surrounding string safe: the shell parses the entire constructed command before grep receives its arguments.

### 2. Terminate grep and read the training credential file

```sh
curl -sS --user natas9 --data-urlencode 'needle=;cat /etc/natas_webpass/natas10 #' -d 'submit=Search' http://natas9.natas.labs.overthewire.org/
```

The semicolon starts a second command. `cat` reads the next level's password file, and the trailing `#` comments out the original `dictionary.txt` suffix. Form URL-encoding preserves spaces and the hash as data in the request. Those characters must reach the server's form parser rather than be interpreted by the local shell.

The saved HTML output contains a `<pre>` block holding the credential; the actual password is redacted in this draft. The attack does not require executing a downloaded file or changing the lab's state.

### 3. Validate the extracted credential

The saved next-host authentication to `natas10` returned **200**. That result verifies the content read by the injected command, not merely whether a shell metacharacter was accepted.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #16 — actual evidence capture

![016-natas-method.png](../screenshots/016-natas-method.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 16 method
```

[Actual command transcript](../screenshots/capture-work/016-natas-method.terminal.log) · [Execution record](../screenshots/capture-work/016-natas-method.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #16 — actual evidence capture

![016-natas-verify.png](../screenshots/016-natas-verify.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 16 verify
```

[Actual command transcript](../screenshots/capture-work/016-natas-verify.terminal.log) · [Execution record](../screenshots/capture-work/016-natas-verify.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved verification at **2026-10-28T22:37:26+08:00** authenticated to **natas10** at `http://natas10.natas.labs.overthewire.org/` and returned **HTTP 200**. Its response SHA-256 is `4a72d3f22c14f9c0adad0a21aa8d7bca745eddd590fec8089c9af8e950b5eb89`. This is a recorded independent OverTheWire check, the earlier authentication record; the screenshot pass also made a fresh successful authentication, documented below.

The demonstration uses the level-specific host and username. Keep the recovered password in a private working copy; the PCGCTF candidate wraps that exact recovered value as `pcgCTF{<RECOVERED_NEXT_LEVEL_PASSWORD>}`. Neither that wrapper nor the PCGCTF solved state was independently confirmed. Redact the password from any browser or terminal capture before publishing it.

## What this challenge taught me

The failure is a trust-boundary error between data and shell syntax. Calling a search API directly, or passing fixed argument arrays without a shell, removes the parsing opportunity that this payload exploits.

## Evidence and references

[Original archived challenge](../../unsolved/web-exploitation-natas/016-command-me/README.md)

- [Sanitized live verification ledger](../evidence/ready-natas/natas-verification-redacted.json)

**Provenance:** Rewritten from saved level-specific investigation and the 2026-10-28 live-authentication ledger. The screenshot pass independently repeated the intended level-specific requests and authentication; runtime passwords were redacted before terminal display and logging.
