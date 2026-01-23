"""
# Descrição

Arquivo relacionado à atividade 7.9 da parte 1.
"""

sandwich_orders = [
    "Presunto e queijo", "Pastrami", "Presunto", "Queijo", "Frango",
    "Mortadela", "Pastrami", "Pastrami"
]

finished_sandwiches = []

print("A lanchonete está sem pastrami.")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich_order = sandwich_orders.pop().lower()
    print(f"Preparei seu sanduíche de {sandwich_order}.")
    finished_sandwiches.append(sandwich_order)

for finished_sandwich in finished_sandwiches:
    print(f"O sanduíche de {finished_sandwich} foi preparado.")
