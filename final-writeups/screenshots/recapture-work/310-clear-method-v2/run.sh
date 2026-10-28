#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/310 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/310-clear-method-v2/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ exiftool -XMP:all aurora_chest_xray.jpg'
exiftool -XMP:all aurora_chest_xray.jpg
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/310-clear-method-v2/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/310-clear-method-v2/done
printf '$ '
sleep 120
