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
