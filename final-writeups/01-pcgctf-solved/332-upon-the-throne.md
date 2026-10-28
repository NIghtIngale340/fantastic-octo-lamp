# Upon the Throne

**Platform:** PCGCTF · **Challenge ID:** 332 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot; reproduced from the database.

## The challenge

Find the handler codename that appears in both the audit users and the EHR providers, and submit that shared codename.

## Solving it

Both tables carry a `handler_ref`, so I joined on it (trimmed and case-normalized, excluding blanks) to find the codename linking an audit account to a provider:

```sql
SELECT u.handler_ref
FROM aurora_audit.users u
JOIN aurora_ehr.providers p
  ON LOWER(TRIM(u.handler_ref)) = LOWER(TRIM(p.handler_ref))
WHERE TRIM(u.handler_ref) <> '';
```

```text
REVENANT-7
```

The codename links audit account `rborden` and provider 5 — but the flag is the shared codename, not either username.

## Screenshot

![332-step-02.png](../screenshots/332-step-02.png)

## Flag

```text
deadface{REVENANT-7}
```

## Takeaway

Trim and case-normalize before joining on a reference field, and exclude blank placeholders so empty strings don't match each other.

## Reference

- [Original challenge and attachments](../../solved/deadface/332-upon-the-throne/README.md)
