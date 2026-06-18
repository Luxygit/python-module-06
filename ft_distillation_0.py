"""testing direct imports for submodules"""
from alchemy.potions import healing_potion, strength_potion

if __name__ == "__main__":
    print("=== Distillatio 0 ===")
    print("Direct access to alchemy/potions.py")
    res_str = strength_potion()
    print(f"Testing strength_potion: {res_str}")
    res_heal = healing_potion()
    print(f"Testing healing_potion: {res_heal}")
