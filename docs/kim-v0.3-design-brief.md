# KIM v0.3 — Aged IBM / Höllvania 1999

**Status:** Design specification only; **not installed** in Vesktop.
**Reference:** Warframe 1999's Kinemantik Instant Messenger (KIM), filtered through the appearance of an aged beige IBM Model M keyboard and late-1990s desktop messaging software.

> **North star:** "A 1999 messaging client running on an old cream-colored office workstation." A little weathered, carefully maintained, and immediately readable. NOT bright green Discord, and NOT pastel-tinted Discord.

## 1. Visual principles

1. **Aged cream, not mint.** Primary panels use warm bone, cream and beige; don't tint every surface green.
2. **Legible ink.** Dark graphite/brown text on cream. Never render white or low-opacity text on pale surfaces. No text-opacity hacks to imitate aging.
3. **Material hierarchy.** Outer desktop/chrome is darker; inset chat transcript is lighter; selected/contact items are distinct.
4. **One strong teal accent.** Deep teal title bars evoke KIM. Teal is an accent, never the dominant fill across the whole screen.
5. **Period hardware details.** Subtle 1 px bevels, square edges, thin inset fields, tight control spacing, slightly faded plastic trim. No gradients that resemble modern glassmorphism.
6. **Functionality first.** No obscured text, icon-only buttons with invisible hover states, broken mentions, reactions, file uploads or voice controls.
7. **Era-appropriate, not unusable.** Borrow early desktop software's language while retaining readable sizes, accessible focus outlines and contemporary Discord features.
8. **No wholesale custom client.** CSS restyles Vesktop/Discord's frontend. It cannot create genuine OS-level conversation windows or change Discord's data model.

## 2. Palette (approved design tokens)

| Token | Hex | Where it goes |
|---|---|---|
| `plastic` | `#DDD8C8` | Main application chrome, frame, conventional panel |
| `paper` | `#E8E2D2` | Chat transcript background |
| `paper-highlight` | `#F9F6EB` | Inputs, inset chat fields, popovers |
| `smoked-beige` | `#CFC7B4` | Sidebars, secondary chrome and status strips |
| `aged-trim` | `#A89F8C` | Bevel shadow, muted hardware details |
| `ink` | `#2B2A26` | Primary text, controls and icons |
| `ink-muted` | `#5B574E` | Secondary labels **on lighter paper/plastic**, not on beige |
| `teal` | `#4F7A73` | Secondary highlights, focus borders and inactive title |
| `teal-deep` | `#355C57` | Active title bar (paired with near-white text) |
| `teal-selection` | `#B7CFBA` | Selected contact/channel row with dark text |
| `frame` | `#77847A` | Border between content and chrome |
| `amber` | `#A56032` | Limited warning / unread accent; use dark ink for text unless checked |

Use `discord/prototypes/kim-v0.3.tokens.css` as the machine-readable prototype palette. Do **not** install that file as a Vesktop theme by itself.

### Verified WCAG contrast checks (relative luminance)

| Pair | Ratio | Requirement |
|---|---:|---|
| Ink `#2B2A26` on paper `#E8E2D2` | 11.11:1 | Pass AA normal text (4.5:1) |
| Ink on plastic `#DDD8C8` | 10.08:1 | Pass |
| Ink on smoked-beige `#CFC7B4` | 8.54:1 | Pass |
| Muted ink `#5B574E` on paper | 5.57:1 | Pass |
| Muted ink on smoked-beige | 4.28:1 | **Fail** normal text — use primary ink instead |
| Near-white `#F9F6EB` on deep teal `#355C57` | 6.88:1 | Pass |
| Near-white on standard teal `#4F7A73` | 4.45:1 | **Fail** normal text — use deep teal title |
| Deep teal on plastic | 5.22:1 | Pass |

Targets: >= 4.5:1 for normal text, >= 3:1 for large text and meaningful non-text interface indicators. Actual rendering and native Discord tokens must be visually audited; color-pair calculations alone aren't sufficient.

## 3. Shape, type and interaction

