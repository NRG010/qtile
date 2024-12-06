local wezterm = require("wezterm")

local config = wezterm.config_builder()

config.font = wezterm.font("CaskaydiaCove Nerd Font Mono")

config.color_scheme = "Catppuccin Mocha"

config.enable_tab_bar = false

config.font_size = 12.5

config.window_padding = {
	left = 5,
	right = 5,
	top = 5,
	bottom = 5,
}

return config
