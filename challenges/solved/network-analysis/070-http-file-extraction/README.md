# HTTP File Extraction

Status: Solved  
Category:  Network Analysis  
Points: 150  
Challenge ID: 70  
Source: https://cgcybercom.online/challenges#70

## Description

An analyst was monitoring HTTP traffic when a suspicious ZIP file was downloaded from mywebsite.hv.

The file appears harmless, but something inside it contains a secret.

Your task is to analyze the captured network traffic, recover the downloaded file, and uncover the password hidden inside.

🎯 Mission

Analyze the provided PCAP and extract the ZIP file downloaded from mywebsite.hv.

Recover the contents of the ZIP file and identify the password contained inside.

📁 Evidence

network_capture.pcap

The evidence contains HTTP traffic involving the download of a ZIP file from:

mywebsite.hv

🛠️ Suggested Tools
Wireshark
Kali Linux
unzip
cat

🚩 Flag Format

Submit the password using the standard PCGCTF flag format:

pcgCTF{theflaghere}

## Files

- [http_file_extraction.pcap](files/http_file_extraction.pcap) (3,914 bytes)