- **Fonts:** Try Tahoma/Arial/"Liberation Sans" for window chrome and forms; chat content can use readable sans serif. Avoid site-wide monospace for every message. Do not bundle proprietary IBM or game fonts.
- **Font sizes:** 13–14 px minimum normal labels; chat text 14–15 px; headers 12–13 px semibold; never fake old screens by shrinking body text to 10 px.
- **Radii:** 0–2 px for most interface surfaces; avatars remain round or as Discord provides.
- **Borders:** 1 px frame, 2 px inset for message transcript if spacing allows. Avoid stacking 3+ competing outlines.
- **Bevel:** top/left a light 1 px line; bottom/right a slightly darker 1 px line. Reserve for buttons, fields and panel framing, not each individual message.
- **Hover / selected / focus:** hover subtle warm beige; selected pale teal `#B7CFBA` with ink; keyboard focus visible 2 px dark teal outline.
- **Motion:** no flashing, glitching, scanline interference or simulated blur; optional restrained transitions only.
- **Wallpaper/background:** outer frame a little darker than window chrome; *never* put textured imagery behind message text.

## 4. The layout we are trying to build

```text
╔══════════════════════════════════════════════════════════════╗
║  KIM // COMMUNICATIONS DIRECTORY                      _ □ X  ║  <- deep teal
╠═══════════╦═════════════════════════════════╦════════════════╣
║ DIRECTORY ║  CONTACT: [NAME]  • CONNECTED    ║ CONNECTION     ║
║           ╠═════════════════════════════════╣ INFORMATION    ║
║ > Friends ║                                 ║                ║
║ > Hex     ║  Sender                     14:32║ avatar / status ║
║ > Servers ║  A compact legible message...   ║                ║
║           ║                                 ║                ║
║ [avatar]  ║  Sender                     14:35║                ║
║ Contact A ║  Reply...                       ║                ║
║ [avatar]  ║                                 ║                ║
║ Contact B ╠═════════════════════════════════╣                ║
║           ║ [ Message...              ][SEND]║                ║
╚═══════════╩═════════════════════════════════╩════════════════╝
```

This is a **visual mockup**, not a promise that CSS can independently split Discord into actual OS-level windows.

### Hierarchy

- **Servers:** remain discoverable; visually become a compact directory rail rather than huge colorful circles dominating the screen.
- **DM contacts:** warm-beige roster with portraits, dark names, clear online and selected markers, visible unread indicators.
- **Conversation header:** a single deep-teal or cream-framed title strip. Only one dominant teal bar per logical window.
- **Messages:** cream paper, crisp name and timestamp distinction, generous enough line height. No individual message bubbles unless they meaningfully support KIM reference.
- **Composer:** off-white inset field with tactile border and a recognizable send/action area; uploads, emoji and keyboard navigation still work.
- **Voice:** conventional controls remain functional; adapt the styling to radio/frequency framing later, in its own development pass.

## 5. Explicitly banned from v0.3

- Recoloring the entire application with a single `--bg-* = teal/green` value.
- Overriding `color-scheme: light` without comprehensive token and actual-screen verification.
- Global `opacity`, `filter`, `brightness`, `mix-blend-mode`, `pointer-events` or blanket `display:none` tricks.
- White/light text on cream, low-contrast placeholder text, washed-out disabled-looking active buttons.
- Updating the *live* `~/.config/vesktop/themes/kim.theme.css` before screenshot review.
- Editing Discord account state, messages, credentials, or API behavior as part of CSS work.

## 6. Implementation / release plan

1. **Prototype only:** build `discord/prototypes/kim-v0.3.html` using *fictional* contacts and local CSS tokens. No live Discord DOM. Showcase friends view, DM view, narrow viewport, overlay/popover, and voice placeholder.
2. **Human visual review:** inspect screenshots for warm cream, readable ink, teal only where purposeful, and convincing period UI.
3. **Vesktop CSS integration:** inspect actual Discord element structure for each view; map selectors carefully; add one component at a time.
4. **Test matrix:** Friends, DMs, server channel, threads, member popout, Settings, voice/video, uploads, search, unread, tooltips, emoji, focused keyboard navigation, and modal overlays.
5. **Rollback:** keep `kim.theme.css` and v0.1 local backup untouched until sign-off. If any UI breaks, disable the custom theme in Vencord.
6. **Release gate:** screenshot approval on both an OLED monitor and standard secondary monitor before activation.

**Current state:** GitHub's existing `discord/kim.theme.css` tracks an experimental prior CSS iteration. The local machine was restored to v0.1 after v0.2's low-contrast failure. No v0.3 live theme has been deployed.

## 7. Relationship to the rest of Höllvania

This brief governs **KIM 1999**, not the separate **Voidtouched / Orokin Derelict** desktop profile. Both may share an architecture, but their palettes and ornamentation must remain independent.

Reference: `docs/kim-design-contract.md` is the higher-level design and safety contract.
