# Too Good to be True — saved solution

Flag / submission candidate: `deadface{VELT-0148}`

Our original PCGCTF snapshot already marks this challenge solved. Imported Garcia writeup; not independently reproduced during this import. Challenge already solved in our saved scoreboard snapshot.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Teammate’s writeup (quoted)

> ### Too Good to be True (1200) — Statistical Outlier / SQL
>
> **Flag:** `deadface{VELT-0148}`
>
> #### Challenge
>
> One subject's recorded efficacy improvement is a statistical impossibility — more than three standard deviations above the study-wide mean for the primary endpoint, a sign the number was invented rather than measured. Identify the outlier subject and report their subject code.
>
> #### Solution
>
> The primary endpoint is the `primary_efficacy_delta` measure in `aurora_trials.results`, recorded at Week 24 for 60 subjects. Compute each subject's z-score against the measure's mean and standard deviation in one pass, using a `CROSS JOIN` to a single-row aggregate:
>
> ```sql
> SELECT s.subject_code, s.arm, r.value,
>        ROUND((r.value - st.m)/st.sd_pop, 2)  AS z_pop,
>        ROUND((r.value - st.m)/st.sd_samp, 2) AS z_samp,
>        r.recorded_by, r.modified_by
> FROM aurora_trials.results r
> JOIN aurora_trials.subjects s ON s.subject_id = r.subject_id
> CROSS JOIN (
>   SELECT AVG(value) m, STDDEV_POP(value) sd_pop, STDDEV_SAMP(value) sd_samp
>   FROM aurora_trials.results WHERE measure = 'primary_efficacy_delta'
> ) st
> WHERE r.measure = 'primary_efficacy_delta'
> ORDER BY r.value DESC
> LIMIT 8;
> ```
>
> ```
> +--------------+-----------+-------+-------+--------+-------------+-------------+
> | subject_code | arm       | value | z_pop | z_samp | recorded_by | modified_by |
> +--------------+-----------+-------+-------+--------+-------------+-------------+
> | VELT-0148    | placebo   | 22.00 |  6.78 |   6.73 | tstack      | NULL        |
> | VELT-0137    | treatment |  6.00 |  1.08 |   1.07 | achang      | mreyes      |
> | VELT-0138    | placebo   |  5.25 |  0.81 |   0.81 | achang      | NULL        |
> | VELT-0130    | placebo   |  5.22 |  0.80 |   0.80 | tstack      | NULL        |
> +--------------+-----------+-------+-------+--------+-------------+-------------+
> ```
>
> Only `VELT-0148` clears the 3-SD bar — it sits **6.78** standard deviations above the mean of 2.97. The next-highest subject is at 1.08, and the lowest value (−1.00) is only ~1.4 SD below the mean, so nothing on the low tail qualifies either.
>
> Two points keep this from being confused with the *After the Lock* challenge:
>
> - `VELT-0148` has **no** `data_changes` entry and `modified_by` is `NULL` — it was fabricated at recording time, not edited after the lock.
> - The post-lock edit (`VELT-0137`, 2.3 → 6.0 by `mreyes`) only reaches z ≈ 1.08. It is a separate fabrication and is *not* the statistical outlier.
>
> A 22-point improvement on a **placebo** subject is the "too good to be true" tell. Subject code: `VELT-0148`.
>
> ---
