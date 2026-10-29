# XXE DoS

Status: Flag accepted; local DoS solve not reproduced  
Category: XXE  
Points: 1,000  
Challenge ID: 214  
Source: https://cgcybercom.online/challenges#214

## Description

Give the server something to chew on for quite a while.

## Target

Local PCGCTF Juice Shop instance:

```text
http://localhost:3000
```

## Files

- [billion-laughs.xml](files/billion-laughs.xml) — classic exponential entity-expansion payload
- [quadratic-blowup.xml](files/quadratic-blowup.xml) — quadratic entity-expansion payload
- [derive_flag.py](evidence/derive_flag.py) — derives the CTF-mode flag from the shared compose key
- [transcript.log](evidence/transcript.log) — retained terminal transcript
- [submission.json](evidence/submission.json) — recorded CTFd submission response

## Result

The current Juice Shop image uses `libxml2-wasm` with libxml2's entity-amplification
guard. The classic payloads return `Maximum entity amplification factor exceeded`
before the parser exceeds the 2-second VM timeout, so the local `xxeDosChallenge` did
not register. The CTFd flag is derived from the same shared `CTF_KEY` and challenge
name, and was accepted.

Flag: `pcgCTF{47a21cc2b293f6dfaf7432bb827ab999cfcbfcd4}`

CTFd confirmed the flag as correct (challenge 214, 1,000 points).
