# Web Recon — View Source

**Platform:** PCGCTF · **Challenge ID:** 113 · **Category:** Web Exploitation · **Points:** 150

**Status:** Unresolved. The technique is clear from the clue, but the target (http://flag1.cgcybercom.online/) wasn't reachable from here, so there's no response to work with and no confirmed flag. Honest stub.

## The challenge

A flag is hidden in the page's HTML source.

## What I could do

The approach is to view source (or `curl` the page) and read it — comments and hidden elements included.

I probed the target read-only:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://flag1.cgcybercom.online/
```

The connection timed out — no response body. Reporting a working exploit here would be inventing evidence.

## Screenshot

![113-web-recon-view-source-actual-target-response.png](../screenshots/113-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered — target unreachable, and the exact string inside `pcgCTF{...}` isn't known.

## Still to do

- Reach the target from an authorized network, run the check above, and record one justified candidate with its real submission result.

## Takeaway

Anything the server sends to render a page is readable; view-source is the first recon step.

## Reference

- [Original challenge description](../../unsolved/web-exploitation/113-web-recon-view-source/README.md)
