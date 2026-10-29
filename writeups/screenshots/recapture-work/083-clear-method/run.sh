#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/083 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/083-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ xxd -l 4 EASY_PACKET_1.pcap'
xxd -l 4 EASY_PACKET_1.pcap
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/083-clear-method/exit-codes
printf '\n'
printf '%s\n' '$ capinfos -t EASY_PACKET_1.pcap'
capinfos -t EASY_PACKET_1.pcap
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/083-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/083-clear-method/done
printf '$ '
sleep 120
