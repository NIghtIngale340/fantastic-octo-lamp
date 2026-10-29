# Hooked

**Platform:** PCGCTF · **Challenge ID:** 320 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot; reproduced from the History database.

## The challenge

Recover the phishing landing URL the employee clicked, from their captured Chrome history.

## Solving it

Chrome history is a SQLite database, so I opened the copy read-only and read the `urls` table in order:

```sh
sqlite3 'file:Hooked-History.sqlite?mode=ro' \
  "SELECT url FROM urls ORDER BY last_visit_time;"
```

The visit chain runs email → inbox → the credential-collection landing page → an auth redirect. The landing URL is the phishing page:

```text
http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc
```

## Screenshot

The terminal image below displays a retained verification transcript.

![320-step-01.png](../screenshots/320-step-01.png)

## Flag

```text
deadface{http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc}
```

## Takeaway

Browser history is a SQLite file — open it read-only and the visit sequence reconstructs the click chain, pinpointing the landing page the user actually hit.

## Reference

- [Original challenge and attachments](../../challenges/solved/deadface/320-hooked/README.md)
