"""
# Descrição

Arquivo relacionado à atividade 6.4 da parte 1.
"""

glossario = {
    "lista": "Agrupamento de itens.",
    "laço": "Bloco de repetição.",
    "print": "Imprimir em inglês.",
    "for": "Para em inglês.",
    "zen": "Escola do budismo.",
    "if": "Se em inglês.",
    "else": "Senão em inglês",
    "elif": "Mistura de Se e Senão em inglês.",
    "condicional": "Que possui condição.",
    "variável": "Etiqueta para espaço de memória."
}

# Não precisei mudar.
for k, v in glossario.items():
    print(k + ":", end="\n\t")
    print(v)
