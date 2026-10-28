# ACT 1 - FIRST SIGNAL: Patient Zero

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 262 |
| Category | Network Forensics |
| Points | 100 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. |

## Challenge and objective

Find the internal host generating the suspicious FormBook-pattern connections.

The original description and prerequisite chain are preserved in [the challenge README](../../solved/network-forensics/262-act-1-first-signal-patient-zero/README.md). The supplied evidence is `ACT12026-08-09-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

I began with outbound HTTP from the internal subnet rather than choosing the noisiest host. The important correlation is a recurring connection pattern from one client to the same suspicious infrastructure.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `0ea6b597732a9ce6af9a7e3adff4512c9a91b4bce27184c8fdeb746f05cce170`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
ip.src == 172.16.8.49 && ip.dst == 146.59.71.167 && http.request
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/262-act-1-first-signal-patient-zero/files/ACT12026-08-09-traffic-analysis-exercise.pcap \
  -Y '(ip.src == 172.16.8.49 && ip.dst == 146.59.71.167 && http.request) && frame.number in {11227, 11714}' \
  -T fields -E header=y -e frame.number -e eth.src -e ip.src -e ip.dst -e http.host -e http.request.uri
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	eth.src	ip.src	ip.dst	http.host	http.request.uri
11227	00:12:f0:28:d4:34	172.16.8.49	146.59.71.167	www.grinswakebthu.info	/irpw/
11714	00:12:f0:28:d4:34	172.16.8.49	146.59.71.167	www.grinswakebthu.info	/irpw/?2kn1=kzCvvy54rrIQXFKjfYifb866d+M9hs2fv6bSi3WikvZmjVluebu6mUUhZtMb+2Gf6oxOm28aYOpkAiGzpoG3XIhyRfkkPR06YbIov6+BKgDj686nddFR9ZDwA1TR6R82KrYMll+QIfUC&kbBSJ=Ep6t_fJ_
```

### 2. Interpret the result

Frames 11227 and 11714 associate 172.16.8.49 with 146.59.71.167 and www.grinswakebthu.info. The POST uses /irpw/; the GET adds encoded-looking check-in parameters. These related observations support the victim selection without classifying every external address contacted by that client as malicious.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #262 — offline packet evidence

![262-decisive-evidence.png](../screenshots/262-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/262-act-1-first-signal-patient-zero/files/ACT12026-08-09-traffic-analysis-exercise.pcap -Y '(ip.src == 172.16.8.49 && ip.dst == 146.59.71.167 && http.request) && frame.number in {11227, 11714}' -T fields -E header=y -e frame.number -e eth.src -e ip.src -e ip.dst -e http.host -e http.request.uri
```

[Actual command transcript](../screenshots/capture-work/262-network.terminal.log) · [Execution record](../screenshots/capture-work/262-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{172.16.8.49}
```

Verified — marked solved in the original authenticated PCGCTF snapshot. The offline extraction below was reproduced for this draft; no fresh platform submission was made. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The solved snapshot confirms challenge completion, not an independently captured acceptance response for this exact text.

## Conclusion and lesson

Separate a victim address from its remote C2 address and keep an example packet for the association. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../solved/network-forensics/262-act-1-first-signal-patient-zero/README.md)
- [Actual TShark field output](../evidence/network/262-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../solved/network-forensics/262-act-1-first-signal-patient-zero/solution.md)
