# Juice Shop challenge scrape

Source: [PCGCTF challenges](https://cgcybercom.online/challenges)  
Scraped: October 29, 2026 (Asia/Manila).

All **118** Juice Shop–tagged entries: **116 new IDs** compared with the October 28 archive, **1 solved**, **117 unsolved**.

This is a scrape of the website descriptions and metadata, without added solutions. Duplicate titles are preserved under their distinct IDs. The Gateway uses a trailing-hyphen variant of the track tag.

[JSON scrape](live-details-2026-10-29.json) · [Original same-day inventory](live-inventory-2026-10-29.json)

## Index

| ID | Challenge | Category | Points | Status | New ID |
| ---: | --- | --- | ---: | --- | --- |
| 122 | [PCGCTF Juice Shop Gateway](#challenge-122) | Reconnaissance | 100 | Solved | No |
| 134 | [Web3 Sandbox](#challenge-134) | Broken Access Control | 100 | Unsolved | Yes |
| 127 | [Admin Section](#challenge-127) | Broken Access Control | 250 | Unsolved | Yes |
| 152 | [Five-Star Feedback](#challenge-152) | Broken Access Control | 250 | Unsolved | Yes |
| 209 | [View Basket](#challenge-209) | Broken Access Control | 250 | Unsolved | Yes |
| 235 | [AI Debugging](#challenge-235) | Broken Access Control | 250 | Unsolved | Yes |
| 154 | [Forged Feedback](#challenge-154) | Broken Access Control | 450 | Unsolved | Yes |
| 155 | [Forged Review](#challenge-155) | Broken Access Control | 450 | Unsolved | Yes |
| 174 | [Manipulate Basket](#challenge-174) | Broken Access Control | 450 | Unsolved | Yes |
| 187 | [Product Tampering](#challenge-187) | Broken Access Control | 450 | Unsolved | Yes |
| 222 | [CSRF](#challenge-222) | Broken Access Control | 450 | Unsolved | Yes |
| 145 | [Easter Egg](#challenge-145) | Broken Access Control | 700 | Unsolved | Yes |
| 195 | [SSRF](#challenge-195) | Broken Access Control | 1350 | Unsolved | Yes |
| 141 | [Confidential Document](#challenge-141) | Sensitive Data Exposure | 100 | Unsolved | Yes |
| 123 | [Password Hash Leak](#challenge-123) | Sensitive Data Exposure | 250 | Unsolved | Yes |
| 131 | [NFT Takeover](#challenge-131) | Sensitive Data Exposure | 250 | Unsolved | Yes |
| 172 | [Login MC SafeSearch](#challenge-172) | Sensitive Data Exposure | 250 | Unsolved | Yes |
| 225 | [Meta Geo Stalking](#challenge-225) | Sensitive Data Exposure | 250 | Unsolved | Yes |
| 226 | [Visual Geo Stalking](#challenge-226) | Sensitive Data Exposure | 250 | Unsolved | Yes |
| 231 | [Exposed Credentials](#challenge-231) | Sensitive Data Exposure | 250 | Unsolved | Yes |
| 261 | [Password Hash Leak](#challenge-261) | Sensitive Data Exposure | 250 | Unsolved | No |
| 168 | [Login Amy](#challenge-168) | Sensitive Data Exposure | 450 | Unsolved | Yes |
| 157 | [Forgotten Developer Backup](#challenge-157) | Sensitive Data Exposure | 700 | Unsolved | Yes |
| 158 | [Forgotten Sales Backup](#challenge-158) | Sensitive Data Exposure | 700 | Unsolved | Yes |
| 161 | [GDPR Data Theft](#challenge-161) | Sensitive Data Exposure | 700 | Unsolved | Yes |
| 165 | [Leaked Unsafe Product](#challenge-165) | Sensitive Data Exposure | 700 | Unsolved | Yes |
| 224 | [Reset Uvogin's Password](#challenge-224) | Sensitive Data Exposure | 700 | Unsolved | Yes |
| 237 | [Login Cloud Admin](#challenge-237) | Sensitive Data Exposure | 700 | Unsolved | Yes |
| 146 | [Email Leak](#challenge-146) | Sensitive Data Exposure | 1000 | Unsolved | Yes |
| 194 | [Retrieve Blueprint](#challenge-194) | Sensitive Data Exposure | 1000 | Unsolved | Yes |
| 232 | [Leaked API Key](#challenge-232) | Sensitive Data Exposure | 1000 | Unsolved | Yes |
| 142 | [DOM XSS](#challenge-142) | XSS | 100 | Unsolved | Yes |
| 223 | [Bonus Payload](#challenge-223) | XSS | 100 | Unsolved | Yes |
| 188 | [Reflected XSS](#challenge-188) | XSS | 250 | Unsolved | Yes |
| 124 | [API-only XSS](#challenge-124) | XSS | 450 | Unsolved | Yes |
| 140 | [Client-side XSS Protection](#challenge-140) | XSS | 450 | Unsolved | Yes |
| 139 | [CSP Bypass](#challenge-139) | XSS | 700 | Unsolved | Yes |
| 162 | [HTTP-Header XSS](#challenge-162) | XSS | 700 | Unsolved | Yes |
| 199 | [Server-side XSS Protection](#challenge-199) | XSS | 700 | Unsolved | Yes |
| 208 | [Video XSS](#challenge-208) | XSS | 1350 | Unsolved | Yes |
| 149 | [Error Handling](#challenge-149) | Security Misconfiguration | 100 | Unsolved | Yes |
| 144 | [Deprecated Interface](#challenge-144) | Security Misconfiguration | 250 | Unsolved | Yes |
| 220 | [Misplaced IaC Files](#challenge-220) | Security Misconfiguration | 250 | Unsolved | Yes |
| 218 | [Cross-Site Imaging](#challenge-218) | Security Misconfiguration | 1000 | Unsolved | Yes |
| 173 | [Login Support Team](#challenge-173) | Security Misconfiguration | 1350 | Unsolved | Yes |
| 181 | [Outdated Allowlist](#challenge-181) | Unvalidated Redirects | 100 | Unsolved | Yes |
| 212 | [Allowlist Bypass](#challenge-212) | Unvalidated Redirects | 700 | Unsolved | Yes |
| 185 | [Privacy Policy](#challenge-185) | Miscellaneous | 100 | Unsolved | Yes |
| 197 | [Score Board](#challenge-197) | Miscellaneous | 100 | Unsolved | Yes |
| 229 | [Mass Dispel](#challenge-229) | Miscellaneous | 100 | Unsolved | Yes |
| 198 | [Security Policy](#challenge-198) | Miscellaneous | 250 | Unsolved | Yes |
| 230 | [Security Advisory](#challenge-230) | Miscellaneous | 450 | Unsolved | Yes |
| 133 | [Wallet Depletion](#challenge-133) | Miscellaneous | 1350 | Unsolved | Yes |
| 189 | [Repetitive Registration](#challenge-189) | Improper Input Validation | 100 | Unsolved | Yes |
| 216 | [Zero Stars](#challenge-216) | Improper Input Validation | 100 | Unsolved | Yes |
| 217 | [Missing Encoding](#challenge-217) | Improper Input Validation | 100 | Unsolved | Yes |
| 147 | [Empty User Registration](#challenge-147) | Improper Input Validation | 250 | Unsolved | Yes |
| 126 | [Admin Registration](#challenge-126) | Improper Input Validation | 450 | Unsolved | Yes |
| 132 | [Mint the Honey Pot](#challenge-132) | Improper Input Validation | 450 | Unsolved | Yes |
| 183 | [Payback Time](#challenge-183) | Improper Input Validation | 450 | Unsolved | Yes |
| 205 | [Upload Size](#challenge-205) | Improper Input Validation | 450 | Unsolved | Yes |
| 206 | [Upload Type](#challenge-206) | Improper Input Validation | 450 | Unsolved | Yes |
| 221 | [Deluxe Fraud](#challenge-221) | Improper Input Validation | 450 | Unsolved | Yes |
| 150 | [Expired Coupon](#challenge-150) | Improper Input Validation | 700 | Unsolved | Yes |
| 227 | [Poison Null Byte](#challenge-227) | Improper Input Validation | 700 | Unsolved | Yes |
| 219 | [Exposed Metrics](#challenge-219) | Observability Failures | 100 | Unsolved | Yes |
| 125 | [Access Log](#challenge-125) | Observability Failures | 700 | Unsolved | Yes |
| 175 | [Misplaced Signature File](#challenge-175) | Observability Failures | 700 | Unsolved | Yes |
| 164 | [Leaked Access Logs](#challenge-164) | Observability Failures | 1000 | Unsolved | Yes |
| 167 | [Login Admin](#challenge-167) | Injection | 250 | Unsolved | Yes |
| 233 | [Chatbot Prompt Injection](#challenge-233) | Injection | 250 | Unsolved | Yes |
| 143 | [Database Schema](#challenge-143) | Injection | 450 | Unsolved | Yes |
| 169 | [Login Bender](#challenge-169) | Injection | 450 | Unsolved | Yes |
| 171 | [Login Jim](#challenge-171) | Injection | 450 | Unsolved | Yes |
| 234 | [Greedy Chatbot Manipulation](#challenge-234) | Injection | 450 | Unsolved | Yes |
| 236 | [System Prompt Extraction](#challenge-236) | Injection | 450 | Unsolved | Yes |
| 138 | [Christmas Special](#challenge-138) | Injection | 700 | Unsolved | Yes |
| 148 | [Ephemeral Accountant](#challenge-148) | Injection | 700 | Unsolved | Yes |
| 178 | [NoSQL DoS](#challenge-178) | Injection | 700 | Unsolved | Yes |
| 180 | [NoSQL Manipulation](#challenge-180) | Injection | 700 | Unsolved | Yes |
| 207 | [User Credentials](#challenge-207) | Injection | 700 | Unsolved | Yes |
| 179 | [NoSQL Exfiltration](#challenge-179) | Injection | 1000 | Unsolved | Yes |
| 196 | [SSTi](#challenge-196) | Injection | 1350 | Unsolved | Yes |
| 182 | [Password Strength](#challenge-182) | Broken Authentication | 250 | Unsolved | Yes |
| 129 | [Bjoern's Favorite Pet](#challenge-129) | Broken Authentication | 450 | Unsolved | Yes |
| 160 | [GDPR Data Erasure](#challenge-160) | Broken Authentication | 450 | Unsolved | Yes |
| 192 | [Reset Jim's Password](#challenge-192) | Broken Authentication | 450 | Unsolved | Yes |
| 170 | [Login Bjoern](#challenge-170) | Broken Authentication | 700 | Unsolved | Yes |
| 190 | [Reset Bender's Password](#challenge-190) | Broken Authentication | 700 | Unsolved | Yes |
| 137 | [Change Bender's Password](#challenge-137) | Broken Authentication | 1000 | Unsolved | Yes |
| 191 | [Reset Bjoern's Password](#challenge-191) | Broken Authentication | 1000 | Unsolved | Yes |
| 203 | [Two Factor Authentication](#challenge-203) | Broken Authentication | 1000 | Unsolved | Yes |
| 211 | [Weird Crypto](#challenge-211) | Cryptographic Issues | 250 | Unsolved | Yes |
| 177 | [Nested Easter Egg](#challenge-177) | Cryptographic Issues | 700 | Unsolved | Yes |
| 153 | [Forged Coupon](#challenge-153) | Cryptographic Issues | 1350 | Unsolved | Yes |
| 163 | [Imaginary Challenge](#challenge-163) | Cryptographic Issues | 1350 | Unsolved | Yes |
| 184 | [Premium Paywall](#challenge-184) | Cryptographic Issues | 1350 | Unsolved | Yes |
| 136 | [CAPTCHA Bypass](#challenge-136) | Broken Anti Automation | 450 | Unsolved | Yes |
| 151 | [Extra Language](#challenge-151) | Broken Anti Automation | 1000 | Unsolved | Yes |
| 193 | [Reset Morty's Password](#challenge-193) | Broken Anti Automation | 1000 | Unsolved | Yes |
| 176 | [Multiple Likes](#challenge-176) | Broken Anti Automation | 1350 | Unsolved | Yes |
| 186 | [Privacy Policy Inspection](#challenge-186) | Security through Obscurity | 450 | Unsolved | Yes |
| 200 | [Steganography](#challenge-200) | Security through Obscurity | 700 | Unsolved | Yes |
| 130 | [Blockchain Hype](#challenge-130) | Security through Obscurity | 1000 | Unsolved | Yes |
| 213 | [XXE Data Access](#challenge-213) | XXE | 450 | Unsolved | Yes |
| 214 | [XXE DoS](#challenge-214) | XXE | 1000 | Unsolved | Yes |
| 238 | [Vulnerable Infrastructure](#challenge-238) | Vulnerable Components | 450 | Unsolved | Yes |
| 166 | [Legacy Typosquatting](#challenge-166) | Vulnerable Components | 700 | Unsolved | Yes |
| 210 | [Vulnerable Library](#challenge-210) | Vulnerable Components | 700 | Unsolved | Yes |
| 159 | [Frontend Typosquatting](#challenge-159) | Vulnerable Components | 1000 | Unsolved | Yes |
| 202 | [Supply Chain Attack](#challenge-202) | Vulnerable Components | 1000 | Unsolved | Yes |
| 204 | [Unsigned JWT](#challenge-204) | Vulnerable Components | 1000 | Unsolved | Yes |
| 228 | [Local File Read](#challenge-228) | Vulnerable Components | 1000 | Unsolved | Yes |
| 128 | [Arbitrary File Write](#challenge-128) | Vulnerable Components | 1350 | Unsolved | Yes |
| 156 | [Forged Signed JWT](#challenge-156) | Vulnerable Components | 1350 | Unsolved | Yes |
| 135 | [Blocked RCE DoS](#challenge-135) | Insecure Deserialization | 1000 | Unsolved | Yes |
| 215 | [Memory Bomb](#challenge-215) | Insecure Deserialization | 1000 | Unsolved | Yes |
| 201 | [Successful RCE DoS](#challenge-201) | Insecure Deserialization | 1350 | Unsolved | Yes |

## Scraped descriptions

<a id="challenge-122"></a>

### 122 — PCGCTF Juice Shop Gateway

Category: Reconnaissance  
Points: 100  
Status: Solved  
Tags: PCGCTF-JuiceShop-Challenges, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#PCGCTF%20Juice%20Shop%20Gateway-122)

Description

Welcome to the PCGCTF OWASP Juice Shop Laboratory.

This challenge is part of the PCGCTF Juice Shop Challenge Track.

All challenges belonging to the OWASP Juice Shop track are identified with the tag PCGCTF-JuiceShop-Challenges.

This challenge requires a local OWASP Juice Shop instance running on your machine.

The following files are provided with this challenge:

docker-compose.yml — Docker configuration for deploying the PCGCTF Juice Shop instance. PLAYER_SETUP.txt — Instructions for installing Docker, configuring the Juice Shop, setting the required CTF_KEY, and starting the application.

Complete the environment setup before beginning the challenge.

Target

Once the Juice Shop is running, access:

http://localhost:3000 Objective

Perform basic reconnaissance against your assigned Juice Shop instance.

Your first task is to locate the hidden Score Board within the application.

Investigate the web application and identify information that is intentionally exposed but not immediately visible from the main page.

The Score Board contains the information required to complete this challenge.

Mission

Find the hidden Score Board and obtain the flag associated with this challenge.

Submit the recovered flag to CTFd.

Flag Format pcgCTF{...}

Unlock Condition

Prerequisite: None

Successfully solving PCGCTF Gateway will unlock the next challenge in the progression.

Links exposed in the challenge:

- [http://localhost:3000](http://localhost:3000/)
- [docker-compose.yml](https://cgcybercom.online/files/d6d550192cdf8f728ca3b0c0aaf448d6/docker-compose.yml)
- [PCGCTF_JuiceShop_Player_Setup_Guide.txt](https://cgcybercom.online/files/cc4217d51cca7f4187d66c532feea19f/PCGCTF_JuiceShop_Player_Setup_Guide.txt)

<a id="challenge-134"></a>

### 134 — Web3 Sandbox

Category: Broken Access Control  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Web3, With Coding Challenge, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Web3%20Sandbox-134)

Find an accidentally deployed code sandbox for writing smart contracts on the fly.

<a id="challenge-127"></a>

### 127 — Admin Section

Category: Broken Access Control  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Good for Demos, With Coding Challenge, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Admin%20Section-127)

Access the administration section of the store.

<a id="challenge-152"></a>

### 152 — Five-Star Feedback

Category: Broken Access Control  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Five-Star%20Feedback-152)

Get rid of all 5-star customer feedback.

<a id="challenge-209"></a>

### 209 — View Basket

Category: Broken Access Control  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Tutorial, Good for Demos, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#View%20Basket-209)

View another user's shopping basket.

<a id="challenge-235"></a>

### 235 — AI Debugging

Category: Broken Access Control  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, AI/LLM, Requires LLM API, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#AI%20Debugging-235)

Reveal some behind-the-scenes information on the chatbot as a non-admin user.

<a id="challenge-154"></a>

### 154 — Forged Feedback

Category: Broken Access Control  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Tutorial, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Forged%20Feedback-154)

Post some feedback in another user's name.

<a id="challenge-155"></a>

### 155 — Forged Review

Category: Broken Access Control  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, With Coding Challenge, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Forged%20Review-155)

Post a product review as another user or edit any user's existing review.

<a id="challenge-174"></a>

### 174 — Manipulate Basket

Category: Broken Access Control  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Manipulate%20Basket-174)

Put an additional product into another user's shopping basket.

<a id="challenge-187"></a>

### 187 — Product Tampering

Category: Broken Access Control  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, With Coding Challenge, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Product%20Tampering-187)

Change the href of the link within the OWASP SSL Advanced Forensic Tool (O-Saft) product description into https://owasp.slack.com.

Links exposed in the challenge:

- [OWASP SSL Advanced Forensic Tool (O-Saft)](https://cgcybercom.online/#/search?q=OWASP%20SSL%20Advanced%20Forensic%20Tool%20(O-Saft))
- [https://owasp.slack.com](https://owasp.slack.com/)

<a id="challenge-222"></a>

### 222 — CSRF

Category: Broken Access Control  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#CSRF-222)

Change the name of a user by performing Cross-Site Request Forgery from another origin.

Links exposed in the challenge:

- [another origin](http://htmledit.squarefree.com/)

<a id="challenge-145"></a>

### 145 — Easter Egg

Category: Broken Access Control  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, Contraption, Good for Demos, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Easter%20Egg-145)

Find the hidden easter egg.

Links exposed in the challenge:

- [easter egg](https://en.wikipedia.org/wiki/Easter_egg_(media))

<a id="challenge-195"></a>

### 195 — SSRF

Category: Broken Access Control  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Code Analysis, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#SSRF-195)

Request a hidden resource on server through server.

<a id="challenge-141"></a>

### 141 — Confidential Document

Category: Sensitive Data Exposure  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Good for Demos, With Coding Challenge, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Confidential%20Document-141)

Access a confidential document.

<a id="challenge-123"></a>

### 123 — Password Hash Leak

Category: Sensitive Data Exposure  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Password%20Hash%20Leak-123)

Obtain the password (hash) of the currently logged-in user directly from a REST API endpoint.

<a id="challenge-131"></a>

### 131 — NFT Takeover

Category: Sensitive Data Exposure  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Contraption, Good for Demos, Web3, With Coding Challenge, rank:operator  
[Source challenge](https://cgcybercom.online/challenges#NFT%20Takeover-131)

Take over the wallet containing our official Soul Bound Token (NFT).

<a id="challenge-172"></a>

### 172 — Login MC SafeSearch

Category: Sensitive Data Exposure  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, OSINT, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Login%20MC%20SafeSearch-172)

Log in with MC SafeSearch's original user credentials without applying SQL Injection or any other bypass.

<a id="challenge-225"></a>

### 225 — Meta Geo Stalking

Category: Sensitive Data Exposure  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Meta%20Geo%20Stalking-225)

Determine the answer to John's security question by looking at an upload of him to the Photo Wall and use it to reset his password via the Forgot Password mechanism.

Links exposed in the challenge:

- [Forgot Password](https://cgcybercom.online/#/forgot-password)

<a id="challenge-226"></a>

### 226 — Visual Geo Stalking

Category: Sensitive Data Exposure  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Visual%20Geo%20Stalking-226)

Determine the answer to Emma's security question by looking at an upload of her to the Photo Wall and use it to reset her password via the Forgot Password mechanism.

Links exposed in the challenge:

- [Forgot Password](https://cgcybercom.online/#/forgot-password)

<a id="challenge-231"></a>

### 231 — Exposed Credentials

Category: Sensitive Data Exposure  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Exposed%20Credentials-231)

A developer was careless with hardcoding unused, but still valid credentials for a testing account on the client-side.

<a id="challenge-261"></a>

### 261 — Password Hash Leak

Category: Sensitive Data Exposure  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Password%20Hash%20Leak-261)

Obtain the password (hash) of the currently logged-in user directly from a REST API endpoint.

<a id="challenge-168"></a>

### 168 — Login Amy

Category: Sensitive Data Exposure  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Login%20Amy-168)

Log in with Amy's original user credentials. (This could take 93.83 billion trillion trillion centuries to brute force, but luckily she did not read the "One Important Final Note")

<a id="challenge-157"></a>

### 157 — Forgotten Developer Backup

Category: Sensitive Data Exposure  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Contraption, Good for Demos, Prerequisite, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Forgotten%20Developer%20Backup-157)

Access a developer's forgotten backup file.

<a id="challenge-158"></a>

### 158 — Forgotten Sales Backup

Category: Sensitive Data Exposure  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Contraption, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Forgotten%20Sales%20Backup-158)

Access a salesman's forgotten backup file.

<a id="challenge-161"></a>

### 161 — GDPR Data Theft

Category: Sensitive Data Exposure  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#GDPR%20Data%20Theft-161)

Steal someone else's personal data without using Injection.

<a id="challenge-165"></a>

### 165 — Leaked Unsafe Product

Category: Sensitive Data Exposure  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, OSINT, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Leaked%20Unsafe%20Product-165)

Identify an unsafe product that was removed from the shop and inform the shop which ingredients are dangerous.

Links exposed in the challenge:

- [inform the shop](https://cgcybercom.online/#/contact)

<a id="challenge-224"></a>

### 224 — Reset Uvogin's Password

Category: Sensitive Data Exposure  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, With Coding Challenge, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Reset%20Uvogin%27s%20Password-224)

Reset Uvogin's password via the Forgot Password mechanism with the original answer to his security question.

Links exposed in the challenge:

- [Forgot Password](https://cgcybercom.online/#/forgot-password)

<a id="challenge-237"></a>

### 237 — Login Cloud Admin

Category: Sensitive Data Exposure  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, With Coding Challenge, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Login%20Cloud%20Admin-237)

Log in with the cloud admin's user account without using SQL Injection.

<a id="challenge-146"></a>

### 146 — Email Leak

Category: Sensitive Data Exposure  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Email%20Leak-146)

Perform an unwanted information disclosure by accessing data cross-domain.

<a id="challenge-194"></a>

### 194 — Retrieve Blueprint

Category: Sensitive Data Exposure  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Retrieve%20Blueprint-194)

Deprive the shop of earnings by downloading the blueprint for one of its products.

<a id="challenge-232"></a>

### 232 — Leaked API Key

Category: Sensitive Data Exposure  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Leaked%20API%20Key-232)

Inform the shop about a leaked API key. (Mention the exact key in your comment)

Links exposed in the challenge:

- [Inform the shop](https://cgcybercom.online/#/contact)

<a id="challenge-142"></a>

### 142 — DOM XSS

Category: XSS  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Tutorial, Good for Demos, With Coding Challenge, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#DOM%20XSS-142)

Perform a DOM XSS attack with <iframe src="javascript:alert(xss)">.

<a id="challenge-223"></a>

### 223 — Bonus Payload

Category: XSS  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, Tutorial, With Coding Challenge, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Bonus%20Payload-223)

Use the bonus payload <iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&amp;color=%23ff5500&amp;auto_play=true&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&quot;&gt;&lt;/iframe> in the DOM XSS challenge.

Links exposed in the challenge:

- [https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&amp;color=%23ff5500&amp;auto_play=true&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&quot;&gt;&lt;/iframe](https://w.soundcloud.com/player/?url=https%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F771984076&amp%3Bcolor=%23ff5500&amp%3Bauto_play=true&amp%3Bhide_related=false&amp%3Bshow_comments=true&amp%3Bshow_user=true&amp%3Bshow_reposts=false&amp%3Bshow_teaser=true)

<a id="challenge-188"></a>

### 188 — Reflected XSS

Category: XSS  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Tutorial, Danger Zone, Good for Demos, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Reflected%20XSS-188)

Perform a reflected XSS attack with <iframe src="javascript:alert(xss)">.

<a id="challenge-124"></a>

### 124 — API-only XSS

Category: XSS  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, With Coding Challenge, rank:operator  
[Source challenge](https://cgcybercom.online/challenges#API-only%20XSS-124)

Perform a persisted XSS attack with <iframe src="javascript:alert(xss)"> without using the frontend application at all.

<a id="challenge-140"></a>

### 140 — Client-side XSS Protection

Category: XSS  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Client-side%20XSS%20Protection-140)

Perform a persisted XSS attack with <iframe src="javascript:alert(xss)"> bypassing a client-side security mechanism.

<a id="challenge-139"></a>

### 139 — CSP Bypass

Category: XSS  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#CSP%20Bypass-139)

Bypass the Content Security Policy and perform an XSS attack with <script>alert(xss)</script> on a legacy page within the application.

<a id="challenge-162"></a>

### 162 — HTTP-Header XSS

Category: XSS  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#HTTP-Header%20XSS-162)

Perform a persisted XSS attack with <iframe src="javascript:alert(xss)"> through an HTTP header.

<a id="challenge-199"></a>

### 199 — Server-side XSS Protection

Category: XSS  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Server-side%20XSS%20Protection-199)

Perform a persisted XSS attack with <iframe src="javascript:alert(xss)"> bypassing a server-side security mechanism.

<a id="challenge-208"></a>

### 208 — Video XSS

Category: XSS  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Video%20XSS-208)

Embed an XSS payload </script><script>alert(xss)</script> into our promo video.

<a id="challenge-149"></a>

### 149 — Error Handling

Category: Security Misconfiguration  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Prerequisite, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Error%20Handling-149)

Provoke an error that is neither very gracefully nor consistently handled.

<a id="challenge-144"></a>

### 144 — Deprecated Interface

Category: Security Misconfiguration  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Contraption, Prerequisite, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Deprecated%20Interface-144)

Use a deprecated B2B interface that was not properly shut down.

<a id="challenge-220"></a>

### 220 — Misplaced IaC Files

Category: Security Misconfiguration  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Prerequisite, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Misplaced%20IaC%20Files-220)

Access the misplaced Infrastructure as Code files that were accidentally included in the web application deliverable.

<a id="challenge-218"></a>

### 218 — Cross-Site Imaging

Category: Security Misconfiguration  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Contraption, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Cross-Site%20Imaging-218)

Stick cute cross-domain kittens all over our delivery boxes.

Links exposed in the challenge:

- [cute cross-domain kittens](https://cataas.com/cat)

<a id="challenge-173"></a>

### 173 — Login Support Team

Category: Security Misconfiguration  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Brute Force, Code Analysis, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Login%20Support%20Team-173)

Log in with the support team's original user credentials without applying SQL Injection or any other bypass.

<a id="challenge-181"></a>

### 181 — Outdated Allowlist

Category: Unvalidated Redirects  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Code Analysis, With Coding Challenge, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Outdated%20Allowlist-181)

Let us redirect you to one of our crypto currency addresses which are not promoted any longer.

<a id="challenge-212"></a>

### 212 — Allowlist Bypass

Category: Unvalidated Redirects  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Prerequisite, With Coding Challenge, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Allowlist%20Bypass-212)

Enforce a redirect to a page you are not supposed to redirect to.

<a id="challenge-185"></a>

### 185 — Privacy Policy

Category: Miscellaneous  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Good Practice, Tutorial, Good for Demos, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Privacy%20Policy-185)

Read our privacy policy.

<a id="challenge-197"></a>

### 197 — Score Board

Category: Miscellaneous  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Tutorial, Code Analysis, With Coding Challenge, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Score%20Board-197)

Find the carefully hidden 'Score Board' page.

<a id="challenge-229"></a>

### 229 — Mass Dispel

Category: Miscellaneous  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Mass%20Dispel-229)

Close multiple "Challenge solved"-notifications in one go.

<a id="challenge-198"></a>

### 198 — Security Policy

Category: Miscellaneous  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Good Practice, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Security%20Policy-198)

Behave like any "white-hat" should before getting into the action.

<a id="challenge-230"></a>

### 230 — Security Advisory

Category: Miscellaneous  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Security%20Advisory-230)

The Juice Shop is susceptible to a known vulnerability in a library, for which an advisory has already been issued, marking the Juice Shop as known affected. A fix is still pending. Inform the shop about a suitable checksum as proof that you did your due diligence.

Links exposed in the challenge:

- [Inform the shop](https://cgcybercom.online/#/contact)

<a id="challenge-133"></a>

### 133 — Wallet Depletion

Category: Miscellaneous  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Web3, With Coding Challenge, Requires Alchemy API Key, Requires Alchemy API, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Wallet%20Depletion-133)

Withdraw more ETH from the new wallet than you deposited.

<a id="challenge-189"></a>

### 189 — Repetitive Registration

Category: Improper Input Validation  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Repetitive%20Registration-189)

Follow the DRY principle while registering a user.

<a id="challenge-216"></a>

### 216 — Zero Stars

Category: Improper Input Validation  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Zero%20Stars-216)

Give a devastating zero-star feedback to the store.

<a id="challenge-217"></a>

### 217 — Missing Encoding

Category: Improper Input Validation  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Missing%20Encoding-217)

Retrieve the photo of Bjoern's cat in "melee combat-mode".

<a id="challenge-147"></a>

### 147 — Empty User Registration

Category: Improper Input Validation  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Empty%20User%20Registration-147)

Register a user with an empty email and password.

<a id="challenge-126"></a>

### 126 — Admin Registration

Category: Improper Input Validation  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, With Coding Challenge, rank:operator  
[Source challenge](https://cgcybercom.online/challenges#Admin%20Registration-126)

Register as a user with administrator privileges.

<a id="challenge-132"></a>

### 132 — Mint the Honey Pot

Category: Improper Input Validation  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Web3, With Coding Challenge, Requires Alchemy API Key, Requires Alchemy API, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Mint%20the%20Honey%20Pot-132)

Mint the Honey Pot NFT by gathering BEEs from the bee haven.

<a id="challenge-183"></a>

### 183 — Payback Time

Category: Improper Input Validation  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Payback%20Time-183)

Place an order that makes you rich.

<a id="challenge-205"></a>

### 205 — Upload Size

Category: Improper Input Validation  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Upload%20Size-205)

Upload a file larger than 100 kB.

<a id="challenge-206"></a>

### 206 — Upload Type

Category: Improper Input Validation  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:novice  
[Source challenge](https://cgcybercom.online/challenges#Upload%20Type-206)

Upload a file that has no .pdf or .zip extension.

<a id="challenge-221"></a>

### 221 — Deluxe Fraud

Category: Improper Input Validation  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Deluxe%20Fraud-221)

Obtain a Deluxe Membership without paying for it.

<a id="challenge-150"></a>

### 150 — Expired Coupon

Category: Improper Input Validation  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Expired%20Coupon-150)

Successfully redeem an expired campaign coupon code.

<a id="challenge-227"></a>

### 227 — Poison Null Byte

Category: Improper Input Validation  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Prerequisite, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Poison%20Null%20Byte-227)

Bypass a security control with a Poison Null Byte to access a file not meant for your eyes.

Links exposed in the challenge:

- [Poison Null Byte](https://hakipedia.com/index.php/Poison_Null_Byte)

<a id="challenge-219"></a>

### 219 — Exposed Metrics

Category: Observability Failures  
Points: 100  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Good Practice, With Coding Challenge, rank:apprentice  
[Source challenge](https://cgcybercom.online/challenges#Exposed%20Metrics-219)

Find the endpoint that serves usage data to be scraped by a popular monitoring system.

Links exposed in the challenge:

- [popular monitoring system](https://github.com/prometheus/prometheus)

<a id="challenge-125"></a>

### 125 — Access Log

Category: Observability Failures  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, With Coding Challenge, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Access%20Log-125)

Gain access to any access log file of the server.

<a id="challenge-175"></a>

### 175 — Misplaced Signature File

Category: Observability Failures  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Good Practice, Contraption, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Misplaced%20Signature%20File-175)

Access a misplaced SIEM signature file.

Links exposed in the challenge:

- [SIEM signature](https://github.com/Neo23x0/sigma)

<a id="challenge-164"></a>

### 164 — Leaked Access Logs

Category: Observability Failures  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Leaked%20Access%20Logs-164)

Dumpster dive the Internet for a leaked password and log in to the original user account it belongs to. (Creating a new account with the same password does not qualify as a solution.)

<a id="challenge-167"></a>

### 167 — Login Admin

Category: Injection  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Tutorial, Good for Demos, With Coding Challenge, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Login%20Admin-167)

Log in with the administrator's user account.

<a id="challenge-233"></a>

### 233 — Chatbot Prompt Injection

Category: Injection  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Good for Demos, AI/LLM, With Coding Challenge, Requires LLM API, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Chatbot%20Prompt%20Injection-233)

Trick the chatbot into generating a coupon code for you despite its coupon policy saying otherwise.

<a id="challenge-143"></a>

### 143 — Database Schema

Category: Injection  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, With Coding Challenge, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Database%20Schema-143)

Exfiltrate the entire DB schema definition via SQL Injection.

<a id="challenge-169"></a>

### 169 — Login Bender

Category: Injection  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Tutorial, With Coding Challenge, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Login%20Bender-169)

Log in with Bender's user account.

<a id="challenge-171"></a>

### 171 — Login Jim

Category: Injection  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Tutorial, With Coding Challenge, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Login%20Jim-171)

Log in with Jim's user account.

<a id="challenge-234"></a>

### 234 — Greedy Chatbot Manipulation

Category: Injection  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, AI/LLM, With Coding Challenge, Requires LLM API, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Greedy%20Chatbot%20Manipulation-234)

Convince the chatbot to give you a coupon of 50% or more. Because apparently a 10% max policy is just a suggestion when you ask nicely enough.

<a id="challenge-236"></a>

### 236 — System Prompt Extraction

Category: Injection  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, AI/LLM, Requires LLM API, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#System%20Prompt%20Extraction-236)

Extract the chatbot's system prompt using prompt injection, then submit your findings (including any confidential sections) via the Customer Complaint form.

Links exposed in the challenge:

- [Customer Complaint form](https://cgcybercom.online/#/complain)

<a id="challenge-138"></a>

### 138 — Christmas Special

Category: Injection  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Christmas%20Special-138)

Order the Christmas special offer of 2014.

<a id="challenge-148"></a>

### 148 — Ephemeral Accountant

Category: Injection  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Ephemeral%20Accountant-148)

Log in with the (non-existing) accountant acc0unt4nt@juice-sh.op without ever registering that user.

Links exposed in the challenge:

- [acc0unt4nt@juice-sh.op](mailto:acc0unt4nt@juice-sh.op)

<a id="challenge-178"></a>

### 178 — NoSQL DoS

Category: Injection  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#NoSQL%20DoS-178)

Let the server sleep for some time. (It has done more than enough hard work for you)

<a id="challenge-180"></a>

### 180 — NoSQL Manipulation

Category: Injection  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, With Coding Challenge, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#NoSQL%20Manipulation-180)

Update multiple product reviews at the same time.

<a id="challenge-207"></a>

### 207 — User Credentials

Category: Injection  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, With Coding Challenge, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#User%20Credentials-207)

Retrieve a list of all user credentials via SQL Injection.

<a id="challenge-179"></a>

### 179 — NoSQL Exfiltration

Category: Injection  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#NoSQL%20Exfiltration-179)

All your orders are belong to us! Even the ones which don't.

<a id="challenge-196"></a>

### 196 — SSTi

Category: Injection  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Contraption, Danger Zone, Code Analysis, rank:god  
[Source challenge](https://cgcybercom.online/challenges#SSTi-196)

Infect the server with juicy malware by abusing arbitrary command execution.

<a id="challenge-182"></a>

### 182 — Password Strength

Category: Broken Authentication  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Brute Force, Tutorial, With Coding Challenge, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Password%20Strength-182)

Log in with the administrator's user credentials without previously changing them or applying SQL Injection.

<a id="challenge-129"></a>

### 129 — Bjoern's Favorite Pet

Category: Broken Authentication  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, With Coding Challenge, rank:operator  
[Source challenge](https://cgcybercom.online/challenges#Bjoern%27s%20Favorite%20Pet-129)

Reset the password of Bjoern's OWASP account via the Forgot Password mechanism with the original answer to his security question.

Links exposed in the challenge:

- [Forgot Password](https://cgcybercom.online/#/forgot-password)

<a id="challenge-160"></a>

### 160 — GDPR Data Erasure

Category: Broken Authentication  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#GDPR%20Data%20Erasure-160)

Log in with Chris' erased user account.

<a id="challenge-192"></a>

### 192 — Reset Jim's Password

Category: Broken Authentication  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, With Coding Challenge, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Reset%20Jim%27s%20Password-192)

Reset Jim's password via the Forgot Password mechanism with the original answer to his security question.

Links exposed in the challenge:

- [Forgot Password](https://cgcybercom.online/#/forgot-password)

<a id="challenge-170"></a>

### 170 — Login Bjoern

Category: Broken Authentication  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Code Analysis, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Login%20Bjoern-170)

Log in with Bjoern's Gmail account without previously changing his password, applying SQL Injection, or hacking his Google account.

<a id="challenge-190"></a>

### 190 — Reset Bender's Password

Category: Broken Authentication  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, With Coding Challenge, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Reset%20Bender%27s%20Password-190)

Reset Bender's password via the Forgot Password mechanism with the original answer to his security question.

Links exposed in the challenge:

- [Forgot Password](https://cgcybercom.online/#/forgot-password)

<a id="challenge-137"></a>

### 137 — Change Bender's Password

Category: Broken Authentication  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Change%20Bender%27s%20Password-137)

Change Bender's password into slurmCl4ssic without using SQL Injection or Forgot Password.

<a id="challenge-191"></a>

### 191 — Reset Bjoern's Password

Category: Broken Authentication  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, With Coding Challenge, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Reset%20Bjoern%27s%20Password-191)

Reset the password of Bjoern's internal account via the Forgot Password mechanism with the original answer to his security question.

Links exposed in the challenge:

- [Forgot Password](https://cgcybercom.online/#/forgot-password)

<a id="challenge-203"></a>

### 203 — Two Factor Authentication

Category: Broken Authentication  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Two%20Factor%20Authentication-203)

Solve the 2FA challenge for user "wurstbrot". (Disabling, bypassing or overwriting his 2FA settings does not count as a solution)

<a id="challenge-211"></a>

### 211 — Weird Crypto

Category: Cryptographic Issues  
Points: 250  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:initiate  
[Source challenge](https://cgcybercom.online/challenges#Weird%20Crypto-211)

Inform the shop about an algorithm or library it should definitely not use the way it does.

Links exposed in the challenge:

- [Inform the shop](https://cgcybercom.online/#/contact)

<a id="challenge-177"></a>

### 177 — Nested Easter Egg

Category: Cryptographic Issues  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, Good for Demos, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Nested%20Easter%20Egg-177)

Apply some advanced cryptanalysis to find the real easter egg.

<a id="challenge-153"></a>

### 153 — Forged Coupon

Category: Cryptographic Issues  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Good for Demos, Code Analysis, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Forged%20Coupon-153)

Forge a coupon code that gives you a discount of at least 80%.

<a id="challenge-163"></a>

### 163 — Imaginary Challenge

Category: Cryptographic Issues  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, Code Analysis, rank:god  
[Source challenge](https://cgcybercom.online/challenges#Imaginary%20Challenge-163)

Solve challenge #999. Unfortunately, this challenge does not exist.

<a id="challenge-184"></a>

### 184 — Premium Paywall

Category: Cryptographic Issues  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Premium%20Paywall-184)

💎💎💎💎💎 ₿ Unlock Premium Challenge to access exclusive content.

Links exposed in the challenge:

- [₿ Unlock Premium Challenge](https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm)

<a id="challenge-136"></a>

### 136 — CAPTCHA Bypass

Category: Broken Anti Automation  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Brute Force, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#CAPTCHA%20Bypass-136)

Submit 10 or more customer feedbacks within 20 seconds.

<a id="challenge-151"></a>

### 151 — Extra Language

Category: Broken Anti Automation  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Brute Force, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Extra%20Language-151)

Retrieve the language file that never made it into production.

<a id="challenge-193"></a>

### 193 — Reset Morty's Password

Category: Broken Anti Automation  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, Brute Force, With Coding Challenge, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Reset%20Morty%27s%20Password-193)

Reset Morty's password via the Forgot Password mechanism with his obfuscated answer to his security question.

Links exposed in the challenge:

- [Forgot Password](https://cgcybercom.online/#/forgot-password)

<a id="challenge-176"></a>

### 176 — Multiple Likes

Category: Broken Anti Automation  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Multiple%20Likes-176)

Like any review at least three times as the same user.

<a id="challenge-186"></a>

### 186 — Privacy Policy Inspection

Category: Security through Obscurity  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, Good for Demos, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Privacy%20Policy%20Inspection-186)

Prove that you actually read our privacy policy.

<a id="challenge-200"></a>

### 200 — Steganography

Category: Security through Obscurity  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Shenanigans, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Steganography-200)

Rat out a notorious character hiding in plain sight in the shop. (Mention the exact name of the character)

Links exposed in the challenge:

- [Rat out](https://cgcybercom.online/#/contact)

<a id="challenge-130"></a>

### 130 — Blockchain Hype

Category: Security through Obscurity  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Contraption, Code Analysis, Web3, With Coding Challenge, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Blockchain%20Hype-130)

Learn about the Token Sale before its official announcement.

<a id="challenge-213"></a>

### 213 — XXE Data Access

Category: XXE  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#XXE%20Data%20Access-213)

Retrieve the content of C:\Windows\system.ini or /etc/passwd from the server.

<a id="challenge-214"></a>

### 214 — XXE DoS

Category: XXE  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#XXE%20DoS-214)

Give the server something to chew on for quite a while.

<a id="challenge-238"></a>

### 238 — Vulnerable Infrastructure

Category: Vulnerable Components  
Points: 450  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, With Coding Challenge, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Vulnerable%20Infrastructure-238)

Inform the shop about the use of a known vulnerable infrastructure component. (Identify the component as specifically as possible in your complaint)

Links exposed in the challenge:

- [Inform the shop](https://cgcybercom.online/#/complain)

<a id="challenge-166"></a>

### 166 — Legacy Typosquatting

Category: Vulnerable Components  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Legacy%20Typosquatting-166)

Inform the shop about a typosquatting trick it has been a victim of at least in v6.2.0-SNAPSHOT. (Mention the exact name of the culprit)

Links exposed in the challenge:

- [Inform the shop](https://cgcybercom.online/#/contact)

<a id="challenge-210"></a>

### 210 — Vulnerable Library

Category: Vulnerable Components  
Points: 700  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, rank:specialist  
[Source challenge](https://cgcybercom.online/challenges#Vulnerable%20Library-210)

Inform the shop about a high-severity vulnerability caused by one of its directly used dependencies. (Mention the exact library name and version in your comment)

Links exposed in the challenge:

- [Inform the shop](https://cgcybercom.online/#/contact)

<a id="challenge-159"></a>

### 159 — Frontend Typosquatting

Category: Vulnerable Components  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Frontend%20Typosquatting-159)

Inform the shop about a typosquatting imposter that dug itself deep into the frontend. (Mention the exact name of the culprit)

Links exposed in the challenge:

- [Inform the shop](https://cgcybercom.online/#/contact)

<a id="challenge-202"></a>

### 202 — Supply Chain Attack

Category: Vulnerable Components  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Supply%20Chain%20Attack-202)

Inform the development team about a danger to some of their credentials. (Send them the URL of the original report or an assigned CVE or another identifier of this vulnerability)

Links exposed in the challenge:

- [Inform the development team](https://cgcybercom.online/#/contact)

<a id="challenge-204"></a>

### 204 — Unsigned JWT

Category: Vulnerable Components  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Unsigned%20JWT-204)

Forge an essentially unsigned JWT token that impersonates the (non-existing) user jwtn3d@juice-sh.op.

Links exposed in the challenge:

- [jwtn3d@juice-sh.op](mailto:jwtn3d@juice-sh.op)

<a id="challenge-228"></a>

### 228 — Local File Read

Category: Vulnerable Components  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, OSINT, Danger Zone, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Local%20File%20Read-228)

Gain read access to an arbitrary local file on the web server.

<a id="challenge-128"></a>

### 128 — Arbitrary File Write

Category: Vulnerable Components  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, Prerequisite, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Arbitrary%20File%20Write-128)

Overwrite the Legal Information file.

Links exposed in the challenge:

- [Legal Information](https://cgcybercom.online/ftp/legal.md)

<a id="challenge-156"></a>

### 156 — Forged Signed JWT

Category: Vulnerable Components  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, rank:master  
[Source challenge](https://cgcybercom.online/challenges#Forged%20Signed%20JWT-156)

Forge an almost properly RSA-signed JWT token that impersonates the (non-existing) user rsa_lord@juice-sh.op.

Links exposed in the challenge:

- [rsa_lord@juice-sh.op](mailto:rsa_lord@juice-sh.op)

<a id="challenge-135"></a>

### 135 — Blocked RCE DoS

Category: Insecure Deserialization  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Blocked%20RCE%20DoS-135)

Perform a Remote Code Execution that would keep a less hardened application busy forever.

<a id="challenge-215"></a>

### 215 — Memory Bomb

Category: Insecure Deserialization  
Points: 1000  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Memory%20Bomb-215)

Perform a Remote Code Execution that would keep a less hardened application busy forever.


<a id="challenge-201"></a>

### 201 — Successful RCE DoS

Category: Insecure Deserialization  
Points: 1350  
Status: Unsolved  
Tags: PCGCTF-JuiceShop-Challenges, Danger Zone, rank:expert  
[Source challenge](https://cgcybercom.online/challenges#Successful%20RCE%20DoS-201)

Perform a Remote Code Execution that would keep a less hardened application busy forever.


## Attachments

Only the Gateway exposes direct file downloads (2). Existing downloaded copies are available here:

- [docker-compose.yml](../unsolved/reconnaissance/122-pcgctf-juice-shop-gateway/files/docker-compose.yml)
- [Player setup guide](../unsolved/reconnaissance/122-pcgctf-juice-shop-gateway/files/PCGCTF_JuiceShop_Player_Setup_Guide.txt)

Some descriptions contain app-relative links resolved by the challenge site to its own domain; these are preserved as scraped.
