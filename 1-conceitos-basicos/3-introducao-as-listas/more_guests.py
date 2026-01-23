"""
# Descrição

Arquivo relacionado à atividade 3.6 da parte 1.
"""

# START - Código do programa 3.5

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

# END - Código do programa 3.5

print("Rapaziada, encontrei uma mesa de jantar maior!!!")

lista_de_convidados.insert(0, "Bill Gates")
lista_de_convidados.insert(
    # Seleciona o centro se for par e um dos dois meios do centro se for 
    # ímpar.
    round(len(lista_de_convidados)/2), 
    "Ada Lovelace"
)
lista_de_convidados.append("Richard Stallman")

for convidado in lista_de_convidados:
    print(f"{convidado}, você está convidado para um jantar.")