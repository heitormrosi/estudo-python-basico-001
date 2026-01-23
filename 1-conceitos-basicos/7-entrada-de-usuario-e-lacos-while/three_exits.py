"""
# Descrição

Arquivo relacionado à atividade 7.6 da parte 1.

# Resposta

OK, vou utilizar a atividade 7.5.
"""

active = True

# Primeira iteração
idade = int(input("Insira a idade: "))
if idade < 0:
    active = False

while active:    
    if idade < 3:
        print("O ingresso é gratuito para crianças abaixo de 3 anos.")
    elif idade < 12:
        print("O ingresso custa 10 dólares para crianças entre 3 e 12 anos.")
    else:
        print("O ingresso custa 15 dólares para pessoas acima de 12 anos.")
    
    idade = int(input("Insira a idade: "))
    if idade < 0:
        active = False