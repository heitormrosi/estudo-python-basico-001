"""
# Descrição

Arquivo relacionado à atividade 10.9 da parte 1.
"""

def main() -> None:
    arquivos = ["cats.txt", "dogs.txt"]

    for arquivo in arquivos:
        try:
            with open(arquivo) as fd:
                for linha in fd:
                    print(linha.strip())
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    main()