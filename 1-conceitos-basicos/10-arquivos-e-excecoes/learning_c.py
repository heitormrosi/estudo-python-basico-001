"""
# Descrição

Arquivo relacionado à atividade 10.2 da parte 1.
"""

def main() -> None:
    arquivo = "learning_python.txt"

    with open(arquivo) as fd:
        for linha in fd:
            # Total mentira... C é "low level" hoje em dia ;-;
            print(linha.replace("Python", "C"))


if __name__ == "__main__":
    main()