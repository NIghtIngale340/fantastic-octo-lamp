# ACT 2 - THE COMPROMISE: Infected IPV4

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 268 |
| Category | Network Forensics |
| Points | 100 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. |

## Challenge and objective

Identify the Windows client generating NetSupport RAT traffic.

The original description and prerequisite chain are preserved in [the challenge README](../../solved/network-forensics/268-act-2-the-compromise-infected-ipv4/README.md). The supplied evidence is `2026-02-28-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

NetSupport Manager/1.3 in a readable user agent is a stronger starting point than a port number. In this capture, the malicious HTTP happens to use TCP 443.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `3dc470f5490ec15b4024c513e87c67e0b17caeae2a2ce3d83541be24ef407e61`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
http.user_agent contains "NetSupport"
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap \
  -Y '(http.user_agent contains "NetSupport") && frame.number in {2638}' -d tcp.port==443,http \
  -T fields -E header=y -e frame.number -e eth.src -e ip.src -e ip.dst -e http.user_agent -e http.request.uri
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above. `-d tcp.port==443,http` tells the dissector to treat that port as HTTP for this known capture. It changes the decoding choice, not the underlying bytes, and does not mean all port-443 traffic is HTTP.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	eth.src	ip.src	ip.dst	http.user_agent	http.request.uri
2638	00:19:d1:b2:4d:ad	10.2.28.88	45.131.214.85	NetSupport Manager/1.3	http://45.131.214.85/fakeurl.htm
```

### 2. Interpret the result

Frame 2638 ties the NetSupport request to source 10.2.28.88 and destination 45.131.214.85. The target is an absolute-form HTTP URL ending in /fakeurl.htm. Because the bytes are HTTP, port 443 must not be interpreted as proof of TLS.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #268 — offline packet evidence

![268-decisive-evidence.png](../screenshots/268-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap -Y '(http.user_agent contains "NetSupport") && frame.number in {2638}' -d tcp.port==443,http -T fields -E header=y -e frame.number -e eth.src -e ip.src -e ip.dst -e http.user_agent -e http.request.uri
```

[Actual command transcript](../screenshots/capture-work/268-network.terminal.log) · [Execution record](../screenshots/capture-work/268-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{10.2.28.88}
```

Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The solved snapshot confirms challenge completion, not an independently captured acceptance response for this exact text.

## Conclusion and lesson

Decode the payload and attribute the client before reasoning from service ports. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../solved/network-forensics/268-act-2-the-compromise-infected-ipv4/README.md)
- [Actual TShark field output](../evidence/network/268-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../solved/network-forensics/268-act-2-the-compromise-infected-ipv4/solution.md)
