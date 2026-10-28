# Bedside Manner

**Platform:** PCGCTF · **Challenge ID:** 315 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot; reproduced from the device response.

## The challenge

Inspect the exposed medical-device kiosk's HTML for a developer string.

## Solving it

The kiosk login page renders normally, but the flag is in a left-behind developer comment in the source:

```html
<!-- TODO(dev): REMOVE before go-live — temporary QA technician PIN: deadface{v13w_s0urc3_sav3s_l1v3s} -->
```

That's the challenge flag. (Note the comment frames it as a QA PIN — I kept the challenge flag separate from anything that would be an operational credential.)

## Screenshots

![315-actual-device-response.png](../screenshots/315-actual-device-response.png)

![315-actual-device-proof.png](../screenshots/315-actual-device-proof.png)

## Flag

```text
deadface{v13w_s0urc3_sav3s_l1v3s}
```

## Takeaway

"View source saves lives" is the point — anything the server sends to render the page is readable, including the comments developers forget to strip.

## Reference

- [Original challenge and attachments](../../solved/deadface/315-bedside-manner/README.md)
