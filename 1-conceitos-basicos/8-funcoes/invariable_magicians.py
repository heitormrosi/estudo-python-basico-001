"""
# Descrição

Arquivo relacionado à atividade 8.11 da parte 1.
"""

def show_magicians(nomes_de_magicos: list[str]) -> None:
    """ Mostra na tela os nomes da lista de nomes de mágicos. """

    for nome_de_magico in nomes_de_magicos:
        print(nome_de_magico)


def make_great(nomes_de_magicos: list[str]) -> list[str]:
    """ 
        Modifica a lista de nomes de mágicos in-place e adiciona "Grande" no 
        início de cada nome. 
    """

    for i, nome_de_magico in enumerate(nomes_de_magicos):
        nomes_de_magicos[i] = "Grande " + nome_de_magico
    
    return nomes_de_magicos


def main() -> None:
    nomes_de_magicos = [
        "Mágico João", "Mágico Pedro", "Mágica Maria"
    ]

    nomes_de_grandes_magicos = make_great(nomes_de_magicos[:])
    
    show_magicians(nomes_de_magicos)
    show_magicians(nomes_de_grandes_magicos)


if __name__ == "__main__":
    main()