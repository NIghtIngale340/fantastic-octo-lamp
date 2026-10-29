#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/266 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/266-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act1.pcap -Y '"'"'kerberos.CNameString'"'"' \
  -T fields -e kerberos.CNameString -e kerberos.realm | sort -u | head -n 8'
tshark -nr act1.pcap -Y 'kerberos.CNameString' \
  -T fields -e kerberos.CNameString -e kerberos.realm | sort -u | head -n 8
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/266-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/266-clear-method/done
printf '$ '
sleep 120
