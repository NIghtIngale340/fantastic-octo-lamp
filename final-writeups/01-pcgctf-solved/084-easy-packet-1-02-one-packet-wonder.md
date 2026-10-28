# EASY PACKET 1 #02  One Packet Wonder

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 84 |
| Category | Network Forensics |
| Points | 100 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. |

## Challenge and objective

Count the packets in the capture.

The original description and prerequisite chain are preserved in [the challenge README](../../solved/network-forensics/084-easy-packet-1-02-one-packet-wonder/README.md). The supplied evidence is `EASY_PACKET_1.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

A packet count should come from the capture records, not from a guessed frame number. A display filter can hide packets, so I first used an unfiltered file-level count.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `e4735559a704fcd56ac790602e875a713f94a665af16ecd3ad49ea40ff394faa`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Count capture records without an HTTP filter

```sh
capinfos -t -c /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap
```

`-c` asks `capinfos` for the packet count; `-t` also confirms which capture container it parsed. These flags inspect the file instead of counting a filtered GUI view.

Recorded output:

```text
File name:           /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap
File type:           Wireshark/tcpdump/... - pcap
Number of packets:   1
```

### 2. Confirm the single frame can be decoded

capinfos reports exactly one packet. The focused TShark read then shows frame 1, which is consistent with that count. This prevents accidentally counting only the packets that happen to match an HTTP filter.

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap \
  -Y 'frame.number == 1' \
  -T fields -E header=y -e frame.number
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. `frame.number == 1` is appropriate because the independent capture count is one; it is not being used to prove that count.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number
1
```

### 3. Interpret the result

The requested count is 1. The capture file includes a global header and one per-packet record; neither header creates an additional network packet.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #84 — offline packet evidence

![084-decisive-evidence.png](../screenshots/084-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap -Y 'frame.number == 1' -T fields -E header=y -e frame.number
```

[Actual command transcript](../screenshots/capture-work/084-network.terminal.log) · [Execution record](../screenshots/capture-work/084-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{1}
```

Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The solved snapshot confirms challenge completion, not an independently captured acceptance response for this exact text.

## Conclusion and lesson

Count before filtering. This is especially important when a much larger capture has only one matching HTTP request. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../solved/network-forensics/084-easy-packet-1-02-one-packet-wonder/README.md)
- [Actual TShark field output](../evidence/network/084-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../solved/network-forensics/084-easy-packet-1-02-one-packet-wonder/solution.md)
