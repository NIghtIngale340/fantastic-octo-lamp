# Live Boot

**Platform:** PCGCTF · **Challenge ID:** 318 · **Category:** Deadface · **Points:** 100

**Status:** Solved in the last snapshot; reproduced from the device response.

## The challenge

Reach the simulated scanner's internal filesystem via its live Linux environment and recover a hardcoded API key.

## Solving it

Booting the device's live Linux tool gives access to the mounted application config, which has the key sitting in plaintext:

```text
live Linux → read mounted app config → API key hardcoded in the config
deadface{h4rdc0d3d_k3ys_1n_th3_c0nf1g}
```

## Screenshots

The terminal image below displays a retained verification transcript.

![318-actual-device-response.png](../screenshots/318-actual-device-response.png)

![318-actual-device-proof.png](../screenshots/318-actual-device-proof.png)

## Flag

```text
deadface{h4rdc0d3d_k3ys_1n_th3_c0nf1g}
```

## Takeaway

A secret hardcoded in a config file is only as protected as filesystem access — a live-boot environment walks right past the application.

## Reference

- [Original challenge and attachments](../../solved/deadface/318-live-boot/README.md)
