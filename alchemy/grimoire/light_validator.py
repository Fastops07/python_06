from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> tuple[str, str]:
    valid_ingredients = light_spell_allowed_ingredients()
    for valid_ingredient in valid_ingredients:
        if ingredients == valid_ingredient:
            return ("VALID", ingredients)
    return ("INVALID", ingredients)
