# ACT 1 — Easy as 123: Protocol Deception

**Platform:** PCGCTF · **Challenge ID:** 299 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the capture and cited public sources. Exact PCGCTF submission not re-confirmed.

**Evidence:** Packet 2638 · TCP stream 40 · [2026-02-28-traffic-analysis-exercise.pcap](../../challenges/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap).

## The challenge

What protocol is the C2 actually using on port 443?

## Solving it

Use [the shared capture](../../challenges/solved/network-forensics/268-act-2-the-compromise-infected-ipv4/files/2026-02-28-traffic-analysis-exercise.pcap) as `act.pcap`.

Port 443 usually means HTTPS, but a port is just a convention — the payload decides. Telling tshark to decode the 443 stream as HTTP, the request lines are fully readable:

```sh
tshark -nr act.pcap -d tcp.port==443,http -Y 'ip.dst==45.131.214.85 && http.request' \
  -T fields -e tcp.dstport -e http.request.method -e http.request.uri | sort -u | head -n 8
```

```text
443	POST	http://45.131.214.85/fakeurl.htm
```

Cleartext HTTP, no TLS handshake — the "443" is camouflage. So the protocol is HTTP.

## Screenshot

Fresh local reproduction using the command described above.

![Command and result](../screenshots/299-clear-method-v3.png)

## Flag

```text
pcgCTF{HTTP}
```

## Takeaway

Don't infer TLS from port 443. `decode as` is just a viewing choice; the readable request syntax is what proves it's plain HTTP.

## References

- [Analyst writeup (Easy as 123)](https://rvmchua.com/posts/mta-easy-as-123/)
- [Original challenge description](../../challenges/solved/osint/299-act-1-easy-as-123-protocol-deception/README.md)
