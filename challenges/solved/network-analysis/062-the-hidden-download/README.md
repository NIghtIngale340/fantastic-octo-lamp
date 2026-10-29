# THE HIDDEN DOWNLOAD

Status: Unsolved  
Category: Network Analysis  
Points: 150  
Challenge ID: 62  
Source: https://cgcybercom.online/challenges#62

## Description

A network capture contains evidence of a file being downloaded from a web server.

Your task is to investigate the captured HTTP traffic, recover the downloaded archive, and examine its contents to uncover the password hidden inside the extracted file.

🎯 Mission

What is the password contained inside the ZIP file downloaded from mywebsite.hv?

📁 Evidence

A PCAP file containing the captured network traffic.

🛠️ Recommended Tool

Wireshark

🚩 Flag Format

pcgCTF{answer}


Analyst Note: Treat the PCAP as forensic evidence. Your objective is to recover and analyze the transferred file without modifying the original evidence.

## Files

- [http_file_extraction.pcap](files/http_file_extraction.pcap) (3,914 bytes)
