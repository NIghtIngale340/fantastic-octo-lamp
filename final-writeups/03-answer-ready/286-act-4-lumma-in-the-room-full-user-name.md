# ACT 4 - LUMMA IN THE ROOM: Full User Name

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 286 |
| Category | Network Forensics |
| Points | 175 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Resolve the Lumma account to a full user name.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/286-act-4-lumma-in-the-room-full-user-name/README.md). The supplied evidence is `2026-01-31-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

The directory response that confirms the account also contains the full name. That paired mapping is stronger than guessing a name from the account abbreviation.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `f755444d0b6eac847e07b73dea0774084b232d8577f536547a12f39b959d7833`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
samr.samr_UserInfo21.full_name
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/files/2026-01-31-traffic-analysis-exercise.pcap \
  -Y '(samr.samr_UserInfo21.full_name) && frame.number in {358}' \
  -T fields -E header=y -e frame.number -e samr.samr_UserInfo21.account_name -e samr.samr_UserInfo21.full_name
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	samr.samr_UserInfo21.account_name	samr.samr_UserInfo21.full_name
358	gwyatt	Gabriel Wyatt
```

### 2. Interpret the result

SAMR frame 358 contains account_name=gwyatt and full_name=Gabriel Wyatt. The raw name has a space. The challenge does not specify that it should be replaced with an underscore.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #286 — offline packet evidence

![286-decisive-evidence.png](../screenshots/286-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/files/2026-01-31-traffic-analysis-exercise.pcap -Y '(samr.samr_UserInfo21.full_name) && frame.number in {358}' -T fields -E header=y -e frame.number -e samr.samr_UserInfo21.account_name -e samr.samr_UserInfo21.full_name
```

[Actual command transcript](../screenshots/capture-work/286-network.terminal.log) · [Execution record](../screenshots/capture-work/286-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{Gabriel Wyatt}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

Preserve literal directory values, then describe any unverified answer normalization separately. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/286-act-4-lumma-in-the-room-full-user-name/README.md)
- [Actual TShark field output](../evidence/network/286-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/286-act-4-lumma-in-the-room-full-user-name/solution.md)
