# KIM // VITRUVIAN — first dark-mode prototype

**Date:** 2026-10-22  
**Status:** Installed on CachyOS as an **optional, disabled** Vesktop theme. Offline mockup tests pass; actual live Discord layout/settings still need visual QA.  
**Do not replace the approved KIM Classic light theme.**

## Intent

Inspired by the user's supplied Warframe Vitruvian visual reference: midnight navy, deep charcoal, archival gold framing, ivory readable text, quiet Void-blue accents, line-diagram geometry, and reserved original geometric ornaments. This is **actual Vesktop CSS**, not an image mockup.

The reference art itself is **not included or redistributed**; no remote textures, game assets, fonts, downloaded icons, or scripts are used.

## Files

- Standalone full dark variant source: `discord/staging/kim-vitruvian-v0.1.theme.css`.
- Installed local file: `~/.config/vesktop/themes/kim-vitruvian.theme.css`.
- Side-by-side preview fixture: `discord/prototypes/kim-vitruvian-v0.1-regression.html`.
- Account/profile/settings fixture: `discord/prototypes/kim-vitruvian-v0.1-settings-regression.html`.
- Approved Classic source: `discord/releases/kim-v0.4b-known-good.theme.css`.
- Approved Classic backup: `~/.local/share/hollvania/backups/kim-v0.4b-approved-2026-10-22.css`.

The dark theme is self-contained and inherited KIM v0.4b's structurally-safe selectors; it is **not** intended to be enabled together with Classic.

## Palette

| Surface / token | Color |
|---|---|
| Night / shell background | `#0B1120` |
| Transcript | `#131A2A` |
| Chrome / sidebar | `#1C2434` |
| Raised input/card | `#263144` |
| Ink / primary text | `#EEE5D3` |
| Muted text | `#BDB59F` |
| Orokin gold | `#D8B96F` |
| Light gold header text | `#E3C986` |
| Gold linework | `#AC8950` |
| Void blue links | `#91B9E8` |
| Selected contact | `#304153` |

Color contrast is evaluated on dark surfaces; target is 4.5:1 for normal text. Text appearance must be checked in actual Discord before approval.

## Toggle in Vesktop

1. Settings → Vencord → Themes.
2. Turn **OFF** `kim-v0.3-preview.theme.css` (Classic).
3. Turn **ON** `kim-vitruvian.theme.css`.
4. Reload with `Ctrl+R` if needed.

To return to approved Classic, reverse the switches. Leave the older `kim.theme.css` disabled while using either new variant.

No edits to the Discord account, user data, KDE, Hyprland, or system packages are required.

## Tested in offline browser

- A KIM directory, transmission pane, dossier/profile and composer appeared with only their intended pseudo-headers (10/10 containment guards).
- Dark ivory text, gold window chrome and a restrained archival/geometry motif rendered properly.
- Fixed a CSS specificity issue where a header sigil would tile over the entire titlebar.
- Settings, profile and status-menu simulated content remained readable.

## Still to test in live Discord

- Friends, DMs, servers, voice and video/screen sharing, profile/activity cards, status picker, search, settings and scroll performance.
- Contrast and focus outlines on differently themed user profiles and warnings.
- Emoji, media attachments, streaming previews, and video buttons.
- Evaluate whether the orbit-line texture should be weaker, stronger or disabled.

Do not declare the Vitruvian variant user-approved until the actual screenshots and interactions are reviewed.

## Future integration

Once approved, offer one convenient Classic / Vitruvian switch. Keep it separate from the eventual modern Voidtouched Hyprland profile; sharing a palette doesn't require merging desktop configuration and Discord CSS.
