import sqlite3
c=sqlite3.connect('file:/home/nightingale/CTF/PCGCTF/team-writeups/garcia-day1/aurora_meds.sqlite?mode=ro',uri=True)
for r in c.execute("SELECT * FROM medications WHERE medication_1 LIKE '%buprofen%' OR medication_2 LIKE '%buprofen%'"):print(r)
