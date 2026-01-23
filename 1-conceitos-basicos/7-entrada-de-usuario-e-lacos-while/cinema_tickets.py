"""
# Descrição

Arquivo relacionado à atividade 7.5 da parte 1.
"""

idade = int(input("Insira a idade: "))

while idade > 0:
    if idade < 3:
        print("O ingresso é gratuito para crianças abaixo de 3 anos.")
    elif idade < 12:
        print("O ingresso custa 10 dólares para crianças entre 3 e 12 anos.")
    else:
        print("O ingresso custa 15 dólares para pessoas acima de 12 anos.")

    idade = int(input("Insira a idade: "))