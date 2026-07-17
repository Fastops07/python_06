from .light_validator import validate_ingredients
def light_spell_allowed_ingredients() -> list[str] : 
    allowed_ingredients: list[str] = ["earth", "air", "fire", "water"]
    return allowed_ingredients

def light_spell_record(spell_name: str, ingredients: str) -> str :
    validity, _ = validate_ingredients(ingredients)
    if (validity == "VALID"):
        return "recorded"
    return "rejected"