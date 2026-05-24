""""""


def brew_potion(elem1: str, elem2: str) -> str:
    """"""
    e1 = elem1.lower().strip()
    e2 = elem2.lower().strip()

    if ("fire" in e1 and "water" in e2) or ("water" in e1 and "fire" in e2):
        return "Steam Potion"
    if ("earth" in e1 and "air" in e2) or ("air" in e1 and "earth" in e2):
        return "Dust Potion"

    return "Unknown Sludge"
