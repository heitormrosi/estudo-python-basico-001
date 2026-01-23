"""
# Descrição

Arquivo relacionado à atividade 3.7 da parte 1.
"""

# START - Código do programa 3.6

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

# Insere os novos convidados.
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

# END - Código do programa 3.7

print("Agora, só posso convidar duas pessoas para o jantar.")

# Remove os convidados até que sobrem apenas dois.
while len(lista_de_convidados) > 2:
    desconvidado = lista_de_convidados.pop()
    print(
        f"Me desculpe, {desconvidado}, por não poder te convidar para o jantar."
    )

for convidado in lista_de_convidados:
    print(f"{convidado}, você está convidado para um jantar.")

del lista_de_convidados[1]
del lista_de_convidados[0]

print(lista_de_convidados)