#!/usr/bin/env bash

sudo pacman -Syu

# Aur helper
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

# Nvidia
yay -S --needed linux-zen-headers nvidia-dkms neovim xorg-xinit xorg-xrandr xorg-server
sudo cp ./grub /etc/default/grub
sudo cp ./mkinitcpio.conf /etc/mkinitcpio.conf
sudo cp ./10-nvidia-drm-outputclass.conf /etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf
sudo cp ./10-nvidia-drm-outputclass.conf /usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf
sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo mkinitcpio -P

# Fish
yay -S --needed fish starship
chsh -s /usr/bin/fish

# Fonts
yay -S --needed noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra ttf-cascadia-code-nerd

# Coding
yay -S --needed pyright python-black python-isort shfmt bash-language-server stylua lua-language-server

# Network
yay -S --needed nm-connection-editor networkmanager-openvpn

# Audio
yay -S --needed pipewire pipewire-audio pipewire-alsa pipewire-pulse pipewire-jack bluez bluez-utils pamixer

# Yazi
yay -S --needed yazi ffmpegthumbnailer p7zip jq poppler fd ripgrep fzf zoxide imagemagick imv zathura zathura-cb zathura-pdf-mupdf

# Media
yay -S --needed qutebrowser mpv yt-dlp obsidian qbittorrent steam

# Aurs
yay -S --needed vivaldi-widevine ani-cli youtube-music-bin

# Qtile
yay -S --needed wezterm qtile dunst bpytop feh redshift brightnessctl xsel clipmenu dmenu

# Misc.
rustup default stable
sudo systemctl enable bluetooth.service
