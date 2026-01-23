"""
# Descrição

Arquivo relacionado à atividade 4.10 da parte 1.

# Resposta

OK, usarei o programa 4.6.
"""

# START - Código do programa 4.6

# Como os ímpares são 2n + 1 e já tenho 1, é só continuamente somar 2.
impares = range(1, 21, 2)

for impar in impares:
    print(impar)

# END - Código do programa 4.6

impares = list(impares)

print(f"Os três primeiros items da lista são: {impares[:3]}")
meio = impares[round(len(impares)/2)-2:round(len(impares)/2)+1]
print(f"Três itens do meio da lista são: {meio}")
print(f"Os três últimos itens da lista são: {impares[-3:]}")

