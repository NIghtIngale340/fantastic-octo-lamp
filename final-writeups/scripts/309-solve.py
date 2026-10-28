from pathlib import Path
import base64
import json
import plistlib

info = plistlib.loads(Path("Info.plist").read_bytes())
patient = json.loads(base64.b64decode(info["AuroraPatientBootstrap"]))
print(json.dumps(patient, indent=2))
