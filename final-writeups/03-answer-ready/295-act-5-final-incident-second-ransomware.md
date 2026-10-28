# ACT 5 - FINAL INCIDENT: Second Ransomware

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 295 |
| Category | Network Forensics |
| Points | 200 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Attribute the ransomware affecting 10.3.14.134.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/295-act-5-final-incident-second-ransomware/README.md). The supplied evidence is `2017-02-11-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

A UDP port on its own would be a weak family identifier. Here it occurs alongside a distinctive payment-domain pattern.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `6971ca45f782265b10378d8331201b14704cd8525922fd89bb909fef3e788075`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
ip.src == 10.3.14.134 && (http.host contains "p27dokhpz2n7nvgr" || udp.dstport == 6892)
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/289-act-5-final-incident-map-the-network/files/2017-02-11-traffic-analysis-exercise.pcap \
  -Y '(ip.src == 10.3.14.134 && (http.host contains "p27dokhpz2n7nvgr" || udp.dstport == 6892)) && frame.number in {8820, 11043, 16354}' \
  -T fields -E header=y -e frame.number -e ip.src -e udp.dstport -e http.host -e http.request.uri
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	ip.src	udp.dstport	http.host	http.request.uri
8820	10.3.14.134	6892		
11043	10.3.14.134		p27dokhpz2n7nvgr.1nmrtq.top	/3402-41D8-C680-0091-CCCF?iframe&_=1486782175308
16354	10.3.14.134		p27dokhpz2n7nvgr.1nmrtq.top	/3402-41D8-C680-0091-CCCF
```

### 2. Interpret the result

Frame 8820 shows UDP destination port 6892; frame 11043 uses p27dokhpz2n7nvgr.1nmrtq.top with a victim-ID-shaped path. Brad Duncan’s firsthand Cerber research describes that same combination of port and host prefix. The changing suffix is expected infrastructure variation rather than a reason to discard the match.

### Correlate the behavior with firsthand Cerber research

[Brad Duncan’s SANS ISC report](https://isc.sans.edu/diary/22215) describes a controlled Cerber infection that generated UDP traffic to port 6892 and HTTP traffic to a domain beginning `p27dokhpz2n7nvgr` and ending `.top`. Our recorded suffix differs, but the two independent behavior features match. This source explains why the combination is meaningful; we did not run a ransomware binary or submit this capture to an external service.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #295 — offline packet evidence

![295-decisive-evidence.png](../screenshots/295-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/289-act-5-final-incident-map-the-network/files/2017-02-11-traffic-analysis-exercise.pcap -Y '(ip.src == 10.3.14.134 && (http.host contains "p27dokhpz2n7nvgr" || udp.dstport == 6892)) && frame.number in {8820, 11043, 16354}' -T fields -E header=y -e frame.number -e ip.src -e udp.dstport -e http.host -e http.request.uri
```

[Actual command transcript](../screenshots/capture-work/295-network.terminal.log) · [Execution record](../screenshots/capture-work/295-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{Cerber}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

Corroborate multiple indicators and cite the research that connects them to a malware family. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/295-act-5-final-incident-second-ransomware/README.md)
- [Actual TShark field output](../evidence/network/295-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/295-act-5-final-incident-second-ransomware/solution.md)
