#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/277 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/277-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act3.pcap -Y '"'"'kerberos.CNameString || samr.samr_UserInfo21.account_name'"'"' \
  -T fields -e kerberos.CNameString -e samr.samr_UserInfo21.account_name -e samr.samr_UserInfo21.full_name | sort -u | head -n 8'
tshark -nr act3.pcap -Y 'kerberos.CNameString || samr.samr_UserInfo21.account_name' \
  -T fields -e kerberos.CNameString -e samr.samr_UserInfo21.account_name -e samr.samr_UserInfo21.full_name | sort -u | head -n 8
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/277-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/277-clear-method/done
printf '$ '
sleep 120
