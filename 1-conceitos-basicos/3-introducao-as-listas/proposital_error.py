"""
# Descrição

Arquivo relacionado à atividade 3.11 da parte 1.

# Resposta

OK, vou introduzir o erro em 3.2.
"""

nomes = [
    "Danilo", "Natã", "Lorran"
]

mensagem = "Olá, {0}!"

print(mensagem.format(nomes[0]))
print(mensagem.format(nomes[4])) # IndexError
print(mensagem.format(nomes[5])) # IndexError