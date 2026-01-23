"""
# Descrição

Arquivo relacionado à atividade 8.6 da parte 1.
"""

def city_country(cidade: str, pais: str) -> str:
    return f"{cidade}, {pais}"


def main() -> None:
    print(city_country("Vitória", "Brasil"))
    print(city_country("Serra", "Brasil"))
    print(city_country("Rio de Janeiro", "Brasil"))


if __name__ == "__main__":
    main()