# PCGCTF Juice Shop Gateway

Status: Unsolved  
Category: Reconnaissance  
Points: 100  
Challenge ID: 122  
Source: https://cgcybercom.online/challenges#122

## Description

Description

Welcome to the PCGCTF OWASP Juice Shop Laboratory.

This challenge is part of the PCGCTF Juice Shop Challenge Track.

All challenges belonging to the OWASP Juice Shop track are identified with the tag PCGCTF-JuiceShop-Challenges.

This challenge requires a local OWASP Juice Shop instance running on your machine.

The following files are provided with this challenge:

docker-compose.yml — Docker configuration for deploying the PCGCTF Juice Shop instance.
PLAYER_SETUP.txt — Instructions for installing Docker, configuring the Juice Shop, setting the required CTF_KEY, and starting the application.

Complete the environment setup before beginning the challenge.

Target

Once the Juice Shop is running, access:

http://localhost:3000
Objective

Perform basic reconnaissance against your assigned Juice Shop instance.

Your first task is to locate the hidden Score Board within the application.

Investigate the web application and identify information that is intentionally exposed but not immediately visible from the main page.

The Score Board contains the information required to complete this challenge.

Mission

Find the hidden Score Board and obtain the flag associated with this challenge.

Submit the recovered flag to CTFd.

Flag Format
pcgCTF{...}


Unlock Condition

Prerequisite: None

Successfully solving PCGCTF Gateway will unlock the next challenge in the progression.

## Files

- [docker-compose.yml](files/docker-compose.yml) (416 bytes)
- [PCGCTF_JuiceShop_Player_Setup_Guide.txt](files/PCGCTF_JuiceShop_Player_Setup_Guide.txt) (2,441 bytes)
