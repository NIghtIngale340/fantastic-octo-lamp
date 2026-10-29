SELECT s.subject_code,s.arm,r.value,
 ROUND((r.value-st.m)/st.sd,2) AS z_score
FROM aurora_trials.results r
JOIN aurora_trials.subjects s ON s.subject_id=r.subject_id
CROSS JOIN (SELECT AVG(value) AS m,STDDEV_POP(value) AS sd
            FROM aurora_trials.results
            WHERE measure='primary_efficacy_delta') st
WHERE r.measure='primary_efficacy_delta'
ORDER BY z_score DESC LIMIT 5;
