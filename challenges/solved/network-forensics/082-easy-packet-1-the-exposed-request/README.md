# EASY PACKET 1  The Exposed Request

Status: Solved  
Category: Network Forensics  
Points: 100  
Challenge ID: 82  
Source: https://cgcybercom.online/challenges#82

## Description

A network capture has been recovered from a suspicious communication session.

Download EASY PACKET 1.pcap and investigate it in Wireshark. Examine the Ethernet, IPv4, TCP, and HTTP layers. Pay particular attention to the HTTP request headers and the Authorization field.

OBJECTIVE: Recover the credentials exposed in the captured HTTP Basic Authentication request and submit them in the format pcgCTF{flagheree}.

HINT: Basic Authentication encodes credentials with Base64. Look for an Authorization header inside the HTTP request.

## Files

- [EASY_PACKET_1.pcap](files/EASY_PACKET_1.pcap) (558 bytes)
