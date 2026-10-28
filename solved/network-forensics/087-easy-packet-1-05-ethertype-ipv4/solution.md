# EASY PACKET 1 #05  EtherType: IPv4 — saved solution

Flag / submission candidate: `pcgCTF{IPv4}`

Our original PCGCTF snapshot already marks this challenge solved. Packet value corroborated by our saved original-capture analysis; candidate spelling imported from Garcia. Existing site-solved snapshot unchanged.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../team-writeups/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Evidence

EASY PACKET 1 question #05. Requested protocol: **IPv4**.

The original capture is stored under challenge #82. [Saved frame dissection](../../../analysis-network-forensics/easy-packet-frame-1.txt) and [capture metadata](../../../analysis-network-forensics/easy-packet-capture-info.txt) preserve the original packet evidence. The teammate’s [EASY PACKET table and formatting notes](../../../team-writeups/garcia-day1/source.md) provide the matching value.

This submission spelling is a saved candidate; historical site acceptance of this exact string is not independently logged here.

## Exact-question correction

The question asks which network protocol EtherType 0x0800 identifies, so answer IPv4, not the numeric EtherType. This corrects the teammate table’s shorthand when turning it into a flag; the accepted spelling has not been independently retested.
