"""
# Descrição

Arquivo relacionado à atividade 5.11 da parte 1.
"""

lista = [i for i in range(1, 10)]

for i in lista:
    # Prefiro switch-case (match)
    if i == 1:
        print(f"{i}st", end=" ")
    elif i == 2:
        print(f"{i}nd", end=" ")
    elif i == 3:
        print(f"{i}rd", end=" ")
    else:
        print(f"{i}th", end=" ")