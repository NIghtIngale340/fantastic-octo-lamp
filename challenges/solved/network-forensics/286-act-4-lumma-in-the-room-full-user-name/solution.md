# ACT 4 - LUMMA IN THE ROOM: Full User Name — analysis

Answer: **Gabriel Wyatt**

Candidate flag (not platform validated):

```text
pcgCTF{Gabriel Wyatt}
```

Capture: `2026-01-31-traffic-analysis-exercise.pcap`

Filter:

```wireshark
samr.samr_UserInfo21.full_name
```

Evidence: Frames 358; TCP streams 8.

The same SAMR UserInfo21 response pairs account gwyatt with full name Gabriel Wyatt. Preserve the space in the raw answer; the challenge does not specify underscore normalization.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.

The raw full name contains a space. If the organizer expects underscores, its submission spelling will differ; this has not been tested.
