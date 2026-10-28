# ACT 5 — Final Incident: Host Three MAC

**Platform:** PCGCTF · **Challenge ID:** 292 · **Category:** Network Forensics · **Points:** 100

**Status:** Answer backed by the Act 5 capture. Exact PCGCTF submission not independently re-confirmed.

## The challenge

MAC for 10.3.14.135.

## Solving it

Use [the shared capture](../../unsolved/network-forensics/289-act-5-final-incident-map-the-network/files/2017-02-11-traffic-analysis-exercise.pcap) as `act5.pcap` for the commands below.

```sh
tshark -nr act5.pcap -Y 'ip.src==10.3.14.135' -T fields -e eth.src | head -1
```

```text
00:26:bb:4c:6b:e1
```

## Screenshot

Fresh local reproduction using the command described above.

![Command and result](../screenshots/292-clear-method.png)

## Flag

```text
pcgCTF{00:26:bb:4c:6b:e1}
```

## Reference

- [Original challenge description](../../unsolved/network-forensics/292-act-5-final-incident-host-three-mac/README.md)
