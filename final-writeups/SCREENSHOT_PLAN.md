# Screenshot capture results

Updated: 2026-10-29T04:13:22+08:00.

> **Rendering note (2026-10-29):** the 199 terminal captures were re-rendered in Konsole from the same retained PTY transcripts so the published images look like a real terminal rather than the xterm.js viewer. This is a presentation change only; the transcripts remain the source of truth. See `screenshots/konsole/render-manifest.json`; originals are in `screenshots/xtermjs-backup/`.

**230 real captures across all 192 challenge drafts.** Terminal images show actual local PTY output; browser images show actual pages, original supplied images or live SQL results. Commands, timestamps, exit codes, transcripts and image SHA-256 values are retained in the [capture manifest](screenshots/capture-manifest.json). Passwords were redacted before display.

The original 253 placement requests remain in [the machine-readable plan](screenshot-plan.json), each mapped to the actual captures. A related capture demonstrates only its stated action; it does not stand in for a missing artifact analysis, a full schema listing, a fresh external IOC query or an unrecorded grader result. No screenshot chores have been assigned to the user.

## Remaining evidence dependencies

- 26 challenge services could not be reached in bounded requests. Their actual errors were captured.
- Seven historical challenge payloads are missing. Their actual directory inventories were captured.
- #319 has a captured first-party anniversary page, but its original truck photograph is missing.
- #261 supplies no target URL or original API response. The available evidence was captured.
- #83, #102 and #112 still need the organizer’s accepted wording; #18 still has no accepted flag. Their technical analyses are captured, but no new PCGCTF submissions were made.
- Original source images support the OSINT/IMINT reasoning but do not replace primary-source corroboration. Saved IOC records are labeled as preserved records rather than fresh lookups.

## Captures by challenge

