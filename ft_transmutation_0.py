"""testing direct paths to the recipes"""

import alchemy.transmutation.recipes


if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/trasmutation/recipes.py directly")
    res = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {res}")
