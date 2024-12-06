abbr pu "yay -R"
abbr pi "yay -S --needed"
abbr pc "yay -Yc; yay -Sc; yay"

abbr gb "git add -A; git commit -am '$(date +%d/%m/%y\ %H:%m)'; git push"
abbr pb "pass git add -A; pass git commit -am '$(date +%d/%m/%y\ %H:%m)';pass git push"

# Start at login
if status is-login
  if test -z "$DISPLAY" -a "$XDG_VTNR" = 1
    /usr/bin/startx
  end
end

# File
function yy
  set tmp (mktemp -t "yazi-cwd.XXXXXX")
  yazi $argv --cwd-file="$tmp"
  if set cwd (command cat -- "$tmp"); and [ -n "$cwd" ]; and [ "$cwd" != "$PWD" ]
    builtin cd -- "$cwd"
  end
  rm -f -- "$tmp"
end

starship init fish | source
