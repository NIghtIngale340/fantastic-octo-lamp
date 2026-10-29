#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/263 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/263-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act1.pcap -Y '"'"'ip.src==172.16.8.49'"'"' -T fields -e eth.src -e ip.src -e ip.dst | sort -u'
tshark -nr act1.pcap -Y 'ip.src==172.16.8.49' -T fields -e eth.src -e ip.src -e ip.dst | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/263-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/263-clear-method/done
printf '$ '
sleep 120
