"""defining components for dark magic intentionnally causing an error"""

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """list of forbidden ingredients allowed for dark magic"""
    return ["bats", "frogs", "arsenic", "eyeball"]


def darl_spell_record(spell_name: str, ingredients: str) -> str:
    """tries to evaluate and log a darkspell"""
    val_string = validate_ingredients(ingredients)
    return  f"Spell recorded: {spell_name} ({val_string})"
