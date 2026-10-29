# Info Leaks — recovered answer

Flag candidate: `deadface{Mara-Voss-1988-04-17}`

Verified independently against the original `files/AuroraPatientPortal.ipa.zip`. The inner IPA is a ZIP containing `Payload/aurora-patient-portal.app/Info.plist`. Its `AuroraPatientBootstrap` property is base64, which decodes to:

```json
{
  "patientName": "Mara Voss",
  "dateOfBirth": "1988-04-17",
  "clinic": "Westlake"
}
```

The challenge explicitly requests `deadface{firstname-lastname-YYYY-MM-DD}`, so retain the `deadface` prefix and hyphenate the patient's name.

Evidence: [original plist](evidence/Info.plist), [decoded bootstrap](evidence/patient-bootstrap.json), [artifact hashes](../../../../analysis/team-verification/aurora-identities.json), [REA extraction evidence](../../../../analysis/team-verification/aurora-rea-evidence.json). REA extraction IDs: `ev_8a9d70f27f76e6bd08277192f2e6651ab891d02fdcab1bd94f7accc00d44dea0` and `ev_c9e0f7421f401b1b5f4cf77a1102516befffa54ea3d99d2f5dcf0a8a00aeaa0c`.

Status: answer recovered locally; not submitted or confirmed accepted on PCGCTF. Teammate's potential writeup supplied the lead; the original file was independently checked.
