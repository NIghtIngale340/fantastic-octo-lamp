# Network Analysis answers

Five challenges from the unsolved folder analyzed; the already site-solved duplicate #70 is included for reference. No new submissions or acceptance claims.

| ID | Challenge | Answer | Flag candidate |
| ---: | --- | --- | --- |
| 21 | [Packet Detective](../../challenges/unsolved/network-analysis/021-packet-detective/solution.md) | `zip` | `pcgCTF{zip}` |
| 22 | [FTP Credential Leak](../../challenges/solved/network-analysis/022-ftp-credential-leak/solution.md) | `AfricaCTF2021` | `pcgCTF{AfricaCTF2021}` |
| 61 | [The Exposed Password](../../challenges/unsolved/network-analysis/061-the-exposed-password/solution.md) | `John1234!` | `pcgCTF{John1234!}` |
| 62 | [THE HIDDEN DOWNLOAD](../../challenges/solved/network-analysis/062-the-hidden-download/solution.md) | `Cx689iO7Fu4G` | `pcgCTF{Cx689iO7Fu4G}` |
| 69 | [Bitcoin Trail](../../challenges/solved/network-analysis/069-bitcoin-trail/solution.md) | `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh` | `pcgCTF{bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh}` |
| 70 | [HTTP File Extraction](../../challenges/solved/network-analysis/070-http-file-extraction/solution.md) | `Cx689iO7Fu4G` | `pcgCTF{Cx689iO7Fu4G}` |

**Packet Detective ambiguity:** The FTP download is `accountNum.zip` (extension `zip`); the capture also includes a later HTTP Chrome-extension download. The recovered FTP archive is valid, but the short question does not disambiguate protocol or filename versus extension. The writeup records this limitation.

All cited frames were checked, the successful HVBank response was correlated to the correct password attempt, and the recovered password ZIP passed its integrity check. Original captures were preserved.
