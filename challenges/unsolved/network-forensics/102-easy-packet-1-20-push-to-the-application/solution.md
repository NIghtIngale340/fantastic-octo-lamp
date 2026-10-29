# EASY PACKET 1 #20  Push to the Application — analysis

Answer: **Push buffered data to the receiving application without waiting for more data**

**Exact accepted flag string is unknown.** The conceptual answer above is established; the question does not identify the grader's required wording.

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && tcp.flags.push == 1
```

Evidence: Frames 1; TCP streams 0.

PSH requests the push function: make buffered data available to the receiving user/application rather than waiting for additional data to fill a buffer. It is not a record boundary or a guarantee of immediate application scheduling. This conceptual answer is established, but the challenge does not disclose the exact phrase its flag matcher expects. Do not invent an accepted flag spelling. Reference: https://www.rfc-editor.org/rfc/rfc9293.html#section-3.9.1.2

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
