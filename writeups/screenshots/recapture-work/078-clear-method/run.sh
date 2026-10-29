#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/078 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/078-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ rg '"'"'^X-Spam-(Signature|Validator):'"'"' intercepted.txt'
rg '^X-Spam-(Signature|Validator):' intercepted.txt
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/078-clear-method/exit-codes
printf '\n'
printf '%s\n' '$ python3 solve.py'
python3 solve.py
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/078-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/078-clear-method/done
printf '$ '
sleep 120
