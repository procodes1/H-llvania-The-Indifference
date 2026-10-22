# End-4 // Höllvania Vitruvian v0.1

**Status:** Installed on CachyOS / end-4 illogical-impulse, 2026-10-22. The end-4 Quickshell `ii` family has been restarted successfully after applying the palette.

This is a **non-destructive dark Orokin color layer**, not a fork of end-4. It leaves the user's functional dotfiles, workspace navigation, keybindings, Swedish keyboard, monitors, screenshots, KDE Plasma and Vesktop themes in place. Later polish steps intentionally recolor Fastfetch and Kitty.

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
- The base palette installer does not replace wallpaper images. A separate optional polish script changes **Kitty and Fastfetch only**; KDE colors remain unchanged.

The Matugen setup on this installation still resolves to a **leftover ML4W configuration**, so the regular wallpaper color-generation script should not be used as the first choice for this fixed theme. The custom palette deliberately bypasses that pipeline.

## Original Orokin Ivory Palace wallpaper v0.2 (optional / historical)

The user requested that the **wallpaper be visibly Orokin architecture**, while the **desktop chrome stays Vitruvian**. After previewing the stylized SVG they chose a **high-quality realistic generated image** instead, which is now the active background. Both original SVG versions remain optional, reversible art assets.

- `wallpapers/orokin-ivory-palace-v0.2.svg` — editable original 4K vector concept: ivory marble, flowing gilded arches, ceremonial stairs, light-blue Void highlights, and a reflective floor. No baked-in bars, icons, clock, launcher or screenshots.
- `scripts/end4-orokin-wallpaper.py` — renders the 3840×2160 WebP and updates only `background.wallpaperPath` in end-4's config (no Matugen).
- Stored as `~/.local/share/hollvania/wallpapers/orokin-ivory-palace-v0.2.webp`, no longer the active background. The earlier `vitruvian-void-v0.1.webp` also remains on disk.
- Restore marker `~/.local/state/hollvania/end4-orokin-wallpaper-v0.2.json` records the **immediately prior wallpaper**, which was `vitruvian-void-v0.1.webp`.

To switch back to the earlier darker wallpaper:
```bash
cd ~/Projects/Hollvania-The-Indifference
python3 scripts/end4-orokin-wallpaper.py restore
qs -c ii kill; qs -c ii -d
```

You can reapply the white-gold wallpaper later with `python3 scripts/end4-orokin-wallpaper.py apply`. Quickshell was restarted successfully and the keyboard/monitor configuration was verified after applying v0.2.

## Wallpaper: Vitruvian Void v0.1

The first clean 4K dark Vitruvian-style wallpaper remains installed as an alternate wallpaper. The user currently has the more photorealistic Orokin palace PNG selected.

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

## Currently active wallpaper (user selected)

As of October 22, 2026, end-4's actual `background.wallpaperPath` is `~/Downloads/Celestial Golden Temple Hall.png`, a high-quality **photorealistic generated Orokin hall** selected by the user. This image intentionally remains outside Git and has **not been uploaded or redistributed** by this theme project. Do not overwrite it when applying the palette or polishing the UI.

## Fastfetch / Kitty / bar polish v0.1 (active)

The user noticed the Arch-logo Fastfetch was still pink, because its custom labels embedded `{#34}`, while Kitty continued to load pinkish colors from the earlier ML4W theme. The new reversible pass was applied directly on the running workstation:

- `scripts/end4-orokin-polish.py`: idempotent apply/status/restore, validates a temporary copy of Fastfetch before writing, captures only the affected small original config contents in `~/.local/state/hollvania/end4-orokin-polish-v0.1.json`, and refuses to overwrite manual post-install edits on restore.
- Fastfetch's existing `~/.config/fastfetch/config.jsonc` retains the user's custom layout and displayed `arch` identity, but its Arch ASCII logo/keys now use **true-color gold** `#D8B96F`, box outlines brass `#947A50`, and output ivory `#EEE5D3`. On this system, `~/.config/fastfetch` still points to the old ML4W dotfiles directory.
- `profiles/end4-vitruvian/kitty-orokin.conf`: installed as `~/.config/kitty/custom.conf`, loaded *last* by existing `kitty.conf`. Deep navy `#0B1120` at 87% opacity, blur 14, ivory text, Orokin gold cursor/tab borders, Void-blue hyperlinks and updated ANSI palette. No edits to Kitty's original base config or fonts. Kitty parsed the effective colors correctly.
- Material `outline_variant` moved from muted `#6B5A3D` to a slightly brighter antique gold `#947A50`, affecting **real end-4 Quickshell separators and outlines** without editing upstream QML, workspace logic or the bar implementation.
- Wallpaper and KDE remain untouched by this polish script; the optional cookie clock remains **disabled** as preferred by the user.

```bash
cd ~/Projects/Hollvania-The-Indifference
python3 scripts/end4-orokin-polish.py status
python3 scripts/end4-orokin-polish.py apply
python3 scripts/end4-orokin-polish.py restore  # Reverts just this polish pass
```

For a visual refresh after apply or restore:

```bash
pkill -SIGUSR1 -x kitty   # Reload existing Kitty windows
qs -c ii kill
qs -c ii -d               # Restart the end-4 panels, not the desktop session
```

Validated: Fastfetch emitted RGB `216;185;111` (gold) and `238;229;211` (ivory) in a pseudo-terminal; Kitty's config parser yielded opacity `0.87`, blur `14`, correct colors; Quickshell relaunched with no palette or Hyprland config errors; Swedish keyboard and both 144/239.97 Hz monitors unchanged.

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
