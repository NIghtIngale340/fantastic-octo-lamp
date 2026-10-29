#!/bin/bash
cd /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/062 || exit 1
exec > >(tee /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/062-final-method/output.log) 2>&1
printf '\033[2J\033[H'
printf '%s\n' '$ tshark -nr http_file_extraction.pcap -Y http -T fields -e http.request.uri -e http.content_type
tshark -q -r http_file_extraction.pcap --export-objects http,objects
unzip -p objects/password.zip password.txt'
tshark -nr http_file_extraction.pcap -Y http -T fields -e http.request.uri -e http.content_type
tshark -q -r http_file_extraction.pcap --export-objects http,objects
unzip -p objects/password.zip password.txt
result=$?
printf "%s\n" "$result" >> /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/062-final-method/exit-codes
printf '\n'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/recapture-work/062-final-method/done
printf '$ '
sleep 120
