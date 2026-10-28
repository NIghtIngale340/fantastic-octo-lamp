#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/002 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/002-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ exiftool -Make -Model -Software '"'"'cydex (1).jpg'"'"''
exiftool -Make -Model -Software 'cydex (1).jpg'
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/002-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/002-clear-method/done
printf '$ '
sleep 120
