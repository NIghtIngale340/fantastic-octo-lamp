# The Hidden Download

**Platform:** PCGCTF · **Challenge ID:** 62 · **Category:** Network Analysis · **Points:** 100

**Status:** Answer backed by the capture. Exact PCGCTF submission not re-confirmed. (Same capture/answer as HTTP File Extraction #70.)

## The challenge

Recover the text inside a ZIP downloaded over HTTP.

## Solving it

The capture carries the file bytes, not just URLs, so I found the ZIP response and exported it:

```sh
tshark -nr http_file_extraction.pcap -Y http -T fields -e http.request.uri -e http.content_type
tshark -r http_file_extraction.pcap --export-objects http,/tmp/out
unzip -p /tmp/out/password.zip password.txt
```

```text
my password is:
Cx689iO7Fu4G
```

## Screenshot

![062-packet-proof.png](../screenshots/062-packet-proof.png)

## Flag

```text
pcgCTF{Cx689iO7Fu4G}
```

## Takeaway

Reconstruct the HTTP object and read the member — grepping packet strings would miss anything inside a compressed archive.

## Reference

- [Original challenge description](../../unsolved/network-analysis/062-the-hidden-download/README.md)
