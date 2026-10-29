# Too Good to be True

**Platform:** PCGCTF · **Challenge ID:** 335 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the saved snapshot. The query and screenshots below come from the saved database verification.

## The challenge

Find the primary-endpoint value more than three standard deviations above the study mean, and report its subject code.

## Solving it

Compute each primary-efficacy value’s z-score using the study mean and population standard deviation, then sort from highest to lowest:

```sql
SELECT s.subject_code,s.arm,r.value,
 ROUND((r.value-st.m)/st.sd,2) AS z_score
FROM aurora_trials.results r
JOIN aurora_trials.subjects s ON s.subject_id=r.subject_id
CROSS JOIN (SELECT AVG(value) AS m,STDDEV_POP(value) AS sd
            FROM aurora_trials.results
            WHERE measure='primary_efficacy_delta') st
WHERE r.measure='primary_efficacy_delta'
ORDER BY z_score DESC;
```

Selected result from the saved verification:

```text
VELT-0148
```

`VELT-0148` exceeds the threshold specified by the challenge. This identifies the requested outlier; the threshold alone does not prove that the result was fabricated.

## Screenshots

![335-step-02.png](../screenshots/335-step-02.png)

![335-leading-outliers.png](../screenshots/335-leading-outliers.png)

## Flag

```text
deadface{VELT-0148}
```

## Takeaway

Use the study measure and standard-deviation definition specified by the question. An outlier warrants investigation, but is not proof of fabrication.

## Reference

- [Original challenge and attachments](../../challenges/solved/deadface/335-too-good-to-be-true/README.md)
