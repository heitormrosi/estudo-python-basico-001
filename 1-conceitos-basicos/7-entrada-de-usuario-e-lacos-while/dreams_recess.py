"""
# Descrição

Arquivo relacionado à atividade 7.10 da parte 1.
"""

ferias_dos_sonhos = []

while True:
    print(
        "Se pudesse visitar um lugar do mundo, "
        + "para onde você iria (quit para sair)?"
    )
    lugar = input()

    if lugar == "quit":
        break
    
    ferias_dos_sonhos.append(lugar)

for lugar in ferias_dos_sonhos:
    print(f"Uma pessoa gostaria de ir para {lugar} em suas férias dos sonhos!")
    
