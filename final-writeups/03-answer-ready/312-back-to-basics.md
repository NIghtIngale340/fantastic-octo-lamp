# Back to Basics

**Platform:** PCGCTF · **Challenge ID:** 312 · **Category:** Aurora Patient Zero · **Points:** 100

**Status:** Answer backed by the binary's strings. Exact PCGCTF submission not re-confirmed.

## The challenge

Identify the gateway named in the app's hidden diagnostic data.

## Solving it

I ran a strings pass over the bundled executable to navigate to the diagnostic section, where the gateway label and value sit together:

```sh
strings -n 4 'Aurora Health Mobile' | rg -i -A 2 'gateway'
```

The relevant value is `gw-westlake-int-03`.

The gateway is `gw-westlake-int-03` (the Westlake clinic, matching the bootstrap data from #309).

## Screenshot

Fresh local reproduction using the command described above.

![Command and result](../screenshots/312-clear-method-v2.png)

## Flag

```text
deadface{gw-westlake-int-03}
```

## Takeaway

`strings` is navigation, not proof — it points you at the diagnostic section, then follow the label→value pairing in the actual code to be sure you've got the gateway, not a neighbouring field.

## Reference

- [Original challenge description](../../unsolved/aurora-patient-zero/312-back-to-basics/README.md)
