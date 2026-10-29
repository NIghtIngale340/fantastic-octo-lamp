#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/275 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/275-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act3.pcap -Y '"'"'ip.src==172.16.1.66'"'"' -T fields -e eth.src -e ip.src | sort -u'
tshark -nr act3.pcap -Y 'ip.src==172.16.1.66' -T fields -e eth.src -e ip.src | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/275-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/275-clear-method/done
printf '$ '
sleep 120
