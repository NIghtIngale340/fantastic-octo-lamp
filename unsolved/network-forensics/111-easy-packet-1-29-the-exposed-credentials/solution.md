# EASY PACKET 1 #29  The Exposed Credentials — analysis

Answer: **usertest:password**

Candidate flag (not platform validated):

```text
pcgCTF{usertest/password}
```

Capture: `EASY_PACKET_1.pcap`

Filter:

```wireshark
frame.number == 1 && http.authorization
```

Evidence: Frames 1; TCP streams 0.

Authorization is Basic dXNlcnRlc3Q6cGFzc3dvcmQ=. Base64 decoding yields username usertest and password password, separated by a colon. These are challenge-supplied packet contents.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.

## Day 1 formatting correction

Garcia explicitly reports `pcgCTF{usertest/password}` as accepted. This replaces our untested spelling `pcgCTF{usertest:password}`. The packet-derived raw value is preserved; the acceptance report is attributed to the teammate and was not retested in our account. [Imported source](../../../team-writeups/garcia-day1/source.md).
