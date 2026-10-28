#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/311 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/311-clear-method-v2/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ sqlite3 -header -column '"'"'file:aurora_meds.sqlite?mode=ro'"'"' \
  "SELECT pid, medication_1, medication_2 FROM medications WHERE pid=847261;"'
sqlite3 -header -column 'file:aurora_meds.sqlite?mode=ro' \
  "SELECT pid, medication_1, medication_2 FROM medications WHERE pid=847261;"
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/311-clear-method-v2/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/311-clear-method-v2/done
printf '$ '
sleep 120
