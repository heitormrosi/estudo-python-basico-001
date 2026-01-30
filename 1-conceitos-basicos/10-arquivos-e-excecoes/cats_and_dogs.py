"""
# Descrição

Arquivo relacionado à atividade 10.8 da parte 1.
"""

def main() -> None:
    arquivos = ["cats.txt", "dogs.txt"]

    for arquivo in arquivos:
        try:
            with open(arquivo) as fd:
                for linha in fd:
                    print(linha.strip())
        except FileNotFoundError:
            print(f"O arquivo {arquivo} não foi encontrado.")


if __name__ == "__main__":
    main()