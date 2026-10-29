#!/usr/bin/env python3
"""Recover this challenge's unencrypted normal-quality DeepSound MP4."""
import hashlib
import json
import struct
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent
archive = root / 'files/elliots_secret_stash.zip'
out = root / 'evidence'
out.mkdir(exist_ok=True)
with zipfile.ZipFile(archive) as z:
    members = z.namelist()
    assert members == ['Dubwreckerz - Digital Revolution (Anonymous VIP).wav']
    wav = z.read(members[0])  # ZipFile validates the member's CRC.
assert wav[:4] == b'RIFF' and wav[8:12] == b'WAVE'
pos = 12
while pos + 8 <= len(wav):
    kind, size = struct.unpack_from('<4sI', wav, pos)
    end = pos + 8 + size
    assert end <= len(wav)
    if kind == b'data':
        carrier_offset = pos + 8
        carrier = wav[carrier_offset:end]
        break
    pos = end + (size & 1)
else:
    raise ValueError('No WAV data chunk')

# One hidden byte uses the low nibble of two consecutive 16-bit samples.
assert len(carrier) % 4 == 0
hidden = bytes(((carrier[i] & 15) << 4) | (carrier[i + 2] & 15)
               for i in range(0, len(carrier), 4))
assert hidden[:6] == b'DSCF\x04\x00'  # normal quality, no password/encryption
assert hidden[6:10] == b'DSSF'
name = hidden[10:30].split(b'\0', 1)[0].decode('ascii')
assert name == 'digital revolut.mp4'
length = struct.unpack_from('>I', hidden, 30)[0]
assert hidden[34:38] == bytes(4)
payload = hidden[38:38 + length]
padded_end = 34 + ((4 + length + 15) // 16) * 16
assert hidden[padded_end:padded_end + 4] == b'DSSF'
assert len(payload) == length and payload[4:8] == b'ftyp'
assert hashlib.sha256(payload).hexdigest() == '69bf7d4fa71f3274dda897ffde1a6e929bace7a429ce1eb60f09d029779c4001'
(out / name).write_bytes(payload)
def identity(data):
    return {'size': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
record = {
    'archive': identity(archive.read_bytes()),
    'wav_member': members[0], 'wav': identity(wav),
    'wav_data_offset': carrier_offset,
    'deepsound_header': hidden[:6].hex(),
    'mode': 'normal-quality (4)', 'encrypted': False,
    'record_filename': name, 'record_length': length,
    'decoded_payload_offset': 38, 'closing_marker_offset': padded_end,
    'payload': identity(payload),
    'visible_flag': 'flag{hello_Elliot}',
    'flag_candidate': 'pcgCTF{hello_Elliot}',
    'visual_evidence': 'flag-frame-39s.png',
    'flag_observation': 'Visually read from video frame; not claimed to be plaintext in the MP4 bytes.',
    'platform_accepted': False,
}
(out / 'verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(f'Recovered {name}: {length} bytes')
print('Visual flag: flag{hello_Elliot}')
print('Submission candidate: pcgCTF{hello_Elliot}')
