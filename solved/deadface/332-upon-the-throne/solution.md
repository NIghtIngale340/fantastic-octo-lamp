# Upon the Throne — saved solution

Flag / submission candidate: `deadface{REVENANT-7}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### Upon the Throne (500) — Correlation / SQL
>
> **Flag:** `deadface{REVENANT-7}`
>
> #### Challenge
>
> A DEADFACE handler ran one insider on each side of the house. The handler's codename sits in a `handler_ref` field on both the audit-system users and the EHR providers. Around fifteen codenames appear on each side, but only one appears in both.
>
> #### Solution
>
> This is a set intersection across two databases. MySQL allows cross-database joins in a single query, so no export is needed:
>
> ```sql
> SELECT u.handler_ref, u.username, p.provider_id
> FROM aurora_audit.users u
> JOIN aurora_ehr.providers p
>   ON UPPER(TRIM(u.handler_ref)) = UPPER(TRIM(p.handler_ref))
> WHERE u.handler_ref IS NOT NULL AND TRIM(u.handler_ref) <> '';
> ```
>
> `UPPER(TRIM(...))` guards against case or whitespace differences between the two tables, which would otherwise hide a valid match.
>
> ```
> +------------+----------+-------------+
> | u_ref      | username | provider_id |
> +------------+----------+-------------+
> | REVENANT-7 | rborden  |           5 |
> +------------+----------+-------------+
> 1 row in set
> ```
>
> Sanity check on the population size — 16 distinct values on each side, matching the challenge's "around fifteen":
>
> ```sql
> SELECT COUNT(DISTINCT handler_ref) FROM aurora_audit.users;      -- 16
> SELECT COUNT(DISTINCT handler_ref) FROM aurora_ehr.providers;    -- 16
> ```
>
> One codename in both: `REVENANT-7`, running audit user `rborden` and EHR provider 5.
>
> ---
