# EASY PACKET 1 #30  Cleartext on the Wire — analysis

Answer: **HTTP Basic credentials are recoverable over unencrypted HTTP; use HTTPS (HTTP over TLS)**

**Exact accepted flag string is unknown.** The conceptual answer above is established; the question does not identify the grader's required wording.

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && http.authorization
```

Evidence: Frames 1; TCP streams 0.

Base64 is encoding, not encryption: an observer can recover the username/password. Protect credential transport with HTTPS/TLS. This is the semantic answer; the exact compound phrase expected inside the flag is not specified. Reference: https://www.rfc-editor.org/rfc/rfc7617.html#section-1

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
