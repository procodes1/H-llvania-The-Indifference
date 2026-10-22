# Höllvania implementation roadmap

## Phase 1 — KIM messaging interface (NOW)

**Goal:** actual late-1990s communications-window styling, not simply green recolored Discord.

### 1A. Design prototype — completed

- [x] Define cream IBM Model M material palette.
- [x] Document contrast criteria (normal text 4.5:1 or higher).
- [x] Build standalone HTML/CSS/JS preview with fictional contacts, messages, and radio view.
- [x] Preview in 1600 × 900 and narrow 680 × 940 headless Firefox.
- [x] Add automated offline syntax/contrast DOM smoke checks.
- [x] Clone repository locally to `~/Projects/Hollvania-The-Indifference` on CachyOS.
- [ ] Operator reviews appearance and proportions in normal browser.

### 1B. Vesktop adaptation — staged, NOT live

- [x] Put initial adaptation in `discord/staging/kim-v0.3.theme.css`.
- [ ] Inspect Vesktop's DOM on Friends/DM/server views to confirm modern selector mapping.
- [ ] Test styled title bar, directory sidebar, chat transcript and composer *individually*.
- [ ] Check user-profile side panel and settings popovers in both light/normal and active contexts.
- [ ] Check Discord voice/video, streaming, emoji, mentions, file upload, search and thread UI.
- [ ] Verify accessibility and contrast of text, icons, timestamps, status and focus.
- [ ] Introduce the tested version as a **separate**, toggleable theme; preserve active v0.1 and its backup.
- [ ] Collect screenshots, fix defects, then promote to `discord/kim.theme.css` only after approval.

### Acceptance criteria

- Discord remains usable, readable and recognizable enough to find settings, servers and contacts.
- No hidden controls, accidental pointer blockers, unreadable timestamps, or overwritten account state.
- Retro visual hierarchy: darker aged-plastic chrome, pale paper transcript, deep-teal title bars, dark ink.
- Easy rollback: simply disable the new local theme in Vesktop.
- Works on the main OLED and the secondary display.

## Phase 2 — Hyprland / desktop skin

**Goal:** extend the approved KIM look to all desktop chrome, without changing how apps behave.

The user's machine was previously audited as **CachyOS + Hyprland 0.56.2 + ML4W Lua/Quickshell**. KDE Plasma is installed and stays a fallback. Current `~/.config/hypr` and `~/.config/waybar` are symlinks into ML4W.

**Important:** Don't overwrite ML4W-owned files directly or blindly link upstream dotfiles into the existing symlink target.

- [ ] Establish a new Höllvania overlay directory and backup strategy for ML4W `custom.lua`, Quickshell components, and any bar/launcher files.
- [ ] Map shared palette tokens into Hyprland borders, shadows, and dimming without modifying monitor timing or GPU settings.
- [ ] Build matching launcher, notifications, lock screen and Waybar/Quickshell panel design.
- [ ] Match window chrome while preserving original geometry/scroll behavior.
- [ ] Build a minimal, themed SDDM design **only after** confirming SDDM is installed and selected; keep a recovery route via tty/Plasma.
- [ ] Commit profile switching logic with rollback and validation.

## Phase 3 — Fix the little irks

Only after KIM and the desktop's visual language are stable:

- [ ] Make the region-screenshot keybinding copy actual `image/png` to clipboard (with optional file save), and test paste into browser.
- [ ] Map familiar shortcuts such as Super+T for terminal and a deliberate Super+W action without colliding with ML4W defaults.
- [ ] Explain and remap scratchpad behavior (Super+S), and offer floating behavior where desired while preserving optional tiling.
- [ ] Review dual-monitor workspaces, active displays, VRR settings and fullscreen-game behavior **without changing them blindly**.
- [ ] Validate PipeWire, portals, screen sharing and Vesktop voice integration.
- [ ] Keep keyboard and mouse workflows comprehensible; document shortcuts.

## Phase 4 — Voidtouched

- [ ] Separate palette: dark indigo Void, worn Orokin ivory/gold, restrained cyan.
- [ ] Standalone visual prototype + review, just as for KIM.
- [ ] Same feature checks and rollback before activation.
- [ ] Optional Wally Easter eggs (quiet and nonintrusive) and local Ordis joke service (CPU-friendly, opt-in, silence during fullscreen gaming).

## Quality gates

1. **Prototype** in isolation.
2. **Screenshot + accessibility review.**
3. **Staged implementation** with lint and smoke checks.
4. **Limited live test** with a known-good backup.
5. **Promote** only after user approval.
6. **Keep Git history** and preserve KDE/Plasma login recovery.
