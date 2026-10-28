# Car Crash

**Platform:** PCGCTF · **Challenge ID:** 319 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot, but the original `car_crash.jpg` wasn't preserved — the USDOT number below comes from the teammate's recorded reading, not a crop I could re-verify. Flagging that.

## The challenge

Identify the trucking company in the crash photo and give its founding date as `MM_DD_YYYY`.

## Solving it

The cargo box carries a USDOT marking (teammate-recorded as `080806`). Looking that number up in FMCSA SAFER identifies the carrier, and the founding date comes from the carrier's own history — J.B. Hunt, founded 10 August 1961:

```text
USDOT 080806 → FMCSA SAFER → J.B. Hunt
Founding date: 1961-08-10 → 08_10_1961
```

## Flag

```text
deadface{08_10_1961}
```

## Still to do

- Recover `car_crash.jpg` and verify the exact USDOT digits from a crop before fully trusting the carrier identification.

## Takeaway

Attribute from the registration number (USDOT via FMCSA), not a visual resemblance — and get the founding date from the company's own record, watching the MM_DD_YYYY order.

## Reference

- [Original challenge and attachments](../../solved/deadface/319-car-crash/README.md)
