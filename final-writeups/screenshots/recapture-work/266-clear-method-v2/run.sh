#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/266 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/266-clear-method-v2/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr act1.pcap -Y '"'"'ip.src==172.16.8.49 && kerberos.CNameString'"'"' \
  -T fields -e kerberos.CNameString -e kerberos.realm | sort -u'
tshark -nr act1.pcap -Y 'ip.src==172.16.8.49 && kerberos.CNameString' \
  -T fields -e kerberos.CNameString -e kerberos.realm | sort -u
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/266-clear-method-v2/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/266-clear-method-v2/done
printf '$ '
sleep 120
