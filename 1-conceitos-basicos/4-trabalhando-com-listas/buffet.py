"""
# Descrição

Arquivo relacionado à atividade 4.13 da parte 1.
"""

pratos = (
    "Filet Mignon", "X-Burguer", "X-Bacon", "Tortilla", "Crepe"
)

print(" Cardápio ".center(30, "="))
for prato in pratos:
    print(prato)

# pratos[0] = "X-Bacon" # TypeError

pratos = list(pratos)
pratos[0] = "X-Bacon"
pratos[4] = "X-Tudo"
pratos = tuple(pratos)

print(" Cardápio ".center(30, "="))
for prato in pratos:
    print(prato)