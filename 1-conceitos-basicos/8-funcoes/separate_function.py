"""
# Descrição

Arquivo relacionado à atividade 8.16 da parte 1.

Função da atividade 8.12.
"""

def mostrar_sanduiche(*ingredientes: list[str]) -> None:
    print("Sanduíche: ")
    for ingrediente in ingredientes:
        print(ingrediente)