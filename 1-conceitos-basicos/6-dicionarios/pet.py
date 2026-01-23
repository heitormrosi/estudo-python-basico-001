"""
# Descrição

Arquivo relacionado à atividade 6.8 da parte 1.
"""

rex = {
    "tipo": "cachorro",
    "dono": "Augusto"
}

felix = {
    "tipo": "gato",
    "dono": "Beatriz"
}

goldie = {
    "tipo": "peixe",
    "dono": "Carlos"
}

pets = [rex, felix, goldie]

print("-"*20)
for pet in pets:
    print(f"Tipo do animal: {pet.get("tipo")}")
    print(f"Dono do pet: {pet.get("dono")}")
    print("-"*20)