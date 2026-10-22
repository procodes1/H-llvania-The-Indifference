-- Project Höllvania / ML4W Hyprland 0.56.x (Lua config)
-- Dedicated gaming workspace. Never pin Warframe to every workspace,
-- never send it to special:scratchpad, and never force it to float.
-- Steam app ID 230410 = Warframe (XWayland class: steam_app_230410).
-- Normal workspace 5 belongs on primary OLED display DP-2.
-- On the AOC DP-3, retain independent Discord/browser workspaces.
hl.window_rule({
    name = "hollvania-warframe-workspace",
    match = { class = "^steam_app_230410$" },
    workspace = "5",
    monitor = "DP-2",
    content = "game",
})
