"""
# Descrição

Arquivo relacionado à atividade 4.11 da parte 1.
"""

# START - Código do programa 4.1

pizzas_favoritas = [
    "Pepperoni", "Queijo", "Frango com catupiry"
]

for pizza_favorita in pizzas_favoritas:
    print(f"Gosto de pizza de {pizza_favorita.lower()}")

print("Eu realmente adoro pizza!")

# END - Código do programa 4.1

friend_pizzas = pizzas_favoritas[:]

pizzas_favoritas.append("Nutella")

friend_pizzas.append("Salame")

print("Minhas pizzas favoritas são:")
for pizza_favorita in pizzas_favoritas:
    print(pizza_favorita)

print("As pizzas favoritas de meu amigo são:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)