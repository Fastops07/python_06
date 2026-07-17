def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed_ingredients: list[str] = light_spell_allowed_ingredients()
    normalized_ingredients: str = ingredients.lower()

    for allowed_ingredient in allowed_ingredients:
        if allowed_ingredient in normalized_ingredients:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
