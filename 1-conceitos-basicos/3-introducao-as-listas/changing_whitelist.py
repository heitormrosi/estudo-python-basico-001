"""
# Descrição

Arquivo relacionado à atividade 3.5 da parte 1.
"""

lista_de_convidados = [
    "Albert Einstein", "César Lattes", "Edward Snowden", "Alan Turing"
]

# Mostra a lista de convidados.
for convidado in lista_de_convidados:
    print(f"{convidado}, você está convidado para um jantar.")


print("Alan Turing não poderá comparecer.")
# Substitui o convidado ausente por outro.
index_convidado_ausente = lista_de_convidados.index("Alan Turing")
lista_de_convidados[index_convidado_ausente] = "Linus Torvalds"

for convidado in lista_de_convidados:
    print(f"{convidado}, você está convidado para um jantar.")