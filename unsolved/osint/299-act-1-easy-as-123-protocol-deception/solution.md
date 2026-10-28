# ACT 1 - EASY AS 123: Protocol Deception — verified answer evidence

Answer: **HTTP**

Flag candidate:

```text
pcgCTF{HTTP}
```

## Independent verification

In the original 2026-02-28 capture, a fresh TShark decode-as for TCP 443 yields 264 readable HTTP requests to 45.131.214.85. Frame 2638 is a POST to http://45.131.214.85/fakeurl.htm with user agent NetSupport Manager/1.3. Readable HTTP headers and URL-encoded content establish the requested cleartext application protocol. The [firsthand analyst report](https://rvmchua.com/posts/mta-easy-as-123/) agrees.

## Reproducible local evidence

- [Verification evidence](../../../analysis-team-verification/netsupport-http.tsv)
- [Capture identities, filters, counts and first packets](../../../analysis-team-verification/packet-checks.json)
- [Recorded primary public-source observations](../../../analysis-team-verification/public-source-observations.json)

## Limits

Confirmed for the cited C2 requests; this does not claim there is no TLS elsewhere in the capture. This is an evidence-backed answer and saved submission candidate, not a verified PCGCTF acceptance.

Provenance: initially suggested in Antonio B. Garcia Jr.’s potential writeups; independently checked against the sources and original evidence above on 2026-10-28.
