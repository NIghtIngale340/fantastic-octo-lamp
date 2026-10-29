# Commitment Issues — saved solution

Flag / submission candidate: `picoCTF{s@n1t1z3_be3dd3da}`

Our original PCGCTF snapshot already marks this challenge solved. Flag independently recovered from the original archive’s Git object and SHA-1 checked. Original picoCTF wrapper retained; exact historical PCGCTF submission is not recorded.

Source: **Antonio B. Garcia Jr.**, 2026-10-28, [Day 1 writeup](../../../../team/garcia-day1/source.md). The challenge’s name, points and solved snapshot remain those of our original inventory.

## Independent recovery

The original archive contains loose Git objects. Decompressing the blob and verifying its SHA-1 yields `picoCTF{s@n1t1z3_be3dd3da}`. Commit `7d3aa557ff7ba7d116badaf5307761efb3622249` is the create-flag commit, followed by removal commit `144fdc44b09058d7ea7f224121dfa5babadddbb9`. [Recovered object and hash](../../../../team/garcia-day1/git-recovered-objects.json).

The recovered source uses the `picoCTF` prefix; this challenge specifies no replacement wrapper, so it is preserved. We did not infer a `pcgCTF` variant.

## Teammate’s method (quoted)

> ## Git History Recovery — Forensics
>
> **Directory:** `drop-in/`
>
> #### Challenge
>
> A directory containing a `.git` folder and a single `message.txt`.
>
> #### Solution
>
> The working tree gives nothing:
>
> ```bash
> cat message.txt
> # TOP SECRET
> ```
>
> But the repository history has two commits:
>
> ```bash
> git log --oneline
> ```
> ```
> 144fdc4 remove sensitive info
> 7d3aa55 create flag
> ```
>
> A commit that removes a file does not erase it — the earlier blob stays in the object database. Either command recovers it:
>
> ```bash
> git show 144fdc4              # the removed line appears as a '-' in the diff
> git show 7d3aa55:message.txt  # prints the file as it was at that commit
> ```
>
> The second form is cleaner, printing the original file contents directly.
>
> **Takeaway:** anything ever committed to git survives later deletion. Removing a secret properly requires rewriting history (`git filter-repo`) and rotating the secret, since clones and forks keep their own copies.
>
> ---
