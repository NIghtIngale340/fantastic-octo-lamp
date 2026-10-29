#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/303 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/303-clear-method-v3/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act.pcap -Y '"'"'ip.dst==141.98.10.79 && tcp contains "STRRAT"'"'"' \
  -T fields -e tcp.dstport | sort -u'
tshark -nr act.pcap -Y 'ip.dst==141.98.10.79 && tcp contains "STRRAT"' \
  -T fields -e tcp.dstport | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/303-clear-method-v3/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/303-clear-method-v3/done
printf '$ '
sleep 120
