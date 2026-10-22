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

A true Orokin/Vitruvian wallpaper, subtle original sigils, and optional Quickshell-specific ornamentation can be added later without rewriting the UI. Keep **KIM Classic v0.4b** frozen and preserve the separate **KIM // Vitruvian** theme.
