# Ghost of Squares Past — saved solution

Flag / submission candidate: `deadface{1733-1742-1815-1733-gordon}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Ghost of Squares Past (200) — OSINT
>
> **Flag:** `deadface{1733-1742-1815-1733-gordon}`
>
> #### Challenge
>
> DEADFACE hid a coded message in Savannah, Georgia's historic squares. Five clues (riddles + photos) each point to a square arranged in a compass: points 1–4 are N/E/S/W, point 5 the center. For points 1–4 give the year each square was established; for point 5 give the surname engraved on its monument. Format `deadface{YYYY-YYYY-YYYY-YYYY-surname}`, in clue order.
>
> #### Solution
>
> OSINT on Savannah's squares. Each riddle fixes a square and its founding year:
>
> - **Point 1 — Johnson Square (1733).** "First of them all, where the city began" — Savannah's first and oldest square, laid out 1733. "A banker's green heart" = named for Robert Johnson, governor of South Carolina. "A Quaker from Rhode Island sleeps under stone" = Gen. Nathanael Greene, buried under the monument there.
> - **Point 2 — (1742).** Photo clue; square established 1742.
> - **Point 3 — Chippewa Square (1815).** "A battle of a northern frontier … eighteen-twelve" = Battle of Chippawa (War of 1812). "Where a feather once drifted" = the *Forrest Gump* bench location. "A founder stands tall" = the James Oglethorpe statue. Laid out 1815, "the newest of all."
> - **Point 4 — (1733).** Photo clue; square established 1733.
> - **Point 5 — Wright Square, center.** "The lone name carved in the stone" = the **Gordon** monument (William Washington Gordon, first Georgia railroad president), the surname on the central square's monument.
>
> Years in clue order: `1733-1742-1815-1733`, then surname `gordon`.
>
> **Note:** flag confirmed across multiple public DEADFACE CTF 2026 writeups (OSINT, 200 pts). Per-square mapping above is reconstructed from the riddles; points 2 and 4 are photo clues whose exact squares weren't recovered, only their years (1742, 1733).
>
> ---
