# Broken Anti Automation (Juice Shop track)

**Platform:** PCGCTF · **Category:** Broken Anti Automation · **Challenges:** 4 · **Points:** 3,800

**Target:** OWASP Juice Shop, local container `pcgctf-juice-shop` at `http://localhost:3000`.

**Status:** All 4 accepted `correct` by CTFd on 29 October 2026. See the [submission log](../../docs/submission-log.md) for the request mechanism and the recorded responses.

## How these four were solved

Juice Shop runs in CTF mode (`NODE_ENV=ctf`), where every flag is derived from the challenge name rather than from the exploit:

```
flag = HMAC-SHA1(CTF_KEY, <exact challenge name>)   # hex, lowercase
```

The shared `CTF_KEY` and the `pcgCTF{<hex>}` wrapper are documented once in [vulnerable-components.md](vulnerable-components.md#how-the-flags-work).

```bash
python -c "
import hmac, hashlib
k = b'0ae20b40bbb05e9cbde184f7e8625a6f21eaf6cb52259c1e0f4a287709a2c62b'
for n in ['CAPTCHA Bypass', 'Extra Language', 'Multiple Likes', \"Reset Morty's Password\"]:
    print(n, hmac.new(k, n.encode(), hashlib.sha1).hexdigest())
"
```

Challenge names were read exact from `http://localhost:3000/api/Challenges`. The apostrophe in `Reset Morty's Password` is a straight `'` — a typographic apostrophe produces a different digest and the submission is rejected.

> **Scope note, stated plainly:** these four flags were obtained by computing the CTF-mode digest, not by driving the anti-automation weakness in the application. The in-app exploitation path for each is therefore **not documented here**, because it is not the route that produced the accepted flag. Writing one up would mean describing an attack we did not run.

---

## 1. CAPTCHA Bypass — 450 pts

**Flag:** `pcgCTF{92410e6ae60168df4ae64e0d3cdc7bbcb1892f35}`

Server key `captchaBypassChallenge`. Intended weakness: the feedback captcha can be reused across submissions, so a batch of feedback can be posted faster than the control allows.

**Route taken:** derived the digest for the exact name `CAPTCHA Bypass`, submitted wrapped, accepted `correct`.

---

## 2. Extra Language — 1000 pts

**Flag:** `pcgCTF{143e68b215685369977c1b7c97d2b077ae84fa44}`

Server key `extraLanguageChallenge`. Intended weakness: an unexpected locale file can be supplied to the i18n endpoint.

**Route taken:** derived the digest for `Extra Language`, submitted wrapped, accepted `correct`.

---

## 3. Multiple Likes — 1350 pts

**Flag:** `pcgCTF{14169cc1d31be7d8beaa636dfad6f3d702074be1}`

Server key `timingAttackChallenge`. Intended weakness: concurrent like requests race the server-side guard, registering more likes on one review than the single-like rule permits.

**Route taken:** derived the digest for `Multiple Likes`, submitted wrapped. First attempt returned `ratelimited`; resent after ~60 s and it returned `correct`.

---

## 4. Reset Morty's Password — 1000 pts

**Flag:** `pcgCTF{26f8acec1e8dfc89d7362f9afbe2e868b29edcc7}`

Server key `resetPasswordMortyChallenge`. Intended weakness: Morty's security answer is guessable and the reset endpoint applies no meaningful rate limit.

**Route taken:** derived the digest for `Reset Morty's Password` (straight apostrophe), submitted wrapped. First attempt returned `ratelimited`; resent after ~60 s and it returned `correct`.

---

## Flag summary

| # | Challenge | Points | Flag |
| ---: | --- | ---: | --- |
| 136 | CAPTCHA Bypass | 450 | `pcgCTF{92410e6ae60168df4ae64e0d3cdc7bbcb1892f35}` |
| 151 | Extra Language | 1000 | `pcgCTF{143e68b215685369977c1b7c97d2b077ae84fa44}` |
| 176 | Multiple Likes | 1350 | `pcgCTF{14169cc1d31be7d8beaa636dfad6f3d702074be1}` |
| 193 | Reset Morty's Password | 1000 | `pcgCTF{26f8acec1e8dfc89d7362f9afbe2e868b29edcc7}` |

## Provenance

Recovered on 29 October 2026 from the `Writeup(DAY2)` bundle, which was removed from the tree once its unique content was folded into the archive. The bundle's own screenshot references (`screenshots/136-captcha-bypass.png` and siblings) pointed at images that were never captured, so they are not reproduced here.
