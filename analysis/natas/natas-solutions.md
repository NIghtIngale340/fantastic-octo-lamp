# Natas 0–10 — solution chain

Solved live on 2026-10-28. Each level's password is the answer to the challenge for the *next* level, so the table lists the recovered secret per challenge.

| ID | Challenge | Level | Answer (next password) | Method |
| ---: | --- | --- | --- | --- |
| 6 | Hidden in Plain Sight | natas0 | `scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7` | HTML comment in source |
| 7 | Access Denied? Think Again | natas1 | `vsDOxoXyq3wckCP1ZmTZ71ngIA606odB` | Source despite right-click block |
| 8 | Forgotten Files | natas2 | `K30JrSRHzjxq3paUQuwozY4MNvmNFyhI` | `/files/` directory listing + `users.txt` |
| 9 | Robots Know Everything | natas3 | `JDrPnuZAKyl6MkiqQGFIddrqpvgOASth` | `robots.txt` → `/s3cr3t/users.txt` |
| 10 | Trust the Referer | natas4 | `e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M` | Forged `Referer` header |
| 12 | The Cookie Jar | natas5 | `7mhjtShJAcld2NYbKHEadnhEwRn2P8VT` | `loggedin=1` cookie |
| 13 | The Exposed Script | natas6 | `B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0` | Read `includes/secret.inc`, POST secret |
| 14 | Path Explorer | natas7 | `ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc` | LFI `?page=/etc/natas_webpass/natas8` |
| 15 | Layers of Encoding | natas8 | `UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9` | Reverse hex → strrev → base64 |
| 16 | Command Me | natas9 | `EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv` | `; cat /etc/natas_webpass/natas10 #` |
| 17 | Filtered but Broken | natas10 | `VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd` | `.* /etc/natas_webpass/natas11` (extra grep file arg) |

Flag candidates are the passwords wrapped as `pcgCTF{...}` (for example `pcgCTF{scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7}`). The wrapper is inferred from the challenge text `FLAG: pcgCTF{***hash***}`; platform acceptance was not tested.

Full command transcripts and output excerpts are in each challenge folder as `solution.md`.

## Chain verification

The recovered passwords form a working chain; the final credential was confirmed with:

```bash
curl -sS -o /dev/null -w 'natas11 HTTP %{http_code}\n' \
  -u 'natas11:VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd' \
  http://natas11.natas.labs.overthewire.org/
```

```text
natas11 HTTP 200
```

Natas rotates passwords periodically, so these values may stop working later.

## Verification status update

All 11 passwords verified live on OverTheWire at 2026-10-28T22:37:26+08:00. [Verification report](verification.md). PCGCTF scoreboard acceptance remains unconfirmed.
