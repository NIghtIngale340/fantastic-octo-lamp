# Packet Detective — solution

Recovered answer: **zip**

Flag candidate:

```text
pcgCTF{zip}
```

Capture: `UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng`

Filter:

```wireshark
ftp.request.command == "RETR" || ftp-data.command contains "accountNum.zip"
```

Frames: 11831, 11837. TCP streams: 19, 20.

FTP RETR requests accountNum.zip in frame 11831; frame 11837 transfers a valid ZIP file. The two .jpg files earlier in the capture are FTP uploads (STOR), not this download. A Chrome extension .crx is also downloaded later over HTTP; because the question does not identify a protocol, the answer here follows the FTP download paired with the FTP Credential Leak question. The page says extension but gives a filename placeholder: accountNum.zip is the filename; zip is the extension. Exact grader wording remains unvalidated.

Platform acceptance: unconfirmed. No submissions made in this batch.
