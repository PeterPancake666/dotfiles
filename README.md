# dotfiles

This directory contains the dotfiles for my system.

## Programs
### - git

```bash
pacman -S git
```

### - stow

```bash
pacman -S stow
```

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
