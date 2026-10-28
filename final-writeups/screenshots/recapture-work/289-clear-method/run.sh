#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/289 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/289-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act5.pcap -Y '"'"'ip.src==10.3.14.0/24'"'"' -T fields -e ip.src | sort -u'
tshark -nr act5.pcap -Y 'ip.src==10.3.14.0/24' -T fields -e ip.src | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/289-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/289-clear-method/done
printf '$ '
sleep 120
