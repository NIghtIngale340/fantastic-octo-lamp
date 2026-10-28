from PIL import Image

image = Image.open("bricks.png").convert("RGB")
colors = {(240, 227, 213): "0", (224, 212, 199): "1"}
message = []
for row in range(12):
    y = 38 + 56 * row
    first_x = 115 if row % 2 == 0 else 62
    bits = "".join(colors[image.getpixel((round(first_x + 108.5 * col), y))]
                   for col in range(8))
    message.append(chr(int(bits, 2)))
    print(bits, message[-1])
print("".join(message))
