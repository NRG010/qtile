#!/usr/bin/env bash

# Bluetooth
/usr/bin/systemctl --user restart pipewire &
/usr/bin/systemctl --user restart pipewire-pulse &
/usr/bin/bluetoothctl connect 30:53:C1:C7:8D:9E &

# Brightness
/usr/bin/brightnessctl s 500 &

# Redshift
/usr/bin/redshift -P -O 2500 &

# Wallpaper
/usr/bin/feh --bg-scale ~/.config/qtile/wallpapers/hanged_man_tree.jpg &

# Clipboard
/usr/bin/clipmenud &

# Notifications
/usr/bin/dunst &
