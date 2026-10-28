# ACT 5 - FINAL INCIDENT: First Ransomware

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 294 |
| Category | Network Forensics |
| Points | 200 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Attribute the ransomware affecting 10.3.14.131.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/294-act-5-final-incident-first-ransomware/README.md). The supplied evidence is `2017-02-11-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

The useful network clue is the ransomware-specific host spora.biz. I inspected which local client requested it and separated the request evidence from claims about an executable.

I kept the original capture intact and used offline packet analysis. The file’s SHA-256 is `6971ca45f782265b10378d8331201b14704cd8525922fd89bb909fef3e788075`. This identifies the exact evidence behind the frame references; no reconstructed program was executed and no request was sent to an address found inside the capture.

## Step-by-step solution

### 1. Narrow the incident to a reproducible evidence set

The discovery filter for this question is:

```wireshark
ip.src == 10.3.14.131 && http.host == "spora.biz"
```

In Wireshark, the filter removes unrelated frames from the display without deleting them from the file. For a command-line reproduction, the following extraction additionally selects the cited frames where appropriate:

```sh
tshark -n \
  -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/289-act-5-final-incident-map-the-network/files/2017-02-11-traffic-analysis-exercise.pcap \
  -Y '(ip.src == 10.3.14.131 && http.host == "spora.biz") && frame.number in {16762, 16772, 16979}' \
  -T fields -E header=y -e frame.number -e ip.src -e http.host -e http.request.uri
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	ip.src	http.host	http.request.uri
16762	10.3.14.131	spora.biz	/
16772	10.3.14.131	spora.biz	/
16979	10.3.14.131	spora.biz	/
```

### 2. Interpret the result

Frames 16762, 16772 and 16979 tie .131 to spora.biz. This supports Spora attribution in the challenge’s stated infection context. Some responses are redirects or DDoS-Guard interstitials, so their content is not proof that an encryption binary was downloaded or run.

### Attribution boundary and supporting research

The observed indicator is `spora.biz`, not an extracted ransomware executable. [Malwarebytes’ primary Spora analysis](https://www.malwarebytes.com/blog/news/2017/03/spora-ransomware) explains its victim-facing payment infrastructure and offline encryption workflow. The family identification here remains a network-based inference combining the captured ransomware-specific domain with the challenge’s infection context; redirects alone are not execution evidence.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #294 — offline packet evidence

![294-decisive-evidence.png](../screenshots/294-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/unsolved/network-forensics/289-act-5-final-incident-map-the-network/files/2017-02-11-traffic-analysis-exercise.pcap -Y '(ip.src == 10.3.14.131 && http.host == "spora.biz") && frame.number in {16762, 16772, 16979}' -T fields -E header=y -e frame.number -e ip.src -e http.host -e http.request.uri
```

[Actual command transcript](../screenshots/capture-work/294-network.terminal.log) · [Execution record](../screenshots/capture-work/294-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{Spora}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

State what the traffic proves and what attribution infers. A payment-domain visit is meaningful, but it is not a reconstructed malware execution trace. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/294-act-5-final-incident-first-ransomware/README.md)
- [Actual TShark field output](../evidence/network/294-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/294-act-5-final-incident-first-ransomware/solution.md)
