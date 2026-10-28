# EASY PACKET 1 #17  TCP Acknowledgment Marker

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 99 |
| Category | Network Forensics |
| Points | 100 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. |

## Challenge and objective

Recover the packet’s TCP acknowledgment number.

The original description and prerequisite chain are preserved in [the challenge README](../../solved/network-forensics/099-easy-packet-1-17-tcp-acknowledgment-marker/README.md). The supplied evidence is `EASY_PACKET_1.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

An acknowledgment number is the next byte expected from the peer, when ACK is set. It is not the same as this segment’s own sequence number.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `e4735559a704fcd56ac790602e875a713f94a665af16ecd3ad49ea40ff394faa`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Select the field at the correct protocol layer

tcp.ack_raw is 1790813139. Selecting the raw field avoids any relative-number presentation used by Wireshark.

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap \
  -Y 'frame.number == 1' \
  -T fields -E header=y -e frame.number -e tcp.ack_raw
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. `frame.number == 1` is appropriate because the independent capture count is one; it is not being used to prove that count. The selected `tcp.seq_raw`/`tcp.ack_raw` field is the on-wire value, avoiding relative sequence presentation.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	tcp.ack_raw
1	1790813139
```

### 2. Interpret the result

The answer is 1790813139. The acknowledgment value belongs with the ACK flag that is set in the same TCP header.

The request does not include a full TCP handshake, so relative sequence displays are a presentation convenience rather than new evidence. For a GUI screenshot, expand the TCP tree and show the raw number explicitly. [Wireshark’s TCP analysis guide](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvTCPAnalysis.html) distinguishes analyzer calculations from the underlying sequence state.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #99 — offline packet evidence

![099-decisive-evidence.png](../screenshots/099-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/082-easy-packet-1-the-exposed-request/files/EASY_PACKET_1.pcap -Y 'frame.number == 1' -T fields -E header=y -e frame.number -e tcp.ack_raw
```

[Actual command transcript](../screenshots/capture-work/099-network.terminal.log) · [Execution record](../screenshots/capture-work/099-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{1790813139}
```

Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The solved snapshot confirms challenge completion, not an independently captured acceptance response for this exact text.

## Conclusion and lesson

Separate the two sequence spaces of a TCP connection and distinguish raw values from relative displays. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../solved/network-forensics/099-easy-packet-1-17-tcp-acknowledgment-marker/README.md)
- [Actual TShark field output](../evidence/network/099-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../solved/network-forensics/099-easy-packet-1-17-tcp-acknowledgment-marker/solution.md)
