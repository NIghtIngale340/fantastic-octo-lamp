#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/312 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/312-clear-method-v2/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ strings -n 4 '"'"'Aurora Health Mobile'"'"' | rg -i -A 2 '"'"'gateway'"'"''
strings -n 4 'Aurora Health Mobile' | rg -i -A 2 'gateway'
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/312-clear-method-v2/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/312-clear-method-v2/done
printf '$ '
sleep 120
