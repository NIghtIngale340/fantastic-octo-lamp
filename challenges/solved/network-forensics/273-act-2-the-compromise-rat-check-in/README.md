# ACT 2 - THE COMPROMISE: RAT Check-In

Status: Unsolved  
Category: Network Forensics  
Points: 150  
Challenge ID: 273  
Source: https://cgcybercom.online/challenges#273

## Description

The compromised endpoint is communicating with a NetSupport Manager RAT command-and-control server.

Identify the HTTP path repeatedly used for the RAT C2 check-ins.

Evidence:
2026-02-28-traffic-analysis-exercise.pcap

Submission requirement:
Answer: pcgCTF{...}
Filter: ...
Evidence: Packet/Stream ...

Hint:
Start broad, identify the relevant endpoint/conversation, then narrow your display filter and preserve a packet or stream reference. Look for repeated HTTP POST requests with the NetSupport Manager user-agent.

Rules:
Analyze the supplied PCAP. Do not execute reconstructed binaries or scripts.

## Files

No directly attached files. See description for shared evidence, target websites, and other references.
