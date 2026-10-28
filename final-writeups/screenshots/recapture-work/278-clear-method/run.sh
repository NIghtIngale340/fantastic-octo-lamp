#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/278 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/278-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act3.pcap -Y '"'"'samr.samr_UserInfo21.account_name=="ccollier"'"'"' \
  -T fields -e samr.samr_UserInfo21.full_name | sort -u'
tshark -nr act3.pcap -Y 'samr.samr_UserInfo21.account_name=="ccollier"' \
  -T fields -e samr.samr_UserInfo21.full_name | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/278-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/278-clear-method/done
printf '$ '
sleep 120
