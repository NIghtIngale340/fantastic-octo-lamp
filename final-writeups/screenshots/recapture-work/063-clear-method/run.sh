#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/063 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/063-clear-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ printf '"'"'%s\n'"'"' '"'"'cptpgs{pnrfne_jnf_bayl_gur_ortvaavat}'"'"' | tr '"'"'A-Za-z'"'"' '"'"'N-ZA-Mn-za-m'"'"''
printf '%s\n' 'cptpgs{pnrfne_jnf_bayl_gur_ortvaavat}' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/063-clear-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/063-clear-method/done
printf '$ '
sleep 120
