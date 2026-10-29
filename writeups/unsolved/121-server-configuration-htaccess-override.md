# Server Configuration — .htaccess Override

**Platform:** PCGCTF · **Challenge ID:** 121 · **Category:** Web Exploitation · **Points:** 200

**Status:** Unresolved. The saved connection attempt failed, so no live response or flag was recovered.

## The challenge

A server misconfiguration lets `.htaccess` rules be read or overridden.

## Investigation notes

The approach is to request `/.htaccess` (served as text if not blocked) and read the rules, or exploit an AllowOverride misconfig.

The saved connection attempt used:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://flag2.cgcybercom.online/
```

The connection timed out — no response body.

## Flag

None recovered — target unreachable, and the exact string inside `pcgCTF{...}` isn't known.

## Next step

Once the lab is reachable, test the challenge-specific approach above and record the response and submission result.

## Reference

- [Original challenge description](../../challenges/unsolved/web-exploitation/121-server-configuration-htaccess-override/README.md)
