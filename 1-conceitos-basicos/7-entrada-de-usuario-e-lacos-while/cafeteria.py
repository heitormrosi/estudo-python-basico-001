"""
# Descrição

Arquivo relacionado à atividade 7.8 da parte 1.
"""

sandwich_orders = [
    "Presunto e queijo", "Presunto", "Queijo", "Frango",
    "Mortadela"
]

finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop().lower()
    print(f"Preparei seu sanduíche de {sandwich_order}.")
    finished_sandwiches.append(sandwich_order)

for finished_sandwich in finished_sandwiches:
    print(f"O sanduíche de {finished_sandwich} foi preparado.")


