# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

mod = "mod4"
terminal = "alacritty"
rofi = "rofi -show drun"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),


    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    #Key([mod, "shift"], "q", lazy.spawn("/home/petrup/.local/bin/powermenu"), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawn(rofi), desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

groups = [
    Group("1", label=""),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label=""),
]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
    "border_width":2,
    "margin":15,
    "border_focus":"FFFFFF",
    "border_normal":"CCCCCC",
}

layouts = [ 
    layout.MonadTall(**layout_theme),
    #layout.Columns(),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Jetbrains mono NF",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

### WIDGETS LEFT ###

p_widgets_left = [
    widget.Sep(
        linewidth = 1,
        padding = 5,
        foreground = "#45475a",
        background = "#1e1e2e"
    ),
    widget.CurrentLayoutIcon(
        padding = 4,
        scale = 0.7,
        foreground = "#cdd6f4",
        background = "#1e1e2e"
    ),
    widget.Sep(
        linewidth = 1,
        padding = 5,
        foreground = "#45475a",
        background = "#1e1e2e"
    ),
    widget.GroupBox(
        font = "JetBrains Mono Nerd Font Bold",
        fontsize = 12,
        margin_y = 2,
        margin_x = 3,
        padding_y = 2,
        padding_x = 3,
        borderwidth = 0,
        disable_drag = True,
        active = "#6c7086",
        inactive = "#313244",
        rounded = False,
        highlight_method = "text",
        this_current_screen_border = "#cdd6f4",
        foreground = "#45475a",
        background = "#1e1e2e"
    ),
    widget.Sep(
        linewidth = 1,
        padding = 5,
        foreground = "#45475a",
        background = "#1e1e2e"
    ),
    widget.Prompt(
        font = "Jetbrains Mono Nerd Font",
        fontsize = 12,
        background = "#1e1e2e",
        foreground = "#cdd6f4"
    ),
    widget.WindowName(
        font = "Jetbrains Mono Nerd Font Bold",
        fontsize = 12,
        foreground = "#cdd6f4",
        background = "#1e1e2e"
    ),]

### WIDGETS RIGHT ###

p_widgets_right = [
    widget.Sep(
        linewidth = 1,
        padding = 5,
        foreground = "#45475a",
        background = "#1e1e2e"
    ),
    widget.Clock(
        foreground = "#181825",
        background = "#1e1e2e",
        font = "Jetbrains Mono Nerd Font Bold",
        fontsize = 12,
        format = "%d/%m/%y %H:%M:%S",
        decorations = [
            RectDecoration (
                colour = "#89b4fa",
                padding_y = 3,
                radius = 2,
                filled = True
            ),
        ],),

    widget.Sep(
        linewidth = 1,
        padding = 5,
        foreground = "#45475a",
        background = "#1e1e2e"
    ),
    widget.Systray(
        background = "#1e1e2e",
        icon_size = 20,
        padding = 5,
    ),
    widget.Sep(
        linewidth = 1,
        padding = 5,
        foreground = "#45475a",
        background = "#1e1e2e"
    ),
]

### SECONDARY WIDGETS ###

secondary_widgets = [
    widget.Sep(
        foreground = "#45475a",
        background = "#1e1e2e",
        padding = 5,
        linewidth = 1
    ),
    widget.Net(
        foreground = "#181825",
        background = "#1e1e2e",
        font = 'Jetbrains Mono Nerd Font Bold',
        fontsize = 12,
        format = '{down} ↓↑ {up}',
        decorations = [
            RectDecoration (
                colour = "#cba6f7",
                padding_y = 3,
                radius = 2,
                filled = True
            ),
        ],
    ),
    widget.Sep(
        linewidth = 1,
        padding = 5,
        foreground = "#45475a",
        background = "#1e1e2e"
    ),
    widget.CPU(
        background = "#1e1e2e",
        foreground = "#181825",
        font = "Jetbrains Mono Nerd Font Bold",
        fontsize = 12,
        decorations = [
            RectDecoration (
                colour = "#f38ba8",
                padding_y = 3,
                radius = 2,
                filled = True
            ),
        ],),
    widget.Sep(
        linewidth = 1,
        padding = 5,
        foreground = "4c566a",
        background = "#1e1e2e"
    ),
    widget.Memory(
        measure_mem = 'G',
        foreground = "#181825",
        background = "#1e1e2e",
        font = "Jetbrains Mono Nerd Font Bold",
        fontsize = 12,
        format = 'RAM{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        decorations = [
            RectDecoration (
                colour = "#fab387",
                padding_y = 3,
                radius = 2,
                filled = True
            ),
        ],),
        widget.Sep(
        linewidth = 1,
        padding = 5,
        foreground = "#45475a",
        background = "#1e1e2e"
    ),
    widget.Battery(
        foreground = "#181825",
        background = "#1e1e2e",
        font = "Jetbrains Mono Nerd Font Bold",
        fontsize = 12,
        charge_char = "󱐋",
        discharge_char = "",
        not_charging_char = "󰚥",
        format = "{char}{percent: 2.0%}",
        update_interval = 1,
        decorations = [
            RectDecoration (
                colour = "#a6e3a1",
                padding_y = 3,
                radius = 2,
                filled = True
            ),
        ],),
]

primary_widgets = p_widgets_left + p_widgets_right

def status_bar(widgets):
    return bar.Bar(widgets, 28, opacity=0.75)

screens = [
    Screen(
        bottom=status_bar(p_widgets_left + secondary_widgets + p_widgets_right),
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
        # Run the utility of `xprop` to see the wm class and name of an X client.
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
