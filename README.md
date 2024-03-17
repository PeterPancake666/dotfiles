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

