#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/279 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/279-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act3.pcap -Y '"'"'tcp.payload contains "STRRAT"'"'"' -T fields -e ip.dst -e tcp.dstport | sort -u'
tshark -nr act3.pcap -Y 'tcp.payload contains "STRRAT"' -T fields -e ip.dst -e tcp.dstport | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/279-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/279-clear-method/done
printf '$ '
sleep 120
