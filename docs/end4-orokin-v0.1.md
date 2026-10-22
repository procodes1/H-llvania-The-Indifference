# End-4 // Höllvania Vitruvian v0.1

**Status:** Installed on CachyOS / end-4 illogical-impulse, 2026-10-22. The end-4 Quickshell `ii` family has been restarted successfully after applying the palette.

This is a **non-destructive dark Orokin color layer**, not a fork of end-4. It leaves the user's functional dotfiles, workspace navigation, keybindings, Swedish keyboard, monitors, screenshots, KDE Plasma, Fastfetch and Vesktop themes in place.

## Design

Inspired by Orokin/Vitruvian interfaces and the separately developed **KIM // Vitruvian** Discord theme. All assets and values are original styling choices, not ripped game textures.

| Role | Color |
| --- | --- |
| Void night | `#0B1120` |
| Raised midnight panel | `#1C2638` |
| Primary archive gold | `#D8B96F` |
| Aged bronze outline | `#A88B58` |
| Warm ivory text | `#EEE5D3` |
| Void-blue secondary glow | `#91B9E8` |
| Raised blue-gray divider | `#33445B` |

A deliberately restrained palette: panels stay navy, **gold is for hierarchy**, Void blue is secondary, and legibility beats decorative effects.

## Implementation

- `profiles/end4-vitruvian/colors.json`: 53 validated Material/Quickshell colors. Installed into `~/.local/state/quickshell/user/generated/colors.json`, which `MaterialThemeLoader.qml` already reads.
- `scripts/end4-orokin.py`: validates every color key against end-4's `Appearance.qml`, atomically installs/removes the palette, and appends/removes a **marked** gold border override in `~/.config/hypr/custom/general.lua`. This avoids editing upstream QML or end-4 keybindings.
- The script sets only `appearance.wallpaperTheming.enableAppsAndShell=false` in `~/.config/illogical-impulse/config.json` to keep the hand-tuned theme from being replaced by wallpaper-derived colors. It stores just the previous boolean as a small restore marker; no old ML4W dotfiles backup is made.
- No wallpaper image is installed or replaced. Terminal and KDE colors are not changed.

The Matugen setup on this installation still resolves to a **leftover ML4W configuration**, so the regular wallpaper color-generation script should not be used as the first choice for this fixed theme. The custom palette deliberately bypasses that pipeline.

## Orokin Ivory Palace wallpaper v0.2 (current)

The user requested that the **wallpaper be visibly Orokin architecture**, while the **desktop chrome stays Vitruvian**. The first dark "Vitruvian Void" geometry wallpaper was retained as an alternative rather than overwritten.

- `wallpapers/orokin-ivory-palace-v0.2.svg` — editable original 4K vector concept: ivory marble, flowing gilded arches, ceremonial stairs, light-blue Void highlights, and a reflective floor. No baked-in bars, icons, clock, launcher or screenshots.
- `scripts/end4-orokin-wallpaper.py` — renders the 3840×2160 WebP and updates only `background.wallpaperPath` in end-4's config (no Matugen).
- Installed as `~/.local/share/hollvania/wallpapers/orokin-ivory-palace-v0.2.webp`. The earlier `vitruvian-void-v0.1.webp` remains on disk.
- Restore marker `~/.local/state/hollvania/end4-orokin-wallpaper-v0.2.json` records the **immediately prior wallpaper**, which was `vitruvian-void-v0.1.webp`.

To switch back to the earlier darker wallpaper:
```bash
cd ~/Projects/Hollvania-The-Indifference
python3 scripts/end4-orokin-wallpaper.py restore
qs -c ii kill; qs -c ii -d
```

You can reapply the white-gold wallpaper later with `python3 scripts/end4-orokin-wallpaper.py apply`. Quickshell was restarted successfully and the keyboard/monitor configuration was verified after applying v0.2.

## Wallpaper: Vitruvian Void v0.1

The first clean 4K dark Vitruvian-style wallpaper remains installed as a restore option; the current background is the brighter Orokin Ivory Palace v0.2 above.

- Source: `wallpapers/vitruvian-void-v0.1.svg` (editable original SVG vector art, 3840×2160; geometric portal, gilded filigree, Void lighting, temple arches, reflective floor).
- Rendered locally using `rsvg-convert` and ImageMagick to `~/.local/share/hollvania/wallpapers/vitruvian-void-v0.1.webp`.
- Changed **only** `background.wallpaperPath` in `~/.config/illogical-impulse/config.json`. No modifications to KDE wallpaper, Quickshell UI code, system-wide color schemes, Matugen, or shortcuts.
- Previous background path recorded in `~/.local/state/hollvania/end4-wallpaper-v0.1.json` for quick restoration; not a backup of ML4W or system configuration.
- No fake icons, clocks or UI graphics are baked into the actual wallpaper; widgets remain functional real end-4 components. The wallpaper is 16:9, suitable for both the 1440p OLED and 1080p AOC.

```bash
cd ~/Projects/Hollvania-The-Indifference
python3 scripts/end4-wallpaper.py status
python3 scripts/end4-wallpaper.py apply       # rerender/reapply
python3 scripts/end4-wallpaper.py restore     # previous purple background
qs -c ii kill; qs -c ii -d                     # only if the live view did not refresh
```

The installer stages its WebP in the destination directory before atomic replacement (because /tmp may be on another filesystem). The first successful rollout was checked with ImageMagick, Quickshell reload, and Hyprland 240Hz/144Hz monitor and Swedish-keyboard verifications.

## Controls

From the Höllvania repo directory:

```bash
python3 scripts/end4-orokin.py status
python3 scripts/end4-orokin.py apply
python3 scripts/end4-orokin.py restore
```

If the color file has been changed by another theme, `apply` refuses to overwrite it unless explicitly called with `--force`.

After changing or restoring a theme, restart **Quickshell only** to refresh all panels:

```bash
qs -c ii kill
qs -c ii -d
```

The first apply was verified with a clean `hyprctl reload`, no Hyprland configuration errors, and a successful new `qs -c ii` instance. The installed monitors remained DP-3 at 1920×1080@144Hz on the **left**, and DP-2 at 2560×1440@239.97Hz on the **right**; keyboard remained `se`.

### Future work

The clean geometric wallpaper is now in place. Next refinements: tune the cookie-clock style and optional Quickshell-specific gold separators or ornate glyphs while preserving all keybindings and widgets. Keep **KIM Classic v0.4b** frozen and preserve the separate **KIM // Vitruvian** theme.
