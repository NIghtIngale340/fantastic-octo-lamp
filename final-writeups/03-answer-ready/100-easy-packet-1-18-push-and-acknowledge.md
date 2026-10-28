# EASY PACKET 1 #18  Push and Acknowledge

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 100 |
| Category | Network Forensics |
| Points | 100 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Identify the TCP control flags set on the packet.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/100-easy-packet-1-18-push-and-acknowledge/README.md). The supplied evidence is `EASY_PACKET_1.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

Flags are a bit mask; a hexadecimal mask can contain more than one asserted control bit. I inspected both the combined mask and individual bits.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `e4735559a704fcd56ac790602e875a713f94a665af16ecd3ad49ea40ff394faa`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Select the field at the correct protocol layer

The mask is 0x0018: PSH is 0x08 and ACK is 0x10. Both tcp.flags.push and tcp.flags.ack are 1. Their bitwise combination explains the displayed mask.

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap \
  -Y 'frame.number == 1' \
  -T fields -E header=y -e frame.number -e tcp.flags -e tcp.flags.push -e tcp.flags.ack
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. `frame.number == 1` is appropriate because the independent capture count is one; it is not being used to prove that count.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	tcp.flags	tcp.flags.push	tcp.flags.ack
1	0x0018	True	True
```

### 2. Interpret the result

Garcia reports PSH and ACK as the accepted phrase. Commas or underscores are formatting alternatives, not different TCP behavior, but they were not the reported accepted text.

The mask decomposes as `0x0018 = 0x0010 | 0x0008`. ACK acknowledges the peer’s byte stream; PSH requests prompt forwarding of data toward the receiving application. Neither bit means that the request is encrypted. The [TCP specification](https://www.rfc-editor.org/rfc/rfc9293.html) explains the flags and PUSH semantics.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #100 — offline packet evidence

![100-decisive-evidence.png](../screenshots/100-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap -Y 'frame.number == 1' -T fields -E header=y -e frame.number -e tcp.flags -e tcp.flags.push -e tcp.flags.ack
```

[Actual command transcript](../screenshots/capture-work/100-network.terminal.log) · [Execution record](../screenshots/capture-work/100-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{PSH and ACK}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. Garcia’s Day 1 document explicitly reports this submission spelling accepted; it was not independently retested in our account. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

Decode the bit mask before choosing words. Treat answer punctuation as a separate verification task. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/100-easy-packet-1-18-push-and-acknowledge/README.md)
- [Actual TShark field output](../evidence/network/100-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/100-easy-packet-1-18-push-and-acknowledge/solution.md)

- [Garcia Day 1 report — attributed formatting/acceptance evidence](../../team-writeups/garcia-day1/source.md)
