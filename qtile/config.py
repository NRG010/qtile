import os
import subprocess

from libqtile import bar, layout, widget
from libqtile.config import Match, Screen, hook

from keybindings import keyConfig, mouseConfig


@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser(".config/qtile/autostart.bash")])


keys = keyConfig()

mouse = mouseConfig()

lay_config = {
    "border_width": 2,
    "margin": 4,
    "border_focus": "#89b4fa",
    "border_normal": "#1e1e2e",
    "font": "CaskaydiaCove Nerd Font Mono",
    "grow_amount": 2,
}

layouts = [
    layout.Bsp(**lay_config),
    layout.Max(),
]

widget_defaults = dict(
    font="CaskaydiaCove Nerd Font Mono",
    background="#11111b",
    foreground="#b4befe",
    fontsize=12,
    padding=4,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(borderwidth=0),
                widget.Prompt(),
                widget.Spacer(),
                widget.Systray(),
                widget.Clock(format="%H:%M %a %d-%m-%y"),
            ],
            20,
        ),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24
