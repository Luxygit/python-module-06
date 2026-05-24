"""structural alias matching interfaces using top-level imports"""

import alchemy

if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    res_str = alchemy.strength_potion()
    print(f"Testing strenghth_potion: {res_str}")
    res_heal = alchemy.heal()
    print(f"Testing heal alias: {res_heal}")
