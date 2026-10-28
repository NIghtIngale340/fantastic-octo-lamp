# The Exposed Password

Status: Unsolved  
Category: Network Analysis  
Points: 150  
Challenge ID: 61  
Source: https://cgcybercom.online/challenges#61

## Description

A user has logged in to HVBank, and their authentication traffic was captured in a network trace.

Your task is to analyze the captured HTTP traffic and determine the password used by the account.

🎯 Mission

What is the password used by user johndoe to log in to HVBank?

📁 Evidence

A PCAP file containing the captured network traffic.

🛠️ Recommended Tool

Wireshark

🚩 Flag Format

SAMPLE FLAG: pcgCTF{vv34k...........}

Analyst Note: The objective is to recover credentials from the provided forensic evidence. Do not attempt to use the recovered credentials against any real system.

## Files

- [http_authentication.pcap](files/http_authentication.pcap) (9,282 bytes)
