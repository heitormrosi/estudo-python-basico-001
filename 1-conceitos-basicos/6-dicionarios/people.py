"""
# Descrição

Arquivo relacionado à atividade 6.1 da parte 1.
"""

pessoa = {}

# Prefiro utilizar .setdefault() e .get() ao invés de acessar com [].

pessoa["first_name"] = "Heitor"
pessoa["last_name"] = "Rosi"
pessoa["age"] = 18
pessoa["city"] = "Serra"

for k, v in pessoa.items():
    print(k + ": " + str(v))