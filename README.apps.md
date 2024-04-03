# Apps

## Necesary apps

### - Qtile (WM)
```bash
pacman -S qtile
```

### - Alacritty (Terminal)
```bash
pacman -S alacritty
```

### - Tmux (Terminal Multiplexer)
```bash
pacman -S tmux
```

### - Neovim (Text Editor)
```bash
pacman -S neovim
```

## zsh

### - zsh (shell)
```bash
pacman -S zsh
chsh -s zsh
```
### - ohmyzsh (zsh config)
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
### - powerlevel9k (ohmyzsh theme)
```bash
paru -S zsh-theme-powerlevel9k-git
```

## Backround programs

### - Dunst (notifications)
```bash
pacman -S dunst
```

### Sxhkd (keybinds)
```bash
pacman -S sxhkd
```

### Variety ()
```bash
pacman -S variety
```

## Rofi

### - Rofi (dmenu alternative)
```bash
pacman -S rofi
```

### - Rofi emoji
```bash
pacman -S rofi-emoji
```

### - Rofi calculator
```bash
pacman -S rofi-calc
```

## Terminal accesories

### - Zoxide (better cd)
```bash
pacman -S zoxide
```

### - fzf (fuzzy finder (for zoxide))
```bash
pacman -S fzf
```

### - Exa (better ls)
```bash
pacman -S exa
```

### - Bat (better cat)
```bash
pacman -S bat
```

### - Ripgrep (better grep)
```bash
pacman -S ripgrep
```

### - Midnight commander (terminal file manger)
```bash
pacman -S mc
```

### - Arandr (xrandr gui)
```bash
pacman -S arandr
```

## For scripts

### - Playerctl
```bash
pacmani -S playerctl
```

### - ACPI (battery cli)
```bash
pacman -S acpi
```

### - nm-applet (for network manager)
```bash
pacman -S network-manager-applet
```

### - picom
```bash
pacman -S picom
```

### - betterlockscreen
```bash
pacman -S betterlockscreen
```

## Themes

### - Papirus icons
```bash
pacman -S papirus-icon-theme
```

### - Jetbrains Mono
```bash
paru -S ttf-jetbrains-mono-nerd
```

### - Catppuccin alacritty theme
```bash
curl -LO --output-dir ~/.config/alacritty https://github.com/catppuccin/alacritty/raw/main/catppuccin-mocha.toml
```

### - Bibata cursor theme
```bash
paru -S bibata-cursor-theme
```

### - Adapta theme
```bash
paru -S adapta-gtk-theme-git
```

### Lxappearance
```bash
sudo pacman -S lxappearance
```
