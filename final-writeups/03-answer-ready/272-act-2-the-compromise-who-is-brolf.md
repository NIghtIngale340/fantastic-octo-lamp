# ACT 2 - THE COMPROMISE: Who Is brolf?

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 272 |
| Category | Network Forensics |
| Points | 125 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Resolve the known account brolf to its full name.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/272-act-2-the-compromise-who-is-brolf/README.md). The supplied evidence is `2026-02-28-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

The challenge already supplies the username. A directory lookup response can answer the full-name question directly without guessing how the abbreviated account was formed.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `3dc470f5490ec15b4024c513e87c67e0b17caeae2a2ce3d83541be24ef407e61`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
samr.samr_UserInfo21.account_name == "brolf"
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap \
  -Y '(samr.samr_UserInfo21.account_name == "brolf") && frame.number in {339}' -d tcp.port==443,http \
  -T fields -E header=y -e frame.number -e samr.samr_UserInfo21.account_name -e samr.samr_UserInfo21.full_name
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above. `-d tcp.port==443,http` tells the dissector to treat that port as HTTP for this known capture. It changes the decoding choice, not the underlying bytes, and does not mean all port-443 traffic is HTTP.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	samr.samr_UserInfo21.account_name	samr.samr_UserInfo21.full_name
339	brolf	Becka Rolf
```

### 2. Interpret the result

SAMR UserInfo21 in frame 339 contains account_name=brolf and full_name=Becka Rolf in the same response. Keeping those paired fields is stronger than matching only the initials of a name.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #272 — offline packet evidence

![272-decisive-evidence.png](../screenshots/272-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap -Y '(samr.samr_UserInfo21.account_name == "brolf") && frame.number in {339}' -d tcp.port==443,http -T fields -E header=y -e frame.number -e samr.samr_UserInfo21.account_name -e samr.samr_UserInfo21.full_name
```

[Actual command transcript](../screenshots/capture-work/272-network.terminal.log) · [Execution record](../screenshots/capture-work/272-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{Becka Rolf}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

Prefer an explicit account-to-display-name mapping over an inferred expansion of a username. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/272-act-2-the-compromise-who-is-brolf/README.md)
- [Actual TShark field output](../evidence/network/272-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/272-act-2-the-compromise-who-is-brolf/solution.md)
