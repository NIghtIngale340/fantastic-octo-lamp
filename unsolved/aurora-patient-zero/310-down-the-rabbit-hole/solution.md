# Down the Rabbit Hole — recovered answer

Flag candidate: `deadface{847261}`

The challenge reuses the Info Leaks IPA and explicitly requests `deadface{ID}`. The bundled `aurora_chest_xray.jpg` includes this XMP metadata:

```xml
<dc:identifier>PID-847261</dc:identifier>
```

Remove the `PID-` label to obtain patient ID `847261`. A read-only lookup of the packaged medication database also finds this patient ID.

Evidence: [XMP metadata](evidence/xray-metadata.xmp), [database cross-check](evidence/database-corroboration.json), [artifact identities](../../../analysis-team-verification/aurora-identities.json). Original JPEG SHA-256: `332f27ab49f5f4a4d0388e0b7aa22e4b4322a716477a0cbd7608d44c3d1b846b`.

Status: answer recovered locally; not submitted or confirmed accepted on PCGCTF. Teammate's lead independently checked against the original package.
