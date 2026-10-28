# ACT 5 - FINAL INCIDENT: Host Three MAC

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 292 |
| Category | Network Forensics |
| Points | 125 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Find the MAC address associated with 10.3.14.135.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/292-act-5-final-incident-host-three-mac/README.md). The supplied evidence is `2017-02-11-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

Even routine traffic can establish a useful endpoint mapping. A malicious packet is not needed to determine an ordinary workstation’s source MAC.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `6971ca45f782265b10378d8331201b14704cd8525922fd89bb909fef3e788075`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
ip.src == 10.3.14.135
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/289-act-5-final-incident-map-the-network/files/2017-02-11-traffic-analysis-exercise.pcap \
  -Y '(ip.src == 10.3.14.135) && frame.number in {6}' \
  -T fields -E header=y -e frame.number -e eth.src -e ip.src
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	eth.src	ip.src
6	00:26:bb:4c:6b:e1	10.3.14.135
```

### 2. Interpret the result

DNS query frame 6 links source 10.3.14.135 with Ethernet source 00:26:bb:4c:6b:e1. The recipient is the local resolver/gateway, which is a different device.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #292 — offline packet evidence

![292-decisive-evidence.png](../screenshots/292-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/289-act-5-final-incident-map-the-network/files/2017-02-11-traffic-analysis-exercise.pcap -Y '(ip.src == 10.3.14.135) && frame.number in {6}' -T fields -E header=y -e frame.number -e eth.src -e ip.src
```

[Actual command transcript](../screenshots/capture-work/292-network.terminal.log) · [Execution record](../screenshots/capture-work/292-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{00:26:bb:4c:6b:e1}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

Use the earliest suitable packet when it directly answers an address-mapping question; no malware execution is needed. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/292-act-5-final-incident-host-three-mac/README.md)
- [Actual TShark field output](../evidence/network/292-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/292-act-5-final-incident-host-three-mac/solution.md)
