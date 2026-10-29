#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/287 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/287-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act4.pcap -Y '"'"'dns.a==153.92.1.49 || (http.host && ip.dst==153.92.1.49)'"'"' \
  -T fields -e dns.qry.name -e dns.a -e http.host | sort -u | head -n 8'
tshark -nr act4.pcap -Y 'dns.a==153.92.1.49 || (http.host && ip.dst==153.92.1.49)' \
  -T fields -e dns.qry.name -e dns.a -e http.host | sort -u | head -n 8
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/287-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/287-clear-method/done
printf '$ '
sleep 120
