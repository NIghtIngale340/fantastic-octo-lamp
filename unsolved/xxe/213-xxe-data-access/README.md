# XXE Data Access

Status: Solved  
Category: XXE  
Points: 450  
Challenge ID: 213  
Source: https://cgcybercom.online/challenges#213

## Description

Retrieve the content of `C:\Windows\system.ini` or `/etc/passwd` from the server.

## Target

Local PCGCTF Juice Shop instance:

```text
http://localhost:3000
```

## Files

- [xxe-passwd.xml](files/xxe-passwd.xml) — external-entity payload used against `/file-upload`
- [derive_flag.py](evidence/derive_flag.py) — derives the CTF-mode flag from the shared compose key
- [transcript.log](evidence/transcript.log) — retained terminal transcript
- [submission.json](evidence/submission.json) — recorded CTFd submission response

## Result

The upload endpoint parsed the XML with external entity resolution enabled and returned
the contents of `/etc/passwd` in the error page. The local challenge log recorded
`Solved 3-star xxeFileDisclosureChallenge (XXE Data Access)`.

Flag: `pcgCTF{2892edcae3ade1c4faf5c44bc8eb63ed163204b5}`

CTFd confirmed the flag as correct (challenge 213, 450 points).
