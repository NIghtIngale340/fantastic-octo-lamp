#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/295 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/295-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act5.pcap -Y '"'"'ip.src==10.3.14.134 && (udp.dstport==6892 || http.request)'"'"' \
  -T fields -e udp.dstport -e http.host -e http.request.uri | sort -u | head -n 8'
tshark -nr act5.pcap -Y 'ip.src==10.3.14.134 && (udp.dstport==6892 || http.request)' \
  -T fields -e udp.dstport -e http.host -e http.request.uri | sort -u | head -n 8
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/295-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/295-clear-method/done
printf '$ '
sleep 120
