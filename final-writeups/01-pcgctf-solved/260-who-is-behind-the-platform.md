# Who Is Behind the Platform?

**Platform:** PCGCTF · **Challenge ID:** 260 · **Category:** General Skills · **Points:** 20000

**Status:** Solved in the last snapshot. Creator identity confirmed from the primary profile; I haven't re-run the root-commit check, so I'm flagging that as unfinished rather than claiming it.

## The challenge

Find the creator of the open-source CTF platform by following its earliest project history.

## Solving it

The clues point at CTFd (the platform software), not the organiser of this particular event. CTFd's author is Kevin Chung, who goes by `ColdHeat` on GitHub — his own profile states he created CTFd:

```text
Kevin Chung — github.com/ColdHeat — "Creator of CTFd"
```

The clean way to nail "who *started* it" is the root commit of the upstream repo:

```sh
git clone https://github.com/CTFd/CTFd.git /tmp/ctfd
git -C /tmp/ctfd rev-list --max-parents=0 HEAD
git -C /tmp/ctfd show --no-patch --format=fuller <root-commit>
```

I didn't run that clone in this pass, so I'm treating the root-commit author as still-to-confirm rather than asserting it. The profile statement alone already supports Kevin Chung.

## Screenshot

![260-primary-profile.png](../screenshots/260-primary-profile.png)

## Flag

```text
pcgCTF{Kevin Chung}
```

## Still to do

- Run the root-commit commands and save the real author/date/hash.
- Confirm the accepted capitalisation/spacing from the submission history.

## Takeaway

"Who made this project" is a provenance question — a current maintainer isn't necessarily the founder. Use the original history plus a primary identity statement.

## References

- [Kevin Chung / ColdHeat](https://github.com/ColdHeat)
- [CTFd upstream](https://github.com/CTFd/CTFd)
- [Original challenge and attachments](</home/nightingale/CTF/PCGCTF/solved/general-skills/260-who-is-behind-the-platform/README.md>)
