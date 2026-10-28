# ACT 4 - LUMMA IN THE ROOM: Lumma Victim

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 282 |
| Category | Network Forensics |
| Points | 125 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Identify the client sending Lumma victim-fingerprinting requests.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/README.md). The supplied evidence is `2026-01-31-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

The alert provides a remote IOC, 153.92.1.49. I pivoted on outbound HTTP to it and checked which internal source made the fingerprinting requests.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `f755444d0b6eac847e07b73dea0774084b232d8577f536547a12f39b959d7833`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
ip.dst == 153.92.1.49 && http.request
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/files/2026-01-31-traffic-analysis-exercise.pcap \
  -Y '(ip.dst == 153.92.1.49 && http.request) && frame.number in {24500, 25270}' \
  -T fields -E header=y -e frame.number -e ip.src -e ip.dst -e http.host -e http.request.uri
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	ip.src	ip.dst	http.host	http.request.uri
24500	10.1.21.58	153.92.1.49	whitepepper.su	/api/set_agent?id=3BF67EC05320C5729578BE4C0ADF174C&token=842e2802df0f0a06b4ed51f12f4387e761523b&description=&agent=Chrome
25270	10.1.21.58	153.92.1.49	whitepepper.su	/api/set_agent?id=3BF67EC05320C5729578BE4C0ADF174C&token=842e2802df0f0a06b4ed51f12f4387e761523b&description=&agent=Edge
```

### 2. Interpret the result

Frames 24500 and 25270 originate from 10.1.21.58 and use Host whitepepper.su. Their /api/set_agent queries identify Chrome and Edge respectively, demonstrating two requests from the same endpoint rather than two victims.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #282 — offline packet evidence

![282-decisive-evidence.png](../screenshots/282-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/files/2026-01-31-traffic-analysis-exercise.pcap -Y '(ip.dst == 153.92.1.49 && http.request) && frame.number in {24500, 25270}' -T fields -E header=y -e frame.number -e ip.src -e ip.dst -e http.host -e http.request.uri
```

[Actual command transcript](../screenshots/capture-work/282-network.terminal.log) · [Execution record](../screenshots/capture-work/282-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{10.1.21.58}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

A browser or agent parameter is an attribute of a request, not automatically a distinct infected machine. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/README.md)
- [Actual TShark field output](../evidence/network/282-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/solution.md)
