"""
# Descrição

Arquivo relacionado à atividade 6.7 da parte 1.
"""

# START - Código do programa 6.1

pessoa = {}

pessoa["first_name"] = "Heitor"
pessoa["last_name"] = "Rosi"
pessoa["age"] = 18
pessoa["city"] = "Serra"

for k, v in pessoa.items():
    print(k + ": " + str(v))

# END - Código do programa 6.1

pessoa_2 = {}

pessoa_2["first_name"] = "João"
pessoa_2["last_name"] = "Paulo"
pessoa_2["age"] = 21
pessoa_2["city"] = "Sâo Paulo"

pessoa_3 = {}

pessoa_3["first_name"] = "Carlos"
pessoa_3["last_name"] = "Henrique"
pessoa_3["age"] = 28
pessoa_3["city"] = "João Pessoa"

people = [pessoa, pessoa_2, pessoa_3]

for person in people:
    for k, v in person.items():
        print(k + ": " + str(v))