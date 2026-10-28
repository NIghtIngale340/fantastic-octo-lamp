# Final writeup quality report

Checked: 2026-10-29T04:13:22+08:00.

- **192/192 individual challenge writeups**, with 146 complete explanatory drafts, 35 partial drafts and 11 unresolved investigations. Documentation status remains separate from competition status.
- **127,091 words**, **230 new genuine screenshots**, and **274 embedded image references** across all 192 drafts.
- **199 actual terminal runs:** 173 exited successfully; 26 bounded web requests recorded connection failures. Each has an actual transcript and execution record. A zero exit code does not itself mean a challenge was solved.
- The screenshot pass independently repeated all 11 intended Natas methods and next-level authentication checks, 11 read-only Aurora queries, and four Emedra challenge results. Runtime Natas passwords were redacted before terminal display/logging.
- #80’s JPEG-to-ZIP extraction was repeated using the known challenge password and workspace-only steghide from the official package repository. Archive hashes matched; no new password-cracking success is claimed.
- The #1 and #71 RockYou checks completed with no recovered password. Weak RSA remains unfactored; Rotation 36 remains rejected/unresolved.
- **1 broken local links; 0 unbalanced code fences** in the individual drafts. All 230 PNGs have capture-manifest SHA-256 entries.
- Dedicated missing-wording sections remain in #83/#102/#112; #18 retains its rejection diagnostic section.
- The original 81 PCGCTF and 11 OverTheWire solved counts remain unchanged. #77’s independently decoded bytes account for the previously documented change from 68 to 69 ready candidates and from 28 to 27 unresolved entries.
- No new PCGCTF flag submissions or acceptance claims were made.

## Remaining evidence limits

26 web challenge services were unavailable, seven original challenge payloads are missing, #319 lacks the original truck photo, and #261 has no target URL. Actual failure/inventory evidence is embedded. The exact wording cases, rejected flag, missing plaintexts and other unresolved answers remain explicit in the [verification queue](MISSING_EVIDENCE.md).

[Capture results](SCREENSHOT_PLAN.md) · [Capture audit and hashes](screenshots/capture-manifest.json) · [Machine-readable quality report](quality-report.json).
