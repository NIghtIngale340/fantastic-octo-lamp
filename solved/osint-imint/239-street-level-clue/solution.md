# Street-Level Clue — saved solution

Flag / submission candidate: `pcgCTF{Carnaby Street}`

Our original PCGCTF snapshot already marks this challenge solved. Independently inspected original photo: overhead arch reads WELCOME TO CARNABY STREET. Existing solved snapshot unchanged.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ## Street Photo Geolocation — OSINT / IMINT
>
> **Flag:** `pcgCTF{Carnaby Street}`
>
> **File:** `task2_1602089234031.jpg`
>
> #### Challenge
>
> Inspect the provided street photograph and identify the exact street using visible visual clues.
>
> #### Solution
>
> Metadata first, since a GPS tag would end the challenge immediately:
>
> ```bash
> exiftool task2_1602089234031.jpg
> strings -n 8 task2_1602089234031.jpg | grep -iE "ctf|flag|gps"
> ```
>
> No GPS data and no embedded flag. The only metadata is an Adobe Photoshop CC edit dated 2014-09-25, so the answer has to come from the image itself.
>
> Visual clues:
>
> - **Arch sign:** a banner spanning the street reads **"WELCOME TO CARNABY STREET"**.
> - **Building signage:** the shop on the right is labelled **"ON CARNABY STREET"**.
> - **Storefronts:** Fornarina on the left, Make Up Store on the right — both Carnaby Street retailers.
> - **Architecture:** narrow pedestrianised street, red-brick Georgian and Victorian frontages, hanging flower boxes — characteristic of Soho, London.
>
> Carnaby Street, Soho, London W1F. The arch is its best-known landmark.
>
> Flag formatting is worth noting: the answer keeps the space and capitalisation. If a submission is rejected, the variants to try are `carnaby street`, `Carnaby_Street`, `carnaby_street`.
>
> **Note (chat-rendered solve):** when the photo is viewed only as rendered in chat, its EXIF/metadata cannot be inspected, so exact capture coordinates cannot be verified from metadata alone. The solve then rests entirely on the visible clue — the overhead arch sign reading "WELCOME TO CARNABY STREET" — which identifies the street as Carnaby Street, London. Flag: `pcgCTF{Carnaby Street}`.
>
> ---
