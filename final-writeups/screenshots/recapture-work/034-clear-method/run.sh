#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/034 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/034-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ printf '"'"'%s\n'"'"' '"'"'synt vf pbby'"'"' | tr '"'"'A-Za-z'"'"' '"'"'N-ZA-Mn-za-m'"'"''
printf '%s\n' 'synt vf pbby' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/034-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/034-clear-method/done
printf '$ '
sleep 120
