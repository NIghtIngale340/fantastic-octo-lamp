# ACT 2 - THE COMPROMISE: VICTIM MAC

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 269 |
| Category | Network Forensics |
| Points | 100 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. |

## Challenge and objective

Recover the hardware address of the infected NetSupport client.

The original description and prerequisite chain are preserved in [the challenge README](../../solved/network-forensics/269-act-2-the-compromise-victim-mac/README.md). The supplied evidence is `2026-02-28-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

I reused a confirmed C2 request so the Layer-2 address could be read from a frame whose victim identity was already established.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `3dc470f5490ec15b4024c513e87c67e0b17caeae2a2ce3d83541be24ef407e61`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
ip.src == 10.2.28.88 && http.request
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap \
  -Y '(ip.src == 10.2.28.88 && http.request) && frame.number in {2638}' -d tcp.port==443,http \
  -T fields -E header=y -e frame.number -e eth.src -e ip.src -e ip.dst
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above. `-d tcp.port==443,http` tells the dissector to treat that port as HTTP for this known capture. It changes the decoding choice, not the underlying bytes, and does not mean all port-443 traffic is HTTP.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	eth.src	ip.src	ip.dst
2638	00:19:d1:b2:4d:ad	10.2.28.88	45.131.214.85
```

### 2. Interpret the result

In frame 2638 the source IPv4 address is 10.2.28.88 and Ethernet source is 00:19:d1:b2:4d:ad. The destination MAC identifies the next hop on the LAN and would answer a different question.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #269 — offline packet evidence

![269-decisive-evidence.png](../screenshots/269-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap -Y '(ip.src == 10.2.28.88 && http.request) && frame.number in {2638}' -d tcp.port==443,http -T fields -E header=y -e frame.number -e eth.src -e ip.src -e ip.dst
```

[Actual command transcript](../screenshots/capture-work/269-network.terminal.log) · [Execution record](../screenshots/capture-work/269-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{00:19:d1:b2:4d:ad}
```

Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The solved snapshot confirms challenge completion, not an independently captured acceptance response for this exact text.

## Conclusion and lesson

Keep direction and layer consistent when moving from an IP-based pivot to hardware identity. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../solved/network-forensics/269-act-2-the-compromise-victim-mac/README.md)
- [Actual TShark field output](../evidence/network/269-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../solved/network-forensics/269-act-2-the-compromise-victim-mac/solution.md)
