"""
# Descrição

Arquivo relacionado à atividade 11.2 da parte 1.
"""

def city_country(city: str, country: str, population: int = 0) -> str:
    if population == 0:
        return f"{city.title()}, {country.title()}"
    else:
        return f"{city.title()}, {country.title()} - população {population}"