"""
# Descrição

Arquivo relacionado à atividade 5.10 da parte 1.
"""

current_users = ['ana', 'bruno', 'carla', 'diego', 'elena', 'fabio']
new_users = ['carla', 'gabriel', 'HELENA', 'diego', 'lucas']

# O(n^2)
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} já existe. Forneça um novo nome de usuário.")
    else:
        print(f"O nome de usuário {new_user} está disponível.")