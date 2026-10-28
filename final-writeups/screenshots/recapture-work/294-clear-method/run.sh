#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/294 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/294-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act5.pcap -Y '"'"'ip.src==10.3.14.131 && http.request'"'"' -T fields -e http.host | sort -u'
tshark -nr act5.pcap -Y 'ip.src==10.3.14.131 && http.request' -T fields -e http.host | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/294-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/294-clear-method/done
printf '$ '
sleep 120
