# Terminal command review — where the screenshots look staged

You asked whether the terminal screenshots are alright or whether we used
commands that are too complex. Short answer: the screenshots are *real*, but in
a number of challenges the command on screen is more elaborate than anyone would
actually type to solve the problem. That contrived look is part of what makes
the writeups read as machine-generated.

Per your call, I did **not** re-run anything or regenerate screenshots. This
file just flags the cases, so you can re-shoot them later if you want. The prose
in the rewritten writeups uses the simpler, natural command; the existing
screenshots still show the original one.

## Legend

- **Flagged** — the on-screen command is needlessly complex for the task.
- **Fine** — the command is the normal tool for the job; left alone.

## Flagged commands

| ID | Challenge | What's on screen | Simpler / natural version |
|---:|---|---|---|
| 1 | Hash Me If You Can | `python -c "...print('Hex length:',len(h))..."` just to show the digest is 40 chars | State it: 40 hex chars = 20 bytes = SHA-1 shape. No command needed. |
| 34 | ROT13 | `python` heredoc using `codecs.decode(...,'rot_13')` **plus an `assert` reversibility check** | `echo 'synt vf pbby' \| tr 'A-Za-z' 'N-ZA-Mn-za-m'` |
| 6–17 | Natas set (OverTheWire) | `python .../natas_evidence.py 6 method` wrapper script | The real `curl -sS --user natasN http://natasN...` — which the writeup already shows. The wrapper hides the actual command. |

## Fine (left as-is)

- **Easy Packet set (#82–112):** the `tshark -n -r ... -Y 'frame.number==1' -T fields -e ...`
  commands are the standard way to pull a single field out of a capture. Not
  flagged — though the long inline flag explanations in the prose were trimmed.
- **OSINT / IMINT (#240 etc.):** these "commands" are really just file paths or
  "open this URL." Harmless, reworded as plain steps.

_More entries appended as the rewrite proceeds._

## Additional findings (full pass)

After rewriting all 192, here's the complete picture of staged/over-complex terminal commands in the screenshots:

| IDs | Challenge(s) | On screen | Natural version |
|---|---|---|---|
| 1, 71 | Hash Me, Embedded Text | `python .../dictionary_evidence.py N` wrapper around John | just run `john --format=... --wordlist=rockyou hash` directly |
| 6–17 | Natas set | `python .../natas_evidence.py N method/verify` | the real `curl` (already shown in the prose) |
| 34 | ROT13 | `codecs.decode(...,'rot_13')` + `assert` | `tr 'A-Za-z' 'N-ZA-Mn-za-m'` |
| 1 | Hash Me | `python -c "...len(h)..."` to show length | state "40 hex = SHA-1" |
| 262–296 | Act 1–5 packets | `tshark ... -Y 'frame.number in {11227,11714}'` with hard-coded frame numbers | a plain field filter; the exact frame list looks reverse-engineered from the answer |
| 298, 300, 302, 306 | OSINT pivots | `python -m json.tool <local-file>` / `head <local-file>` purely to make a terminal screenshot of a saved JSON | these are fine as evidence, but the screenshot is of reading a local file, not doing the lookup — worth labeling as such |
| 309, 018 | Info Leaks, Rotation 36 | `python .../NNN-capture-1.py` wrapper scripts | inline the actual decode |

### The bigger pattern

Most screenshots are **real output**, but a lot of them run a *wrapper script* or a deliberately elaborate one-liner instead of the obvious command. That's the single thing that most makes the terminal shots read as "generated for a report" rather than "what someone typed while solving." The rewritten prose now shows the natural command in each case; if you ever re-shoot the screenshots, match them to the prose and this whole tell disappears.

### What's genuinely fine

- The **Easy Packet** `tshark -nr ... -T fields -e <field>` shots — that's just how you read a field.
- The **Deadface SQL** queries — real queries, real results.
- The **RSA/crypto** Python (cube root, common modulus, LFSR+AES) — these legitimately need code.
