#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/088 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/088-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr EASY_PACKET_1.pcap -T fields -e ip.version'
tshark -nr EASY_PACKET_1.pcap -T fields -e ip.version
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/088-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/088-clear-method/done
printf '$ '
sleep 120
