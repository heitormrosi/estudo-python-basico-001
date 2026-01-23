"""
# Descrição

Arquivo relacionado à atividade 6.3 da parte 1.
"""

glossario = {
    "lista": "Agrupamento de itens.",
    "laço": "Bloco de repetição.",
    "print": "Imprimir em inglês.",
    "for": "Para em inglês.",
    "zen": "Escola do budismo."
}

for k, v in glossario.items():
    print(k + ":", end="\n\t")
    print(v)
