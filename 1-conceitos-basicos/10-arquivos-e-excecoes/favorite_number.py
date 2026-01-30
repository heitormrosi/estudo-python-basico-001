"""
# Descrição

Arquivo relacionado à atividade 10.11 da parte 1.
"""

import json

def main() -> None:
    arquivo = "fnum.json"

    print("Qual seu número favorito?")
    try:
        fnum = int(input("> "))
    except ValueError:
        print("Insira um valor válido.")
    else:
        with open(arquivo, "w") as fd: 
            json.dump(fnum, fd)


if __name__ == "__main__":
    main()