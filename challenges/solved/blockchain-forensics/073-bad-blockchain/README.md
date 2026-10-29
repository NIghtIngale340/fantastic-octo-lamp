# BAD BLOCKCHAIN

Status: Unsolved  
Category: Blockchain / Forensics  
Points: 150  
Challenge ID: 73  
Source: https://cgcybercom.online/challenges#73

## Description

A newly discovered botnet has been using the Bitcoin blockchain as a backup communication channel.

Instead of placing its command-and-control information in the familiar OP_RETURN field, the malware authors used another part of the Bitcoin transaction data to conceal an IP address.
Investigators recovered the Bitcoin address and two associated transactions, but the actual C2 address is still hidden somewhere in the blockchain data.
Your task is to uncover the hidden IP address.
Note: The answer is an IP address.

🎯 Mission
Analyze the Bitcoin transactions associated with the provided address and identify the hidden IP address being used as the botnet's backup command-and-control server.

📁 Evidence
Bitcoin Address
1CTFzzCwntEm3a6CBGBfgxZdiArwY1HBSD

Bitcoin Transactions
4a616f943720325cc87611bf4a3bbcf2b5071baf5aab9a0ffbb9297371377c41
27bf9358822ef3ae44391950379e9206319e3bb3866d44bd9595a0e7cbdc2ca8

Blockchain API
https://api.blockcypher.com/v1/btc/main/addrs/1CTFzzCwntEm3a6CBGBfgxZdiArwY1HBSD?limit=2&before=696257

The address contains two confirmed transactions corresponding to block heights 696255 and 696256.

## Files

No directly attached files. See description for shared evidence, target websites, and other references.
