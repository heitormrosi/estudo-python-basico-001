"""
# Descrição

Arquivo relacionado à atividade 8.9 da parte 1.
"""

def show_magicians(nomes_de_magicos: list[str]) -> None:
    for nome_de_magico in nomes_de_magicos:
        print(nome_de_magico)


def main() -> None:
    nomes_de_magicos = [
        "Mágico João", "Mágico Pedro", "Mágica Maria"
    ]

    show_magicians(nomes_de_magicos)


if __name__ == "__main__":
    main()