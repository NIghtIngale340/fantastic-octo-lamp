# ACT 2 - THE COMPROMISE: Who Is brolf? — analysis

Answer: **Becka Rolf**

Candidate flag (not platform validated):

```text
pcgCTF{Becka Rolf}
```

Capture: `2026-02-28-traffic-analysis-exercise.pcap`

Filter:

```wireshark
samr.samr_UserInfo21.account_name == "brolf"
```

Evidence: Frames 339; TCP streams 9.

SAMR UserInfo21 pairs brolf with full_name Becka Rolf in one response.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.

The raw full name contains a space. If the organizer expects underscores, its submission spelling will differ; this has not been tested.
