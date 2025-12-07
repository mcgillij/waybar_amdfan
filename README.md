# AMDFAN stats in waybar

small waybar module to show amdfan stats in the bar
## Installation

clone repo into `~/.config/waybar/waybar_amdfan/`
and `poetry install`

## Configuration

**~/.config/waybar/config**

``` json
...
  "modules-center": [
    "hyprland/window",
    "cpu",
    "memory",
    "network",
    "custom/gh",
    "custom/gh#2",
    "custom/fan_monitor", // < add at some spot
  ],
...
"custom/fan_monitor": {
    "format": "{text}",
    "exec": "$HOME/.config/waybar/waybar_amdfan/waybar_amdfan.sh",
    "restart-interval": 5,
    "return-type": "json",
},
...
```


