# ACT 1 — First Signal: Full Identity

**Platform:** PCGCTF · **Challenge ID:** 266 · **Category:** Network Forensics · **Points:** 100

**Status:** Solved in the authenticated snapshot; reproduced from the Act 1 capture.

**Evidence:** Packet 1939 · TCP stream 86 · [ACT12026-08-09-traffic-analysis-exercise.pcap](../../solved/network-forensics/262-act-1-first-signal-patient-zero/files/ACT12026-08-09-traffic-analysis-exercise.pcap).

## The challenge

Build the victim's fully qualified domain name.

## Solving it

Use [the shared capture](../../solved/network-forensics/262-act-1-first-signal-patient-zero/files/ACT12026-08-09-traffic-analysis-exercise.pcap) as `act1.pcap` for the commands below.

Kerberos ties the two halves together — the client name and the realm appear in the AS-REQ:

```sh
tshark -nr act1.pcap -Y 'ip.src==172.16.8.49 && kerberos.CNameString' \
  -T fields -e kerberos.CNameString -e kerberos.realm | sort -u
```

```text
DESKTOP-5NLV63K$	FIRSTTOLAST.TECH
desktop-5nlv63k$	FIRSTTOLAST.TECH
desktop-5nlv63k$	firsttolast.tech
rvance	FIRSTTOLAST
rvance	FIRSTTOLAST.TECH
```

So the hostname is `DESKTOP-5NLV63K` and the domain is `firsttolast.tech` — put together, `DESKTOP-5NLV63K.firsttolast.tech`.

## Screenshot

Fresh local reproduction using the command described above.

![Command and result](../screenshots/266-clear-method-v2.png)

## Flag

```text
pcgCTF{DESKTOP-5NLV63K.firsttolast.tech}
```

## Takeaway

Kerberos carries both the machine account (the `$`-suffixed CNameString) and the realm, which is exactly the hostname + domain you need for an FQDN.

## Reference

- [Original challenge description](../../solved/network-forensics/266-act-1-first-signal-full-identity/README.md)
