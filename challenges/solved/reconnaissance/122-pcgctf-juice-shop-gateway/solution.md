# PCGCTF Juice Shop Gateway — derived answer

Flag candidate: `pcgCTF{73dbb9f2bac263e70119eb5e22d79e029e03a27e}`

The supplied compose file configures the common CTF_KEY, and the challenge asks for the flag associated with finding the hidden Score Board (`http://localhost:3000/#/score-board`).

Independent checks against the official OWASP Juice Shop source establish three steps:

1. [`challenges.yml`](https://github.com/juice-shop/juice-shop/blob/master/data/static/challenges.yml) names this challenge `Score Board` with key `scoreBoardChallenge`.
2. [`challengeUtils.ts`](https://github.com/juice-shop/juice-shop/blob/master/lib/challengeUtils.ts) generates the solved notification flag from `utils.ctfFlag(challenge.name)`.
3. [`utils.ts`](https://github.com/juice-shop/juice-shop/blob/master/lib/utils.ts) obtains CTF_KEY as a string and calculates a hexadecimal HMAC-SHA1 digest of the challenge name. The key must be the literal ASCII string, not hex-decoded bytes.

Recomputing that function with our original compose key and the exact name `Score Board` produces `73dbb9f2bac263e70119eb5e22d79e029e03a27e`, matching the teammate's value.

Evidence: [derivation inputs and source URLs](evidence/flag-derivation.json), [original compose file](files/docker-compose.yml). Official source checked 2026-10-28.

Status: deterministic source-backed answer derived locally. This verification did not run the configured Docker image or observe a solve notification; local HTTP access was unavailable in this environment. The compose image has no fixed version, so an image with changed flag-generation behavior could differ. PCGCTF acceptance remains unconfirmed.
