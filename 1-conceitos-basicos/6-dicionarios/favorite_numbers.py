"""
# Descrição

Arquivo relacionado à atividade 6.2 da parte 1.
"""

# Preguiça de pegar dados reais
numeros_favoritos = {
    "Carlos": 1,
    "Maria": 2,
    "João": 3,
    "André": 6,
    "Pedro": 9
}

print(" Números favoritos ".center(30, "="))
for k, v in numeros_favoritos.items():
    print(k + " -> " + str(v))