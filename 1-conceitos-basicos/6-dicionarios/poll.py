"""
# Descrição

Arquivo relacionado à atividade 6.6 da parte 1.
"""

favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python'
}

pessoas = [
    "heitor", "phil", "carlos", "sarah"
]

for pessoa in pessoas:
    if pessoa in favorite_languages.keys():
        print(f"{pessoa}, obrigado por responder!")
    else:
        print(f"{pessoa}, por favor, participe da enquete!")