# EASY PACKET 1 #21  Speak HTTP — analysis

Answer: **HTTP**

Candidate flag (not platform validated):

```text
pcgCTF{HTTP}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && http.request
```

Evidence: Frames 1; TCP streams 0.

The TCP payload starts GET /statuses/replies.xml HTTP/1.1 and is decoded as HTTP.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
