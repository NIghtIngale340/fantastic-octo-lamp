# ACT 4 — Lumma in the Room: Fingerprint API

**Platform:** PCGCTF · **Challenge ID:** 288 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the Act 4 capture. Exact PCGCTF submission not independently re-confirmed.

## The challenge

Recover the API path Lumma uses for victim registration.

## Solving it

Use [the shared capture](../../unsolved/network-forensics/282-act-4-lumma-in-the-room-lumma-victim/files/2026-01-31-traffic-analysis-exercise.pcap) as `act4.pcap` for the commands below.

```sh
tshark -nr act4.pcap -Y 'http.host=="whitepepper.su"' -T fields -e http.request.uri | sort -u | head -n 8
```

```text
/api/set_agent?id=3BF67EC05320C5729578BE4C0ADF174C&token=842e2802df0f0a06b4ed51f12f4387e761523b&description=&agent=Chrome
/api/set_agent?id=3BF67EC05320C5729578BE4C0ADF174C&token=842e2802df0f0a06b4ed51f12f4387e761523b&description=&agent=Chrome&act=log
/api/set_agent?id=3BF67EC05320C5729578BE4C0ADF174C&token=842e2802df0f0a06b4ed51f12f4387e761523b&description=&agent=Edge
/api/set_agent?id=3BF67EC05320C5729578BE4C0ADF174C&token=842e2802df0f0a06b4ed51f12f4387e761523b&description=&agent=Edge&act=log
/favicon.ico
```

Stripping the query string, the endpoint is `/api/set_agent`.

## Screenshot

Fresh local reproduction using the command described above.

![Command and result](../screenshots/288-clear-method.png)

## Flag

```text
pcgCTF{/api/set_agent}
```

## Takeaway

`/api/set_agent` is Lumma's registration endpoint. The answer is the path — the `id`/`token` query parameters are the per-victim data, not part of it.

## Reference

- [Original challenge description](../../unsolved/network-forensics/288-act-4-lumma-in-the-room-fingerprint-api/README.md)
