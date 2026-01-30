"""
# Descrição

Arquivo relacionado à atividade 10.11 da parte 1.
"""

import json

def main() -> None:
    arquivo = "fnum.json"

    try:
        with open(arquivo) as fd:
            fnum = json.load(fd)
    except FileNotFoundError:
        print("Infelizmente, não sei sei número favorito... buá!")
    else:
        print(f"Eu sei qual é o seu número favorito! É {fnum}.")

if __name__ == "__main__":
    main()