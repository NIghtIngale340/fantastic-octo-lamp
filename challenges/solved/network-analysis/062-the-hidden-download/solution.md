# THE HIDDEN DOWNLOAD — solution

Recovered answer: **Cx689iO7Fu4G**

Flag candidate:

```text
pcgCTF{Cx689iO7Fu4G}
```

Capture: `http_file_extraction.pcap`

Filter:

```wireshark
http
```

Frames: 11, 13. TCP streams: 0.

Frame 11 requests http://mywebsite.hv/password.zip. Frame 13 returns application/zip. The exported ZIP contains password.txt with the text: my password is: followed by Cx689iO7Fu4G. ZIP integrity was checked.

Platform acceptance: unconfirmed. No submissions made in this batch.
