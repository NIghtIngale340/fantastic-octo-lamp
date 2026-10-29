# CryptoMaze

Status: Solved  
Category: Cryptography  
Points: 250  
Challenge ID: 60  
Source: https://cgcybercom.online/challenges#60

## Description

A hidden flag has been protected using two layers of cryptography.

First, a Linear Feedback Shift Register (LFSR) is used to derive the key. The resulting key is then used with AES encryption to protect the flag.

Your mission is to reverse the process, reconstruct the LFSR output, derive the AES key, and decrypt the encrypted flag.

🎯 Mission

Recover the original flag from the encrypted data.

📁 Evidence

Download the encrypted flag file provided with this challenge.

The file contains:

The initial LFSR state
The LFSR taps
The encrypted flag in hexadecimal format

🧠 Objectives
Understand the provided LFSR configuration.
Reconstruct the LFSR sequence.
Derive the AES key from the generated output.
Use the derived key to decrypt the encrypted flag.
Submit the recovered flag.
🛠️ Recommended Tools
Python
A cryptography library such as PyCryptodome
Hexadecimal analysis tools

🚩 Flag Format
FLAG:pcgCTF{scrambledeggg..}


Analyst Note: This challenge is designed to test your ability to reverse a custom key-generation process and apply cryptographic reasoning to recover protected data.

## Files

- [output.txt](files/output.txt) (364 bytes)
