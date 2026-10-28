#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/269 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/269-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act2.pcap -Y '"'"'ip.src==10.2.28.88'"'"' -T fields -e eth.src -e ip.src | sort -u'
tshark -nr act2.pcap -Y 'ip.src==10.2.28.88' -T fields -e eth.src -e ip.src | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/269-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/269-clear-method/done
printf '$ '
sleep 120
