from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class GameOffsets:
    GOD_MODE: int = 0x2a4b537
    UNLIMITED_AMMO: int = 0x2a4b4f1
    ESP_ENABLED: int = 0x2a4b5dc
    SPEED_HACK: int = 0x2a4b751
    NO_RECOIL: int = 0x2a4b821
    LOOT_UNLOCKER: int = 0x2a4b878
    BOUNTY_COMPLETE: int = 0x2a4b8f1
    AIMBOT_FOV: int = 0x2a4b9c0
    PLAYER_BASE: int = 0x1e8a50e
    PLAYER_OFFSETS: list = field(default_factory=lambda: [0x0, 0x30, 0x8, 0x20])
    VERSION_OFFSETS: Dict[str, Dict[str,int]] = field(default_factory=lambda: {
        "2026.06.28-709": {
            "GOD_MODE": 0x2a4b537,
            "UNLIMITED_AMMO": 0x2a4b4f1,
        }
    })
    def get_for_version(self, ver): return self.VERSION_OFFSETS.get(ver, {})

offsets = GameOffsets()
