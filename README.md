# dotfiles

This directory contains the dotfiles for my system.

## Requiered programs
### - git
```bash
pacman -S git
```
### - stow
```bash
pacman -S stow
```

## Installation 

First, clone the dotfiles repo

```bash
git clone https://github.com/PeterPancake666/dotfiles.git
cd dotfiles
```

then use GNU stow to create the symlinks

```bash
stow -vv . --target=$HOME
```

## Packages
### - zsh
```bash
pacman -S zsh
chsh -s zsh
```
### - ohmyzsh
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
### - powerlevel10k
```bash
paru -S zsh-theme-powerlevel10k-git
```
### - Jetbrains Mono
```bash
paru -S ttf-jetbrains-mono-nerd
```
### - Alacritty
```bash
pacman -S alacritty
```
### - Tmux
```bash
pacman -S tmux
```
### - Neovim
```bash
pacman -S neovim
```
### - Zoxide
```bash
pacman -S zoxide
```
### - fzf (for zoxide)
```bash
pacman -S fzf
```
### - Exa
```bash
pacman -S exa
```
### - Bat
```bash
paru -S bat
```
### - Ripgrep
```bash
paru -S ripgrep
```
### - Midnight commander
```bash
pacman -S mc
```
