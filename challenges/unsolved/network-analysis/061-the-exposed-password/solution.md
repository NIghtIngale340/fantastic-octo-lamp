# The Exposed Password — solution

Recovered answer: **John1234!**

Flag candidate:

```text
pcgCTF{John1234!}
```

Capture: `http_authentication.pcap`

Filter:

```wireshark
http.request.method == "POST" || frame.number == 48
```

Frames: 27, 46, 48. TCP streams: 1, 2.

Frame 27 tries john1234, but response frame 29 rejects it. Frame 46 submits username=johndoe&password=John1234%21. URL decoding gives John1234!; frame 48 explicitly confirms a valid login. Use the capital J and trailing exclamation mark.

Platform acceptance: unconfirmed. No submissions made in this batch.
