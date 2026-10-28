#!/usr/bin/env python3
"""Re-render retained terminal transcripts as real Konsole screenshots.

Each capture is displayed with `cat` inside a real Konsole window on an
isolated Xvfb display, then the window is captured with ImageMagick import.
This changes presentation only: the command output is the byte-for-byte
transcript already stored in capture-work/*.terminal.log.
"""
import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "screenshots" / "capture-manifest.json"
DEFAULT_OUT = ROOT / "screenshots" / "konsole"
ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")


def wrapped_rows(text: str, cols: int) -> int:
    rows = 0
    for line in text.splitlines():
        line = ANSI.sub("", line).expandtabs(8)
        rows += max(1, math.ceil(len(line) / cols))
    return rows + 1


def pick_size(text: str):
    # Keep the physical width roughly constant across font sizes.
    for font, cols in ((13, 120), (12, 130), (11, 142)):
        rows = wrapped_rows(text, cols)
        if rows <= (60 if font == 13 else 80):
            return font, cols, min(84, max(10, rows))
    return 11, 142, 84


def wait_for_window(env, title: str, timeout: float = 8.0):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            tree = subprocess.check_output(
                ["xwininfo", "-root", "-tree"], env=env, text=True,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            tree = ""
        for line in tree.splitlines():
            if title in line and "— Konsole" in line:
                match = re.search(r"(0x[0-9a-f]+)", line)
                if match:
                    return match.group(1)
        time.sleep(0.15)
    return None


def render(log: Path, out: Path, display: str, xdg_runtime: str) -> dict:
    text = log.read_text(errors="replace")
    font, cols, rows = pick_size(text)
    title = f"pcgshot-{out.stem}-{os.getpid()}"
    fd, script_name = tempfile.mkstemp(prefix="pcgshot-", suffix=".sh")
    os.close(fd)
    script = Path(script_name)
    script.write_text(f"#!/bin/bash\ncat {shlex_quote(str(log))}\nsleep 24\n")
    script.chmod(0o700)

    env = os.environ.copy()
    env.update({
        "DISPLAY": display,
        "QT_QPA_PLATFORM": "xcb",
        "XDG_RUNTIME_DIR": xdg_runtime,
    })
    cmd = [
        "konsole", "--separate", "--hide-menubar", "--hide-tabbar",
        "-p", f"Font=JetBrains Mono,{font}",
        "-p", "ColorScheme=Breeze",
        "-p", f"TerminalColumns={cols}",
        "-p", f"TerminalRows={rows}",
        "-p", "ScrollBarPosition=0",
        "-p", "ShowTerminalSizeHint=false",
        "-p", "TerminalMargin=12",
        "-p", f"tabtitle={title}",
        "--hold", "-e", "bash", str(script),
    ]
    proc = subprocess.Popen(
        cmd, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    wid = None
    try:
        wid = wait_for_window(env, title)
        if not wid:
            raise RuntimeError("Konsole window did not appear")
        time.sleep(1.5)
        out.parent.mkdir(parents=True, exist_ok=True)
        for attempt in range(3):
            subprocess.run(
                ["import", "-window", wid, str(out)],
                env=env, check=True,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            if out.stat().st_size > 2000:
                break
            time.sleep(0.5)
        if out.stat().st_size <= 2000:
            raise RuntimeError("captured image is blank")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
        script.unlink(missing_ok=True)

    data = out.read_bytes()
    return {
        "source_log": str(log),
        "image": str(out),
        "font": font,
        "columns": cols,
        "rows": rows,
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
    }


def shlex_quote(value: str) -> str:
    return "'" + value.replace("'", "'\\''") + "'"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--display", default=":100")
    parser.add_argument("--xdg-runtime", default="/tmp/opencode/run")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--only", default="")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    captures = json.loads(MANIFEST.read_text())["captures"]
    todo = []
    for capture in captures:
        log = capture.get("log")
        image = capture.get("image")
        if not log or not image or not Path(log).exists():
            continue
        if args.only and args.only not in image:
            continue
        name = Path(image).name
        out = args.out / name
        if out.exists() and not args.force:
            continue
        todo.append((capture, Path(log), out))
    if args.limit:
        todo = todo[: args.limit]

    manifest = []
    for index, (capture, log, out) in enumerate(todo, 1):
        print(f"[{index}/{len(todo)}] {out.name}", flush=True)
        try:
            record = render(log, out, args.display, args.xdg_runtime)
        except Exception as error:
            print(f"FAILED {out.name}: {error}", flush=True)
            continue
        record["image_id"] = capture.get("image")
        record["challenge_id"] = capture.get("id")
        record["purpose"] = capture.get("purpose")
        record["method"] = "Konsole replay of retained PTY transcript"
        record["rendered_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        record["original_image_sha256"] = capture.get("sha256")
        manifest.append(record)

    if manifest:
        target = args.out / "render-manifest.json"
        existing = []
        if target.exists():
            try:
                existing = json.loads(target.read_text())
            except ValueError:
                existing = []
        merged = {item["image"]: item for item in existing}
        merged.update({item["image"]: item for item in manifest})
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(list(merged.values()), indent=2) + "\n")
        print(f"wrote {target}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
