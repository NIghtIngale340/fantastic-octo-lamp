#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/035 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/035-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ pdfinfo confidential_2.pdf | rg '"'"'Author|Pages|File size'"'"''
pdfinfo confidential_2.pdf | rg 'Author|Pages|File size'
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/035-clear-method/exit-codes
printf '\n'
printf '%s\n' '$ printf '"'"'%s'"'"' '"'"'Q1RGe3B1enpsM2RfbTN0YWRhdGFfZjB1bmQhXzQyNDQwYzdkfQ=='"'"' | base64 -d'
printf '%s' 'Q1RGe3B1enpsM2RfbTN0YWRhdGFfZjB1bmQhXzQyNDQwYzdkfQ==' | base64 -d
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/035-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/035-clear-method/done
printf '$ '
sleep 120
