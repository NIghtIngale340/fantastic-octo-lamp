#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/264 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/264-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act1.pcap -Y '"'"'eth.src==00:12:f0:28:d4:34 && dhcp.option.hostname'"'"' \
  -T fields -e dhcp.option.hostname | sort -u'
tshark -nr act1.pcap -Y 'eth.src==00:12:f0:28:d4:34 && dhcp.option.hostname' \
  -T fields -e dhcp.option.hostname | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/264-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/264-clear-method/done
printf '$ '
sleep 120
