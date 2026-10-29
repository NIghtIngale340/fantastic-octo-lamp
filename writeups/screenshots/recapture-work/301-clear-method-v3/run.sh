#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/301 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/301-clear-method-v3/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act.pcap -Y '"'"'tcp.payload contains "STRRAT"'"'"' \
  -T fields -e tcp.payload | head -n 1 | xxd -r -p | strings'
tshark -nr act.pcap -Y 'tcp.payload contains "STRRAT"' \
  -T fields -e tcp.payload | head -n 1 | xxd -r -p | strings
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/301-clear-method-v3/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/301-clear-method-v3/done
printf '$ '
sleep 120
