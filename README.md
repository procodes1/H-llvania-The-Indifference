# Höllvania // The Indifference

A portable Hyprland / Vesktop desktop design project inspired by **Warframe 1999's KIM messenger** and the **Orokin Derelict touched by the Void**.

Fan-made project, not affiliated with Digital Extremes or Discord.

## The two profiles

- **Höllvania 1999:** Warm, aged IBM-beige plastic; retro teal window chrome; compact instant messaging; tactile beveled panels.
- **Voidtouched:** Midnight navy, Orokin archive gold, warm ivory and restrained Void-blue details. **End-4 Vitruvian v0.1** is now implemented for Quickshell and Hyprland.

The current desktop foundation is **end-4's illogical-impulse dotfiles** on Hyprland 0.56.2. This project overlays colors and styling rather than replacing its established bindings, workspaces, or Quickshell features.

## Current milestone: End-4 Orokin desktop v0.1 + KIM Vitruvian v0.2

**KIM Classic v0.4b remains the approved fallback.** Vitruvian v0.1 was tested in live Vesktop; the new **Vitruvian v0.2** is now enabled as an experimental refinement, awaiting a fresh screenshot. It uses a unified navy sidebar, gilded trim, a compact native chat heading, and subtle profile ornamentation. The user's reference art is used for color/style direction only, not redistributed.

