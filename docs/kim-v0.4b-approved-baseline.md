# KIM v0.4b — Approved visual baseline

**Approved:** 2026-10-22  
**Scope:** Vesktop custom CSS, Project Höllvania / The Indifference  
**Status:** User-approved appearance, not a claim of full functional regression coverage

## The version to keep

- **Frozen GitHub stylesheet:** `discord/releases/kim-v0.4b-known-good.theme.css`
- **Working-source stylesheet:** `discord/staging/kim-v0.4b.theme.css`
- **Active Vesktop theme:** `~/.config/vesktop/themes/kim-v0.3-preview.theme.css`
- **Local immutable-by-convention backup:** `~/.local/share/hollvania/backups/kim-v0.4b-approved-2026-10-22.css`
- **SHA-256 of frozen/current CSS:** `ddd609892554da158b7d657faddd4e2a5fe66e85bf58f55ff58f6837910da66a`

The current appearance was approved after the v0.4b repair removed duplicate pseudo-titlebars and restored access to the server rail. **Do not edit or overwrite the approved local backup or frozen GitHub copy during further design work.** Branch or copy to a separately named development stylesheet.

## Preserve these design decisions

- Old cream IBM keyboard plastic, smoke-beige navigation, deep teal small title bars, dark and readable ink.
- Small square avatars/server icons, modest bevels and simple borders, no modern frosted-glass effects.
- Separate KIM Address Book and Profile pane headers; never inject titlebars in the server rail, nested chat content, messages, emoji tray, or toolbar controls.
- The composer is labelled **OUTGOING TRANSMISSION**; avoid overly heavy panel chrome that crowds the message field.
- Scrolling, message attachments, server navigation, chats, profile access, and keyboard interactions take priority over decorative gimmicks.

## Ideas for a future optional *v0.5* experiment

1. **4-bit / 8-bit-style avatar treatment**, opt-in. Genuine indexed-color pixelation cannot be reproduced accurately with ordinary CSS filters. Prototype offline first using **fictional or permissioned images**; avoid modifying/caching other people's profile pictures, animated avatars and game screenshots. CSS-only alternatives: selectively use pixelated image rendering when scaling, gentle desaturation and posterized-like contrast, and crisp bordered tiles. Add a toggle.
2. **Subtle off-white/cream texture** on **non-text-bearing pane backgrounds**, using very low-contrast repeating noise/dots, faint paper grain, or an original tiny inline SVG. No textures behind messages, input text, menus, or settings labels. Test on an OLED for visual noise and accessibility.
3. **KIM Transmission top bar** and **Signal Monitor** are separate future structural changes, not prerequisites for this approved v0.4b version.

### Testing gate for future changes

Make a new version file, test in a static offline fixture, then optionally use a separate Vesktop theme toggle. Confirm no blockers in Settings, Friends, DMs, channels, popouts, voice, upload, chat input, and the contact list. If any element is harder to read, fall back to v0.4b.

## Next milestone: desktop aesthetics

With Vesktop visually accepted, shift focus to **matching Hyprland's** launcher, bar, window decoration, notifications, terminal theme, lock screen and later SDDM. Work as overlays on ML4W/Hyprland configuration with a proven rollback. Leave KDE unchanged. Only then clean up old keybindings, screenshot/clipboard bugs, tiling surprises and other usability irks.

## Recovery commands

To restore the approved Vesktop CSS while staying on the same enabled preview filename:

```bash
cp ~/.local/share/hollvania/backups/kim-v0.4b-approved-2026-10-22.css \
  ~/.config/vesktop/themes/kim-v0.3-preview.theme.css
```

Then reload Vesktop with `Ctrl+R`. The CSS file doesn't handle any passwords, tokens, or account data.

**Do not enable both** `kim-v0.3-preview.theme.css` and `kim.theme.css` at the same time; competing themes will override one another.

This is a fan-made visual interface concept with no bundled game artwork or proprietary fonts.
