#!/usr/bin/env python3
"""Offline smoke checks for the standalone KIM v0.3 design mockup.

No network calls. No Vesktop config modifications. Stdlib + Node.js only.
Run: python3 scripts/test-kim-prototype.py
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "discord" / "prototypes" / "kim-v0.3.html"
DOC = ROOT / "docs" / "kim-v0.3-design-brief.md"

class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.buttons = 0
        self.scripts = []
        self.in_script = False
    def handle_starttag(self, tag, attrs):
        vals = dict(attrs)
        if "id" in vals:
            assert vals["id"] not in self.ids, f"Duplicate HTML ID: {vals['id']}"
            self.ids.add(vals["id"])
        if tag == "button":
            self.buttons += 1
        if tag == "script":
            self.in_script = True
    def handle_endtag(self, tag):
        if tag == "script":
            self.in_script = False
    def handle_data(self, data):
        if self.in_script:
            self.scripts.append(data)

def linear(x):
    return x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4

def luminance(hex_color):
    n = [int(hex_color[i:i+2], 16) / 255 for i in (1,3,5)]
    return sum(w * linear(v) for w, v in zip((.2126,.7152,.0722), n))

def ratio(a,b):
    hi,lo = sorted((luminance(a),luminance(b)),reverse=True)
    return (hi+.05)/(lo+.05)

def main():
    markup = HTML.read_text(encoding="utf-8")
    assert DOC.is_file(), "Design spec not present"
    p = Checker()
    p.feed(markup)
    required = {
        "roster", "roster-search", "roster-caption", "chat-name", "chat-body",
        "messages", "composer", "message-text", "profile-window",
        "profile-toggle", "close-profile", "call-button", "ordis",
        "ordis-message", "reset-demo"
    }
    missing = required - p.ids
    assert not missing, f"Missing prototype control(s): {sorted(missing)}"
    assert p.buttons >= 10, "Prototype lacks expected interface controls"
    assert "LOCAL MOCKUP" in markup and "NOT CONNECTED TO DISCORD" in markup
    assert "fetch(" not in markup and "XMLHttpRequest" not in markup
    assert "localStorage" not in markup and "document.cookie" not in markup
    assert 'http://' not in markup and 'https://' not in markup, "The mockup must work offline"
    assert len(p.scripts) == 1, "Unexpected inline script count"

    if shutil.which("node"):
        with tempfile.TemporaryDirectory(prefix="kim-test-") as folder:
            js = Path(folder) / "prototype.js"
            js.write_text(p.scripts[0], encoding="utf-8")
            result = subprocess.run(["node", "--check", str(js)], text=True, capture_output=True)
            assert result.returncode == 0, result.stderr
        print("PASS: prototype JavaScript syntax")
    else:
        print("WARN: node missing; skipped JavaScript syntax check")

    palette = dict(re.findall(r"--([a-z]+):\s*(#[a-fA-F0-9]{6})\s*;", markup))
    for name in ("ink","paper","plastic","beige","deep","highlight","muted"):
        assert name in palette, f"Missing CSS palette token: {name}"
    tested = {
        "body on cream": (palette["ink"], palette["paper"]),
        "body on plastic": (palette["ink"], palette["plastic"]),
        "body on beige": (palette["ink"], palette["beige"]),
        "muted on cream": (palette["muted"], palette["paper"]),
        "title on deep teal": (palette["highlight"], palette["deep"]),
    }
    for label, pair in tested.items():
        result = ratio(*pair)
        assert result >= 4.5, f"{label}: insufficient contrast ({result:.2f}:1)"
        print(f"PASS: {label} ({result:.2f}:1)")
    print(f"PASS: {len(p.ids)} unique DOM IDs; {p.buttons} buttons; demo data only")
    print("PASS: offline reference mockup; no account integrations")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, OSError, ValueError) as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
