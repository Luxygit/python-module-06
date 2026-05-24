"""defining components for light magic spells"""


def light_spell_allowed_ingredients() -> list[str]:
    """returns list of allowed light magic forms"""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """records light spell if ingredients pass verification. local import"""
    from .light_validator import validate_ingredients
    val_string = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({val_string})"
