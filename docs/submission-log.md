# Submission log — 29 October 2026 session

Nine flags were submitted and returned `status: correct` during this working session. Recorded by Antonio B. Garcia Jr.

This is the only record in the archive of which submissions the platform actually accepted. Several drafts elsewhere are marked *needs flag verification* precisely because no such record exists for them; the five Group A entries below are confirmed.

## Submission mechanism

The scoreboard is CTFd. Each flag was POSTed to `/api/v1/challenges/attempt` with the page CSRF nonce, wrapped as `pcgCTF{...}`, spaced 5 seconds apart.

```js
// run in the browser console on https://cgcybercom.online/challenges
await fetch('/api/v1/challenges/attempt', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'CSRF-Token': window.init.csrfNonce },
  body: JSON.stringify({ challenge_id: ID, submission: 'pcgCTF{...}' })
}).then(r => r.json());
```

CTFd rate-limits at roughly 10 attempts per minute. Exceeding it returns `status: ratelimited` rather than an error, and the attempt does not count — wait ~60 s and resend.

## Group A — forensic and OSINT recovery

These five already have full drafts; this log records that their flags were accepted.

| # | Challenge | Flag | Draft |
| ---: | --- | --- | --- |
| 69 | Bitcoin Trail | `pcgCTF{bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh}` | [069-bitcoin-trail.md](../writeups/solved/069-bitcoin-trail.md) |
| 73 | Bad Blockchain | `pcgCTF{192.168.200.48}` | [073-bad-blockchain.md](../writeups/solved/073-bad-blockchain.md) |
| 298 | EASY AS 123: Domain Pivot | `pcgCTF{vadusa.xyz}` | [298-act-1-easy-as-123-domain-pivot.md](../writeups/solved/298-act-1-easy-as-123-domain-pivot.md) |
| 299 | EASY AS 123: Protocol Deception | `pcgCTF{HTTP}` | [299-act-1-easy-as-123-protocol-deception.md](../writeups/solved/299-act-1-easy-as-123-protocol-deception.md) |
| 301 | YOU DIRTY RAT!: Identify the RAT | `pcgCTF{STRRAT}` | [301-act-2-you-dirty-rat-identify-the-rat.md](../writeups/solved/301-act-2-you-dirty-rat-identify-the-rat.md) |

Condensed method notes recovered with this log:

- **#69** — the capture `cryptocurrency_transfer_tracking.pcap` holds Bitcoin RPC JSON (`listunspent`, `sendtoaddress`) all referencing one wallet. Carve and dedupe the bech32 addresses: `strings cryptocurrency_transfer_tracking.pcap | grep -oE "bc1[a-z0-9]{20,}" | sort -u`.
- **#73** — the botnet hides C2 data in Bitcoin transaction fields (OP_RETURN and crafted output values); the embedded bytes decode to an internal IPv4.
- **#298** — the C2 IOC `45.131.214.85` pivots through passive DNS to `vadusa[.]xyz`.
- **#299** — traffic rides TCP 443 with no TLS handshake; request lines and the `NetSupport Manager/1.3` user agent are cleartext, so the application protocol is plain HTTP.
- **#301** — `tcp contains "STRRAT"` isolates the beacons, which open with the victim-profile marker `ping|STRRAT|` (version 1.6).

## Group B — Juice Shop, CTF-mode digest

Method and per-challenge detail: [broken-anti-automation.md](../writeups/solved/broken-anti-automation.md).

| # | Challenge | Flag | Note |
| ---: | --- | --- | --- |
| 136 | CAPTCHA Bypass | `pcgCTF{92410e6ae60168df4ae64e0d3cdc7bbcb1892f35}` | accepted first attempt |
| 151 | Extra Language | `pcgCTF{143e68b215685369977c1b7c97d2b077ae84fa44}` | accepted first attempt |
| 176 | Multiple Likes | `pcgCTF{14169cc1d31be7d8beaa636dfad6f3d702074be1}` | `ratelimited`, then `correct` after ~60 s |
| 193 | Reset Morty's Password | `pcgCTF{26f8acec1e8dfc89d7362f9afbe2e868b29edcc7}` | `ratelimited`, then `correct` after ~60 s |

## Provenance

Recovered on 29 October 2026 from the `Writeup(DAY2)` bundle, removed from the tree once its unique content was folded into the archive. Its twelve Day 2 screenshots were already present at [writeups/screenshots/day2/](../writeups/screenshots/day2/) and were verified byte-identical before the bundle was deleted.
