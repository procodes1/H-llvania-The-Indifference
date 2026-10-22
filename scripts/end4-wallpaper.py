#!/usr/bin/env python3
"""Install/remove Höllvania's clean Vitruvian Void wallpaper for end-4.

Does NOT run switchwall.sh, matugen, or replace the end-4 installation.
Only changes background.wallpaperPath and installs a user-local WebP.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

HOME = Path.home()
ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "wallpapers/vitruvian-void-v0.1.svg"
OUTPUT = HOME / ".local/share/hollvania/wallpapers/vitruvian-void-v0.1.webp"
CONFIG = HOME / ".config/illogical-impulse/config.json"
MARKER = HOME / ".local/state/hollvania/end4-wallpaper-v0.1.json"

def write_atomic(path: Path, payload: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", dir=path.parent, prefix=".wallpaper-", suffix=".tmp", 
        encoding="utf-8", delete=False
    ) as f:
        f.write(payload)
        tmp = Path(f.name)
    try:
        tmp.chmod(0o644)
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)

def current_settings():
    obj = json.loads(CONFIG.read_text(encoding="utf-8"))
    assert isinstance(obj["background"]["wallpaperPath"], str)
    return obj

def apply():
    assert ART.is_file(), f"SVG source missing: {ART}"
    assert CONFIG.is_file(), f"end-4 config missing: {CONFIG}"
    assert shutil.which("rsvg-convert"), "librsvg command rsvg-convert required"
    assert shutil.which("magick"), "ImageMagick required"
    obj = current_settings()
    oldpath = obj["background"]["wallpaperPath"]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    # Keep just the previous wallpaper path, not a backup of the dotfiles.
    if not MARKER.exists() and oldpath != str(OUTPUT):
        write_atomic(MARKER, json.dumps({"previous_wallpaper_path": oldpath}, indent=2) + "\n")

    with tempfile.TemporaryDirectory(prefix="orokin-wall-") as d:
        png = Path(d) / "render.png"
        webp = Path(d) / "render.webp"
        subprocess.run(["rsvg-convert","-w","3840","-h","2160",str(ART),"-o",str(png)], check=True)
        subprocess.run(["magick",str(png),"-strip","-quality","93",str(webp)], check=True)
        assert webp.exists() and webp.stat().st_size > 20000, "Wallpaper render failed"
        os.replace(webp, OUTPUT)

    obj["background"]["wallpaperPath"] = str(OUTPUT)
    write_atomic(CONFIG, json.dumps(obj, indent=4, ensure_ascii=False) + "\n")
    print(f"Installed wallpaper: {OUTPUT} ({OUTPUT.stat().st_size // 1024} KiB)")
    print("Changed only end-4 background.wallpaperPath; colors and shortcuts untouched.")
    print("Live wallpaper path will be picked up by Config, or restart with: qs -c ii kill; qs -c ii -d")

def restore():
    obj = current_settings()
    if not MARKER.exists():
        print("No prior wallpaper path recorded. Leaving settings untouched.")
        return
    oldpath = json.loads(MARKER.read_text())["previous_wallpaper_path"]
    if obj["background"]["wallpaperPath"] == str(OUTPUT):
        obj["background"]["wallpaperPath"] = oldpath
        write_atomic(CONFIG, json.dumps(obj, indent=4, ensure_ascii=False) + "\n")
        print("Restored wallpaper path:", oldpath)
    else:
        print("User has since chosen another wallpaper; leaving that choice untouched.")
    MARKER.unlink()
    print("No end-4 shell or Hyprland components were modified.")

def status():
    obj = current_settings()
    print("Wallpaper file:", OUTPUT)
    print("Wallpaper file exists:", OUTPUT.is_file())
    print("Active:", obj["background"]["wallpaperPath"] == str(OUTPUT))
    print("Previous wallpaper recorded:", MARKER.exists())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["apply","restore","status"])
    args = parser.parse_args()
    {"apply":apply, "restore":restore, "status":status}[args.action]()
