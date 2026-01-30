"""
# Descrição

Arquivo relacionado à atividade 10.1 da parte 1.
"""

def main() -> None:
    arquivo = "learning_python.txt"

    with open(arquivo) as fd:
        print(fd.read())

    with open(arquivo) as fd:
        for linha in fd:
            print(linha)
    
    linhas = []

    with open(arquivo) as fd:
        for linha in fd:
            linhas.append(linha)

    print("\n".join(linhas))


if __name__ == "__main__":
    main()