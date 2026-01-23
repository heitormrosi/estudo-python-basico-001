"""
# Descrição

Arquivo relacionado à atividade 8.14 da parte 1.
"""

from typing import Any

def salvar_carro_dicionario(
        fabricante: str, 
        modelo: str, 
        **outros_argumentos: dict[str, Any]) -> dict:
    """ Salva as informações de um carro em um dicionário. """
    return {
        "fabricante": fabricante,
        "modelo": modelo,
        **outros_argumentos # Adiciona as informações de outro dicionário.
    }


def main() -> None:
    carro = salvar_carro_dicionario(
        "subaru", 
        "outback",
        color="blue", 
        tow_package=True
    )

    print(carro)


if __name__ == "__main__":
    main()