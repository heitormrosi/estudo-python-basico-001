"""
# Descrição

Arquivo relacionado à atividade 8.12 da parte 1.
"""

def mostrar_sanduiche(*ingredientes: list[str]) -> None:
    print("Sanduíche: ")
    for ingrediente in ingredientes:
        print(ingrediente)


def main() -> None:
    mostrar_sanduiche("Pão", "Queijo", "Alface", "Tomate")
    mostrar_sanduiche("Pão", "Hambúrguer", "Bacon")
    mostrar_sanduiche("Pão", "Tomate", "Frango")


if __name__ == "__main__":
    main()