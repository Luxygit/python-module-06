"""importing thru relative and absolute imports"""


def lead_to_gold() -> str:
    """importing from top level base dir, and relative sister dirs"""
    import elements
    from ..potions import strength_potion
    from ..elements import create_air

    air = create_air()
    potion = strength_potion()
    fire = elements.create_fire()
    return (
            f"Recipe transmuting Lead to Gold: brew '{air}' and '{potion}' "
            f"mixed with '{fire}'"
        )
