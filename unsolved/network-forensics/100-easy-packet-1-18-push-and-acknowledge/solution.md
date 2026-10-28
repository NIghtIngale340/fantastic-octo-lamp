# EASY PACKET 1 #18  Push and Acknowledge — analysis

Answer: **PSH and ACK**

Candidate flag (not platform validated):

```text
pcgCTF{PSH and ACK}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && tcp.flags.push == 1 && tcp.flags.ack == 1
```

Evidence: Frames 1; TCP streams 0.

TCP flags value is 0x018. PSH and ACK are set; SYN, FIN, RST, and URG are clear. The underscore separator is a submission-format candidate, not an observed grader requirement.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.

## Day 1 formatting correction

Garcia explicitly reports `pcgCTF{PSH and ACK}` as accepted. This replaces our untested spelling `pcgCTF{PSH_ACK}`. The packet-derived raw value is preserved; the acceptance report is attributed to the teammate and was not retested in our account. [Imported source](../../../team-writeups/garcia-day1/source.md).
