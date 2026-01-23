"""
# Descrição

Arquivo relacionado à atividade 5.9 da parte 1.
"""

users = [
    "heitor", "pc", "admin", "joao", "pineapple"
]

users = []

if not users:
    print("Precisamos encontrar alguns usuários!")
else:
    for user in users:
        if user == "admin":
            print("Olá, admin, gostaria de ver um relatório de status?")
        else:
            print(f"Olá, {user}, obrigado por fazer login novamente.")