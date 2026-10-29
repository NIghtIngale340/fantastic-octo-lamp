script = bytes.fromhex('6a1f666c61677b496e6630533363426c30636b636834316e416e346c797331357d')
assert script[0] == 0x6a and len(script[2:]) == script[1]
print(script[2:].decode('ascii'))
