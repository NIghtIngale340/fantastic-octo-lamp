#!/usr/bin/env python3
"""Derive a Juice Shop CTF-mode flag from the shared compose key."""
import hashlib
import hmac
import sys

import yaml

COMPOSE = "/home/nightingale/CTF/docker-compose.yml"

name = sys.argv[1]
with open(COMPOSE, encoding="utf-8") as handle:
    config = yaml.safe_load(handle)
key = config["services"]["juice-shop"]["environment"]["CTF_KEY"]
digest = hmac.new(key.encode(), name.encode(), hashlib.sha1).hexdigest()
print(f"pcgCTF{{{digest}}}")
