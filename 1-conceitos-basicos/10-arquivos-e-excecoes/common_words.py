"""
# Descrição

Arquivo relacionado à atividade 10.10 da parte 1.
"""

def main() -> None:
    arquivos = ["the_gift_of_the_magi.txt", "hamlet.txt"]

    for arquivo in arquivos:
        try:
            with open(arquivo) as fd:
                texto = fd.read().lower()
                print(f"No arquivo {arquivo}, ", end="")
                print(f"a palavra \"the\" aparece {texto.count("the")} vezes.")
        except FileNotFoundError:
            print(f"O arquivo {arquivo} não pode ser encontrado.")


if __name__ == "__main__":
    main()