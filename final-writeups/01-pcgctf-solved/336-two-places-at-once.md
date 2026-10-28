# Two Places at Once

**Platform:** PCGCTF · **Challenge ID:** 336 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot; reproduced from the database.

## The challenge

Identify the legitimate account logged into two different workstations at identical timestamps, repeatedly.

## Solving it

I looked for the same account with access-log rows at the same instant on different workstations, and counted those collisions:

```sql
SELECT u.username, COUNT(*) AS collisions
FROM aurora_audit.access_log a
JOIN aurora_audit.access_log b
  ON a.user_id = b.user_id
 AND a.accessed_at = b.accessed_at
 AND a.workstation <> b.workstation
JOIN aurora_audit.users u ON u.user_id = a.user_id
GROUP BY u.username
ORDER BY collisions DESC;
```

```text
kbhat   (e.g. 2025-11-04 23:54:03 on WS-028 and WS-008)
```

`kbhat` is logged into two workstations at once, repeatedly — credentials in use by more than one person.

## Screenshot

![336-step-02.png](../screenshots/336-step-02.png)

## Flag

```text
deadface{kbhat}
```

## Takeaway

Impossible-travel / simultaneous-session detection is a self-join on (user, timestamp) with different workstations — a shared or stolen credential falls right out.

## Reference

- [Original challenge and attachments](../../solved/deadface/336-two-places-at-once/README.md)
