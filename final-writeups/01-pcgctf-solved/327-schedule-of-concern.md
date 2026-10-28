# Schedule of Concern

**Platform:** PCGCTF · **Challenge ID:** 327 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the saved snapshot. The query and screenshots below come from the saved database verification.

## The challenge

Count the drugs in Aurora's formulary classified as DEA Schedule II. The flag is just the count.

## Solving it

```sql
SELECT dea_schedule, COUNT(*) AS drug_count
FROM aurora_pharmacy.drugs
GROUP BY dea_schedule;
```

Selected result from the saved verification:

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
