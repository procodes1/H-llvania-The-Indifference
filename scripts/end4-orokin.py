#!/usr/bin/env python3
"""Reversible Höllvania Orokin palette for end-4's Quickshell and Hyprland."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "profiles/end4-vitruvian/colors.json"
HOME = Path.home()
PALETTE = HOME / ".local/state/quickshell/user/generated/colors.json"
HYPR = HOME / ".config/hypr/custom/general.lua"
PREFS = HOME / ".config/illogical-impulse/config.json"
STATE = HOME / ".local/state/hollvania/end4-orokin-state.json"
APPEARANCE = HOME / ".config/quickshell/ii/modules/common/Appearance.qml"

BEGIN = "-- BEGIN HÖLLVANIA OROKIN CHROME v0.1 (managed by end4-orokin.py)"
END = "-- END HÖLLVANIA OROKIN CHROME v0.1"
BLOCK = """-- BEGIN HÖLLVANIA OROKIN CHROME v0.1 (managed by end4-orokin.py)
-- Gold active borders and restrained bronze idle borders.
hl.config({
    general = {
        col = {
            active_border = "rgba(D8B96FFF)",
            inactive_border = "rgba(6B5A3D80)",
        },
    },
    misc = {
        background_color = "rgba(0B1120FF)",
    },
})
-- END HÖLLVANIA OROKIN CHROME v0.1
"""

def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix=".orokin-", suffix=".tmp", delete=False) as f:
        f.write(content)
        tmp = Path(f.name)
    try:
        tmp.chmod(0o644)
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)

def load_palette():
    colors = json.loads(SOURCE.read_text())
    assert colors["background"] == "#0B1120"
    assert colors["primary"] == "#D8B96F"
    assert colors["secondary"] == "#91B9E8"
    assert all(re.fullmatch(r"#[0-9a-fA-F]{6}", x) for x in colors.values())
    source = APPEARANCE.read_text()
    properties = set(re.findall(r"\bproperty color (m3\w+)\s*:", source))
    for key in colors:
        camel = re.sub(r"_([a-z])", lambda m: m[1].upper(), key)
        assert "m3" + camel in properties, "Unknown Quickshell token: " + key
    print("Validated", len(colors), "Material colors")
    return colors

def modified_hypr(original, on):
    if BEGIN in original or END in original:
        assert original.count(BEGIN) == original.count(END) == 1
        start = original.index(BEGIN)
        end = original.index(END, start) + len(END)
        original = original[:start].rstrip() + "\n\n" + original[end:].lstrip("\n")
    if on:
        return original.rstrip() + "\n\n" + BLOCK
    return original.rstrip() + "\n"

def validate_lua(content):
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".lua") as f:
        f.write(content)
        f.flush()
        subprocess.run(["luac", "-p", f.name], check=True)

def reload_hypr():
    if shutil.which("hyprctl"):
        result = subprocess.run(["hyprctl", "reload"], text=True, capture_output=True)
        print("Hyprland reload:", result.stdout.strip() or result.stderr.strip())
        if result.returncode:
            raise RuntimeError("Hyprland reload failed")
        errs = subprocess.run(["hyprctl", "configerrors"], text=True, capture_output=True)
        if errs.stdout.strip():
            print("Hyprland errors:", errs.stdout.strip())

def apply(force):
    colors = load_palette()
    desired = json.dumps(colors, indent=2) + "\n"
    if PALETTE.exists() and PALETTE.read_text() != desired and not force:
        sys.exit("A different generated theme exists; use --force if replacement is intended.")
    if not HYPR.is_file() or not PREFS.is_file():
        sys.exit("Expected end-4 config missing; nothing modified.")

    hypr_new = modified_hypr(HYPR.read_text(), True)
    validate_lua(hypr_new)
    prefs = json.loads(PREFS.read_text())
    old_auto = prefs["appearance"]["wallpaperTheming"]["enableAppsAndShell"]
    assert isinstance(old_auto, bool)
    prefs["appearance"]["wallpaperTheming"]["enableAppsAndShell"] = False

    # Store the previous single setting so restore can put it back.
    if not STATE.exists():
        atomic_write(STATE, json.dumps({"previous_auto_theming": old_auto}) + "\n")

    atomic_write(PALETTE, desired)
    atomic_write(HYPR, hypr_new)
    atomic_write(PREFS, json.dumps(prefs, indent=4, ensure_ascii=False) + "\n")
    reload_hypr()
    print("Installed: Quickshell palette + Hyprland chrome.")
    print("Wallpaper auto recoloring disabled; no KDE, terminal or keybinds touched.")

def restore():
    desired = json.dumps(load_palette(), indent=2) + "\n"
    if PALETTE.exists() and PALETTE.read_text() == desired:
        PALETTE.unlink()
        print("Removed Höllvania palette.")
    if HYPR.is_file():
        old = HYPR.read_text()
        new = modified_hypr(old, False)
        if old != new:
            validate_lua(new)
            atomic_write(HYPR, new)
            print("Removed Höllvania border override.")
    if PREFS.is_file() and STATE.is_file():
        prefs = json.loads(PREFS.read_text())
        prev = json.loads(STATE.read_text())["previous_auto_theming"]
        prefs["appearance"]["wallpaperTheming"]["enableAppsAndShell"] = bool(prev)
        atomic_write(PREFS, json.dumps(prefs, indent=4, ensure_ascii=False) + "\n")
        STATE.unlink()
        print("Restored original wallpaper-theming setting.")
    reload_hypr()

def status():
    target = json.dumps(load_palette(), indent=2) + "\n"
    print("Orokin palette active:", PALETTE.is_file() and PALETTE.read_text() == target)
    print("Gold border override present:", HYPR.is_file() and BEGIN in HYPR.read_text())
    print("Auto-theme restore marker:", STATE.exists())

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=["apply", "restore", "status"])
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if args.action == "apply":
        apply(args.force)
    elif args.action == "restore":
        restore()
    else:
        status()
    print("To reload Quickshell: qs -c ii kill; qs -c ii -d")
