# File Dump 01

**Platform:** PCGCTF · **Challenge ID:** 339 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the old snapshot, but `File_Dump_Challenge.zip` wasn't preserved. The flag is from the teammate's record; I can't show the decisive artifact here, so I'm flagging it.

## The challenge

Identify the DEADFACE alias responsible for the stolen identity in the intercepted laptop dump.

## Solving it

The method is to triage the dump — file types and explicit identity artifacts first, then follow any real steganography clue to the alias:

```sh
exiftool -a -G1 -s recovered-dump/*
rg -a -i "deadface|alias|handle" recovered-dump/
```

The alias tied to the stolen identity is:

```text
deadface{gh0st404}
```

## Screenshot

![339-actual-artifact-inventory.png](../screenshots/339-actual-artifact-inventory.png)

## Flag

```text
deadface{gh0st404}
```

## Still to do

- Recover the dump, identify the actual alias-bearing artifact, and establish *why* it points to the responsible crew member rather than a contact or decoy.

## Takeaway

Start triage from file type and explicit identity artifacts; a handle found in one unrelated note needs corroboration before it's the answer.

## Reference

- [Original challenge and attachments](../../solved/deadface/339-file-dump-01/README.md)
