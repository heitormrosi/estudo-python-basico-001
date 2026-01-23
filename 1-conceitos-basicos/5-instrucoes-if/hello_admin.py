"""
# Descrição

Arquivo relacionado à atividade 5.8 da parte 1.
"""

users = [
    "heitor", "pc", "admin", "joao", "pineapple"
]

for user in users:
    if user == "admin":
        print("Olá, admin, gostaria de ver um relatório de status?")
    else:
        print(f"Olá, {user}, obrigado por fazer login novamente.")