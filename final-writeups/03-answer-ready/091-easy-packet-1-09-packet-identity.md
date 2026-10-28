# EASY PACKET 1 #09  Packet Identity

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 91 |
| Category | Network Forensics |
| Points | 100 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Recover the IPv4 identification value.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/091-easy-packet-1-09-packet-identity/README.md). The supplied evidence is `EASY_PACKET_1.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

The IP identification field supports IPv4 fragment association. It is an identifier, so a hexadecimal display and a decimal display can represent exactly the same 16-bit value.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `e4735559a704fcd56ac790602e875a713f94a665af16ecd3ad49ea40ff394faa`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Select the field at the correct protocol layer

Wireshark renders ip.id as 0xbed2. Converting hexadecimal bed2 to decimal produces 48850. The capture evidence does not change when the display base changes.

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap \
  -Y 'frame.number == 1' \
  -T fields -E header=y -e frame.number -e ip.id
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. `frame.number == 1` is appropriate because the independent capture count is one; it is not being used to prove that count.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	ip.id
1	0xbed2
```

### 2. Interpret the result

The candidate uses 48850 because Garcia explicitly reports the decimal form as accepted. We do not mistake that formatting correction for discovery of another packet.

### Verify the numeric representation

```sh
python -c "print(int('bed2', 16))"
```

This conversion maps the recorded hexadecimal value to decimal `48850`; it is deterministic arithmetic, not another packet observation. The `16` selects hexadecimal input. The accepted-format report uses decimal, so a base change is sufficient and no byte order reversal is appropriate.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #91 — offline packet evidence

![091-decisive-evidence.png](../screenshots/091-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap -Y 'frame.number == 1' -T fields -E header=y -e frame.number -e ip.id
```

[Actual command transcript](../screenshots/capture-work/091-network.terminal.log) · [Execution record](../screenshots/capture-work/091-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{48850}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. Garcia’s Day 1 document explicitly reports this submission spelling accepted; it was not independently retested in our account. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

Normalize numerical representation deliberately. Record both bases when an exact-string answer could depend on how a tool displays the value. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/091-easy-packet-1-09-packet-identity/README.md)
- [Actual TShark field output](../evidence/network/091-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/091-easy-packet-1-09-packet-identity/solution.md)

- [Garcia Day 1 report — attributed formatting/acceptance evidence](../../team-writeups/garcia-day1/source.md)
