#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/304 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/304-clear-method-v3/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act.pcap -Y '"'"'ip.dst==153.92.1.49 && http.request'"'"' \
  -T fields -e http.host -e http.request.uri | sort -u | head -n 8'
tshark -nr act.pcap -Y 'ip.dst==153.92.1.49 && http.request' \
  -T fields -e http.host -e http.request.uri | sort -u | head -n 8
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/304-clear-method-v3/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/304-clear-method-v3/done
printf '$ '
sleep 120
