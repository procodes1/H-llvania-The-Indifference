# Höllvania: Hyprland workspaces and Warframe

**Date:** 2026-10-22  
**Platform inspected:** CachyOS, Hyprland 0.56.2 (Lua configuration), ML4W dotfiles. Two displays: DP-2 (primary 2560×1440), DP-3 (secondary 1920×1080).

## What we found

Hyprland's normal ML4W keyboard bindings already exist: `Super + 1…9` for numeric workspaces 1…9, `Super + 0` for workspace 10, and `Super + Shift + number` for moving the active window. The bindings use current `hl.dsp.focus({workspace=i})` Lua semantics and showed up in `hyprctl binds -j`.

We successfully switched the active DP-2 monitor from workspace 5 to empty workspace 7 and back with the current Lua IPC form:

```bash
hyprctl dispatch 'hl.dsp.focus({ workspace = 7 })'
hyprctl dispatch 'hl.dsp.focus({ workspace = 5 })'
```

**DO NOT use** the legacy `hyprctl dispatch workspace 7` syntax with this Lua-based session. It fails to parse. Some older Waybar workspace-click integrations use that old IPC form. ML4W's Quickshell `~/.config/quickshell/StatusbarApp/WorkspacesModule.qml` has a `Hyprland.usingLua` branch that already uses the new form.

The live Warframe window had class `steam_app_230410`, was fullscreen, and was located on **`special:scratchpad`** (workspace -98) rather than a normal numbered workspace. The scratchpad is a drop-down workspace layered over the current desktop; putting a fullscreen game there can make ordinary numbered-workspace switching *look* broken because the game remains visible.

The session's original `Super+S` toggles the scratchpad and `Super+Shift+S` moves the active window **into** it. Beware accidentally triggering the latter while trying to take screenshots.

## Persistent Warframe placement

Configured a narrowly scoped **ML4W Lua window rule** to open Warframe on normal workspace **5**, on **DP-2** (the primary OLED monitor). This does not force floating, pinning or fullscreen mode; the game itself chooses window mode.

Source tracked in Höllvania repo:
`profiles/hyprland/warframe-workspace.lua`

Installed ML4W custom hook:
`~/.config/hypr/custom.lua`

The standard ML4W `hyprland.lua` already loads `custom.lua` if present, so no upstream keybinding files were edited.

```lua
hl.window_rule({
    name = "hollvania-warframe-workspace",
    match = { class = "^steam_app_230410$" },
    workspace = "5",
    monitor = "DP-2",
    content = "game",
})
```

Validated the Lua syntax with `luac -p`, reloaded Hyprland successfully with `hyprctl reload`. **The placement rule awaits verification the next time Warframe starts**; the game was no longer running by the final inspection. Avoid relaunching it without the user's direction.

To leave a scratchpad overlay, use `Super+S`, or:

```bash
hyprctl dispatch 'hl.dsp.workspace.toggle_special("scratchpad")'
```

The special workspace may reappear when the user deliberately opens it again.

## Workspace usage

- `Super+1` through `Super+9` → focus numeric workspace 1–9.
- `Super+0` → workspace 10.
- `Super+Shift+number` → move active window to corresponding workspace.
- `Super+S` → toggle scratchpad; *not* a numbered workspace.
- `Super+Shift+S` → move active window into scratchpad. Be careful while Warframe is focused.
- `Super+Alt+S` → the ML4W screenshot-area hotkey currently configured.

The compositor was verified capable of switching numbered workspaces; physical keypresses and a new Warframe launch were not tested remotely. On a dual-monitor setup, click/focus the intended monitor before choosing a numbered workspace.

## Recovery

If the Warframe window rule ever causes trouble, temporarily disable it (this was a new file, no previous custom.lua existed):

```bash
mv ~/.config/hypr/custom.lua ~/.config/hypr/custom.lua.hollvania-disabled
hyprctl reload
```

Restore:

```bash
mv ~/.config/hypr/custom.lua.hollvania-disabled ~/.config/hypr/custom.lua
hyprctl reload
```

No KDE, bootloader, Proton, graphics, or Steam settings were modified.
