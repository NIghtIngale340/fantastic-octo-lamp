#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/262 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/262-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act1.pcap -Y '"'"'http.request && ip.dst==146.59.71.167'"'"' \
  -T fields -e ip.src -e http.host -e http.request.uri | sort -u | head -n 8'
tshark -nr act1.pcap -Y 'http.request && ip.dst==146.59.71.167' \
  -T fields -e ip.src -e http.host -e http.request.uri | sort -u | head -n 8
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/262-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/262-clear-method/done
printf '$ '
sleep 120
