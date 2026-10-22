# KIM-inspired Discord redesign — visual contract

## Problem observed in v0.2

The 2026-10-22 screenshot of Vesktop showed unreadable low-contrast text, washed-out pale green surfaces, white icons on light backgrounds, and almost no structural resemblance to Warframe 1999's Kinemantik Instant Messenger (KIM). The first revision had mostly changed colors; the second set Discord to light color-scheme without covering every modern text/icon token.

**Do not redeploy v0.2 without fixing those issues.**

## References and intent

KIM in Warframe 1999 resembles late-1990s instant messaging software: small framed desktop windows, grey window chrome, restrained teal title bars, crisp labels, contact portraits, square beveled buttons, and clearly bounded conversation panes.

No game assets, artwork, screenshots, extracted textures or proprietary fonts should be committed to this public repository without rights to redistribute them.

## Design rules

1. **Legibility first:** body text and metadata should maintain clear contrast. Never pair pale text with pale surfaces. Test avatars, timestamps, icons, menus, reactions, and input placeholders.
2. **Split chrome from content:** a dark or patterned OS desktop background frames independent grey messenger windows. Do not recolor the entire application uniformly.
3. **Readable compact typography:** period-style UI fonts for chrome, readable chat text.
4. **KIM contact panel:** sidebar becomes a framed roster with tabs or categories, statuses, small portraits, and clear active selection.
5. **Conversation:** a title strip, framed transcript, plain input bar, bordered actions. Visually distinct sender names and timestamps.
6. **Discord functionality stays:** accessible servers, DMs, voice, search, emoji, uploads, buttons and popovers.
7. **Responsive:** do not collapse functionality at small widths or during voice calls.
8. **No broad fragile selectors:** prefer semantically scoped CSS in clearly named layers. Test the actual 2026 Vesktop DOM rather than guessing Discord-generated class names.
9. **No blind rollout:** prototype and screenshot each component separately, then apply a small reversible change.
10. **Keep original client working:** no Discord API recreation or credential handling.

## Implementation sequence

- [ ] Prototype a static KIM visual mockup in HTML/CSS using placeholder data and original styling.
- [ ] Review mockup against a KIM screenshot: proportions, palettes, window chrome, spacing and legibility.
- [ ] Inspect Vesktop's relevant DOM/classes locally and build a compatibility layer for CSS selectors.
- [ ] Implement title bar, contact list, conversation panel and voice view in separate CSS sections.
- [ ] Regression-test Friends, DM, server, voice call, Settings, modal dialogs, emoji and links.
- [ ] Maintain a single toggleable local theme, with backups and a rollback command.

## Release gates

- No disappearing chat content or unreadable timestamps.
- No inaccessible buttons or obscured menus.
- Theme may be disabled without losing messages, settings or account state.
- Keep KDE / ML4W and Hyprland configuration separate from Vesktop styling.
