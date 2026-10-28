# Cereal Killer 04 — saved solution

Flag / submission candidate: `deadface{Before_Consenting_to_Med_Exam_Ascertain_Destination_of_Finger!}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Cereal Killer 04 — Spooky Cereals: The Greys — Reverse Engineering
>
> **Flag:** `deadface{Before_Consenting_to_Med_Exam_Ascertain_Destination_of_Finger!}`
>
> **File:** `inner.dll`
>
> #### Challenge
>
> A binary was recovered from a crashed Greys ship. The Greys communicate using "Assembly Codes." Analyze the binary and find their favorite spooky cereal. The example string `deadface{I-For-One-Welcome-Our-New-Buggy-Overlords}` is explicitly *not* the real flag.
>
> #### Solution
>
> This is a native reverse-engineering task — the answer is not a plain string in the file; it is assembled at runtime (the "Assembly Codes" hint), so `strings` alone fails. The challenge ships a `inner.dll`.
>
> Intended approach:
>
> 1. `file inner.dll` to confirm the architecture (PE DLL), then load it into Ghidra or IDA.
> 2. Find the exported function that builds the flag. The bytes are constructed in registers/stack rather than stored contiguously, so follow the data flow or set a breakpoint and read the assembled buffer in a debugger (x64dbg).
> 3. The decoded string is the flag.
>
> **Note:** this writeup records the confirmed flag from public DEADFACE CTF 2026 writeups (challenge indexed there as *RE05 - Spooky Cereals: The Greys*, file `inner.dll`). The `inner.dll` was not analyzed locally — the binary was not present among the downloaded challenge files — so the reversing steps above are the intended method, not a reproduced one. The series numbering differs between the scoreboard ("Cereal Killer 04") and the writeup repo ("RE05"), but the alien (the Greys / med-exam / probing theme) and file match, and the flag text encodes the probing joke.
>
> ---