**Desktop:** [End-4 Orokin v0.1 deployment and rollback](docs/end4-orokin-v0.1.md). The 53-token Vitruvian Material palette and **4K white-gold Orokin Ivory Palace wallpaper v0.2** are installed in end-4 Quickshell, with gilded window borders. The earlier darker Vitruvian Void wallpaper is preserved for rollback. User hardware preferences are preserved (Swedish keyboard, AOC left 144Hz, Lenovo OLED right 239.97Hz). Original Discord palette notes: [KIM // Vitruvian v0.1](docs/kim-vitruvian-v0.1.md). The older [ML4W scratchpad/Warframe troubleshooting guide](docs/hyprland-warframe-workspaces.md) is retained as historical context, **not** as the current end-4 configuration.

## KIM Classic archive

**KIM v0.4b is the user-approved Classic baseline, preserved as a separate disabled Vesktop theme and local backup.** The older experimental v0.4 block inserted runaway titlebars into guild navigation, nested chat content, and toolbar buttons. v0.4b replaces that block entirely with selectors targeting only three actual pane roots and the composer; the original v0.3f CSS is preserved separately.

The standalone KIM v0.3 HTML concept remains the approved visual reference. The live CSS implementation is a work in progress, not yet equivalent to the HTML prototype.

Open `discord/prototypes/kim-v0.3.html` in a browser. It runs completely offline and uses **fictional demo messages**; it does not connect to Discord or read personal messages.

To preview from a local clone on Linux:

```bash
xdg-open discord/prototypes/kim-v0.3.html
```

To run smoke checks (Python 3 and optionally Node.js):

```bash
python3 scripts/test-kim-prototype.py
```

The prototype includes People / Groups / Radio directory tabs, contact switching, a dummy message composer, a profile panel, and a hidden Ordis joke. All demo actions stay in the local page until refresh.

### Theme development status

| Component | Status |
|---|---|
| `wallpapers/vitruvian-void-v0.1.svg` | Previous dark Vitruvian geometry wallpaper; retained for rollback |
| `wallpapers/orokin-ivory-palace-v0.2.svg` | **Current 4K Orokin architecture wallpaper** with gilded arches, ivory marble and ceremonial stairs |
| `scripts/end4-orokin-wallpaper.py` | Installs/restores the active Orokin palace wallpaper without Matugen |
| `scripts/end4-wallpaper.py` | Render, install, and restore end-4's wallpaper without triggering Matugen |
| `profiles/end4-vitruvian/colors.json` | **Active end-4 Orokin Material palette** (midnight/navy, ivory, gold, Void-blue) |
| `scripts/end4-orokin.py` | Reversible theme installation, palette validation and gold Hyprland chrome |
| `docs/end4-orokin-v0.1.md` | Installed scope, color tokens, reapply and restore commands |
| `docs/kim-v0.3-design-brief.md` | Approved design direction, accessibility and color rules |
| `discord/prototypes/kim-v0.3.html` | Standalone preview, tested at desktop and narrow sizes |
| `discord/prototypes/kim-v0.3.tokens.css` | Reusable palette tokens |
| `scripts/test-kim-prototype.py` | Offline checks including color contrast and JS syntax |
| `discord/staging/kim-vitruvian-v0.1.theme.css` | Retained standalone v0.1 dark baseline and local rollback copy |
| `discord/staging/kim-vitruvian-v0.2.theme.css` | **Current active** v0.2 dark source copied to `~/.config/vesktop/themes/kim-vitruvian.theme.css` |
| `discord/prototypes/kim-vitruvian-v0.2-regression.html` | Offline pane/toolbar layout fixture for v0.2 |
| `discord/prototypes/kim-vitruvian-v0.2-settings-regression.html` | Offline profile/settings text fixture for v0.2 |
| `profiles/hyprland/warframe-workspace.lua` | ML4W custom.lua override routing Warframe to DP-2 / normal workspace 5 |
| `docs/hyprland-warframe-workspaces.md` | Hyprland 0.56 Lua workspace commands, scratchpad gotcha and rollback |
| `discord/prototypes/kim-vitruvian-v0.1-regression.html` | Offline dark palette/containment visual test |
| `discord/prototypes/kim-vitruvian-v0.1-settings-regression.html` | Offline profile, menu and settings visual test |
| `docs/kim-vitruvian-v0.1.md` | How to toggle and test the dark Vitruvian variant |
| `discord/releases/kim-v0.4b-known-good.theme.css` | **Frozen, user-approved CSS**: restore point for later theme experiments |
| `docs/kim-v0.4b-approved-baseline.md` | Visual acceptance, rollback instructions and future 4-bit/8-bit avatar / cream-paper texture ideas |
| `discord/staging/kim-v0.4b.theme.css` | **Currently deployed** in `~/.config/vesktop/themes/kim-v0.3-preview.theme.css`; full functional test coverage still pending |
| `discord/staging/kim-v0.3.theme.css` | Last clean v0.3f base and fallback source |
| `discord/prototypes/kim-v0.4b-shell-regression.html` | Offline visual fixture: verifies labels only on intended panes, not servers/toolbar |
| `discord/kim.theme.css` | Older experimental source; not the active preview |

**Approved version backup:** `~/.local/share/hollvania/backups/kim-v0.4b-approved-2026-10-22.css`. **Earlier rollback:** the previous user-edited v0.4 stylesheet is at `~/.local/share/hollvania/backups/kim-v0.4-manual.pre-v0.4b.css`. The currently enabled file is `~/.config/vesktop/themes/kim-v0.3-preview.theme.css`. To revert the v0.4b patch, copy the backup onto that preview file and reload Vesktop; to return to the earlier green theme, disable the preview and enable `kim.theme.css` instead.

**Never replace or symlink the older `kim.theme.css` as part of experimental theme updates.** Keep work reversible and test account settings, popouts, DMs, servers, and calls before declaring a release.

## Future milestones

1. **KIM:** approve visual prototype, carefully adapt Vesktop styling by component, validate legibility and Discord functionality.
2. **Desktop 1999:** match Hyprland window decoration, ML4W/Quickshell, launcher, notifications and eventually SDDM to the same palette; KDE remains untouched.
3. **Polish and irks:** remap shortcuts, fix screenshot/clipboard flow, review scratchpad/tiling expectations, test voice sharing and multi-monitor ergonomics.
4. **Voidtouched:** build a separate visual profile using shared core, with optional Wally and Ordis details.

Full plan: `docs/implementation-roadmap.md`.

## Safety and licensing

- Preserve KDE as fallback; no display manager or system package changes via these theme files.
- No credentials, personal messages, game saves, private logs, or machine-specific secrets belong in public Git.
- Use original or appropriately licensed fonts and artwork; **no redistributed game textures or screenshots**.
- No unofficial client tokens or Discord automation required for this visual-only fan project.
