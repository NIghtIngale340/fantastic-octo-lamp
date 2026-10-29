#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/273 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/273-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act2.pcap -d tcp.port==443,http -Y '"'"'http.user_agent contains "NetSupport"'"'"' \
  -T fields -e http.request.uri | sort -u'
tshark -nr act2.pcap -d tcp.port==443,http -Y 'http.user_agent contains "NetSupport"' \
  -T fields -e http.request.uri | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/273-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/273-clear-method/done
printf '$ '
sleep 120
