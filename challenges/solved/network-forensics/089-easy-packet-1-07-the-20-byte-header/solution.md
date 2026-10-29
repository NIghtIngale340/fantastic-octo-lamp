# EASY PACKET 1 #07  The 20-Byte Header — analysis

Answer: **20 bytes (IHL = 5)**

Candidate flag (not platform validated):

```text
pcgCTF{20 bytes}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && ip.hdr_len == 20
```

Evidence: Frames 1; TCP streams 0.

The IHL nibble is 5, meaning five 32-bit words: 5 × 4 = 20 bytes. The numeric flag candidate uses bytes, without a units suffix.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.

## Day 1 formatting correction

Garcia explicitly reports `pcgCTF{20 bytes}` as accepted. This replaces our untested spelling `pcgCTF{20}`. The packet-derived raw value is preserved; the acceptance report is attributed to the teammate and was not retested in our account. [Imported source](../../../../team/garcia-day1/source.md).
