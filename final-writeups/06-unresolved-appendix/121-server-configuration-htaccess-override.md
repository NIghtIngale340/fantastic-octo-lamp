# Server Configuration — .htaccess Override

**Platform:** PCGCTF · **Challenge ID:** 121 · **Category:** Web Exploitation · **Points:** 200

**Status:** Unresolved. The technique is clear from the clue, but the target (http://flag2.cgcybercom.online/) wasn't reachable from here, so there's no response to work with and no confirmed flag. Honest stub.

## The challenge

A server misconfiguration lets `.htaccess` rules be read or overridden.

## What I could do

The approach is to request `/.htaccess` (served as text if not blocked) and read the rules, or exploit an AllowOverride misconfig.

I probed the target read-only:

```sh
curl --connect-timeout 5 --max-time 12 -sS -D - http://flag2.cgcybercom.online/
```

The connection timed out — no response body. Reporting a working exploit here would be inventing evidence.

## Screenshot

![121-server-configuration-htaccess-override-actual-target-response.png](../screenshots/121-actual-target-response.png)

(The capture shows the failed connection, not an exploit or a flag.)

## Flag

None recovered — target unreachable, and the exact string inside `pcgCTF{...}` isn't known.

## Still to do

- Reach the target from an authorized network, run the check above, and record one justified candidate with its real submission result.

## Takeaway

`.htaccess` served as text leaks your rewrite/auth rules — deny access to dotfiles at the server.

## Reference

- [Original challenge description](../../unsolved/web-exploitation/121-server-configuration-htaccess-override/README.md)
