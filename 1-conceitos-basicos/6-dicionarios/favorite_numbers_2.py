"""
# Descrição

Arquivo relacionado à atividade 6.10 da parte 1.
"""

OUTPUT_SIZE = 30

# Preguiça de pegar dados reais
numeros_favoritos = {
    "Carlos": [1, 10, 15],
    "Maria": [2, 22],
    "João": [3],
    "André": [6, 60, 600],
    "Pedro": [9, 99]
}

print(" Números favoritos ".center(30, "="))
for nome, numeros in numeros_favoritos.items():
    print(f"+{"= Números favoritos de =".center(OUTPUT_SIZE, "-")}+")
    print(f"|{"   ".center(OUTPUT_SIZE, " ")}|")
    print(f"|{nome.center(OUTPUT_SIZE, " ")}|")
    print(f"|{"   ".center(OUTPUT_SIZE, " ")}|")
    print(f"+{"=$=".center(OUTPUT_SIZE, "-")}+")
    print(f"|{"   ".center(OUTPUT_SIZE, " ")}|")
    for numero in numeros:
        print(f"|{numero.center(OUTPUT_SIZE, " ")}|")
    print(f"|{"   ".center(OUTPUT_SIZE, " ")}|")
    print(f"+{"=$=".center(OUTPUT_SIZE, "-")}+")
    print()
    