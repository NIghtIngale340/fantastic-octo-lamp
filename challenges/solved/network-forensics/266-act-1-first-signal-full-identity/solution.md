# ACT 1 - FIRST SIGNAL: Full Identity — saved solution

Flag / submission candidate: `pcgCTF{DESKTOP-5NLV63K.firsttolast.tech}`

Our original PCGCTF snapshot already marks this challenge solved. Original capture analysis agrees with Garcia’s ACT identity value; teammate reports acceptance. Existing solved snapshot unchanged.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Evidence

Recovered FQDN: **DESKTOP-5NLV63K.firsttolast.tech**. The hostname is DESKTOP-5NLV63K and the DNS domain is firsttolast.tech. The associated user rvance is a separate fact.

Saved original-capture tables: [FIRST SIGNAL identity](../../../../analysis/network-forensics/act1-identity.tsv), [THE COMPROMISE identity](../../../../analysis/network-forensics/act2-identity.tsv). [Garcia’s ACT Storyline section](../../../../team/garcia-day1/source.md) reports successful submissions for this ID. Exact accepted formatting has not been independently retested here.

## Exact-question correction

The question explicitly asks for the FQDN. Combine the DHCP/NBNS workstation name with the DNS domain. The bare hostname omits the requested domain. This corrects the teammate table’s shorthand when turning it into a flag; the accepted spelling has not been independently retested.
