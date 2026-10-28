# Diagnosis

**Platform:** PCGCTF · **Challenge ID:** 325 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the old snapshot, but the APK wasn't preserved. The flag is from the teammate's record; I can't show the exact exported component here.

## The challenge

Identify the hidden Android activity the manifest exposes, and recover its flag.

## Recorded method

The method is to decode the manifest and find an exported diagnostic activity, then inspect its implementation:

```sh
apktool d app-release.apk -o decoded-apk
# read AndroidManifest.xml for an exported diagnostic activity, then inspect it in jadx
```

The recorded flag from that activity is:

```text
deadface{flaG_ManIfesT3d}
```

## Flag

```text
deadface{flaG_ManIfesT3d}
```

## Still to do

- Get the APK and identify the exact exported component; if runtime confirmation is needed, build the explicit intent from the real package/component names.

## Takeaway

`android:exported` activities in the manifest are reachable from outside the app — a "hidden" diagnostic screen left exported is the whole vulnerability.

## Reference

- [Original challenge and attachments](../../solved/deadface/325-diagnosis/README.md)
