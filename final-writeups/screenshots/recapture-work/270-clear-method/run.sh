#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/270 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/270-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act2.pcap -Y '"'"'eth.src==00:19:d1:b2:4d:ad && (dhcp.option.hostname || nbns.name)'"'"' \
  -T fields -e dhcp.option.hostname -e nbns.name | sort -u'
tshark -nr act2.pcap -Y 'eth.src==00:19:d1:b2:4d:ad && (dhcp.option.hostname || nbns.name)' \
  -T fields -e dhcp.option.hostname -e nbns.name | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/270-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/270-clear-method/done
printf '$ '
sleep 120
