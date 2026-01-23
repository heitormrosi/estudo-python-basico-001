"""
# Descrição

Arquivo relacionado à atividade 8.4 da parte 1.
"""

def make_shirt(tamanho: str = "grande", texto: str = "Eu amo Python") -> None:
    print(
        f"Tamanho da camiseta: {tamanho}\n"
        + f"Mensagem estampada: {texto}"
    )


def main() -> None:
    make_shirt()
    make_shirt("média")
    make_shirt(texto="SUPER IDOL", tamanho="pequena")


if __name__ == "__main__":
    main()