| ID | Draft | Actual screenshots | Evidence dependency |
|---:|---|---:|---|
| 1 | [Hash Me If You Can](01-pcgctf-solved/001-hash-me-if-you-can.md) | 2 | No capture dependency for the documented result |
| 2 | [Picture Perfect Evidence](01-pcgctf-solved/002-picture-perfect-evidence.md) | 2 | No capture dependency for the documented result |
| 3 | [Ancient Message](01-pcgctf-solved/003-ancient-message.md) | 1 | No capture dependency for the documented result |
| 4 | [Encoded Secret](01-pcgctf-solved/004-encoded-secret.md) | 1 | No capture dependency for the documented result |
| 5 | [Silent Signal](01-pcgctf-solved/005-silent-signal.md) | 1 | No capture dependency for the documented result |
| 6 | [Hidden in Plain Sight](02-overthewire-verified/006-hidden-in-plain-sight.md) | 2 | No capture dependency for the documented result |
| 7 | [Access Denied? Think Again](02-overthewire-verified/007-access-denied-think-again.md) | 2 | No capture dependency for the documented result |
| 8 | [Forgotten Files](02-overthewire-verified/008-forgotten-files.md) | 2 | No capture dependency for the documented result |
| 9 | [Robots Know Everything](02-overthewire-verified/009-robots-know-everything.md) | 2 | No capture dependency for the documented result |
| 10 | [Trust the Referer](02-overthewire-verified/010-trust-the-referer.md) | 2 | No capture dependency for the documented result |
| 12 | [The Cookie Jar](02-overthewire-verified/012-the-cookie-jar.md) | 2 | No capture dependency for the documented result |
| 13 | [The Exposed Script](02-overthewire-verified/013-the-exposed-script.md) | 2 | No capture dependency for the documented result |
| 14 | [Path Explorer](02-overthewire-verified/014-path-explorer.md) | 2 | No capture dependency for the documented result |
| 15 | [Layers of Encoding](02-overthewire-verified/015-layers-of-encoding.md) | 2 | No capture dependency for the documented result |
| 16 | [Command Me](02-overthewire-verified/016-command-me.md) | 2 | No capture dependency for the documented result |
| 17 | [Filtered but Broken](02-overthewire-verified/017-filtered-but-broken.md) | 2 | No capture dependency for the documented result |
| 18 | [Rotation 36](05-rejected-flag/018-rotation-36.md) | 1 | No capture dependency for the documented result |
| 20 | [Base Maze](01-pcgctf-solved/020-base-maze.md) | 2 | No capture dependency for the documented result |
| 21 | [Packet Detective](03-answer-ready/021-packet-detective.md) | 1 | No capture dependency for the documented result |
| 22 | [FTP Credential Leak](03-answer-ready/022-ftp-credential-leak.md) | 1 | No capture dependency for the documented result |
| 33 | [Multi-Base Layers](01-pcgctf-solved/033-multi-base-layers.md) | 2 | No capture dependency for the documented result |
| 34 | [ROT13](01-pcgctf-solved/034-rot13.md) | 1 | No capture dependency for the documented result |
| 35 | [Riddle Registry](01-pcgctf-solved/035-riddle-registry.md) | 2 | No capture dependency for the documented result |
| 36 | [Commitment Issues](01-pcgctf-solved/036-commitment-issues.md) | 2 | No capture dependency for the documented result |
| 38 | [The Lazy Gatekeeper](01-pcgctf-solved/038-the-lazy-gatekeeper.md) | 1 | target unreachable |
| 39 | [The Forgotten Path](06-unresolved-appendix/039-the-forgotten-path.md) | 1 | target unreachable |
| 40 | [Silent Witness](06-unresolved-appendix/040-silent-witness.md) | 1 | target unreachable |
| 41 | [The Cracked Seal](06-unresolved-appendix/041-the-cracked-seal.md) | 1 | target unreachable |
| 42 | [The Changing Door](06-unresolved-appendix/042-the-changing-door.md) | 1 | target unreachable |
| 43 | [The Invisible Crown](06-unresolved-appendix/043-the-invisible-crown.md) | 1 | target unreachable |
| 45 | [The Open Warehouse](06-unresolved-appendix/045-the-open-warehouse.md) | 1 | target unreachable |
| 46 | [The Open Door API](06-unresolved-appendix/046-the-open-door-api.md) | 1 | target unreachable |
| 47 | [The Base64](06-unresolved-appendix/047-the-base64.md) | 1 | target unreachable |
| 49 | [Robots That Talk Too Much](06-unresolved-appendix/049-robots-that-talk-too-much.md) | 1 | target unreachable |
| 50 | [Commented Out Secrets](06-unresolved-appendix/050-commented-out-secrets.md) | 1 | target unreachable |
| 51 | [The JavaScript Slip](06-unresolved-appendix/051-the-javascript-slip.md) | 1 | target unreachable |
| 52 | [Configuration Left Behind](06-unresolved-appendix/052-configuration-left-behind.md) | 1 | target unreachable |
| 53 | [Through the Wrong Door](06-unresolved-appendix/053-through-the-wrong-door.md) | 1 | target unreachable |
| 54 | [The Exposed Repository](06-unresolved-appendix/054-the-exposed-repository.md) | 1 | target unreachable |
| 55 | [Environment Variables Gone Public](06-unresolved-appendix/055-environment-variables-gone-public.md) | 1 | target unreachable |
| 56 | [The Hidden Storage](06-unresolved-appendix/056-the-hidden-storage.md) | 1 | target unreachable |
| 57 | [The Viral Name](03-answer-ready/057-the-viral-name.md) | 1 | No capture dependency for the documented result |
| 60 | [CryptoMaze](01-pcgctf-solved/060-cryptomaze.md) | 2 | No capture dependency for the documented result |
| 61 | [The Exposed Password](03-answer-ready/061-the-exposed-password.md) | 1 | No capture dependency for the documented result |
| 62 | [THE HIDDEN DOWNLOAD](03-answer-ready/062-the-hidden-download.md) | 1 | No capture dependency for the documented result |
| 63 | [Caesar's Last Stand](01-pcgctf-solved/063-caesar-s-last-stand.md) | 1 | No capture dependency for the documented result |
| 64 | [Broken Vigenere](01-pcgctf-solved/064-broken-vigenere.md) | 2 | No capture dependency for the documented result |
| 65 | [Small Exponent](01-pcgctf-solved/065-small-exponent.md) | 1 | No capture dependency for the documented result |
| 66 | [Common Modulus](01-pcgctf-solved/066-common-modulus.md) | 1 | No capture dependency for the documented result |
| 67 | [Weak RSA](06-unresolved-appendix/067-weak-rsa.md) | 1 | No capture dependency for the documented result |
| 69 | [Bitcoin Trail](03-answer-ready/069-bitcoin-trail.md) | 1 | No capture dependency for the documented result |
| 70 | [HTTP File Extraction](01-pcgctf-solved/070-http-file-extraction.md) | 2 | No capture dependency for the documented result |
| 71 | [EMBEDDED TEXT](01-pcgctf-solved/071-embedded-text.md) | 2 | No capture dependency for the documented result |
| 73 | [BAD BLOCKCHAIN](03-answer-ready/073-bad-blockchain.md) | 1 | No capture dependency for the documented result |
| 74 | [ELLIOT'S SECRET STASH](03-answer-ready/074-elliot-s-secret-stash.md) | 1 | No capture dependency for the documented result |
| 75 | [HIDDEN](03-answer-ready/075-hidden.md) | 2 | No capture dependency for the documented result |
| 77 | [HIT A BRICK WALL](03-answer-ready/077-hit-a-brick-wall.md) | 2 | No capture dependency for the documented result |
| 78 | [INTERCEPTED](01-pcgctf-solved/078-intercepted.md) | 2 | No capture dependency for the documented result |
| 79 | [SEQUENCE](03-answer-ready/079-sequence.md) | 2 | No capture dependency for the documented result |
| 80 | [TO THE MOON!](03-answer-ready/080-to-the-moon.md) | 3 | No capture dependency for the documented result |
| 81 | [TURTLES ALL THE WAY DOWN](01-pcgctf-solved/081-turtles-all-the-way-down.md) | 2 | No capture dependency for the documented result |
| 82 | [EASY PACKET 1  The Exposed Request](01-pcgctf-solved/082-easy-packet-1-the-exposed-request.md) | 1 | No capture dependency for the documented result |
| 83 | [EASY PACKET 1 #01  The Capture Signature](04-exact-wording-missing/083-easy-packet-1-01-the-capture-signature.md) | 2 | No capture dependency for the documented result |
| 84 | [EASY PACKET 1 #02  One Packet Wonder](01-pcgctf-solved/084-easy-packet-1-02-one-packet-wonder.md) | 1 | No capture dependency for the documented result |
| 85 | [EASY PACKET 1 #03  Destination at Layer 2](03-answer-ready/085-easy-packet-1-03-destination-at-layer-2.md) | 1 | No capture dependency for the documented result |
| 86 | [EASY PACKET 1 #04  Source at Layer 2](03-answer-ready/086-easy-packet-1-04-source-at-layer-2.md) | 1 | No capture dependency for the documented result |
| 87 | [EASY PACKET 1 #05  EtherType: IPv4](01-pcgctf-solved/087-easy-packet-1-05-ethertype-ipv4.md) | 1 | No capture dependency for the documented result |
| 88 | [EASY PACKET 1 #06  Version Four](01-pcgctf-solved/088-easy-packet-1-06-version-four.md) | 1 | No capture dependency for the documented result |
| 89 | [EASY PACKET 1 #07  The 20-Byte Header](03-answer-ready/089-easy-packet-1-07-the-20-byte-header.md) | 1 | No capture dependency for the documented result |
| 90 | [EASY PACKET 1 #08  Total Packet Weight](03-answer-ready/090-easy-packet-1-08-total-packet-weight.md) | 1 | No capture dependency for the documented result |
| 91 | [EASY PACKET 1 #09  Packet Identity](03-answer-ready/091-easy-packet-1-09-packet-identity.md) | 1 | No capture dependency for the documented result |
| 92 | [EASY PACKET 1 #10  TTL: 64 Hops](01-pcgctf-solved/092-easy-packet-1-10-ttl-64-hops.md) | 1 | No capture dependency for the documented result |
| 93 | [EASY PACKET 1 #11  Protocol 6](01-pcgctf-solved/093-easy-packet-1-11-protocol-6.md) | 1 | No capture dependency for the documented result |
| 94 | [EASY PACKET 1 #12  Who Sent It?](01-pcgctf-solved/094-easy-packet-1-12-who-sent-it.md) | 1 | No capture dependency for the documented result |
| 95 | [EASY PACKET 1 #13  Where Is It Going?](01-pcgctf-solved/095-easy-packet-1-13-where-is-it-going.md) | 1 | No capture dependency for the documented result |
| 96 | [EASY PACKET 1 #14  Ephemeral Source](01-pcgctf-solved/096-easy-packet-1-14-ephemeral-source.md) | 1 | No capture dependency for the documented result |
| 97 | [EASY PACKET 1 #15  Port 80](01-pcgctf-solved/097-easy-packet-1-15-port-80.md) | 1 | No capture dependency for the documented result |
| 98 | [EASY PACKET 1 #16  TCP Sequence Marker](01-pcgctf-solved/098-easy-packet-1-16-tcp-sequence-marker.md) | 1 | No capture dependency for the documented result |
| 99 | [EASY PACKET 1 #17  TCP Acknowledgment Marker](01-pcgctf-solved/099-easy-packet-1-17-tcp-acknowledgment-marker.md) | 1 | No capture dependency for the documented result |
| 100 | [EASY PACKET 1 #18  Push and Acknowledge](03-answer-ready/100-easy-packet-1-18-push-and-acknowledge.md) | 1 | No capture dependency for the documented result |
| 101 | [EASY PACKET 1 #19  TCP Window](01-pcgctf-solved/101-easy-packet-1-19-tcp-window.md) | 1 | No capture dependency for the documented result |
| 102 | [EASY PACKET 1 #20  Push to the Application](04-exact-wording-missing/102-easy-packet-1-20-push-to-the-application.md) | 1 | No capture dependency for the documented result |
| 103 | [EASY PACKET 1 #21  Speak HTTP](03-answer-ready/103-easy-packet-1-21-speak-http.md) | 1 | No capture dependency for the documented result |
| 104 | [EASY PACKET 1 #22  GET the Resource](01-pcgctf-solved/104-easy-packet-1-22-get-the-resource.md) | 1 | No capture dependency for the documented result |
| 105 | [EASY PACKET 1 #23  The Requested Path](01-pcgctf-solved/105-easy-packet-1-23-the-requested-path.md) | 1 | No capture dependency for the documented result |
| 106 | [EASY PACKET 1 #24  HTTP/1.1](01-pcgctf-solved/106-easy-packet-1-24-http-1-1.md) | 1 | No capture dependency for the documented result |
| 107 | [EASY PACKET 1 #25  Know Your Host](01-pcgctf-solved/107-easy-packet-1-25-know-your-host.md) | 1 | No capture dependency for the documented result |
| 108 | [EASY PACKET 1 #26  Identify the Client](01-pcgctf-solved/108-easy-packet-1-26-identify-the-client.md) | 1 | No capture dependency for the documented result |
| 109 | [EASY PACKET 1 #27  Keep the Connection](01-pcgctf-solved/109-easy-packet-1-27-keep-the-connection.md) | 1 | No capture dependency for the documented result |
| 110 | [EASY PACKET 1 #28  Basic Authentication](01-pcgctf-solved/110-easy-packet-1-28-basic-authentication.md) | 1 | No capture dependency for the documented result |
| 111 | [EASY PACKET 1 #29  The Exposed Credentials](03-answer-ready/111-easy-packet-1-29-the-exposed-credentials.md) | 1 | No capture dependency for the documented result |
| 112 | [EASY PACKET 1 #30  Cleartext on the Wire](04-exact-wording-missing/112-easy-packet-1-30-cleartext-on-the-wire.md) | 1 | No capture dependency for the documented result |
| 113 | [Web Recon - View Source](06-unresolved-appendix/113-web-recon-view-source.md) | 1 | target unreachable |
| 114 | [Web Recon — Hidden Directory](06-unresolved-appendix/114-web-recon-hidden-directory.md) | 1 | target unreachable |
| 115 | [Web Recon — Git Repository Leak](06-unresolved-appendix/115-web-recon-git-repository-leak.md) | 1 | target unreachable |
| 116 | [Web Recon — Read the Headers](06-unresolved-appendix/116-web-recon-read-the-headers.md) | 1 | target unreachable |
| 117 | [Infrastructure — Unsecured Reverse Proxy](06-unresolved-appendix/117-infrastructure-unsecured-reverse-proxy.md) | 1 | target unreachable |
| 118 | [Path Traversal — Off by Slash](06-unresolved-appendix/118-path-traversal-off-by-slash.md) | 1 | target unreachable |
| 119 | [SSRF — Reach the Internal Service](06-unresolved-appendix/119-ssrf-reach-the-internal-service.md) | 1 | target unreachable |
| 120 | [Access Control — User-Agent Bypass](06-unresolved-appendix/120-access-control-user-agent-bypass.md) | 1 | target unreachable |
| 121 | [Server Configuration — .htaccess Override](06-unresolved-appendix/121-server-configuration-htaccess-override.md) | 1 | target unreachable |
| 122 | [PCGCTF Juice Shop Gateway](03-answer-ready/122-pcgctf-juice-shop-gateway.md) | 1 | No capture dependency for the documented result |
| 239 | [Street-Level Clue](01-pcgctf-solved/239-street-level-clue.md) | 1 | No capture dependency for the documented result |
| 240 | [Tube Station — City](01-pcgctf-solved/240-tube-station-city.md) | 1 | No capture dependency for the documented result |
| 241 | [Tube Station — Station](01-pcgctf-solved/241-tube-station-station.md) | 1 | No capture dependency for the documented result |
| 242 | [Tube Station — Opening Year](01-pcgctf-solved/242-tube-station-opening-year.md) | 1 | No capture dependency for the documented result |
| 243 | [Tube Station — Platforms](01-pcgctf-solved/243-tube-station-platforms.md) | 1 | No capture dependency for the documented result |
| 244 | [Airport Context — Building](03-answer-ready/244-airport-context-building.md) | 1 | No capture dependency for the documented result |
| 247 | [Coffee Shop — City](03-answer-ready/247-coffee-shop-city.md) | 1 | No capture dependency for the documented result |
| 252 | [Reverse Image — Restaurant](01-pcgctf-solved/252-reverse-image-restaurant.md) | 1 | No capture dependency for the documented result |
| 253 | [Reverse Image — Editor](03-answer-ready/253-reverse-image-editor.md) | 1 | No capture dependency for the documented result |
| 254 | [Sculpture — Identification](03-answer-ready/254-sculpture-identification.md) | 1 | No capture dependency for the documented result |
| 256 | [Justice — Character](03-answer-ready/256-justice-character.md) | 1 | No capture dependency for the documented result |
| 259 | [Hotel From the Past](03-answer-ready/259-hotel-from-the-past.md) | 1 | No capture dependency for the documented result |
| 260 | [Who Is Behind the Platform?](01-pcgctf-solved/260-who-is-behind-the-platform.md) | 1 | No capture dependency for the documented result |
| 261 | [Password Hash Leak](06-unresolved-appendix/261-password-hash-leak.md) | 1 | target unspecified |
| 262 | [ACT 1 - FIRST SIGNAL: Patient Zero](01-pcgctf-solved/262-act-1-first-signal-patient-zero.md) | 1 | No capture dependency for the documented result |
| 263 | [ACT 1 - FIRST SIGNAL: Hardware Fingerprint](01-pcgctf-solved/263-act-1-first-signal-hardware-fingerprint.md) | 1 | No capture dependency for the documented result |
| 264 | [ACT 1 - FIRST SIGNAL: Name the Host](01-pcgctf-solved/264-act-1-first-signal-name-the-host.md) | 1 | No capture dependency for the documented result |
| 265 | [ACT 1 - FIRST SIGNAL: Domain Membership](03-answer-ready/265-act-1-first-signal-domain-membership.md) | 1 | No capture dependency for the documented result |
| 266 | [ACT 1 - FIRST SIGNAL: Full Identity](01-pcgctf-solved/266-act-1-first-signal-full-identity.md) | 1 | No capture dependency for the documented result |
| 267 | [ACT 1 - FIRST SIGNAL: Calling Home](03-answer-ready/267-act-1-first-signal-calling-home.md) | 1 | No capture dependency for the documented result |
| 268 | [ACT 2 - THE COMPROMISE: Infected IPV4](01-pcgctf-solved/268-act-2-the-compromise-infected-ipv4.md) | 1 | No capture dependency for the documented result |
| 269 | [ACT 2 - THE COMPROMISE: VICTIM MAC](01-pcgctf-solved/269-act-2-the-compromise-victim-mac.md) | 1 | No capture dependency for the documented result |
| 270 | [ACT 2 - THE COMPROMISE: VICTIM HOSTNAME](01-pcgctf-solved/270-act-2-the-compromise-victim-hostname.md) | 1 | No capture dependency for the documented result |
| 271 | [ACT 2 - THE COMPROMISE: Identify the User -User Account](01-pcgctf-solved/271-act-2-the-compromise-identify-the-user-user-account.md) | 1 | No capture dependency for the documented result |
| 272 | [ACT 2 - THE COMPROMISE: Who Is brolf?](03-answer-ready/272-act-2-the-compromise-who-is-brolf.md) | 1 | No capture dependency for the documented result |
| 274 | [ACT 2 - THE COMPROMISE: RAT Check-In](03-answer-ready/274-act-2-the-compromise-rat-check-in.md) | 1 | No capture dependency for the documented result |
| 274 | [ACT 3 - MALWARE INVESTIGATION: Compromised Endpoint](03-answer-ready/274-act-3-malware-investigation-compromised-endpoint.md) | 1 | No capture dependency for the documented result |
| 275 | [ACT 3 - MALWARE INVESTIGATION: Endpoint MAC](03-answer-ready/275-act-3-malware-investigation-endpoint-mac.md) | 1 | No capture dependency for the documented result |
| 276 | [ACT 3 - MALWARE INVESTIGATION: Endpoint Name](03-answer-ready/276-act-3-malware-investigation-endpoint-name.md) | 1 | No capture dependency for the documented result |
| 277 | [ACT 3 - MALWARE INVESTIGATION: Compromised Account](03-answer-ready/277-act-3-malware-investigation-compromised-account.md) | 1 | No capture dependency for the documented result |
| 278 | [ACT 3 - MALWARE INVESTIGATION: User Identity](03-answer-ready/278-act-3-malware-investigation-user-identity.md) | 1 | No capture dependency for the documented result |
| 279 | [ACT 3 - MALWARE INVESTIGATION: C2 Destination](03-answer-ready/279-act-3-malware-investigation-c2-destination.md) | 1 | No capture dependency for the documented result |
| 280 | [ACT 3 - MALWARE INVESTIGATION: Malware Family](03-answer-ready/280-act-3-malware-investigation-malware-family.md) | 1 | No capture dependency for the documented result |
| 281 | [ACT 3 - MALWARE INVESTIGATION: Beacon Evidence](03-answer-ready/281-act-3-malware-investigation-beacon-evidence.md) | 1 | No capture dependency for the documented result |
| 282 | [ACT 4 - LUMMA IN THE ROOM: Lumma Victim](03-answer-ready/282-act-4-lumma-in-the-room-lumma-victim.md) | 1 | No capture dependency for the documented result |
| 283 | [ACT 4 - LUMMA IN THE ROOM: Victim MAC](03-answer-ready/283-act-4-lumma-in-the-room-victim-mac.md) | 1 | No capture dependency for the documented result |
| 284 | [ACT 4 - LUMMA IN THE ROOM: Victim Hostname](03-answer-ready/284-act-4-lumma-in-the-room-victim-hostname.md) | 1 | No capture dependency for the documented result |
| 285 | [ACT 4 - LUMMA IN THE ROOM: Compromised User](03-answer-ready/285-act-4-lumma-in-the-room-compromised-user.md) | 1 | No capture dependency for the documented result |
| 286 | [ACT 4 - LUMMA IN THE ROOM: Full User Name](03-answer-ready/286-act-4-lumma-in-the-room-full-user-name.md) | 1 | No capture dependency for the documented result |
| 287 | [ACT 4 - LUMMA IN THE ROOM: Malicious Domain](03-answer-ready/287-act-4-lumma-in-the-room-malicious-domain.md) | 1 | No capture dependency for the documented result |
| 288 | [ACT 4 - LUMMA IN THE ROOM: Fingerprint API](03-answer-ready/288-act-4-lumma-in-the-room-fingerprint-api.md) | 1 | No capture dependency for the documented result |
| 289 | [ACT 5 - FINAL INCIDENT: Map the Network](03-answer-ready/289-act-5-final-incident-map-the-network.md) | 1 | No capture dependency for the documented result |
| 290 | [ACT 5 - FINAL INCIDENT: Host One MAC](03-answer-ready/290-act-5-final-incident-host-one-mac.md) | 1 | No capture dependency for the documented result |
| 291 | [ACT 5 - FINAL INCIDENT: Host Two MAC](03-answer-ready/291-act-5-final-incident-host-two-mac.md) | 1 | No capture dependency for the documented result |
| 292 | [ACT 5 - FINAL INCIDENT: Host Three MAC](03-answer-ready/292-act-5-final-incident-host-three-mac.md) | 1 | No capture dependency for the documented result |
| 293 | [ACT 5 - FINAL INCIDENT: Find the Victims](03-answer-ready/293-act-5-final-incident-find-the-victims.md) | 1 | No capture dependency for the documented result |
| 294 | [ACT 5 - FINAL INCIDENT: First Ransomware](03-answer-ready/294-act-5-final-incident-first-ransomware.md) | 1 | No capture dependency for the documented result |
| 295 | [ACT 5 - FINAL INCIDENT: Second Ransomware](03-answer-ready/295-act-5-final-incident-second-ransomware.md) | 1 | No capture dependency for the documented result |
| 296 | [ACT 5 - FINAL INCIDENT: Final Assessment](03-answer-ready/296-act-5-final-incident-final-assessment.md) | 1 | No capture dependency for the documented result |
| 297 | [ACT 1 - EASY AS 123: Threat Identity](03-answer-ready/297-act-1-easy-as-123-threat-identity.md) | 1 | No capture dependency for the documented result |
| 298 | [ACT 1 - EASY AS 123: Domain Pivot](03-answer-ready/298-act-1-easy-as-123-domain-pivot.md) | 1 | No capture dependency for the documented result |
| 299 | [ACT 1 - EASY AS 123: Protocol Deception](03-answer-ready/299-act-1-easy-as-123-protocol-deception.md) | 1 | No capture dependency for the documented result |
| 300 | [ACT 1 - EASY AS 123: Malware Hash Pivot](03-answer-ready/300-act-1-easy-as-123-malware-hash-pivot.md) | 1 | No capture dependency for the documented result |
| 301 | [ACT 2 - YOU DIRTY RAT!: Identify the RAT](03-answer-ready/301-act-2-you-dirty-rat-identify-the-rat.md) | 1 | No capture dependency for the documented result |
| 302 | [ACT 2 - YOU DIRTY RAT!: Infrastructure Owner](03-answer-ready/302-act-2-you-dirty-rat-infrastructure-owner.md) | 1 | No capture dependency for the documented result |
| 303 | [ACT 2 - YOU DIRTY RAT!: C2 Service Port](03-answer-ready/303-act-2-you-dirty-rat-c2-service-port.md) | 1 | No capture dependency for the documented result |
| 304 | [ACT 3 - LUMMA IN THE ROOM-AH!: Identify the Stealer](03-answer-ready/304-act-3-lumma-in-the-room-ah-identify-the-stealer.md) | 1 | No capture dependency for the documented result |
| 305 | [ACT 3 - LUMMA IN THE ROOM-AH!: Domain Pivot](03-answer-ready/305-act-3-lumma-in-the-room-ah-domain-pivot.md) | 1 | No capture dependency for the documented result |
| 306 | [ACT 3 - LUMMA IN THE ROOM-AH!: Registration OSINT](03-answer-ready/306-act-3-lumma-in-the-room-ah-registration-osint.md) | 1 | No capture dependency for the documented result |
| 307 | [ACT 4 - FIRST TO LAST: Malware Attribution](03-answer-ready/307-act-4-first-to-last-malware-attribution.md) | 1 | No capture dependency for the documented result |
| 308 | [ACT 4 - FIRST TO LAST: Infrastructure Pivot](03-answer-ready/308-act-4-first-to-last-infrastructure-pivot.md) | 1 | No capture dependency for the documented result |
| 309 | [Info Leaks](03-answer-ready/309-info-leaks.md) | 1 | No capture dependency for the documented result |
| 310 | [Down the Rabbit Hole](03-answer-ready/310-down-the-rabbit-hole.md) | 1 | No capture dependency for the documented result |
| 311 | [SQL Skillz](01-pcgctf-solved/311-sql-skillz.md) | 1 | No capture dependency for the documented result |
| 312 | [Back to Basics](03-answer-ready/312-back-to-basics.md) | 1 | No capture dependency for the documented result |
| 313 | [Ghost of Squares Past](01-pcgctf-solved/313-ghost-of-squares-past.md) | 1 | No capture dependency for the documented result |
| 315 | [Bedside Manner](01-pcgctf-solved/315-bedside-manner.md) | 3 | No capture dependency for the documented result |
| 316 | [Factory Setting](01-pcgctf-solved/316-factory-setting.md) | 4 | No capture dependency for the documented result |
| 317 | [Second Opinion](01-pcgctf-solved/317-second-opinion.md) | 3 | No capture dependency for the documented result |
| 318 | [Live Boot](01-pcgctf-solved/318-live-boot.md) | 3 | No capture dependency for the documented result |
| 319 | [Car Crash](01-pcgctf-solved/319-car-crash.md) | 1 | truck image missing |
| 320 | [Hooked](01-pcgctf-solved/320-hooked.md) | 1 | No capture dependency for the documented result |
| 321 | [Art Heist: The Forgery](01-pcgctf-solved/321-art-heist-the-forgery.md) | 1 | original artifact missing |
| 322 | [Hard Kept Secrets](01-pcgctf-solved/322-hard-kept-secrets.md) | 1 | original artifact missing |
| 323 | [Inside Man](01-pcgctf-solved/323-inside-man.md) | 1 | original artifact missing |
| 325 | [Diagnosis](01-pcgctf-solved/325-diagnosis.md) | 1 | original artifact missing |
| 326 | [Admitted Under Another Name](01-pcgctf-solved/326-admitted-under-another-name.md) | 3 | No capture dependency for the documented result |
| 327 | [Schedule of Concern](01-pcgctf-solved/327-schedule-of-concern.md) | 3 | No capture dependency for the documented result |
| 328 | [The Attending](01-pcgctf-solved/328-the-attending.md) | 3 | No capture dependency for the documented result |
| 329 | [Prying Eyes](01-pcgctf-solved/329-prying-eyes.md) | 3 | No capture dependency for the documented result |
| 330 | [The Original Reading](01-pcgctf-solved/330-the-original-reading.md) | 3 | No capture dependency for the documented result |
| 331 | [Heavy Hand](01-pcgctf-solved/331-heavy-hand.md) | 3 | No capture dependency for the documented result |
| 332 | [Upon the Throne](01-pcgctf-solved/332-upon-the-throne.md) | 3 | No capture dependency for the documented result |
| 333 | [After the Lock](01-pcgctf-solved/333-after-the-lock.md) | 3 | No capture dependency for the documented result |
| 334 | [Ghost in the Registry](01-pcgctf-solved/334-ghost-in-the-registry.md) | 3 | No capture dependency for the documented result |
| 335 | [Too Good to be True](01-pcgctf-solved/335-too-good-to-be-true.md) | 4 | No capture dependency for the documented result |
| 336 | [Two Places at Once](01-pcgctf-solved/336-two-places-at-once.md) | 3 | No capture dependency for the documented result |
| 337 | [Cereal Killer 04](01-pcgctf-solved/337-cereal-killer-04.md) | 1 | original artifact missing |
| 338 | [Headshot](01-pcgctf-solved/338-headshot.md) | 1 | original artifact missing |
| 339 | [File Dump 01](01-pcgctf-solved/339-file-dump-01.md) | 1 | original artifact missing |
