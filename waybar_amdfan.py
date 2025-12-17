#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Waybar custom module to display AMDGPU fan speed and temperature.
"""

import json
import time
import sys
from amdfan.controller import Scanner

if len(sys.argv) > 1:
    CARD = sys.argv[1]
else:
    CARD = "card1"

FORMAT = "{card}: 🌬️{fan_speed} / {gpu_temp}℃🌡️"
INTERVAL = 5  # seconds

def get_fan_info():
    try:
        scanner = Scanner()
        card = scanner.cards.get(CARD)
        if card is None:
            return "error: card not found", None
        return None, (card.fan_speed, int(card.gpu_temp))
    except Exception as e:
        return f"error: {e}", None

while True:
    error, info = get_fan_info()
    if error:
        text = error
    else:
        fan_speed, gpu_temp = info
        text = FORMAT.format(card=CARD, fan_speed=fan_speed, gpu_temp=gpu_temp)
    print(json.dumps({"text": text}), flush=True)
    time.sleep(INTERVAL)
