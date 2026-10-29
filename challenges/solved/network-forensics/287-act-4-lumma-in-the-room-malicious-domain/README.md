# ACT 4 - LUMMA IN THE ROOM: Malicious Domain

Status: Unsolved  
Category: Network Forensics  
Points: 200  
Challenge ID: 287  
Source: https://cgcybercom.online/challenges#287

## Description

The IDS alert identifies 153.92.1.49 as the suspicious infrastructure. Determine the domain associated with that IP in the supplied network evidence.

Evidence:
2026-01-31-traffic-analysis-exercise.pcap

Mission:
Identify the malicious domain associated with 153.92.1.49.

Submission requirement:
Answer: pcgCTF{...}
Filter: ...
Evidence: Packet/Stream ...

Hint:
Start broad, identify DNS traffic for 153.92.1.49, then correlate the returned domain with the HTTP Host header and TLS SNI.

## Files

No directly attached files. See description for shared evidence, target websites, and other references.
