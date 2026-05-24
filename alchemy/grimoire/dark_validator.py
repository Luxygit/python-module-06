"""validating dark magic material lists. triggering circular lock"""

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """checking if any dark ingredient matches the allowed list"""
    allowed = dark_spell_allowed_ingredients()
    clean_input = ingredients.lower()
    is_valid = any(element in clean_input for element in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
