"""
# Descrição

Arquivo relacionado à atividade 8.5 da parte 1.
"""

def describe_city(cidade: str, pais: str = "Brasil") -> None:
    print(f"{cidade} está localizada em(a) {pais}")

def main() -> None:
    describe_city("Vitória")
    describe_city("Pindamonhangaba")
    describe_city("Nova Iorque", "Estados Unidos")


if __name__ == "__main__":
    main()