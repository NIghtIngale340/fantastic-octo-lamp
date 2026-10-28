# ACT 1 - FIRST SIGNAL: Patient Zero

Status: Solved  
Category: Network Forensics  
Points: 100  
Challenge ID: 262  
Source: https://cgcybercom.online/challenges#262

## Description

Your SOC has received indicators of possible command-and-control activity originating from a Windows endpoint.

Analyze the supplied packet capture and identify the internal IPv4 address associated with the suspicious FormBook traffic.

Mission:
Identify the internal IPv4 address responsible for the suspicious FormBook command-and-control traffic.

Evidence:
ACT12026-08-09-traffic-analysis-exercise.pcap

Submission requirement:
Answer: pcgCTF{...}
Filter: ...
Evidence: Packet/Stream ....

Hint:
Start with Statistics → Endpoints and Statistics → Conversations. Look for an internal host repeatedly initiating suspicious outbound connections.

Rules:
Use only the supplied packet capture. Wireshark, tshark, and offline analysis tools are permitted. Do not use public solution pages during the event. Do not execute files reconstructed from the capture.

## Files

- [ACT12026-08-09-traffic-analysis-exercise.pcap](files/ACT12026-08-09-traffic-analysis-exercise.pcap) (16,007,378 bytes)
