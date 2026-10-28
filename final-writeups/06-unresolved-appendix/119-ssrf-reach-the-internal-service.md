# SSRF — Reach the Internal Service

## Challenge information

Platform: **PCGCTF** · ID **119** · Category: **Web Exploitation** · Points: **200**. Difficulty was not supplied.

Saved status: **Unresolved**. No accepted flag or successful exploit is recorded for this ID.

**Objective:** follow the [original task](../../unsolved/web-exploitation/119-ssrf-reach-the-internal-service/README.md) at `http://flag.cgcybercom.online/` and recover the flag or requested infrastructure fact. There is no direct attachment and no saved successful response for this ID. Expected wrapper: `pcgCTF{answer}`.

## Initial analysis

The application fetches a remote URL on behalf of the user. SSRF occurs when the server follows an attacker-chosen destination into its own internal network. The challenge specifically limits the objective to a loopback-bound service, but gives neither the proxy parameter nor the internal port.

I used the saved question to keep the target precise. The archive names both `flag1.cgcybercom.online` and `flag.cgcybercom.online`; they are separate hostnames. A path on the scoreboard is not an interchangeable replacement. Earlier notes also contain historical IP addresses, but those are not fixed target identities and should not be substituted for the current hostname without evidence.

## Independent attempt

A read-only GET was attempted to `http://flag.cgcybercom.online/` with a 12-second timeout and redirects disabled:

```python
requests.get('http://flag.cgcybercom.online/', timeout=12, allow_redirects=False)
```

The recorded result was **ConnectionError**. No HTTP response carrying the intended challenge page was available. [Actual probe log](../evidence/web/endpoint-probes.json) records the full error and time. This check observes reachability from this environment, not permanent site availability or vulnerability status.

That distinction controls the next step: there is no page source, upload form, proxy route, response header or Git object to analyze from this attempt. The following procedure therefore describes what to do after access is restored; it does not manufacture the missing output.

## Reproduction procedure and interpretation

```sh
curl --connect-timeout 5 --max-time 12 -sS http://flag.cgcybercom.online/ -o proxy-form.html
```

This is a **next-step command**, not recorded successful execution. `--connect-timeout 5` bounds connection setup, `--max-time 12` bounds the complete request, and `-sS` preserves diagnostic errors without a progress meter. `-D` captures headers where relevant; `-o` saves the actual response instead of mixing it with terminal messages. Any search over a saved file must follow a genuine successful HTTP fetch, not an error document.

Read the actual proxy form and capture its outbound-URL parameter from the lab’s own request. Use the service address/port discovered in the challenge, compare a public baseline with that loopback target, and preserve the internal flag response. No loopback request has been made through an observed proxy because no proxy endpoint was reachable.

Expected **kind** of result: the challenge resource and decisive proof described above. Exact response text is intentionally absent because it has not been observed. Preserve both the request and response so the writeup can explain why the returned value belongs to this challenge. [Primary technical reference](https://community.owasp.org/attacks/Server_Side_Request_Forgery) supports the mechanism; it does not supply this deployment’s flag.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #119 — actual evidence capture

![119-actual-target-response.png](../screenshots/119-actual-target-response.png)

Fresh bounded read-only response or connection error; no invented exploit/flag. The actual connection failed; the screenshot does not show a working exploit or a recovered flag.

Command/action actually executed:

```sh
curl --connect-timeout 3 --max-time 6 -sS -D - http://flag.cgcybercom.online/
```

[Actual command transcript](../screenshots/capture-work/119-reachability.terminal.log) · [Execution record](../screenshots/capture-work/119-reachability.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

**Blocked evidence:** bounded requests could not reach the challenge service. The failure was captured; an authenticated page, exploit result and any flag remain unverified.

## Flag and verification status

No final flag has been recovered for this ID. The preserved title and scenario identify the technique, but they do not prove a deployment-specific answer. No live exploit, uploaded server file or successful submission was performed during this investigation. Exact capitalization and separators remain unknown because the flag-bearing response is missing.

[FINAL VERIFICATION NEEDED: Restore access to http://flag.cgcybercom.online/; execute the bounded evidence-based procedure; save the raw response and screenshot; explain the transformation, if any, from that response to pcgCTF{...}; record the actual platform submission outcome.]

## Lesson and remaining work

A URL fetcher runs with the server’s network perspective, not the browser’s. The current result is a documented connection blocker and a specific reproduction path. The missing evidence is the service response that would connect the technique to a real flag.
