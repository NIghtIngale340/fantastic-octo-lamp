# HTTP File Extraction

**Platform:** PCGCTF · **Challenge ID:** 70 · **Category:** Network Analysis · **Points:** 150

**Status:** Solved in the last snapshot; reproduced locally. (This capture is byte-identical to Hidden Download #62 — same file, reused extraction.)

**Evidence:** Packets 11, 13 · TCP stream 0 · [http_file_extraction.pcap](../../solved/network-analysis/070-http-file-extraction/files/http_file_extraction.pcap).

## The challenge

A ZIP was downloaded over HTTP in a packet capture. Pull it out and read the password in its text file.

## Solving it

The capture contains an HTTP download of `password.zip`. Locate the request and response:

```sh
tshark -nr http_file_extraction.pcap -Y http -T fields -e frame.number -e http.request.uri -e http.content_type
```

```text
11	/password.zip
13	/password.zip	application/zip
```

Then export the HTTP objects, check the archive, and print the member:

```sh
tshark -q -r http_file_extraction.pcap --export-objects http,objects
unzip -p objects/password.zip password.txt
```

```text
my password is:
Cx689iO7Fu4G
```

The password in `password.txt` is `Cx689iO7Fu4G`. Preserve its case when submitting it.

## Screenshots

Fresh local reproduction using the commands described above.

![Command and result](../screenshots/070-final-method.png)

## Flag

```text
pcgCTF{Cx689iO7Fu4G}
```

## Takeaway

Reassemble the actual object instead of grepping raw packet bytes, and keep the secret inside the file distinct from transport metadata around it.

## References

- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/network-analysis/070-http-file-extraction/README.md>)
- [Extracted archive](</home/nightingale/CTF/PCGCTF/analysis-network-analysis/hidden-download-objects/password.zip>)
