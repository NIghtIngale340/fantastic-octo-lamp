# ACT 1 - FIRST SIGNAL: Hardware Fingerprint

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 263 |
| Category | Network Forensics |
| Points | 100 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. |

## Challenge and objective

Associate the compromised IPv4 address with its Ethernet hardware address.

The original description and prerequisite chain are preserved in [the challenge README](../../solved/network-forensics/263-act-1-first-signal-hardware-fingerprint/README.md). The supplied evidence is `ACT12026-08-09-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

Once 172.16.8.49 was known, the next step was to examine an actual frame sent by that address on the captured LAN.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `0ea6b597732a9ce6af9a7e3adff4512c9a91b4bce27184c8fdeb746f05cce170`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
ip.src == 172.16.8.49
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/262-act-1-first-signal-patient-zero/files/ACT12026-08-09-traffic-analysis-exercise.pcap \
  -Y '(ip.src == 172.16.8.49) && frame.number in {1884}' \
  -T fields -E header=y -e frame.number -e eth.src -e ip.src -e ip.dst
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	eth.src	ip.src	ip.dst
1884	00:12:f0:28:d4:34	172.16.8.49	172.16.8.255
```

### 2. Interpret the result

Frame 1884 pairs ip.src=172.16.8.49 with eth.src=00:12:f0:28:d4:34. The packet is a local announcement, so the association does not depend on guessing a vendor from a MAC prefix or mistaking the router’s destination MAC for the workstation.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #263 — offline packet evidence

![263-decisive-evidence.png](../screenshots/263-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/262-act-1-first-signal-patient-zero/files/ACT12026-08-09-traffic-analysis-exercise.pcap -Y '(ip.src == 172.16.8.49) && frame.number in {1884}' -T fields -E header=y -e frame.number -e eth.src -e ip.src -e ip.dst
```

[Actual command transcript](../screenshots/capture-work/263-network.terminal.log) · [Execution record](../screenshots/capture-work/263-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{00:12:f0:28:d4:34}
```

Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The solved snapshot confirms challenge completion, not an independently captured acceptance response for this exact text.

## Conclusion and lesson

Correlate source IP and source MAC in the same frame rather than combining values from unrelated packets. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../solved/network-forensics/263-act-1-first-signal-hardware-fingerprint/README.md)
- [Actual TShark field output](../evidence/network/263-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../solved/network-forensics/263-act-1-first-signal-hardware-fingerprint/solution.md)
