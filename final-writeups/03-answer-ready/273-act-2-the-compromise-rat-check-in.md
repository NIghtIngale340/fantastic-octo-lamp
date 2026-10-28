# ACT 2 - THE COMPROMISE: RAT Check-In

| Item | Record |
|---|---|
| Platform | PCGCTF |
| Challenge ID | 273 |
| Category | Network Forensics |
| Points | 150 |
| Difficulty | Not separately recorded in the available inventory |
| Verification | Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. |

## Challenge and objective

Recover the repeatedly used NetSupport HTTP check-in path.

The original description and prerequisite chain are preserved in [the challenge README](../../unsolved/network-forensics/273-act-2-the-compromise-rat-check-in/README.md). The supplied evidence is `2026-02-28-traffic-analysis-exercise.pcap`; related storyline questions reuse the same capture rather than providing another download.

## Initial analysis

The request target is absolute-form in this capture. I separated its scheme and host from the path because the question asks for an endpoint path.

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
  -T fields -E header=y -e frame.number -e ip.src -e ip.dst -e tcp.dstport -e http.request.uri -e http.user_agent
```

`-n` disables address/name resolution so that recorded numeric addresses stay visible. `-r` reads the existing capture, and `-Y` applies a display filter after decoding. `-T fields` outputs selected fields; each `-e` adds one named column, and `-E header=y` records the column names. The `frame.number in {...}` clause makes the final evidence small and auditable; the wider discovery filter remains documented above. `-d tcp.port==443,http` tells the dissector to treat that port as HTTP for this known capture. It changes the decoding choice, not the underlying bytes, and does not mean all port-443 traffic is HTTP.

**Actual reproduced output** (tab-separated; full lines are preserved in the linked TSV):

```text
frame.number	ip.src	ip.dst	tcp.dstport	http.request.uri	http.user_agent
2638	10.2.28.88	45.131.214.85	443	http://45.131.214.85/fakeurl.htm	NetSupport Manager/1.3
```

### 2. Interpret the result

Frame 2638 shows http://45.131.214.85/fakeurl.htm with user agent NetSupport Manager/1.3 and TCP destination 443. The earlier complete extraction counted 264 matching HTTP requests. Removing only scheme and authority leaves /fakeurl.htm.

### Keep the raw value separate from the submission

An absolute URI such as `http://45.131.214.85/fakeurl.htm` can appear in an HTTP request. Parsing it into scheme, authority and path gives the requested `/fakeurl.htm`. The source/destination IPs and TCP 443 provide context; they are not characters to include in a path flag.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #273 — offline packet evidence

![273-decisive-evidence.png](../screenshots/273-decisive-evidence.png)

Fresh execution of the draft’s field-specific TShark command.

Command/action actually executed:

```sh
tshark -n -r /home/nightingale/CTF/PCGCTF/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap -Y '(http.user_agent contains "NetSupport") && frame.number in {2638}' -d tcp.port==443,http -T fields -E header=y -e frame.number -e ip.src -e ip.dst -e tcp.dstport -e http.request.uri -e http.user_agent
```

[Actual command transcript](../screenshots/capture-work/273-network.terminal.log) · [Execution record](../screenshots/capture-work/273-network.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

## Flag discovery and verification

Saved submission candidate:

```text
pcgCTF{/fakeurl.htm}
```

Needs Flag Verification — the answer has offline evidence, but our PCGCTF snapshot does not record acceptance. A teammate’s reported acceptance, where noted, is separate evidence. The exact wrapper comes from the challenge’s `pcgCTF{...}` requirement; literal spaces, capitalization and separators are retained as recorded. The focused final check is to submit this exact saved spelling when the platform is available and preserve the resulting acceptance or rejection with the challenge ID.

## Conclusion and lesson

A request URI can contain a full URL. Preserve the requested path while avoiding unrelated scheme, host or port text. The artifact-backed answer and the platform acceptance state remain separate in this draft.

## Reproduction evidence and references

- [Original challenge description](../../unsolved/network-forensics/273-act-2-the-compromise-rat-check-in/README.md)
- [Actual TShark field output](../evidence/network/273-fields.tsv)
- [Commands, hashes and reproduction results](../evidence/network/reproduction.json)
- [TShark version](../evidence/network/tshark-version.txt)
- [TShark official manual](https://www.wireshark.org/docs/man-pages/tshark.html)

- [Earlier local solution and provenance](../../unsolved/network-forensics/273-act-2-the-compromise-rat-check-in/solution.md)
