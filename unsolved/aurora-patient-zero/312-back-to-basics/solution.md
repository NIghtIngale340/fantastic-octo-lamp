# Back to Basics — recovered answer

Flag candidate: `deadface{gw-westlake-int-03}`

The original challenge asks for the hidden diagnostics page's gateway name and explicitly specifies `deadface{gateway-name}`.

Independent REA/Ghidra static analysis of the original ARM64 app executable identifies `DiagnosticInfo.items` at `0x100009a68`. This initializer constructs seven diagnostic rows. Its second row pairs the Swift string **Sync Gateway** with **gw-westlake-int-03**. REA decoded those literals from the initializer's constant registers at `0x100009b78` and `0x100009b90`, respectively. This establishes the gateway's role, beyond merely finding an unrelated string.

The same initializer includes Clinic Route = westlake, and Last Gateway Check = 2026-05-30 09:42 UTC. The executable also contains DiagnosticScreen and Aurora Diagnostics.

Evidence: [REA dossier and extraction evidence](../../../analysis-team-verification/aurora-rea-evidence.json), especially function dossier `ev_0745d9ce2e4004ae34aeecbb779fa55c6063564dad5864cc49c3447d06f4df54`; [artifact hashes](../../../analysis-team-verification/aurora-identities.json). Executable SHA-256: `017cf57640359bd4b0c03da2e4a311d8a405595bd028cb5ba55934a2d6c19658`. Analysis provider: Ghidra 12.1.4.

Status: answer recovered by static analysis; the iOS app and diagnostics screen were not executed, no live gateway was contacted, and the flag has not been confirmed accepted by PCGCTF.
