# FTP Credential Leak — solution

Recovered answer: **AfricaCTF2021**

Flag candidate:

```text
pcgCTF{AfricaCTF2021}
```

Capture: `UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng`

Filter:

```wireshark
ftp.request.command == "PASS" || ftp.response.code == 230
```

Frames: 500, 502, 587, 11816. TCP streams: 10, 13, 19.

The shared evidence is the parent Packet Detective capture. FTP PASS exposes AfricaCTF2021; frame 502 reports Login successful. The username is kali. Repeated sessions show the same password.

Platform acceptance: unconfirmed. No submissions made in this batch.
