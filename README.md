# Höllvania // The Indifference

A portable Hyprland / Vesktop desktop design project inspired by **Warframe 1999's KIM messenger** and the **Orokin Derelict touched by the Void**.

Fan-made project, not affiliated with Digital Extremes or Discord.

## The two profiles

- **Höllvania 1999:** Warm, aged IBM-beige plastic; retro teal window chrome; compact instant messaging; tactile beveled panels.
- **Voidtouched:** Dark Void blues, worn Orokin ivory/gold, and optional subtle Wally Easter eggs. This profile is planned, not yet implemented.

Both profiles will ultimately share the same functional Hyprland core, while swapping visual components.

## Current milestone: KIM v0.3

**The standalone interactive concept is ready to preview, but the new Discord stylesheet is NOT enabled on the user's machine.**

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
| `docs/kim-v0.3-design-brief.md` | Approved design direction, accessibility and color rules |
| `discord/prototypes/kim-v0.3.html` | Standalone preview, tested at desktop and narrow sizes |
| `discord/prototypes/kim-v0.3.tokens.css` | Reusable palette tokens |
| `scripts/test-kim-prototype.py` | Offline checks including color contrast and JS syntax |
| `discord/staging/kim-v0.3.theme.css` | **Unapproved** Vencord/Vesktop CSS adaptation, not loaded |
| `discord/kim.theme.css` | Previous experimental live theme source; NOT v0.3 |

**Never automatically replace or symlink `~/.config/vesktop/themes/kim.theme.css` with the staging theme.** First review the prototype visually, then test CSS in a separate removable theme with rollback.

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
