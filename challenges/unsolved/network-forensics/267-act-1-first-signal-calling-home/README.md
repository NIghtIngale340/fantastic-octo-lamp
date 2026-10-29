# ACT 1 - FIRST SIGNAL: Calling Home

Status: Unsolved  
Category: Network Forensics  
Points: 125  
Challenge ID: 267  
Source: https://cgcybercom.online/challenges#267

## Description

The identity of the compromised workstation has been established. Now determine where the malware is communicating.

Mission:
Identify one confirmed FormBook command-and-control IPv4 address contacted by the compromised endpoint.

Evidence:
ACT12026-08-09-traffic-analysis-exercise.pcap

Submission requirement:
Answer: pcgCTF{...}
Filter: ...
Evidence: Packet/Stream ...

Hint:
Begin with the compromised endpoint identified in Patient Zero. Filter traffic originating from that system and investigate repeated outbound HTTP connections. Correlate source IP, destination IP, destination port, TCP streams, HTTP requests, connection frequency, and timing. Do not assume every external IP is malicious.

Prerequisite:
ACT 1 - FIRST SIGNAL: Full Identity

## Files

No directly attached files. See description for shared evidence, target websites, and other references.
