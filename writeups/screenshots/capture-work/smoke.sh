#!/bin/bash
printf '%s' "$WINDOWID" > /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/smoke.window
printf '\033[2J\033[H'
printf 'PCGCTF — actual offline reproduction
Challenge 77: HIT A BRICK WALL

'
printf '$ python brick_decode.py

'
python - <<'DECODE'
from PIL import Image
im=Image.open('/home/nightingale/CTF/PCGCTF/unsolved/forensics-steganography/077-hit-a-brick-wall/files/bricks.png').convert('RGB')
message=''
for row in range(12):
    x0=115 if row%2==0 else 62
    colors=[im.getpixel((round(x0+108.5*c),38+56*row)) for c in range(8)]
    bits=''.join('0' if c==(240,227,213) else '1' if c==(224,212,199) else '?' for c in colors)
    char=chr(int(bits,2));message+=char
    print(f'Row {row+1:2}: {bits} -> {char}')
print('
Recovered:',message)
DECODE
printf '
[Actual process finished]
'
touch /home/nightingale/CTF/PCGCTF/final-writeups/screenshots/capture-work/smoke.done
sleep 30
