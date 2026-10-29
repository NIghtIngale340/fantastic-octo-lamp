#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/296 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/296-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act5.pcap -Y '"'"'ip.src==10.3.14.135 && (http.request || dns.qry.name)'"'"' \
  -T fields -e dns.qry.name -e http.host -e http.user_agent | sort -u | head -n 8'
tshark -nr act5.pcap -Y 'ip.src==10.3.14.135 && (http.request || dns.qry.name)' \
  -T fields -e dns.qry.name -e http.host -e http.user_agent | sort -u | head -n 8
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/296-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/296-clear-method/done
printf '$ '
sleep 120
