#!/usr/bin/env python3
"""Apply or undo the end-4 Höllvania Vitruvian polish: Fastfetch, Kitty, bar.

Supports the user's existing Fastfetch config (even if ~/.config/fastfetch is
an old ML4W symlink). Does NOT overwrite the original end-4 Quickshell QML,
keybinds, desktop widgets, wallpapers, or KDE configuration.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HOME = Path.home()
ROOT = Path(__file__).resolve().parent.parent
FASTFETCH = HOME / ".config/fastfetch/config.jsonc"
KITTY = HOME / ".config/kitty/custom.conf"
KITTY_SOURCE = ROOT / "profiles/end4-vitruvian/kitty-orokin.conf"
PALETTE = HOME / ".local/state/quickshell/user/generated/colors.json"
PALETTE_SOURCE = ROOT / "profiles/end4-vitruvian/colors.json"
MARKER = HOME / ".local/state/hollvania/end4-orokin-polish-v0.1.json"
BORDER = "#947A50"
GOLD = "#D8B96F"

def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", prefix=".orokin-",
        suffix=".tmp", dir=path.parent, delete=False
    ) as f:
        f.write(text)
        temp = Path(f.name)
    try:
        temp.chmod(0o644)
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)

def make_fastfetch(original: str) -> str:
    if '"source": "arch"' not in original:
        raise RuntimeError("Not the user's known Arch Fastfetch config; refusing to modify.")
    pattern = r'(?m)^(\s*"type": "builtin",[^\n]*\n)'
    if len(re.findall(pattern, original)) != 1:
        raise RuntimeError("Unexpected Fastfetch logo structure.")
    original = re.sub(
        pattern,
        lambda m: m.group(1) +
          '        "color": {"1": "#D8B96F", "2": "#E3C986", "3": "#91B9E8"},\n',
        original, count=1
    )
    pattern = r'("display":\s*\{\s*"separator":\s*" "\s*)\}'
    if len(re.findall(pattern, original)) != 1:
        raise RuntimeError("Unexpected Fastfetch display section.")
    original = re.sub(
        pattern,
        lambda m: m.group(1).rstrip() +
        ',\n        "color": {"keys": "#D8B96F", "title": "#E3C986", '
        '"output": "#EEE5D3", "separator": "#947A50"}\n    }',
        original, count=1
    )
    # {#34} used to pick up the old blue/pink ANSI slot.
    if "{#34}" not in original:
        raise RuntimeError("Expected old module-key escape {#34} was not found.")
    original = original.replace("{#34}", "{##D8B96F}")
    # Bronze ornamentation to connect the box drawing to Orokin filigree.
    def recolor_rule(m):
        return m.group(1) + "{##947A50}" + m.group(2) + "{#}" + m.group(3)
    original = re.sub(r'("key": ")([╭├╰][^"]+)(")', recolor_rule, original)
    return original

def verify_fastfetch(config: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".jsonc", encoding="utf-8") as f:
        f.write(config)
        f.flush()
        cmd = ["fastfetch", "--config", f.name, "--pipe", "--show-errors"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if r.returncode != 0 or "Error" in r.stderr:
            raise RuntimeError("Fastfetch validation failed:\n" + (r.stderr or r.stdout)[-1300:])
        if "Arch Linux x86_64" not in r.stdout or "arch" not in r.stdout:
            raise RuntimeError("Fastfetch preview lost the user's custom Arch identity.")

def formats():
    return (
        KITTY_SOURCE.read_text(encoding="utf-8"),
        json.dumps(json.loads(PALETTE_SOURCE.read_text()), indent=2) + "\n",
    )

def contents_for_state(original):
    ff = make_fastfetch(original["fastfetch"])
    kitty, palette = formats()
    verify_fastfetch(ff)
    return {"fastfetch": ff, "kitty": kitty, "palette": palette}

def apply():
    for f in (FASTFETCH, KITTY_SOURCE, PALETTE, PALETTE_SOURCE):
        if not f.is_file():
            raise RuntimeError("Expected config missing: " + str(f))
    if not MARKER.exists():
        original = {
            "fastfetch": FASTFETCH.read_text(),
            "kitty": KITTY.read_text() if KITTY.exists() else None,
            "palette": PALETTE.read_text(),
        }
        expected = contents_for_state(original)
        # Existing palette must be the Orokin palette, not a foreign theme.
        old_palette = json.loads(original["palette"])
        if old_palette.get("background") != "#0B1120" or old_palette.get("primary") != GOLD:
            raise RuntimeError("Current end-4 palette is not the expected Orokin palette.")
        marker = {"version": 1, "original": original}
    else:
        marker = json.loads(MARKER.read_text())
        original = marker["original"]
        expected = contents_for_state(original)
        # Do not clobber a user's edits that occurred after installing this pass.
        for name, path in (("fastfetch", FASTFETCH), ("kitty", KITTY)):
            current = path.read_text() if path.exists() else None
            if current not in (original[name], expected[name]):
                raise RuntimeError("User customized " + str(path) + " after polish; refusing to overwrite.")
        present = PALETTE.read_text()
        if json.loads(present).get("primary") != GOLD:
            raise RuntimeError("Orokin palette no longer active; refusing to overwrite.")
    if json.loads(expected["palette"]).get("outline_variant") != BORDER:
        raise RuntimeError("Source palette does not contain the expected gilded separator.")

    if not MARKER.exists():
        atomic_write(MARKER, json.dumps(marker, indent=2, ensure_ascii=False) + "\n")
    atomic_write(FASTFETCH, expected["fastfetch"])
    atomic_write(KITTY, expected["kitty"])
    atomic_write(PALETTE, expected["palette"])
    print("Fastfetch: gold/ivory Arch logo and labels")
    print("Kitty: navy glass, ivory text, gold tabs, Void-blue hyperlinks")
    print("Quickshell: antique-gold separators and outlines")
    print("No UI widgets, clock visibility, keybindings, wallpapers or KDE files changed.")

def restore():
    if not MARKER.exists():
        print("No previous Orokin polish state exists. Leaving files alone.")
        return
    marker = json.loads(MARKER.read_text())
    original = marker["original"]
    expected = contents_for_state(original)
    pairs = (("fastfetch", FASTFETCH), ("kitty", KITTY), ("palette", PALETTE))
    retained = False
    for name, path in pairs:
        current = path.read_text() if path.exists() else None
        if current != expected[name]:
            # Protect any tweaks made after the theme was applied.
            if current != original[name]:
                print("Skipped modified file:", path)
                retained = True
            continue
        if original[name] is None:
            path.unlink(missing_ok=True)
        else:
            atomic_write(path, original[name])
        print("Restored:", path)
    if retained:
        print("Restore marker retained; resolve customizations before a complete rollback.")
    else:
        MARKER.unlink()
    print("Reload Kitty/Quickshell if already running.")

def status():
    print("Theme source:", ROOT)
    print("Polish restore marker:", MARKER.is_file())
    if MARKER.is_file():
        expected = contents_for_state(json.loads(MARKER.read_text())["original"])
        for name, path in (("fastfetch", FASTFETCH), ("kitty", KITTY), ("palette", PALETTE)):
            print(name + " active:", path.is_file() and path.read_text() == expected[name])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("apply", "restore", "status"))
    args = parser.parse_args()
    {"apply": apply, "restore": restore, "status": status}[args.action]()
