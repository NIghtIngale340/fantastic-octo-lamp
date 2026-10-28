#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/003 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/003-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ printf '"'"'%s\n'"'"' '"'"'Frdvw Jxdug Fbehu Frppdqg'"'"' | tr '"'"'A-Za-z'"'"' '"'"'X-ZA-Wx-za-w'"'"''
printf '%s\n' 'Frdvw Jxdug Fbehu Frppdqg' | tr 'A-Za-z' 'X-ZA-Wx-za-w'
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/003-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/003-clear-method/done
printf '$ '
sleep 120
