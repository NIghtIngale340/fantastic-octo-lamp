# Robots That Talk Too Much

## Challenge information

Platform: **PCGCTF** · ID **49** · Category: **Web Exploitation - DVWA** · Points: **200**. Difficulty was not supplied.

Saved status: **Unresolved**. No accepted flag or successful exploit is recorded for this ID.

[Original saved question](../../unsolved/web-exploitation-dvwa/049-robots-that-talk-too-much/README.md). The challenge points to `http://10.56.102.240:4280/`; no attachment is supplied. The task asks for a vulnerability name or discovery location rather than an artifact containing a literal flag.

## Reading the clue

**Concept indicated by the question:** Information disclosure through robots.txt.

Here the question asks for the weakness, not the filename requested in #39. Listing sensitive paths in robots.txt can advertise internal locations. The crawler rule does not make a path private. A directory mentioned there can still be harmless if independent access control protects it.

The saved inventory contains no earlier solution for this challenge. I compared the wording with the other DVWA questions before choosing an investigation: #39 and #49 refer to the same file but ask different things; #46 and #47 have duplicate descriptions. This prevents a title or a sibling flag from silently becoming evidence for this ID.

## Independent attempt and recorded result

The live prerequisite was checked with a bounded, read-only request. This is the Python request used by the batch evidence collector, with redirects deliberately disabled so an unrelated landing page could not look like the intended lab:

```python
requests.get('http://10.56.102.240:4280/', timeout=12, allow_redirects=False)
```

`timeout=12` bounds the connection/read wait. `allow_redirects=False` preserves the original endpoint’s response instead of following a redirect. The actual recorded result was **ConnectTimeout**, not a page containing a flag. [Raw request/error record](../evidence/web/endpoint-probes.json). The separate `/robots.txt` probe also failed to connect.

This establishes a reachability limit from the working environment at the recorded time. It does not prove the challenge is permanently offline, and it does not confirm or refute the suspected vulnerability. There is no response body to inspect here; reporting a working exploit would invent evidence.

## Reproduction and next investigative step

The following commands are a **specific next procedure, not successful historical execution**:

```sh
curl --connect-timeout 5 --max-time 12 -sS 'http://10.56.102.240:4280/robots.txt'
```

`curl` fetches the named lab resource. `--connect-timeout 5` limits connection establishment; `--max-time 12` bounds the whole request; `-sS` suppresses progress but preserves error messages. Where used, `-o` saves the response body, `-D` saves response headers, and `rg -n` prints matching lines with their line numbers. Run searches only after a genuine successful response, otherwise a missing file or error page can create misleading matches.

Capture a Disallow entry and the actual response from that challenge path. Record whether the issue is disclosed naming information, accessible content, or both; exact grader terminology is not recorded.

Record the actual result before interpreting it. A useful reproduction must connect the original clue to an observed resource or request, not simply identify a familiar OWASP label. [Technical reference](https://developers.google.com/search/docs/crawling-indexing/robots/intro) supports the underlying concept; it is not a source for the organizer’s exact flag string.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #49 — actual evidence capture

![049-actual-target-response.png](../screenshots/049-actual-target-response.png)

Fresh bounded read-only response or connection error; no invented exploit/flag. The actual connection failed; the screenshot does not show a working exploit or a recovered flag.

Command/action actually executed:

```sh
curl --connect-timeout 3 --max-time 6 -sS -D - http://10.56.102.240:4280/
```

[Actual command transcript](../screenshots/capture-work/049-reachability.terminal.log) · [Execution record](../screenshots/capture-work/049-reachability.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

**Blocked evidence:** bounded requests could not reach the challenge service. The failure was captured; an authenticated page, exploit result and any flag remain unverified.

## Flag discovery and final verification

The question suggests the concept above, but no platform-accepted string is preserved. In particular, we do not know whether the grader expects an acronym, expanded phrase, capitalization or spaces. The displayed wrapper is `pcgCTF{answer}`; it does not settle the text inside the braces.

[FINAL VERIFICATION NEEDED: Save the live hint/question, document the observation described above, then record one justified candidate and its actual submission response. Add the exact accepted string only after observing it.]

## Lesson and remaining limit

A publicly readable exclusion list can become an attacker’s navigation list. The current partial writeup establishes the interpretation and a reproducible next check. Its unresolved dependency is a response from the intended lab and the organizer’s accepted wording, not a missing screenshot disguised as a successful solve.
