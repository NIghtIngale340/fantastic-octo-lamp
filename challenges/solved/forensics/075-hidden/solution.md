# HIDDEN — recovered answer

Flag candidate: `pcgCTF{me0w_hia!}`

The supplied ZIP's `winsock32.dll` is a disk image rather than an ordinary PE DLL. Sleuth Kit `mmls` identifies an NTFS partition starting at sector 128 (65536 bytes).

```sh
fls -r -o 128 winsock32.dll
icat -o 128 winsock32.dll 40-128-3 > flag.jpg
```

The NTFS listing identifies `40-128-3` as the named data stream `passwords.txt:flag.jpg`. Exporting that stream yields a 24,023-byte JPEG, independently matching the teammate's carve at absolute offset 294912. Its visible text reads `flag{me0w_hia!}`. The challenge explicitly requests the `pcgCTF{...}` wrapper.

Evidence: [extracted image](evidence/flag.jpg), [partition table](evidence/partition-table.txt), [NTFS listing](evidence/ntfs-files.txt). Image SHA-256: `f513d38515dc97946983a6b036c6a56a59f1d084831e7cd790342ad8b178428e`. Disk image SHA-256: `8e5be0056a8ea7e0f98bde634bf68adbcc24d25949557d0b51e14dd7a6aff266`.

Status: image and payload recovered locally; platform wrapper is inferred from the explicit challenge format, and acceptance is not yet confirmed.
