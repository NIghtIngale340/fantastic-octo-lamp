# ACT 4 - FIRST TO LAST: Infrastructure Pivot — analysis

Answer: **handyman24.eu**

Flag to submit (acceptance unvalidated):

```text
pcgCTF{handyman24.eu}
```

Evidence source: `Public DNS lookup`

Wireshark display filter:

```wireshark
dns.qry.name == "handyman24.eu"
```

Evidence: Public DNS/question evidence.

The question explicitly specifies this domain. A live public DNS lookup also returned 146.59.71.167. This is the requested public DNS pivot, while the captured C2 HTTP Host is www.grinswakebthu.info; shared IP hosting does not mean all hosted sites are malicious.

Platform status: PCGCTF is paused. No acceptance confirmed.

The display filter is for reproducing a DNS lookup in a new capture, not a claim that handyman24.eu occurs in the supplied incident PCAP. The actual public DNS JSON is saved in the analysis folder.

Sources:

- [Google public DNS result](https://dns.google/resolve?name=handyman24.eu&type=A)
