# Who Is Behind the Platform?

**Platform:** PCGCTF · **Challenge ID:** 260 · **Category:** General Skills · **Points:** 20000

**Status:** Solved in the last snapshot. The saved primary-profile evidence supports the creator's identity; the earliest-commit check remains unverified.

## The challenge

Find the creator of the open-source CTF platform by following its earliest project history.

## Solving it

The clues point at CTFd (the platform software), not the organiser of this particular event. CTFd's author is Kevin Chung, who goes by `ColdHeat` on GitHub — his own profile states he created CTFd:

```text
Kevin Chung — github.com/ColdHeat — "Creator of CTFd"
```

The saved profile supports Kevin Chung as the creator. The challenge also points to the project's earliest history; checking the root commit would complete that part of the evidence. It has not been rerun here.

## Screenshot

![260-primary-profile.png](../screenshots/260-primary-profile.png)

## Flag

```text
pcgCTF{Kevin Chung}
```

## Still to do

- Inspect the upstream repository’s earliest commit and record its author, date and hash.
- Confirm the accepted capitalisation/spacing from the submission history.

## Takeaway

"Who made this project" is a provenance question — a current maintainer isn't necessarily the founder. Use the original history plus a primary identity statement.

## References

- [Kevin Chung / ColdHeat](https://github.com/ColdHeat)
- [CTFd upstream](https://github.com/CTFd/CTFd)
- [Original challenge and attachments](<../../home/nightingale/CTF/PCGCTF/solved/general-skills/260-who-is-behind-the-platform/README.md>)
