# ACT 4 - LUMMA IN THE ROOM: Fingerprint API

Status: Unsolved  
Category: Network Forensics  
Points: 225  
Challenge ID: 288  
Source: https://cgcybercom.online/challenges#288

## Description

The infected endpoint communicates with the Lumma infrastructure over HTTP.

Mission:
Identify the API path used by the stealer to register and fingerprint the victim.

Evidence:
2026-01-31-traffic-analysis-exercise.pcap

Submission requirement:
Answer: pcgCTF{...}
Filter: ...
Evidence: Packet/Stream ...
Hint:
Filter HTTP traffic to 153.92.1.49 and inspect repeated requests. Look at the HTTP request URI and Host header. Pay attention to the agent parameter values for Chrome and Edge.

## Files

No directly attached files. See description for shared evidence, target websites, and other references.
