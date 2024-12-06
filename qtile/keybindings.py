from libqtile import extension
from libqtile.config import Click, Drag, Group, Key
from libqtile.lazy import lazy

mod = "mod4"

term = "wezterm"
file = "wezterm start yazi"
code = "wezterm start nvim"

note = "obsidian"
browser = "qutebrowser"

windowFocus = [
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
]

windowSize = [
    Key([mod, "shift"], "l", lazy.layout.grow_right()),
    Key([mod, "shift"], "h", lazy.layout.grow_left()),
    Key([mod, "shift"], "j", lazy.layout.grow_down()),
    Key([mod, "shift"], "k", lazy.layout.grow_up()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
]

dmenu = [
    Key(
        [mod],
        "r",
        lazy.run_extension(
            extension.DmenuRun(
                fontsize=12,
                dmenu_prompt=">",
                dmenu_bottom=True,
                background="#11111b",
                foreground="#b4befe",
                selected_background="#89dceb",
                selected_foreground="#11111b",
                font="CaskaydiaCove Nerd Font Mono",
            )
        ),
    ),
    Key(
        [mod],
        "v",
        lazy.spawn(
            r"clipmenu -b -p '>'"
            + r" -fn CaskaydiaCove\ Nerd\ Font\ Mono=12"
            + r" -nb '#11111b' -nf '#b4befe'"
            + r" -sb '#89dceb' -sf '#11111b'"
        ),
    ),
]

applications = [
    Key([mod], "t", lazy.spawn(term)),
    Key([mod], "e", lazy.spawn(file)),
    Key([mod], "c", lazy.spawn(code)),
    Key([mod], "n", lazy.spawn(note)),
    Key([mod], "f", lazy.spawn(browser)),
]

windowFunctions = [
    Key([mod], "Return", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key(
        [mod, "shift"],
        "f",
        lazy.window.toggle_fullscreen(),
    ),
    Key(
        [mod, "shift"],
        "Space",
        lazy.window.toggle_floating(),
    ),
    Key([mod, "control"], "r", lazy.reload_config()),
]

for i in [Group(i) for i in "123456789"]:
    windowFunctions.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
            ),
        ]
    )


def keyConfig() -> list:
    return windowFocus + windowSize + dmenu + applications + windowFunctions


def mouseConfig(mod: str = mod) -> list:
    return [
        Drag(
            [mod],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [mod],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([mod], "Button2", lazy.window.bring_to_front()),
    ]
