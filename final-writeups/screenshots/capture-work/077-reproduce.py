from PIL import Image
im = Image.open('/home/nightingale/CTF/PCGCTF/unsolved/forensics-steganography/077-hit-a-brick-wall/files/bricks.png').convert('RGB')
message = ''
for row in range(12):
    y = 38 + 56 * row
    first_x = 115 if row % 2 == 0 else 62
    colors = [im.getpixel((round(first_x + 108.5 * c), y))
              for c in range(8)]
    bits = ''.join('0' if c == (240, 227, 213) else
                   '1' if c == (224, 212, 199) else '?'
                   for c in colors)
    assert '?' not in bits
    message += chr(int(bits, 2))
print(message)
