# Bitcoin Trail — solution

Recovered answer: **bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh**

Flag candidate:

```text
pcgCTF{bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh}
```

Capture: `cryptocurrency_transfer_tracking.pcap`

Filter:

```wireshark
frame.number == 196 || frame.number == 187 || frame.number == 218
```

Frames: 187, 196, 218. TCP streams: 17, 18.

The wallet appears in a Bitcoin JSON-RPC sendtoaddress request (frame 196), as well as listunspent/gettransaction responses (frames 187 and 218). The address is an observed string from the supplied capture; no wallet interaction or transfer was performed.

Platform acceptance: unconfirmed. No submissions made in this batch.
