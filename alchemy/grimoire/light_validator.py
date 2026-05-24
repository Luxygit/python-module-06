"""validates alchemy elements"""

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """checking if ingredients have at least one valid element"""
    allowed = light_spell_allowed_ingredients()
    clean_input = ingredients.lower()
    is_valid = any(element in clean_input for element in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
