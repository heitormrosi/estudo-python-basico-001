"""
# Descrição

Arquivo relacionado à atividade 7.2 da parte 1.
"""

print("Quantas pessoas estão em teu grupo para jantar?")
qtd_pessoas = int(input("Insira sua resposta: "))

if qtd_pessoas > 8:
    print("Por favor, espereis por uma mesa.")
else:
    print("Vossa mesa está pronta.")