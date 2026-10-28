# Heavy Hand

**Platform:** PCGCTF · **Challenge ID:** 331 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot; reproduced from the database.

## The challenge

Rank prescribers by total quantity of Schedule II drugs dispensed in Q4 2025, and report the leading prescriber's DEA number.

## Solving it

I joined dispenses to the drug table, filtered to Schedule II in the final quarter, summed quantity per prescriber, and took the top one:

```sql
SELECT p.dea_number, SUM(d.quantity) AS total
FROM aurora_pharmacy.dispenses d
JOIN aurora_pharmacy.drugs g ON g.id = d.drug_id
JOIN aurora_ehr.prescribers p ON p.prescriber_id = d.prescriber_id
WHERE g.dea_schedule = 'II'
  AND d.dispensed_at >= '2025-10-01' AND d.dispensed_at < '2026-01-01'
GROUP BY p.dea_number
ORDER BY total DESC
LIMIT 1;
```

Top prescriber's DEA number: `BR2938471`.

## Screenshot

![331-step-02.png](../screenshots/331-step-02.png)

## Flag

```text
deadface{BR2938471}
```

## Takeaway

Aggregate on quantity (not prescription count), bound the quarter with a half-open range, and return the DEA number the question asks for.

## Reference

- [Original challenge and attachments](../../solved/deadface/331-heavy-hand/README.md)
