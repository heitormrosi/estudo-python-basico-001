"""
# Descrição

Arquivo relacionado à atividade 8.3 da parte 1.
"""

def make_shirt(tamanho: int, texto: str) -> None:
    print(
        f"Tamanho da camiseta: {tamanho}\n"
        + f"Mensagem estampada: {texto}"
    )


def main() -> None:
    make_shirt(10, "Sweet")
    make_shirt(texto="Super Idol", tamanho=36)


if __name__ == "__main__":
    main()