# Schedule of Concern

**Platform:** PCGCTF · **Challenge ID:** 327 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot; reproduced from the database.

## The challenge

Count the drugs in Aurora's formulary classified as DEA Schedule II. The flag is just the count.

## Solving it

```sql
SELECT COUNT(*) FROM formulary WHERE dea_schedule = 'II';
```

```text
9
```

## Screenshot

![327-step-02.png](../screenshots/327-step-02.png)

## Flag

```text
deadface{9}
```

## Takeaway

When the flag is a count, match the classification exactly (Schedule `II`, not `2` or `II`-plus-others) so the number is right.

## Reference

- [Original challenge and attachments](../../solved/deadface/327-schedule-of-concern/README.md)
