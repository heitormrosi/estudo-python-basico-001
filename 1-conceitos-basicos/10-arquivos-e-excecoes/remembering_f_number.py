"""
# Descrição

Arquivo relacionado à atividade 10.12 da parte 1.
"""

import json

def main() -> None:
    arquivo = "fnum.json"

    try:
        with open(arquivo) as fd:
            fnum = json.load(fd)
    except FileNotFoundError:
        print("Qual seu número favorito?")
        try:
            fnum = int(input("> "))
        except ValueError:
            print("Insira um valor válido.")
        else:
            with open(arquivo, "w") as fd: 
                json.dump(fnum, fd)
    else:
        print(f"Eu sei qual é o seu número favorito! É {fnum}.")


if __name__ == "__main__":
    main()