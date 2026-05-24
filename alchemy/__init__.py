"""exposing only a part of alchemy module and exposes healingpotion as alias"""

from .elements import create_air
from .potions import healing_potion, strength_potion
from . import transmutation
from . import grimoire

heal = healing_potion
# explicitely exporting some properties
__all__ = [
        "create_air",
        "strength_potion",
        "heal",
        "transmutation",
        "grimoire",
        ]
