# Inside Man

**Platform:** PCGCTF · **Challenge ID:** 323 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the old snapshot, but the APK wasn't preserved. The flag is from the teammate's record; I can't name the exact login class or show the bypass branch here.

## The challenge

Find the hardcoded developer/backdoor credential that grants access ordinary customers can't get.

## Recorded method

The method is to decompile and read the login activity for a credential constant that routes into a privileged path:

```sh
jadx -d decompiled app-release.apk
# inspect the login activity for a hardcoded dev/backdoor credential
```

The recorded backdoor credential/flag is:

```text
deadface{l3FT_b3Hind!}
```

## Flag

```text
deadface{l3FT_b3Hind!}
```

## Still to do

- Get the APK and show the actual authentication comparison and how the credential reaches the privileged branch — distinguish a real backdoor from a test string.

## Takeaway

A backdoor credential is proven by the code path it unlocks, not just by appearing in the source — trace it to the privileged branch.

## Reference

- [Original challenge and attachments](../../challenges/solved/deadface/323-inside-man/README.md)
