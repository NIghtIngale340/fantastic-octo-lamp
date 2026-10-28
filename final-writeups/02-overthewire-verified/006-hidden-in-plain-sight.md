# Hidden in Plain Sight

| Field | Details |
|---|---|
| Platform | OverTheWire Natas, mirrored by PCGCTF |
| Challenge ID | 6 |
| Technical category | Web Exploitation - Natas |
| Points in saved inventory | 100 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Inspect HTML source to recover the credential for natas1. |
| Result | Recovered next-level password — intentionally redacted in this publication draft. |

**Verified on OverTheWire** from the saved live-authentication record; PCGCTF acceptance remains unconfirmed.

## Reading the clues

The page need not visibly display a secret for the browser to receive it. The description suggests Ctrl+U, so the first useful distinction is rendered content versus the HTML delivered over HTTP. An HTML comment is hidden by rendering, but it is still client-side data.

## Working through the evidence

Commands below reproduce the recorded training procedure; the screenshot pass independently replayed the level-specific method and next-level authentication. `curl --user natasN` prompts for the current level password rather than putting it in shell history. `-sS` hides the progress meter while retaining errors. The output excerpts are redacted from the saved investigation; the redaction is not part of the server response.

### 1. Read the source instead of only the rendered page

```sh
curl -sS --user natas0 http://natas0.natas.labs.overthewire.org/
```

Use the public starting password `natas0` at the prompt. The target is the level-zero training host, not the PCGCTF login. A browser's View Source command retrieves the same clue without needing a proxy.

The recorded decisive source excerpt is:

```html
<!--The password for natas1 is [REDACTED_LEVEL_PASSWORD] -->
```

The comment names the next account, which is important: its content is a password for `natas1`, not a replacement for the `natas0` username. Copy only the value between “is” and the comment terminator; do not include spaces or `-->`.

### 2. Check the recovered value against the next level

```sh
curl -sS --user natas1 -o /dev/null -w '%{http_code}\n' http://natas1.natas.labs.overthewire.org/
```

`-o /dev/null` discards the HTML and `-w` prints the HTTP code. The saved verification returned **200**, establishing that the recovered value authenticated to the next host. This is stronger than merely finding a plausible-looking token in a comment.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #6 — actual evidence capture

![006-natas-method.png](../screenshots/006-natas-method.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 6 method
```

[Actual command transcript](../screenshots/capture-work/006-natas-method.terminal.log) · [Execution record](../screenshots/capture-work/006-natas-method.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #6 — actual evidence capture

![006-natas-verify.png](../screenshots/006-natas-verify.png)

Actual authenticated request to the named authorized Natas training level; passwords redacted before terminal display.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/natas_evidence.py 6 verify
```

[Actual command transcript](../screenshots/capture-work/006-natas-verify.terminal.log) · [Execution record](../screenshots/capture-work/006-natas-verify.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved verification at **2026-10-28T22:37:26+08:00** authenticated to **natas1** at `http://natas1.natas.labs.overthewire.org/` and returned **HTTP 200**. Its response SHA-256 is `cdf0a3d3f99f80b89b93ff0a965323a6ca8e690087c69a29c2cbfb8ff347131b`. This is a recorded independent OverTheWire check, the earlier authentication record; the screenshot pass also made a fresh successful authentication, documented below.

The demonstration uses the level-specific host and username. Keep the recovered password in a private working copy; the PCGCTF candidate wraps that exact recovered value as `pcgCTF{<RECOVERED_NEXT_LEVEL_PASSWORD>}`. Neither that wrapper nor the PCGCTF solved state was independently confirmed. Redact the password from any browser or terminal capture before publishing it.

## What this challenge taught me

A browser hiding an HTML comment does not protect its contents. If a secret has been sent to an unauthenticated or low-privilege client, presentation choices cannot restore its confidentiality.

## Evidence and references

[Original archived challenge](../../unsolved/web-exploitation-natas/006-hidden-in-plain-sight/README.md)

- [Sanitized live verification ledger](../evidence/ready-natas/natas-verification-redacted.json)

**Provenance:** Rewritten from saved level-specific investigation and the 2026-10-28 live-authentication ledger. The screenshot pass independently repeated the intended level-specific requests and authentication; runtime passwords were redacted before terminal display and logging.
