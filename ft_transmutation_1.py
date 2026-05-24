"""testing direct namespaces"""

from alchemy import transmutation

if __name__ == "__main__":
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    res = transmutation.lead_to_gold()
    print(f"Testing led to gold: {res}")
