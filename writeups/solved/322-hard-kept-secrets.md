# Hard Kept Secrets

**Platform:** PCGCTF · **Challenge ID:** 322 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the old snapshot, but the shared APK wasn't preserved. The token below is from the teammate's record — I can't point to the exact class/header in a decompile here.

## The challenge

Recover the internal API token embedded in the De Monne Android app.

## Recorded method

The method is to decompile the APK and trace the token constant to where it's assigned to an outgoing request header:

```sh
jadx -d decompiled app-release.apk
# then grep the networking client / interceptor for the token constant
```

The recorded token is a long Base64-shaped string:

```text
deadface{zqJRlVwBA9Xm2lE5EPjgbj/4rOxlkYZgDtkdP7jV80rZgLFrlnOEn+VAu31YKQrR}
```

(Two UI strings are noted as decoys; their exact locations weren't preserved.)

## Flag

```text
deadface{zqJRlVwBA9Xm2lE5EPjgbj/4rOxlkYZgDtkdP7jV80rZgLFrlnOEn+VAu31YKQrR}
```

## Still to do

- Get the APK, record its SHA-256, and trace the token from its constant to the header assignment so the real-vs-decoy strings are proven, not assumed.

## Takeaway

For a hardcoded API token, don't stop at the string — follow it to the request header it's assigned to, which also separates the live token from UI decoys.

## Reference

- [Original challenge and attachments](../../challenges/solved/deadface/322-hard-kept-secrets/README.md)
