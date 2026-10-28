# Two Places at Once — saved solution

Flag / submission candidate: `deadface{kbhat}`

Our original PCGCTF snapshot already marks this challenge solved. Garcia reports accepted spelling kbhat; underlying database username is kbhatt. Acceptance spelling is a teammate report, not newly tested.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Important spelling distinction

The writeup’s query returns `kbhatt`, while its reported accepted submission is `deadface{kbhat}`. Both are preserved explicitly.

## Teammate’s writeup (quoted)

> ### Two Places at Once (450) — Compromised Account / SQL
>
> **Flag:** `deadface{kbhat}`  *(accepted spelling — single `t`; see note below)*
>
> #### Challenge
>
> DEADFACE bragged on the GhostTown forum about using one legitimate account from two places at once. Find the compromised account — the one whose login shows up on two different workstations at the very same timestamp, over and over. Report the username.
>
> #### Solution
>
> The evidence lives in `aurora_audit.access_log`, which records one row per access with `user_id`, `workstation`, `ip_address`, `action` and `accessed_at`. "Two places at once" means the same account on two distinct workstations at an identical timestamp — a physical impossibility for a real person.
>
> Group by account and timestamp, and keep only groups spanning more than one workstation:
>
> ```sql
> SELECT u.user_id, u.username, COUNT(*) AS collisions
> FROM (
>   SELECT user_id, accessed_at
>   FROM aurora_audit.access_log
>   GROUP BY user_id, accessed_at
>   HAVING COUNT(DISTINCT workstation) > 1
> ) t
> JOIN aurora_audit.users u ON u.user_id = t.user_id
> GROUP BY u.user_id, u.username
> ORDER BY collisions DESC;
> ```
>
> ```
> +---------+----------+------------+
> | user_id | username | collisions |
> +---------+----------+------------+
> |      16 | kbhatt   |          8 |
> +---------+----------+------------+
> ```
>
> Exactly one account, and the "over and over" in the prompt is literal: 8 separate collisions. The colliding rows show the pattern plainly:
>
> ```sql
> SELECT user_id, accessed_at, GROUP_CONCAT(workstation) AS ws,
>        GROUP_CONCAT(ip_address) AS ips
> FROM aurora_audit.access_log
> GROUP BY user_id, accessed_at
> HAVING COUNT(DISTINCT workstation) > 1;
> ```
>
> ```
> | 16 | 2025-11-04 23:54:03 | WS-028,WS-008 | 10.20.3.222,10.20.3.213 |
> | 16 | 2025-11-05 23:55:55 | WS-013,WS-025 | 10.20.1.125,10.20.2.18  |
> | 16 | 2025-11-14 02:18:01 | WS-002,WS-023 | 10.20.4.88,10.20.4.21   |
> | 16 | 2025-11-18 01:23:54 | WS-027,WS-015 | 10.20.2.200,10.20.4.176 |
> | 16 | 2025-11-19 02:37:21 | WS-026,WS-008 | 10.20.3.76,10.20.4.54   |
> | 16 | 2025-11-21 02:51:31 | WS-029,WS-018 | 10.20.1.49,10.20.2.101  |
> | 16 | 2025-11-23 02:29:51 | WS-030,WS-006 | 10.20.4.52,10.20.2.100  |
> | 16 | 2025-11-27 03:57:17 | WS-022,WS-011 | 10.20.4.227,10.20.2.165 |
> ```
>
> Every pair is a different workstation and a different internal IP at the exact same second, all during overnight hours (23:54–03:57). Of the 432 rows in the table, 416 fall on an exact minute (`:00` seconds) and the 16 odd-second rows are precisely these 8 planted pairs — the anomaly stands out even before the join.
>
> `user_id 16` is `kbhatt` (Kavya Bhatt), the only account with the role **Registered Nurse**. That matches DEADFACE's own brag on GhostTown (thread 49, *"Shelby Medical Center really thought nobody would notice?"* by `luciafer`): a socially-engineered registered nurse, VPN access with her valid credentials, both parties logged in at once — *"Same credentials. Same moments. Different workstations."* — including `print` and `export` actions, which appear in her log rows.
>
> **Verification / the gotcha:** the database stores the username as `kbhatt` (double `t`), but the scoreboard only accepts **`deadface{kbhat}`** with a single `t`. The challenge author mistyped the flag when setting it, so the "correct" database value is rejected and the typo is required. This is why every `deadface{kbhatt}` submission failed despite the query being right. If a `deadface{...}` answer keeps bouncing when the data clearly supports it, suspect an author-side typo and try the obvious misspellings before assuming the data is wrong.
>
> ---
