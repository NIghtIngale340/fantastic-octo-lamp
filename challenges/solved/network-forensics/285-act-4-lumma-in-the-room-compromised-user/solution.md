# ACT 4 - LUMMA IN THE ROOM: Compromised User — analysis

Answer: **gwyatt**

Candidate flag (not platform validated):

```text
pcgCTF{gwyatt}
```

Capture: `2026-01-31-traffic-analysis-exercise.pcap`

Filter:

```wireshark
kerberos.CNameString == "gwyatt" || samr.samr_UserInfo21.account_name == "gwyatt"
```

Evidence: Frames 214, 358; TCP streams 4, 8.

Kerberos names gwyatt; the SAMR user-information response confirms the account.

Platform acceptance: unconfirmed. Analysis complete; original account-status snapshot preserved.
