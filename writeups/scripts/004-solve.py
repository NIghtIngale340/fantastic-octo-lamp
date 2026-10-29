import base64

value = b"VVRGU1IyVXlOV3hrYlZaNVdETk9NR0l6UW1aaVIxWm9ZMjAxY0dKdFpEaz0="
for _ in range(3):
    value = base64.b64decode(value)
    print(value.decode())
