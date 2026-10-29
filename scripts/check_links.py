#!/usr/bin/env python3
"""Report relative markdown links in the archive that do not resolve.

Usage:  python scripts/check_links.py [-v] [--max N]

48 links were already broken when the archive was reorganised on
29 October 2026; --max 48 keeps that as the ceiling so a reorganisation
cannot quietly add more.
"""
import collections
import glob
import os
import re
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\]\(\s*<?([^)>\s]+)>?\s*(?:\"[^\"]*\")?\)")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "#", "data:")


def main():
    broken, total = [], 0
    for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        if rel.startswith(".git/"):
            continue
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for link in LINK.findall(text):
            if link.startswith(SKIP_SCHEMES):
                continue
            target = unquote(link.split("#")[0].split("?")[0])
            if not target:
                continue
            total += 1
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
                broken.append((rel, link))

    print(f"relative links checked: {total}")
    print(f"broken: {len(broken)}")
    if "-v" in sys.argv:
        for source, link in broken:
            print(f"  {source} -> {link}")
    else:
        for source, n in collections.Counter(s for s, _ in broken).most_common(15):
            print(f"  {source}: {n}")

    if "--max" in sys.argv:
        ceiling = int(sys.argv[sys.argv.index("--max") + 1])
        if len(broken) > ceiling:
            print(f"FAIL: {len(broken)} broken links exceeds the ceiling of {ceiling}")
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
