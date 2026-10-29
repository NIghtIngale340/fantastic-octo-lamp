#!/usr/bin/env python3
import json
import sys

data = json.load(sys.stdin)["data"]
print("{} | {} pts | solved_by_me={}".format(
    data["name"], data["value"], data["solved_by_me"]
))
