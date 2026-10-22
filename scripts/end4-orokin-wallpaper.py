#!/usr/bin/env python3
"""Install the clean Orokin Ivory Palace wallpaper for end-4 Quickshell.

No Matugen, KDE changes, wallpaper downloads or UI screenshots.
Keeps the previous Vitruvian image as the rollback option.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

HOME = Path.home()
ROOT = Path(__file__).resolve().parent.parent
SVG = ROOT / "wallpapers/orokin-ivory-palace-v0.2.svg"
OUTPUT = HOME / ".local/share/hollvania/wallpapers/orokin-ivory-palace-v0.2.webp"
CONFIG = HOME / ".config/illogical-impulse/config.json"
RESTORE = HOME / ".local/state/hollvania/end4-orokin-wallpaper-v0.2.json"

def atomically_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf8", dir=path.parent, prefix=".orokin-",
        delete=False
    ) as f:
        f.write(data)
        temp = Path(f.name)
    try:
        temp.chmod(0o644)
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)

def getconfig():
    return json.loads(CONFIG.read_text(encoding="utf8"))

def setconfig(config):
    atomically_write(CONFIG, json.dumps(config, indent=4, ensure_ascii=False) + "\n")

def apply():
    if not SVG.is_file():
        raise SystemExit("Orokin SVG source not found.")
    for binary in ("rsvg-convert", "magick"):
        if not shutil.which(binary):
            raise SystemExit("Missing dependency: " + binary)
    cfg = getconfig()
    current = cfg["background"]["wallpaperPath"]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    if not RESTORE.exists() and current != str(OUTPUT):
        atomically_write(RESTORE, json.dumps({"previous_wallpaper_path": current}, indent=2) + "\n")

    with tempfile.TemporaryDirectory(prefix="hollvania-orokin-") as td:
        td = Path(td)
        png = td / "art.png"
        webp = td / "wallpaper.webp"
        subprocess.run(["rsvg-convert", "-w", "3840", "-h", "2160", str(SVG), "-o", str(png)], check=True)
        subprocess.run(["magick", str(png), "-strip", "-quality", "93", str(webp)], check=True)
        if webp.stat().st_size < 20000:
            raise RuntimeError("Rendered wallpaper is unexpectedly small.")
        # Atomic install across /tmp and /home: stage to same filesystem.
        with tempfile.NamedTemporaryFile(dir=OUTPUT.parent, prefix=".palace-", suffix=".webp", delete=False) as fp:
            staged = Path(fp.name)
        try:
            shutil.copyfile(webp, staged)
            os.replace(staged, OUTPUT)
        finally:
            staged.unlink(missing_ok=True)

    cfg["background"]["wallpaperPath"] = str(OUTPUT)
    setconfig(cfg)
    print("Installed:", OUTPUT)
    print("Previous wallpaper:", current)
    print("Theme palette, KDE and Hyprland untouched.")

def restore():
    if not RESTORE.exists():
        print("No previous wallpaper recorded.")
        return
    cfg = getconfig()
    last = json.loads(RESTORE.read_text())["previous_wallpaper_path"]
    if cfg["background"]["wallpaperPath"] == str(OUTPUT):
        cfg["background"]["wallpaperPath"] = last
        setconfig(cfg)
        print("Restored:", last)
    else:
        print("User changed the wallpaper subsequently; current choice preserved.")
    RESTORE.unlink()

def status():
    cfg = getconfig()
    print("Orokin Palace active:", cfg["background"]["wallpaperPath"] == str(OUTPUT))
    print("Orokin Palace image exists:", OUTPUT.is_file())
    print("Previous wallpaper recorded:", RESTORE.exists())

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=("apply", "restore", "status"))
    a = ap.parse_args()
    {"apply": apply, "restore": restore, "status": status}[a.action]()
