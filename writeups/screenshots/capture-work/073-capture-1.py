import ipaddress
raw = (43200).to_bytes(8, 'little')[:2] + (12488).to_bytes(8, 'little')[:2]
print(raw.hex())
print(ipaddress.IPv4Address(raw))
