import plistlib, base64, json
with open('/home/nightingale/CTF/PCGCTF/unsolved/aurora-patient-zero/309-info-leaks/evidence/Info.plist', 'rb') as f:
    info = plistlib.load(f)
patient = json.loads(base64.b64decode(info['AuroraPatientBootstrap']))
print(patient)
