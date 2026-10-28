#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/111 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/111-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr EASY_PACKET_1.pcap -Y http -T fields -e http.authorization
echo '"'"'dXNlcnRlc3Q6cGFzc3dvcmQ='"'"' | base64 -d'
tshark -nr EASY_PACKET_1.pcap -Y http -T fields -e http.authorization
echo 'dXNlcnRlc3Q6cGFzc3dvcmQ=' | base64 -d
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/111-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/111-clear-method/done
printf '$ '
sleep 120
