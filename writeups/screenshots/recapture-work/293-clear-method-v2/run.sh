#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/293 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/293-clear-method-v2/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act5.pcap -Y '"'"'http.host contains "spora" || http.host contains "p27dokhpz2n7nvgr" || udp.dstport==6892'"'"' \
  -T fields -e ip.src -e udp.dstport -e http.host | sort -u'
tshark -nr act5.pcap -Y 'http.host contains "spora" || http.host contains "p27dokhpz2n7nvgr" || udp.dstport==6892' \
  -T fields -e ip.src -e udp.dstport -e http.host | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/293-clear-method-v2/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/293-clear-method-v2/done
printf '$ '
sleep 120
