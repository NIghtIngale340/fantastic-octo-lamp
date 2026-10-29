# The Attending

**Platform:** PCGCTF · **Challenge ID:** 328 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the saved snapshot. The query and screenshots below come from the saved database verification.

## The challenge

Find the attending provider for the VIP's November 2025 inpatient encounter and report that provider's system username.

## Solving it

I joined patient → encounter → provider, filtered to the VIP's November 2025 inpatient stay with a half-open date range (so I don't miss anything late on the last day):

```sql
SELECT e.encounter_id, e.encounter_type, e.admit_date, e.discharge_date,
       p.provider_id, p.first_name, p.last_name, p.username
FROM aurora_ehr.encounters e
JOIN aurora_ehr.patients v ON v.patient_id=e.patient_id
JOIN aurora_ehr.providers p ON p.provider_id=e.attending_provider_id
WHERE v.is_vip=1 AND e.encounter_type='Inpatient'
  AND e.admit_date >= '2025-11-01' AND e.admit_date < '2025-12-01';
```

Selected result from the saved verification:

```text
mreyes
```

The encounter is a three-day Pain Clinic admission; the attending's username is `mreyes`. Note the audit-system username `mreyes_ehr` is a different field — not what's asked.

## Screenshot

![328-step-02.png](../screenshots/328-step-02.png)

## Flag

```text
deadface{mreyes}
```

## Takeaway

Use a half-open date range for "within a month" so you don't drop end-of-month rows, and return the exact username field the question names (`mreyes`, not `mreyes_ehr`).

## Reference

- [Original challenge and attachments](../../challenges/solved/deadface/328-the-attending/README.md)
