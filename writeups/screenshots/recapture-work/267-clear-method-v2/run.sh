#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/267 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/267-clear-method-v2/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act1.pcap -Y '"'"'ip.src==172.16.8.49 && http.request.uri contains "/irpw/"'"'"' \
  -T fields -e ip.dst -e http.host -e http.request.uri.path | sort -u'
tshark -nr act1.pcap -Y 'ip.src==172.16.8.49 && http.request.uri contains "/irpw/"' \
  -T fields -e ip.dst -e http.host -e http.request.uri.path | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/267-clear-method-v2/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/267-clear-method-v2/done
printf '$ '
sleep 120
