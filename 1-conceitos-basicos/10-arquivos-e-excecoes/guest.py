"""
# Descrição

Arquivo relacionado à atividade 10.3 da parte 1.
"""

def main() -> None:
    print("Qual o seu nome?")
    nome = input("> ")

    with open("guest.txt", "w") as fd:
        fd.write(nome)


if __name__ == "__main__":
    main()