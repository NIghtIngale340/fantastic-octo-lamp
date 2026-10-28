# SEQUENCE

| Field | Details |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 79 |
| Technical category | Cryptography / Encoding |
| Points in saved inventory | 150 |
| Difficulty | Not stated in the saved challenge description |
| Objective | Recover the two-word message selected by a mathematical sequence. |
| Result | `pcgCTF{FLAG LANGUAGE}` |

**Needs Flag Verification:** the answer is supported by the evidence described below, but its exact submission has not been confirmed accepted by PCGCTF.

## Reading the clues

Leonardo Bonacci and the phone-like sequence 011235813213455 point toward Fibonacci. The text also says to start the maths again at the JSON section; using only the prose acrostic recovers an incomplete result.

## Working through the evidence

### 1. Recover the first word

Read sentence initials before the JSON: **F L A S G W**. Select one-based Fibonacci positions 1, 2, 3, 5 without repeating position 1. Their initials are **FLAG**, exactly the first word promised by the question.

### 2. Restart on JSON keys in source order

The last sentence before the block explicitly cues a restart. Enumerate every JSON key as it appears in the text, including nested keys; a parser’s postorder traversal would change that order.

```python
import re
from pathlib import Path
text = Path('/home/nightingale/CTF/PCGCTF/unsolved/cryptography-encoding/079-sequence/files/sequence.txt').read_text()
json_text = text[text.index('{'):text.rindex('}') + 1]
keys = re.findall(r'^\s*"([^"\n]+)"\s*:', json_text, re.M)
positions = [1, 2, 3, 5, 8, 13, 21, 34]
print(''.join(keys[i-1][0] for i in positions))
```

`re.M` allows the key pattern to match line starts within the block. `i-1` converts the document’s one-based positions to Python’s zero-based indexes. The selected keys are Location, Accept, No-cache, Gui, User-agent, Alt-svc, Gateway and Expires. Their initials spell **LANGUAGE**.

### 3. Combine the actual recovered words

The message is **FLAG LANGUAGE**, not FLAG FIBONACCI. Fibonacci names the mechanism; it is not the hidden second word. The exact positions and original SHA256 are preserved in the extraction JSON. The candidate retains the space because the task explicitly asks for the complete two-word message.

### Reproduction inputs and preserved output

Use the original artifact links below to replace any angle-bracketed input path. Those placeholders select local files; they are not missing exploit parameters. Commands in this draft explain a recorded method and should be checked against the preserved hashes before rerunning. The linked original investigation retains additional tool output and exact filenames; where a result is reported above, its verification record is linked rather than invented as a terminal screenshot.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #79 — actual offline reproduction

![079-decisive-result.png](../screenshots/079-decisive-result.png)

Run the exact independently checked decoder/check.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/079-reproduce.py
```

[Actual command transcript](../screenshots/capture-work/079-decode.terminal.log) · [Execution record](../screenshots/capture-work/079-decode.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

### Challenge #79 — actual evidence capture

![079-script-1.png](../screenshots/079-script-1.png)

Run the documented self-contained decoder/calculation on original inputs.

Command/action actually executed:

```sh
python /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/079-capture-1.py
```

[Actual command transcript](../screenshots/capture-work/079-script-1.terminal.log) · [Execution record](../screenshots/capture-work/079-script-1.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and final verification

The saved submission candidate is **`pcgCTF{FLAG LANGUAGE}`**. Both words are directly extracted; exact whitespace normalization and acceptance are untested.

The remaining platform check is to open the specific PCGCTF challenge, copy the documented payload with its exact capitalization, spaces and punctuation, and capture the real acceptance or rejection response. No successful submission is inferred from the existence of the answer. If rejected, record the response and compare the stated format before changing the evidence-backed payload.

## What this challenge taught me

Restart cues and lexical order can matter as much as identifying the sequence. Recover the message rather than substituting the mechanism’s name.

## Evidence and references

[Original archived challenge](../../unsolved/cryptography-encoding/079-sequence/README.md)

- [Decisive preserved verification results](../../analysis-team-verification/sequence-extraction.json)
- [Original text document](../../unsolved/cryptography-encoding/079-sequence/files/sequence.txt)
- [Preserved investigation notes](../../unsolved/cryptography-encoding/079-sequence/solution.md)

**Provenance:** Original local artifacts and preserved independent extraction/source verification; drafted without claiming new live attacks or fabricated executions.
