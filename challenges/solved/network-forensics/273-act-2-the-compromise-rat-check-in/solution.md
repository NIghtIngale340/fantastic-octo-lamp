# ACT 2 - THE COMPROMISE: RAT Check-In — analysis

Answer: **/fakeurl.htm**

Candidate flag (not platform validated):

```text
pcgCTF{/fakeurl.htm}
```

Capture: `2026-02-28-traffic-analysis-exercise.pcap`

Filter:

```wireshark
http.user_agent contains "NetSupport"
```

Evidence: Frames 2638; TCP streams 40.

264 HTTP requests use the NetSupport Manager/1.3 user agent. The request target can be absolute-form http://45.131.214.85/fakeurl.htm; the requested path is /fakeurl.htm. HTTP is carried on TCP port 443 in this capture, which does not make it TLS.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
