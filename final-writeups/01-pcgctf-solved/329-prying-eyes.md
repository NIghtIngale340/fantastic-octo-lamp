# Prying Eyes

**Platform:** PCGCTF · **Challenge ID:** 329 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot; reproduced from the database.

## The challenge

Count accesses to the VIP's chart and identify the account with the most.

## Solving it

I grouped the access-log rows for the VIP's chart by account and ordered by count:

```sql
SELECT account, COUNT(*) AS n
FROM chart_access_log
WHERE patient_id = :vip
GROUP BY account
ORDER BY n DESC;
```

The top account is `rborden` — the one snooping the chart most.

## Screenshot

![329-step-02.png](../screenshots/329-step-02.png)

## Flag

```text
deadface{rborden}
```

## Takeaway

Access logs make insider snooping a simple GROUP BY / ORDER BY — the account at the top of the count is the answer.

## Reference

- [Original challenge and attachments](../../solved/deadface/329-prying-eyes/README.md)
