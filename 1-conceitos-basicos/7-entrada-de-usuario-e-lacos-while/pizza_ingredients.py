"""
# Descrição

Arquivo relacionado à atividade 7.4 da parte 1.
"""

ingredient = ""

print("Peço para que forneça os ingredientes para uma pizza.")
# A primeira iteração deve ser fora do laço de repetição condicional.
ingredient = input("Insira o ingrediente (quit para sair): ")

while ingredient != "quit":
    print(f"Vou adicionar {ingredient} à pizza.")
    ingredient = input("Insira o ingrediente (quit para sair): ")

    