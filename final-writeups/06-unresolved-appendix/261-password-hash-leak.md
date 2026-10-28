# Password Hash Leak

## Challenge information

Platform: **PCGCTF** · ID **261** · Category: **Sensitive Data Exposure** · Points: **250**. Difficulty was not supplied.

Saved status: **Unresolved**. No accepted flag or successful exploit is recorded for this ID.

The [entire saved task](../../unsolved/sensitive-data-exposure/261-password-hash-leak/README.md) is: obtain the currently logged-in user’s password hash directly from a REST API endpoint. No URL, endpoint, attachment or session workflow is provided. The archive’s other web tracks include several different hosts; assigning this question to one of them would be speculation.

## Initial analysis

The objective asks for a stored hash, not the plaintext password. A hash exposed by an API is still sensitive because an attacker can test password guesses offline. The phrase “currently logged-in user” also matters: returning a random account’s digest would not answer the task, even if it demonstrated an information leak.

I inspected the saved description, inventory and teammate notes. None contains a captured API response, digest, matching account ID, or a completed solution for #261. Other writeups discuss Juice Shop, but that alone does not establish this challenge’s target. This independent inventory check identified the missing starting information before sending credentials to an unrelated service.

## Reproducible next procedure

1. Open #261 in the original CTF platform and capture the full text, prerequisite and target link. This is the necessary first step; a command cannot discover an unspecified service safely or reproducibly.
2. Log into the intended challenge instance using the supplied training account. In browser DevTools, enable Network and filter Fetch/XHR. Perform the account/profile action referenced by the challenge, then inspect the actual REST response.
3. Match the response’s user identifier to the logged-in account. Inspect the exact JSON field containing the digest. A value called password is a clue, not proof of an algorithm or plaintext.
4. Save a sanitized request/response pair. For terminal reproduction, use the real request’s method and path, keeping session material in a private environment variable rather than in the public draft:

```sh
curl --connect-timeout 5 --max-time 12 -sS \
  -H "Authorization: Bearer $CTF_SESSION_TOKEN" \
  "$CONFIRMED_CTF_BASE_URL/$OBSERVED_API_PATH" -o account-response.json
```

This is an explicitly **unexecuted template**. `CTF_SESSION_TOKEN`, `CONFIRMED_CTF_BASE_URL` and `OBSERVED_API_PATH` must come from the intended lab; they are not discovered values. `-H` reproduces the actual authorization header only if the captured application uses one. A cookie-based session requires the corresponding captured cookie workflow instead. The command saves the real JSON with `-o`, and the two timeout flags prevent an indefinite wait.

```sh
python -m json.tool account-response.json
```

This formats a response that has actually been saved; no response or exact digest is asserted here. Identify the account and digest together before extracting a flag. Do not crack the hash unless a further task asks for the password: this task’s stated objective is the hash itself.

## Captured screenshots and evidence

Captured on 2026-10-29 from actual terminal sessions or browser views. Captions distinguish new results, preserved records, source images and blockers. No platform acceptance is inferred from these images.

### Challenge #261 — actual evidence capture

![261-actual-evidence-gap.png](../screenshots/261-actual-evidence-gap.png)

Read actual saved task to document missing target/API response, not a fabricated hash recovery.

Command/action actually executed:

```sh
cat /home/nightingale/CTF/PCGCTF/unsolved/sensitive-data-exposure/261-password-hash-leak/README.md
```

[Actual command transcript](../screenshots/capture-work/261-description.terminal.log) · [Execution record](../screenshots/capture-work/261-description.result.json). Notice the result fields discussed in the corresponding solution step; the transcript retains lines that extend beyond the screenshot viewport.

**Blocked evidence:** the saved prompt contains no target URL or original response. The available prompt was captured; no leaked hash or successful request is claimed.

## Result and lesson

This remains unresolved because no target or digest is present in the evidence. The useful next action is obtaining the original challenge linkage, not guessing an endpoint or a hash. API serializers should explicitly allow only fields intended for clients, excluding stored authentication material.
